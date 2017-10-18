"""
Provides a manager for DAO objects accessing MediaWiki API.

Created on 17.05.2016

@author: Alvaro.Ortiz
"""
from pyMwImportOWL.repository.AbstractManager import AbstractManager


class Manager(AbstractManager):
    """Provides a manager for DAO objects accessing MediaWiki API."""

    _connector = None

    def __init__(self, connector):
        """Construct."""
        self._connector = connector

    def commit(self, name, values):
        """Override abstract method."""
        for key in values.keys():
            pageName = '%s:%s' % (key, name)
            self._connector.createPage(pageName, values[key])
