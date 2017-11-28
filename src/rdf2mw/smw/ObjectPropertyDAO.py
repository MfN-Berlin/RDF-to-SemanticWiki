"""
Provides a property DAO object.

Created on 09.05.2016

@author: Alvaro.Ortiz
"""
import os
from lxml import etree
from rdf2mw.AbstractDAO import AbstractDAO


class ObjectPropertyDAO(AbstractDAO):
    """Provides a property DAO object."""

    propertyTemplatePath = "templates/property.xslt"

    def __init__(self, manager):
        """
        Construct.

        Instantiate the DAO class and associate it with a DAO manager,
        which manages the connection.

        @param manager: class implementing AbstractManager
        """
        self._manager = manager
        self.values = {}

    def create(self, sprop, language=None):
        """Override abstract method."""
        stree = sprop.asElementTree()
        # Add atributes to the element tree
        if language is not None:
            stree.set('lang', language)
        # Apply the page.xslt template to create the markup for the wiki page
        self.values["property"] = self._transform(stree, ObjectPropertyDAO.propertyTemplatePath)
        # Send to MediaWiki
        self._manager.commit(sprop.name, self.values)

    def delete(self, sprop):
        """Override abstract method."""
        pages = ['property']

        # Send to MediaWiki
        self._manager.delete(sprop.name, pages)

    def getValues(self):
        """Override abstract method."""
        return self.values

    def _transform(self, tree, tplPath):
        """
        Apply and XSLT transformation to obtain a string.

        @param tree etree input xml tree
        @param tplPath path to the template, relative to this file
        @return string containing wiki markup.
        """
        fullPath = os.path.join(os.path.dirname(__file__), tplPath)
        template = etree.parse(fullPath)
        transform = etree.XSLT(template)
        page = transform(tree)
        lines = str(page).splitlines()
        resp = ""
        for line in lines:
            resp += line.lstrip() + "\n"
        return(resp)
