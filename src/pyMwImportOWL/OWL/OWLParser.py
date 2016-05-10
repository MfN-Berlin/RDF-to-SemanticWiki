'''
Created on 02.05.2016
Parse an OWL file in XML format
@author: Alvaro.Ortiz
'''
from xml.dom import minidom
from pyMwImportOWL.model.SemanticModel import SemanticModel
from pyMwImportOWL.model.SemanticClass import SemanticClass
from pyMwImportOWL.model.SemanticProperty import SemanticProperty

class OWLParser:
    _doc = None
    _model = None
    
    def __init__(self):
        self._model = SemanticModel()
        
    
    def parse(self,path):
        '''Load an OWL file
    
        @param path:string path to a file 
        @return SemanticModel: a object representing the parsed OWL
        @raise exception: if not an OWL file 
        '''
        self._doc = minidom.parse( path )
        check, message = self._checkOWL()
        if not check:
            raise Exception( "Not an OWL file: " + message + "  " + path)
        
        self._parseClasses()
        
        return self._model

    
    def _parseClasses(self):
        '''Get the OWL class name declarations
        @return: array of class names'''
        declarations = self._doc.getElementsByTagName("Declaration")
        if declarations == None or len(declarations) == 0:
            raise Exception("No class declarations found in OWL file")
        
        # go through the "Class" OWL-elements and add them to the model 
        for element in declarations:
            for node in element.childNodes:
                if node.nodeName == "Class":
                    value = node.attributes["IRI"].value
                    className = value[1:] # pop leading hash
                    sclass = SemanticClass(className)
                    self._parsePropertyDomains( sclass )
                    self._model.addClass(sclass) # add class to model 
                    
        # Look for unions in the model
        self._parseUnions()

    
    def _parseUnions(self):
        domains = self._doc.getElementsByTagName("ObjectPropertyDomain")
        ranges = self._doc.getElementsByTagName("ObjectPropertyRange")
        
        # go through ObjectPropertyDomain elements
        for domain in domains:
            items = []
            parentClassName = None
            # look if element contains ObjectUnionOf elements
            for node1 in domain.childNodes:
                # Find elements in the union
                if node1.nodeName == "ObjectUnionOf":
                    for node2 in node1.childNodes:
                        if node2.nodeName == "Class":
                            items.append( node2.attributes["IRI"].value[1:] ) # pop leading hash
                            
                # Find the name of the property            
                if node1.nodeName == "ObjectProperty":
                    foundName = node1.attributes["IRI"].value[1:] # pop leading hash
                    
            if len(items) > 0: # if a non-empty union was found 
                for r in ranges:
                    for node1 in r.childNodes:
                        if node1.nodeName == "ObjectProperty":
                            propName = node1.attributes["IRI"].value[1:]
                        if node1.nodeName == "Class":
                            className = node1.attributes["IRI"].value[1:]

                    # if the ObjectProperty in the range is the same as the objectProperty in the domain
                    # then the remember this class                            
                    if propName == foundName:
                        parentClassName = className

                if parentClassName:
                    for item in items:
                        self._model.classes[parentClassName].uniteWith( self._model.classes[ item ] )
        
    
    def _parsePropertyDomains(self, sclass):
        '''Get the OWL properties for a given class, 
        by looking at the property domain declarations
        @param: sclass SemanticClass'''

        # go through DataPropertyDomain elements        
        domains = self._doc.getElementsByTagName("DataPropertyDomain")
        for element in domains:
            foundClassName = foundPropName = None
            
            # read the Class and DataProperty names of each DataPropertyDomain element
            for node in element.childNodes:
                if node.nodeName == "Class":
                    foundClassName = node.attributes["IRI"].value[1:] # pop leading hash
                if node.nodeName == "DataProperty":
                    foundPropName = node.attributes["IRI"].value[1:] # pop leading hash
                    
            # look for DataPropertyDomain elements associated with the given class
            if foundClassName == sclass.name:
                prop = SemanticProperty(foundPropName)
                self._parsePropertyRanges(prop)
                sclass.addProperty( prop )
        
        
    def _parsePropertyRanges(self, prop):
        '''Get the OWL property type for a given property
        @param prop: SemanticProperty 
        '''
        # go through DataPropertyRange elements
        ranges = self._doc.getElementsByTagName("DataPropertyRange")
        for element in ranges:
            foundType = foundPropName = None
        
            # read the DataProperty and Datatype names of each DataPropertyRange element
            for node in element.childNodes:
                if node.nodeName == "DataProperty":
                    foundPropName = node.attributes["IRI"].value[1:] # pop leading hash
                if node.nodeName == "Datatype":
                    foundType = node.attributes["abbreviatedIRI"].value.split(":")[1] # pop leading namespace
                if node.nodeName == "DataOneOf":
                    foundType = "DataOneOf" # enumeration type values
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
        '''Checks that the loaded file is actually an OWL file
        @return boolean,string: True or False, error message (or None if True)
        '''
        if not self._doc: 
            return False, "No doc loaded"
        
        root = self._doc.documentElement
        if not root.tagName == "Ontology":
            return False, "Not an ontology"
        
        if not "http://www.w3.org/2002/07/owl#" in root.namespaceURI:
            return False, "Unknown namespace"
        
        return True, None
        
    
