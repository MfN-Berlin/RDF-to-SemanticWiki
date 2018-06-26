"""
Provides a single point of access and connection scoping for DAO objects accessing MediaWiki API.

Created on 04.05.2016

@author: Alvaro.Ortiz
"""
from rdf2mw.AbstractFactory import AbstractFactory
from smw.SemanticDAO import SemanticClassDAO, DatatypePropertyDAO, ObjectPropertyDAO
from smw.Manager import Manager
from smw.Layout import Layout


class Factory(AbstractFactory):
    """
    Provides a single point of access and connection scoping.

    For DAO objects accessing MediaWiki API.
    """

    _connector = None
    _manager = None
    _dataPropertyDAO = None
    _objectPropertyDAO = None
    _classDAO = None
    _modelDAO = None

    def __init__(self, connector, layoutFile=None):
        """
        Construct.

        @param connector: An object implenenting AbstractConnector
        @param layout: path to a XML layout file
        """
        self._connector = connector
        self.layout = None
        if layoutFile is not None:
            self.layout = Layout(layoutFile)

    def getDAOManager(self):
        """Override abstract method."""
        if self._manager is None:
            self._manager = Manager(self._connector, self.layout)
        return self._manager

    def getDatatypePropertyDAO(self):
        """Override abstract method."""
        if self._dataPropertyDAO is None:
            self._dataPropertyDAO = DatatypePropertyDAO(self.getDAOManager())
        return self._dataPropertyDAO

    def getObjectPropertyDAO(self):
        """Override abstract method."""
        if self._objectPropertyDAO is None:
            self._objectPropertyDAO = ObjectPropertyDAO(self.getDAOManager())
        return self._objectPropertyDAO

    def getSemanticClassDAO(self):
        """Override abstract method."""
        if self._classDAO is None:
            self._classDAO = SemanticClassDAO(self.getDAOManager(), self.layout)
        return self._classDAO
