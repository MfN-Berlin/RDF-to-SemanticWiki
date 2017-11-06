"""
Provides a single point of access and connection scoping for DAO objects accessing MediaWiki API.

Created on 04.05.2016

@author: Alvaro.Ortiz
"""
from pyMwImportOWL.repository.AbstractFactory import AbstractFactory
from pyMwImportOWL.repository.SemanticPropertyDAO import SemanticPropertyDAO
from pyMwImportOWL.repository.SemanticClassDAO import SemanticClassDAO
from pyMwImportOWL.repository.Manager import Manager


class Factory(AbstractFactory):
    """
    Provides a single point of access and connection scoping.

    For DAO objects accessing MediaWiki API.
    """

    _connector = None
    _manager = None
    _propertyDAO = None
    _classDAO = None
    _modelDAO = None

    def __init__(self, connector):
        """Construct."""
        self._connector = connector

    def getDAOManager(self):
        """Override abstract method."""
        if self._manager is None:
            self._manager = Manager(self._connector)
        return self._manager

    def getSemanticPropertyDAO(self):
        """Override abstract method."""
        if self._propertyDAO is None:
            self._propertyDAO = SemanticPropertyDAO(self.getDAOManager())
        return self._propertyDAO

    def getSemanticClassDAO(self):
        """Override abstract method."""
        if self._classDAO is None:
            self._classDAO = SemanticClassDAO(self.getDAOManager())
        return self._classDAO
