"""
Parse an RDF file in XML format.

Created on 02.05.2016

@author: Alvaro.Ortiz
"""

from lxml import etree
from rdf2mw.AbstractParser import AbstractParser
from rdf2mw.SemanticModel import SemanticModel, SemanticClass, DatatypeProperty, ObjectProperty, Enumeration


class RDFParser(AbstractParser):
    """Parse an RDF file in XML format."""

    _doc = None
    _model = None

    def __init__(self):
        """Construct."""
        self._model = SemanticModel()

    def parse(self, path):
        """Override abstract method."""
        self._doc = etree.parse(path)
        check, message = self._checkRDF()
        if not check:
            raise Exception("Not an RDF file: " + message + "  " + path)

        self._parseClasses()
        self._parseDataProperties()
        self._parseObjectProperties()
        self._parseInheritance()

        return self._model

    def _parseInheritance(self):
        """
        Resolve the inheritance relationships between classes.

        If an inheritance relationship is found, then add the
        properties of the superclass to the subclass.
        Run this method AFTER all others.
        """
        declarations = self._doc.findall(RDFParser.path("owl:Class") + "|" + RDFParser.path("rdfs:Class"))
        # go through the "Class" elements
        for element in declarations:
            # find subclasses
            superclasses = element.findall(RDFParser.path("rdfs:subClassOf", startWith='descendant'))
            if len(superclasses) == 0:
                continue
            # get the corresponding semantic elements in the model
            superclassName = superclasses[0].attrib[RDFParser.full('rdf:resource')].split('#')[1]
            sSuperclass = self._model.classes[superclassName]
            subclassName = element.attrib[RDFParser.full('rdf:about')].split('#')[1]
            sSubClass = self._model.classes[subclassName]

            # add the properties of the superclass to the subclass
            dataProperties = sSuperclass.datatypeProperties
            for dataProperty in dataProperties:
                sSubClass.addProperty(dataProperty)
            objProperties = sSuperclass.objectProperties
            for objProperty in objProperties:
                sSubClass.addProperty(objProperty)

    def _parseClasses(self):
        """Get the class name declarations."""
        declarations = self._doc.findall(RDFParser.path("owl:Class"))
        declarations += self._doc.findall(RDFParser.path("rdfs:Class"))
        # go through the "Class" elements and add them to the model
        for element in declarations:
            className = self._parseAboutString(element)

            # is this class a collection?
            oneof = element.findall(RDFParser.path('owl:oneOf', startWith='descendant'))
            if len(oneof) > 0:
                enum = Enumeration(className)
                self._model.addEnum(enum)
                items = oneof[0].findall(RDFParser.path('rdf:Description', startWith='descendant'))
                for item in items:
                    itemName = item.attrib[RDFParser.full('rdf:about')].split('#')[1]
                    itemElement = etree.Element('item')
                    itemElement.text = itemName
                    enum.add(itemElement)

            else:
                sclass = SemanticClass(className)
                self._model.addClass(sclass)  # add class to model
                lang = "en" # default language for labels and comments, unless specified with xml:lang property

                # localized labels of the class
                labels = element.findall(RDFParser.path('rdfs:label', startWith='descendant'))
                for label in labels:
                    if RDFParser.full('xml:lang') in label.attrib:
                        lang = label.attrib[RDFParser.full('xml:lang')]
                    sclass.addLabel(label.text, lang)

                # localized comment of the class
                comments = element.findall(RDFParser.path('rdfs:comment', startWith='descendant'))
                for comment in comments:
                    if RDFParser.full('xml:lang') in comment.attrib:
                        lang = comment.attrib[RDFParser.full('xml:lang')]
                    sclass.addComment(comment.text, lang)

    def _parseDataProperties(self):
        """Get the data properties."""
        # go through DataPropertyDomain elements
        properties = self._doc.findall(RDFParser.full("owl:DatatypeProperty"))
        lang = "en" # default language for labels and comments, unless specified with xml:lang property

        # go through the "dataProperty" elements and add them to the model
        for element in properties:

            # Name of this property
            propName = self._parseAboutString(element)
            prop = DatatypeProperty(propName)

            # localized labels of the property
            labels = element.findall(RDFParser.path('rdfs:label', startWith='descendant'))
            for label in labels:
                if RDFParser.full('xml:lang') in label.attrib:
                    lang = label.attrib[RDFParser.full('xml:lang')]
                prop.addLabel(label.text, lang)

            # localized comment of the property
            comments = element.findall(RDFParser.path('rdfs:comment', startWith='descendant'))
            for comment in comments:
                if RDFParser.full('xml:lang') in comment.attrib:
                    lang = comment.attrib[RDFParser.full('xml:lang')]
                prop.addComment(comment.text, lang)

            # domainName is the name of the class this property belongs to
            domain = element.find(RDFParser.path('rdfs:domain', startWith='descendant'))
            if domain is not None: # subproperties do not always have a domain
                # domainName = domain.attrib[RDFParser.full('rdf:resource')].split('#')[1]
                domainName = self._parseResourceString(domain)
            # rangeType is the variable type of this property
            range = element.find(RDFParser.path('rdfs:range', startWith='descendant'))
            if range is not None:
                # rangeType = range.attrib[RDFParser.full('rdf:resource')].split('#')[1]
                rangeType = self._parseResourceString(range)
                prop.range = rangeType
            else:
                prop.range = "Literal"

            # allowed values from enumeration if applicable
            if prop.range in self._model.enums:
                vals = []
                for item in self._model.enums[prop.range].asList():
                    vals.append(item)
                prop.allowedValues = vals

            # set the global cardinality constraint of this property
            typeConstraint = element.find(RDFParser.path('rdf:type', startWith='descendant'))
            if typeConstraint is not None:
                cardinality = typeConstraint.attrib[RDFParser.full('rdf:resource')].split('#')[1]
                prop.cardinality = cardinality

            # if the class exists, add the property
            if domainName in self._model.getClassNames():
                self._model.classes[domainName].addProperty(prop)

    def _parseObjectProperties(self):
        """Get the object properties."""
        # go through ObjectProperty elements
        properties = self._doc.findall(RDFParser.full("owl:ObjectProperty"))
        lang = "en" # default language for labels and comments, unless specified with xml:lang property

        # go through the "ObjectProperty" elements and add them to the model
        for element in properties:
            # propName is the name of this property
            # propName = element.attrib[RDFParser.full('rdf:about')].split('#')[1]
            propName = self._parseAboutString(element)
            prop = ObjectProperty(propName)

            # domainName is the name of the class this property belongs to
            domain = element.find(RDFParser.path('rdfs:domain', startWith='descendant'))
            # domainName = domain.attrib[RDFParser.full('rdf:resource')].split('#')[1]
            if domain is not None: # subproperties do not always have a domain
                # domainName = domain.attrib[RDFParser.full('rdf:resource')].split('#')[1]
                domainName = self._parseResourceString(domain)

            # localized labels of the property
            labels = element.findall(RDFParser.path('rdfs:label', startWith='descendant'))
            for label in labels:
                #lang = label.attrib[RDFParser.full('xml:lang')]
                #prop.addLabel(label.text, lang)
                if RDFParser.full('xml:lang') in label.attrib:
                    lang = label.attrib[RDFParser.full('xml:lang')]
                prop.addLabel(label.text, lang)

            # localized comments of the property
            comments = element.findall(RDFParser.path('rdfs:comment', startWith='descendant'))
            for comment in comments:
                #lang = comment.attrib[RDFParser.full('xml:lang')]
                #prop.addComment(comment.text, lang)
                if RDFParser.full('xml:lang') in comment.attrib:
                    lang = comment.attrib[RDFParser.full('xml:lang')]
                prop.addLabel(comment.text, lang)

            # rangeType is the variable type of this property
            range = element.find(RDFParser.path('rdfs:range', startWith='descendant'))
            if range is not None:
                # rangeType = range.attrib[RDFParser.full('rdf:resource')].split('#')[1]
                rangeType = self._parseResourceString(range)
                prop.range = rangeType

            # set the global cardinality constraint of this property
            typeConstraint = element.find(RDFParser.path('rdf:type', startWith='descendant'))
            if typeConstraint is not None:
                cardinality = typeConstraint.attrib[RDFParser.full('rdf:resource')].split('#')[1]
                prop.cardinality = cardinality

            # if the class exists, add the property
            if domainName in self._model.getClassNames():
                self._model.classes[domainName].addProperty(prop)

    def _parseAboutString(self, element):
        """
        Parse the "rdf:about" property of element
        
        @param: element, an etree element
        @return string, smplified version of the rdf:about property, for using as e.g. class name
        """
        aboutString = element.attrib[RDFParser.full('rdf:about')]
        # Property name is in the format URL#proName
        if '#' in aboutString:
            resp = element.attrib[RDFParser.full('rdf:about')].split('#')[1]
        # Property name is in the format URL/proName
        elif '/' in aboutString:
            resp = element.attrib[RDFParser.full('rdf:about')].split('/')[-1]
        else:
            resp = aboutString
        return resp

    def _parseResourceString(self, element):
        """
        Parse the "rdf:resource" property of element
        
        @param: element, an etree element
        @return string, smplified version of the rdf:resource property, for using as e.g. domain or range of object properties
        """
        resourceString = element.attrib[RDFParser.full('rdf:resource')]
        # Property name is in the format URL#proName
        if '#' in resourceString:
            resp = element.attrib[RDFParser.full('rdf:resource')].split('#')[1]
        # Property name is in the format URL/proName
        elif '/' in resourceString:
            resp = element.attrib[RDFParser.full('rdf:resource')].split('/')[-1]
        else:
            resp = resourceString
        return resp

    def _checkRDF(self):
        """
        Check that the loaded file is actually an RDF file.

        @return boolean,string: True or False, error message (or None if True)
        """
        if not self._doc:
            return False, "No doc loaded"

        root = self._doc.getroot()
        if not root.tag == RDFParser.full('rdf:RDF'):
            return False, "Not an RDF file"

            if "http://www.w3.org/1999/02/22-rdf-syntax-ns#" not in root.nsmap:
                return False, "Unknown namespace"

        return True, None
