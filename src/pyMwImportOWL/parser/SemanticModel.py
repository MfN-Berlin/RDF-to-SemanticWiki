'''
Created on 03.05.2016
Describes an ontology as a simple object oriented model
@author: Alvaro.Ortiz
'''

class SemanticModel:
    '''
    A class for representing a semantic model in an object oriented way.
    Classes are stored in a dictionary.
    '''
    classes = {}
    
    def addClass(self, sclass):
        self.classes[ sclass.name ] = sclass
    
    
    def countClasses(self):
        '''
        @return: 
        '''
        return len( self.classes )
    
    
    def  getClassNames(self):
        '''
        @return array of strings
        '''
        return self.classes.keys()
    

class SemanticClass:
    '''
    A class for representing a semantic class in an object oriented way.
    Class properties are stored in a dictionary.
    '''
    name = None
    properties = {}
    
    def __init__(self, name):
        self.name = name
    
    
    def addProperty(self, prop):
        self.properties[ prop.name ] = prop
        
    
    def getPropertyNames(self):
        '''
        @return array of strings
        '''
        return self.properties.keys()
        


class SemanticProperty:
    name = None
    type = None
    allowedValues = None
    
    def __init__(self, name):
        self.name = name
        
    
    