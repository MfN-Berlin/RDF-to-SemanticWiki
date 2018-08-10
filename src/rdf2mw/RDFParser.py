"""
Parse an RDF file in XML format.

Created on 02.05.2016

@author: Alvaro.Ortiz
"""

from lxml import etree
from rdf2mw.AbstractParser import AbstractParser
from rdf2mw.SemanticModel import SemanticModel, SemanticClass, DatatypeProperty, ObjectProperty


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

        return self._model

    def _parseClasses(self):
        """
        Get the class name declarations.

        @return: array of class names
        """
        declarations = self._doc.findall(RDFParser.path("owl:Class"))
        # go through the "Class" elements and add them to the model
        for element in declarations:
            className = element.attrib[RDFParser.full('rdf:about')].split('#')[1]
            sclass = SemanticClass(className)
            self._model.addClass(sclass)  # add class to model

            # localized labels of the class
            labels = element.findall(RDFParser.path('rdfs:label', startWith='descendant'))
            for label in labels:
                lang = label.attrib[RDFParser.full('xml:lang')]
                sclass.addLabel(label.text, lang)

            # localized comment of the class
            comments = element.findall(RDFParser.path('rdfs:comment', startWith='descendant'))
            for comment in comments:
                lang = comment.attrib[RDFParser.full('xml:lang')]
                sclass.addComment(comment.text, lang)

    def _parseDataProperties(self):
        """Get the data properties."""
        # go through DataPropertyDomain elements
        properties = self._doc.findall(RDFParser.full("owl:DatatypeProperty"))

        # go through the "dataProperty" elements and add them to the model
        for element in properties:

            # Name of this property
            aboutString = element.attrib[RDFParser.full('rdf:about')]
            # Property name is in the format URL#proName
            if '#' in aboutString:
                propName = element.attrib[RDFParser.full('rdf:about')].split('#')[1]
            # Property name is in the format URL/proName
            elif '/' in aboutString:
                propName = element.attrib[RDFParser.full('rdf:about')].split('/')[-1]
            else:
                propName = aboutString

            prop = DatatypeProperty(propName)

            # localized labels of the property
            labels = element.findall(RDFParser.path('rdfs:label', startWith='descendant'))
            for label in labels:
                lang = label.attrib[RDFParser.full('xml:lang')]
                prop.addLabel(label.text, lang)

            # localized comment of the property
            comments = element.findall(RDFParser.path('rdfs:comment', startWith='descendant'))
            for comment in comments:
                lang = comment.attrib[RDFParser.full('xml:lang')]
                prop.addComment(comment.text, lang)

            # domainName is the name of the class this property belongs to
            domain = element.find(RDFParser.path('rdfs:domain', startWith='descendant'))
            domainName = domain.attrib[RDFParser.full('rdf:resource')].split('#')[1]

            # rangeType is the variable type of this property
            range = element.find(RDFParser.path('rdfs:range', startWith='descendant'))
            if range is not None:
                rangeType = range.attrib[RDFParser.full('rdf:resource')].split('#')[1]
                prop.range = rangeType
            else:
                prop.range = "Literal"

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

        # go through the "ObjectProperty" elements and add them to the model
        for element in properties:
            # propName is the name of this property
            propName = element.attrib[RDFParser.full('rdf:about')].split('#')[1]
            prop = ObjectProperty(propName)

            # domainName is the name of the class this property belongs to
            domain = element.find(RDFParser.path('rdfs:domain', startWith='descendant'))
            domainName = domain.attrib[RDFParser.full('rdf:resource')].split('#')[1]

            # localized labels of the property
            labels = element.findall(RDFParser.path('rdfs:label', startWith='descendant'))
            for label in labels:
                lang = label.attrib[RDFParser.full('xml:lang')]
                prop.addLabel(label.text, lang)

            # localized comments of the property
            comments = element.findall(RDFParser.path('rdfs:comment', startWith='descendant'))
            for comment in comments:
                lang = comment.attrib[RDFParser.full('xml:lang')]
                prop.addComment(comment.text, lang)

            # rangeType is the variable type of this property
            range = element.find(RDFParser.path('rdfs:range', startWith='descendant'))
            if range is not None:
                rangeType = range.attrib[RDFParser.full('rdf:resource')].split('#')[1]
                prop.range = rangeType

            # set the global cardinality constraint of this property
            typeConstraint = element.find(RDFParser.path('rdf:type', startWith='descendant'))
            if typeConstraint is not None:
                cardinality = typeConstraint.attrib[RDFParser.full('rdf:resource')].split('#')[1]
                prop.cardinality = cardinality

            # if the class exists, add the property
            if domainName in self._model.getClassNames():
                self._model.classes[domainName].addProperty(prop)

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
