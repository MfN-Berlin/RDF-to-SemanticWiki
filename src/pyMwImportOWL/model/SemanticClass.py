'''
Created on 10.05.2016

@author: Alvaro.Ortiz
'''
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
