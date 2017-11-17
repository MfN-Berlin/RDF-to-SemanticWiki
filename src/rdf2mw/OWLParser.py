"""
Parse an OWL file in XML format.

Created on 02.05.2016

@author: Alvaro.Ortiz
"""

from xml.dom import minidom
from rdf2mw.AbstractParser import AbstractParser
from rdf2mw.SemanticModel import SemanticModel, SemanticClass, DatatypeProperty


class OWLParser(AbstractParser):
    """Parse an OWL file in XML format."""

    _doc = None
    _model = None

    def __init__(self):
        """Construct."""
        self._model = SemanticModel()

    def parse(self, path):
        """Override abstract method."""
        self._doc = minidom.parse(path)
        check, message = self._checkOWL()
        if not check:
            raise Exception("Not an OWL file: " + message + "  " + path)
        self._parseClasses()
        return self._model

    def _parseClasses(self):
        """
        Get the OWL class name declarations.

        @return: array of class names
        """
        declarations = self._doc.getElementsByTagName("Declaration")
        if declarations is None or len(declarations) == 0:
            raise Exception("No class declarations found in OWL file")

        # go through the "Class" OWL-elements and add them to the model
        for element in declarations:
            for node in element.childNodes:
                if node.nodeName == "Class":
                    value = node.attributes["IRI"].value
                    className = value[1:]  # pop leading hash
                    sclass = SemanticClass(className)
                    self._parsePropertyDomains(sclass)
                    self._model.addClass(sclass)  # add class to model

    def _parsePropertyDomains(self, sclass):
        """
        Get the OWL properties for a given class, by looking at the property domain declarations.

        @param: sclass SemanticClass
        """
        # go through DataPropertyDomain elements
        domains = self._doc.getElementsByTagName("DataPropertyDomain")
        for element in domains:
            foundClassName = foundPropName = None

            # read the Class and DataProperty names of each DataPropertyDomain element
            for node in element.childNodes:
                if node.nodeName == "Class":
                    foundClassName = node.attributes["IRI"].value[1:]  # pop leading hash
                if node.nodeName == "DataProperty":
                    foundPropName = node.attributes["IRI"].value[1:]  # pop leading hash

            # look for DataPropertyDomain elements associated with the given class
            if foundClassName == sclass.name:
                prop = DatatypeProperty(foundPropName)
                self._parsePropertyRanges(prop)
                sclass.addProperty(prop)

    def _parsePropertyRanges(self, prop):
        """
        Get the OWL property type for a given property.

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

    def _checkOWL(self):
        """
        Check that the loaded file is actually an OWL file.

        @return boolean,string: True or False, error message (or None if True)
        """
        if not self._doc:
            return False, "No doc loaded"

        root = self._doc.documentElement
        if not root.tagName == "Ontology":
            return False, "Not an ontology"

        if "http://www.w3.org/2002/07/owl#" not in root.namespaceURI:
            return False, "Unknown namespace"

        return True, None
