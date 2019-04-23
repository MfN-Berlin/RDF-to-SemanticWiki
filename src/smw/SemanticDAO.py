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

    # XSLT templates
    pageTemplate = "page.xslt"
    formTemplate = "form.xslt"
    categoryTemplate = "category.xslt"
    propertyTemplate = "property.xslt"

    def __init__(self, manager):
        """
        Construct.

        Instantiate the DAO class and associate it with a DAO manager,
        which manages the connection.

        @param manager: class implementing AbstractDAOManager
        """
        # The manager object
        self._manager = manager

        # Array that will hold rendered markdown (page, form, class, property)
        self.values = {}

        # Path to the template directory, as specified in config.ini
        self.tplDir = self._manager.tplDir

    def transform(self, tree, tplName):
        """
        Apply and XSLT transformation to obtain a string.

        @param tree etree input xml tree
        @param tplName name of the XSLT template to apply
        @return string containing wiki markup.
        """
        # print(etree.tostring(tree, encoding="utf8", method="xml"))
        fullPath = os.path.join(os.path.dirname(__file__), self.tplDir, tplName)
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

        # Add attributes to the element tree
        if language is not None:
            stree.set('lang', language)

        # SemanticClassDAO and MediaWikiApiConnector are coupled anyway.
        stree.set('baseUrl', self._manager.connector.baseURL)

        # Apply the page.xslt template to create the markup for the wiki page
        self.values["template"] = self.transform(
            stree, SemanticElementDAO.pageTemplate)

        # Apply the form.xslt template to create the markup for the wiki form
        self.values["form"] = self.transform(
            stree, SemanticElementDAO.formTemplate)

        # Markup for the category page
        self.values["category"] = self.transform(
            stree, SemanticElementDAO.categoryTemplate)

        # Send to MediaWiki (template, form and category pages)
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
        pages = ['Property']
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
        self.values["property"] = self.transform(
            stree, SemanticElementDAO.propertyTemplate)
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
        else:
            stree.set('lang', 'en')
        # Apply the page.xslt template to create the markup for the wiki page
        self.values["property"] = self.transform(
            stree, SemanticElementDAO.propertyTemplate)
        # Send to MediaWiki
        self._manager.commit(sprop.name, self.values)
