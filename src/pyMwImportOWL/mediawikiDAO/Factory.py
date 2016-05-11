'''
Created on 04.05.2016
Provides a single point of access and connection scoping for the 
DAO objects accessing the MediaWiki API.

@author: Alvaro.Ortiz
'''
from pyMwImportOWL.mediawikiDAO.AbstractFactory import AbstractFactory
from pyMwImportOWL.mediawikiDAO.SemanticPropertyDAO import SemanticPropertyDAO
from pyMwImportOWL.mediawikiDAO.SemanticClassDAO import SemanticClassDAO

class Factory( AbstractFactory ):
    _connector = None
    _propertyDAO = None
    _classDAO = None
    
    def __init__(self, connector):
        self._connector = connector
    
    
    def commit(self, key, value):
        '''
        Commit the operation in this case using MediaWiki API
        @param key: a string corresponding to a page name
        @param value: a string corresponding to page contents in markdown
        '''
        pass
    
    
    def getSemanticPropertyDAO(self):
        '''
        get a DAO object for the pyMwImportOWL.parser.SemanticModel.SemanticProperty class
        '''
        if self._propertyDAO == None:
            self._propertyDAO = SemanticPropertyDAO(self)
        return self._propertyDAO

    
    def getSemanticClassDAO(self):
        '''
        get a DAO object for the pyMwImportOWL.parser.SemanticModel.SemanticClass class
        '''
        if self._classDAO == None:
            self._classDAO = SemanticClassDAO(self)
        return self._classDAO


        