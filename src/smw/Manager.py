"""
Provides a manager for DAO objects accessing MediaWiki API.

Created on 17.05.2016

@author: Alvaro.Ortiz
"""
from rdf2mw.AbstractManager import AbstractManager


class Manager(AbstractManager):
    """Provides a manager for DAO objects."""

    _connector = None

    def __init__(self, connector, tplDir):
        """
        Construct.

        @param connector: the object that will be used to
        persist the DAO objects.
        @param tplDir: Path to XSLT templates
        """
        self._connector = connector
        self._tplDir = tplDir

    def commit(self, name, values):
        """Override abstract method."""
        for key in values.keys():
            # values contains e.g. "template" and "form" page contents
            pageName = '%s:%s' % (key, name)
            self._connector.createPage(pageName, values[key])
            self._connector.protectPage(pageName)

    def delete(self, name, pages):
        """Override abstract method."""
        for namespace in pages:
            # namespace contains e.g. "template", "form", "property"
            pageName = '%s:%s' % (namespace, name)
            self._connector.deletePage(pageName)

    @property
    def connector(self):
        """Get the connector."""
        return self._connector

    @property
    def tplDir(self):
        """Get the template directory."""
        return self._tplDir
