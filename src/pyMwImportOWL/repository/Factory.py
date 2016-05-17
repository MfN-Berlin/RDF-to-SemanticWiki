'''
Created on 04.05.2016
Provides a single point of access and connection scoping for the 
DAO objects accessing the MediaWiki API.

@author: Alvaro.Ortiz
'''
from pyMwImportOWL.mediawikiDAO.AbstractFactory import AbstractFactory
from pyMwImportOWL.mediawikiDAO.SemanticPropertyDAO import SemanticPropertyDAO
from pyMwImportOWL.mediawikiDAO.SemanticClassDAO import SemanticClassDAO
from pyMwImportOWL.mediawikiDAO.Manager import Manager

class Factory( AbstractFactory ):
    _connector = None
    _manager = None
    _propertyDAO = None
    _classDAO = None
    _modelDAO = None


    def __init__(self, connector):
        self._connector = connector


    def getDAOManager(self):
        '''
        get a manager object for managing commits and connection scope
        '''
        if self._manager == None:
            self._manager = Manager( self._connector )
        return self._manager


    def getSemanticPropertyDAO(self):
        '''
        get a DAO object for the pyMwImportOWL.model.SemanticProperty class
        '''
        if self._propertyDAO == None:
            self._propertyDAO = SemanticPropertyDAO( self.getDAOManager() )
        return self._propertyDAO

    
    def getSemanticClassDAO(self):
        '''
        get a DAO object for the pyMwImportOWL.model.SemanticClass class
        '''
        if self._classDAO == None:
            self._classDAO = SemanticClassDAO( self.getDAOManager() )
        return self._classDAO


        