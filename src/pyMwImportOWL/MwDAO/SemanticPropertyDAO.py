'''
Created on 09.05.2016
DAO classes for persisting SemanticModel classes
using the MediaWiki API

@author: Alvaro.Ortiz
'''
from pyMwImportOWL.DAO.Abstract import AbstractDAO

class SemanticPropertyDAO(AbstractDAO):
    
    _manager = None
    
    def __init__(self, manager):
        '''Instantiate the DAO class and associate it with a DAO manager, which manages the connection
        @param manager: class implementing AbstractDAOManager 
        '''
        self._manager = manager
        
    
    def create(self, sprop):
        '''Create a Semantic MediaWiki page for the property
        @param sprop: SemanticProperty
        '''
        datatype = "Text" # default
        if sprop.type == "dateTime":
            datatype = "Date"
        elif sprop.type == "boolean":
            datatype = "Boolean"
        elif sprop.type == "string":
            datatype = "Text"
        elif sprop.type == "DataOneOf":
            datatype = "Text"
            
        # markdown goes in the MediaWiki page
        response = "This is a property of type [[Has type::%s]].\n" % datatype 
        
        if sprop.type == "DataOneOf":
            response += "The allowed values for this property are:\n"
            for value in sprop.allowedValues:
                response += "[[Allows value::%s]]\n" % value
        
        # Send to MediaWiki    
        self._manager.commit( sprop.name, response )