"""
Provides DAO objects for the semantic model.

Created on 28.11.2017

@author: Alvaro.Ortiz
"""
import os
from lxml import etree
from rdf2mw.AbstractDAO import AbstractDAO


class SemanticElementDAO(AbstractDAO):
    """Base class for all semantic element DAOs."""

    pageTemplatePath = "templates/page.xslt"
    formTemplatePath = "templates/form.xslt"
    categoryTemplatePath = "templates/category.xslt"
    propertyTemplatePath = "templates/property.xslt"

    _manager = None

    def __init__(self, manager):
        """
        Construct.

        Instantiate the DAO class and associate it with a DAO manager,
        which manages the connection.

        @param manager: class implementing AbstractDAOManager
        """
        self._manager = manager
        self.values = {}

    def transform(self, tree, tplPath):
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


class SemanticClassDAO(SemanticElementDAO):
    """Provides a class DAO objects accessing the MediaWiki API."""

    def __init__(self, manager):
        """Construct."""
        super().__init__(manager)

    def create(self, sclass, language='en'):
        """Override abstract method."""
        stree = sclass.asElementTree()

        # Add atributes to the element tree
        if language is not None:
            stree.set('lang', language)
        # SemanticClassDAO and MediaWikiApiConnector are coupled anyway.
        stree.set('baseUrl', self._manager.connector.baseURL)

        # Apply the page.xslt template to create the markup for the wiki page
        self.values["template"] = self.transform(stree, SemanticElementDAO.pageTemplatePath)

        # Apply the form.xslt template to create the markup for the wiki form
        self.values["form"] = self.transform(stree, SemanticElementDAO.formTemplatePath)

        # Markup for the category page
        self.values["category"] = self.transform(stree, SemanticElementDAO.categoryTemplatePath)

        # Send to MediaWiki
        self._manager.commit(sclass.name, self.values)

    def delete(self, sclass):
        """Override abstract method."""
        pages = ['template', 'form', 'category']

        # Send to MediaWiki
        self._manager.delete(sclass.name, pages)

    def getValues(self):
        """Override abstract method."""
        return self.values


class SemanticPropertyDAO(SemanticElementDAO):
    """Represents a semantic property."""

    def __init__(self, manager):
        """Construct."""
        super().__init__(manager)

    def delete(self, sprop):
        """Override abstract method."""
        pages = ['property']

        # Send to MediaWiki
        self._manager.delete(sprop.name, pages)

    def getValues(self):
        """Override abstract method."""
        return self.values


class ObjectPropertyDAO(SemanticPropertyDAO):
    """Provides a property DAO object."""

    def __init__(self, manager):
        """Construct."""
        super().__init__(manager)

    def create(self, sprop, language=None):
        """Override abstract method."""
        stree = sprop.asElementTree()
        # Add atributes to the element tree
        if language is not None:
            stree.set('lang', language)
        # Apply the page.xslt template to create the markup for the wiki page
        self.values["property"] = self.transform(stree, SemanticElementDAO.propertyTemplatePath)
        # Send to MediaWiki
        self._manager.commit(sprop.name, self.values)


class DatatypePropertyDAO(SemanticPropertyDAO):
    """Provides a property DAO object."""

    def __init__(self, manager):
        """Construct."""
        super().__init__(manager)

    def create(self, sprop, language=None):
        """Override abstract method."""
        stree = sprop.asElementTree()
        # Add atributes to the element tree
        if language is not None:
            stree.set('lang', language)
        # Apply the page.xslt template to create the markup for the wiki page
        self.values["property"] = self.transform(stree, SemanticElementDAO.propertyTemplatePath)
        # Send to MediaWiki
        self._manager.commit(sprop.name, self.values)
