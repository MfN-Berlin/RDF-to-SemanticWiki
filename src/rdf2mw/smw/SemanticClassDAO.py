# -*- coding: utf-8 -*-
"""
Provides a class DAO object.

Created on 10.05.2016

@author: Alvaro.Ortiz
"""
import os
import textwrap
from lxml import etree
from rdf2mw.AbstractDAO import AbstractDAO


class SemanticClassDAO(AbstractDAO):
    """Provides a class DAO objects accessing the MediaWiki API."""

    _manager = None
    pageTemplatePath = "templates/page.xslt"
    formTemplatePath = "templates/form.xslt"
    categoryTemplatePath = "templates/category.xslt"

    def __init__(self, manager):
        """
        Construct.

        Instantiate the DAO class and associate it with a DAO manager,
        which manages the connection.

        @param manager: class implementing AbstractDAOManager
        """
        self._manager = manager
        self.values = {}

    def create(self, sclass, language='en'):
        """Override abstract method."""
        stree = sclass.asElementTree()

        # Add atributes to the element tree
        if language is not None:
            stree.set('lang', language)
        # SemanticClassDAO and MediaWikiApiConnector are coupled anyway.
        stree.set('baseUrl', self._manager.connector.baseURL)

        # Apply the page.xslt template to create the markup for the wiki page
        self.values["template"] = self._transform(stree, SemanticClassDAO.pageTemplatePath)

        # Apply the form.xslt template to create the markup for the wiki form
        self.values["form"] = self._transform(stree, SemanticClassDAO.formTemplatePath)

        # Markup for the category page
        self.values["category"] = self._transform(stree, SemanticClassDAO.categoryTemplatePath)

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
