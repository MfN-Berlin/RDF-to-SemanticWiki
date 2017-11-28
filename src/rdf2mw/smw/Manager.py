"""
Provides a manager for DAO objects accessing MediaWiki API.

Created on 17.05.2016

@author: Alvaro.Ortiz
"""
from rdf2mw.AbstractManager import AbstractManager


class Manager(AbstractManager):
    """Provides a manager for DAO objects."""

    _connector = None

    def __init__(self, connector):
        """
        Construct.

        @param connector: the object that will be used to persist the DAO objects.
        """
        self._connector = connector

    def commit(self, name, values):
        """Override abstract method."""
        for key in values.keys():
            # values contains e.g. "template" and "form" page contents
            pageName = '%s:%s' % (key, name)
            self._connector.createPage(pageName, values[key])

    def delete(self, name, pages):
        """Override abstract method."""
        for namespace in pages:
            # namespace contains e.g. "template", "form", "property" page contents
            pageName = '%s:%s' % (namespace, name)
            self._connector.deletePage(pageName)

    @property
    def connector(self):
        """Get the connector."""
        return self._connector
