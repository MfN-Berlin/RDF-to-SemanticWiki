"""
Parse an OWL file in XML format.

Created on 02.05.2016

@author: Alvaro.Ortiz
"""

from lxml import etree
from rdf2mw.AbstractParser import AbstractParser
from rdf2mw.model.SemanticModel import SemanticModel
from rdf2mw.model.SemanticClass import SemanticClass
from rdf2mw.model.SemanticProperty import SemanticProperty
from rdf2mw.model.SemanticObjectProperty import SemanticObjectProperty


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
        # Look for unions in the model
        # self._parseUnions()

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

    def _parseDataProperties(self):
        """Get the data properties."""
        # go through DataPropertyDomain elements
        properties = self._doc.findall(RDFParser.full("owl:DatatypeProperty"))
        # go through the "dataProperty" elements and add them to the model
        for element in properties:
            # propName is the name of this property
            propName = element.attrib[RDFParser.full('rdf:about')].split('#')[1]
            prop = SemanticProperty(propName)
            # domainName is the name of the class this property belongs to
            domain = element.find(RDFParser.path('rdfs:domain', startWith='descendant'))
            domainName = domain.attrib[RDFParser.full('rdf:resource')].split('#')[1]
            # rangeType is the variable type of this property
            range = element.find(RDFParser.path('rdfs:range', startWith='descendant'))
            if range is not None:
                rangeType = range.attrib[RDFParser.full('rdf:resource')].split('#')[1]
                prop.type = rangeType
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
            prop = SemanticProperty(propName)
            # domainName is the name of the class this property belongs to
            domain = element.find(RDFParser.path('rdfs:domain', startWith='descendant'))
            domainName = domain.attrib[RDFParser.full('rdf:resource')].split('#')[1]
            # rangeType is the variable type of this property
            range = element.find(RDFParser.path('rdfs:range', startWith='descendant'))
            if range is not None:
                rangeType = range.attrib[RDFParser.full('rdf:resource')].split('#')[1]
                prop.type = rangeType
            # if the class exists, add the property
            if domainName in self._model.getClassNames():
                self._model.classes[domainName].addProperty(prop)

    def _parsePropertyRanges(self, prop):
        """
        Get the property type for a given property.

        @param prop: SemanticProperty
        """
        # go through DataPropertyRange elements
        ranges = self._doc.getElementsByTagName("DataPropertyRange")
        for element in ranges:
            foundType = foundPropName = None

            # read the DataProperty and Datatype names of each DataPropertyRange element
            for node in element.childNodes:
                if node.nodeName == "DataProperty":
                    foundPropName = node.attributes["IRI"].value[1:]  # pop leading hash
                if node.nodeName == "Datatype":
                    # pop leading namespace
                    foundType = node.attributes["abbreviatedIRI"].value.split(":")[1]
                if node.nodeName == "DataOneOf":
                    foundType = "DataOneOf"  # enumeration type values
                    allowedValues = []
                    for allowed in node.childNodes:
                        if allowed.nodeName == "Literal":
                            allowedValues.append(allowed.firstChild.nodeValue)

            # look for DataType elements associated with the given property
            if foundPropName == prop.name:
                if foundType == "DataOneOf":
                    prop.allowedValues = allowedValues
                prop.type = foundType

    def _checkRDF(self):
        """
        Check that the loaded file is actually an OWL file.

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
    
    def _parseUnions(self):
        domains = self._doc.findall(RDFParser.path("owl:ObjectPropertyDomain"))
        ranges = self._doc.findall(RDFParser.path("owl:ObjectPropertyRange"))

        # go through ObjectPropertyDomain elements
        for domain in domains:
            items = []
            parentClassName = None
            foundName = None
            # look if element contains ObjectUnionOf elements
            for node1 in domain.childNodes:
                # Find elements in the union
                if node1.nodeName == "ObjectUnionOf":
                    for node2 in node1.childNodes:
                        if node2.nodeName == "Class":
                            items.append(node2.attributes["IRI"].value[1:])  # pop leading hash

                # Find the name of the property
                if node1.nodeName == "ObjectProperty":
                    foundName = node1.attributes["IRI"].value[1:]  # pop leading hash

            if len(items) > 0:  # if a non-empty union was found
                for r in ranges:
                    for node1 in r.childNodes:
                        if node1.nodeName == "ObjectProperty":
                            propName = node1.attributes["IRI"].value[1:]
                        if node1.nodeName == "Class":
                            className = node1.attributes["IRI"].value[1:]

                    # if the ObjectProperty in the range is the same
                    # as the objectProperty in the domain
                    # then the remember this class
                    if propName == foundName:
                        parentClassName = className

                if parentClassName:
                    for item in items:
                        self._model.classes[parentClassName].uniteWith(self._model.classes[item])

    # namespaces:
    # keys are short namespace prefixes,
    # values are fully expanded namespace URIs
    ns = {
        'base': "http://example.org/ontologies/test",
        'rdf': "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        'owl': "http://www.w3.org/2002/07/owl#",
        'xml': "http://www.w3.org/XML/1998/namespace",
        'xsd': "http://www.w3.org/2001/XMLSchema#",
        'rdfs': "http://www.w3.org/2000/01/rdf-schema#"
    }

    @staticmethod
    def full(shortName, asURI=False):
        """
        Get the fully qualified name of a prefixed name.

        Expands the short prefix to the full version of the prefix.
        Returns either the curly braces version or the URIversion.
        Prefixes are in the dictionary ODMModel.ns

        e.g.: rdf:bla gets expanded to:
        * If asURI is True - {http://www.w3.org/1999/02/22-rdf-syntax-ns#}bla
        * If asURI is True - http://www.w3.org/1999/02/22-rdf-syntax-ns#bla

        If the namespace was not found in ODMModel.ns, then the shortName is returned.

        @shortName: string, name without the short version of the prefix
        @asURI: Boolean, when true, return the URI representation
        @return: string, the fully qualified name
        """
        prefix, rawName = shortName.split(':', 2)

        # expand with curly braces
        if asURI is False:
            if prefix in RDFParser.ns:
                # get prefix from dictionary ODMModel.ns
                resp = "{" + RDFParser.ns[prefix] + "}" + rawName
            else:
                # prefix not in dict, return shortName
                resp = shortName
        # expand as URI
        else:
            prefix = RDFParser.ns[prefix].split('#', 2)[0]
            resp = prefix + "#" + rawName
        return resp

    @staticmethod
    def path(*args, **kwargs):
        """
        Join any number of qualified element names.

        example 2:
            ODMModel.path('owl:Class', 'rdfs:subClassOf'), startWith='descendant')
        returns:
            .//{http://www.w3.org/2002/07/owl#}Class/{http://www.w3.org/2000/01/rdf-schema#}subClassOf

        @param *args, string any number of qualified names in short form, e.g. rdf:bla
        @param kwargs, start the path with /, .// or //,
        resp. startWith=root(default)|descendant|any

        """
        expressions = {'root': '/', 'descendant': './/', 'any': '//'}
        exp = "/"
        if kwargs is not None:
            if 'startWith' in kwargs:
                exp = expressions[kwargs['startWith']]
        resp = ''
        for path in args:
            resp += exp + RDFParser.full(path)
            exp = '/'
        return resp
