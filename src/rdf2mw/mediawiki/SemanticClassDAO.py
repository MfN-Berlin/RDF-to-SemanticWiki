# -*- coding: utf-8 -*-
"""
Provides a class DAO object.

Created on 10.05.2016

@author: Alvaro.Ortiz
"""
import os
from lxml import etree
from rdf2mw.AbstractDAO import AbstractDAO


class SemanticClassDAO(AbstractDAO):
    """Provides a class DAO objects accessing the MediaWiki API."""

    _manager = None
    pageTemplatePath = "templates/page.xslt"

    def __init__(self, manager):
        """
        Construct.

        Instantiate the DAO class and associate it with a DAO manager,
        which manages the connection.

        @param manager: class implementing AbstractDAOManager
        """
        self._manager = manager
        self.values = {}

    def create(self, sclass, language=None):
        """Override abstract method."""
        stree = sclass.asElementTree()

        # Apply the page.xslt template to create the markup for the wiki page
        fullPath = os.path.join(os.path.dirname(__file__), SemanticClassDAO.pageTemplatePath)
        template = etree.parse(fullPath)
        transform = etree.XSLT(template)
        page = transform(stree)
        self.values["template"] = str(page)

        # Markup for the form
        form = "<noinclude>{{#forminput:form=%s}}</noinclude>\n" % sclass.name
        form += "<includeonly>\n{{{for template|%s}}}\n" % sclass.name

        # Add form input fields
        for prop in sclass.datatypeProperties:
            form += "==%s==\n\n" % prop.getLabel(language)
            if prop.getComment(language):
                form += "''%s''" % prop.getComment(language)
            if prop.range == "Literal":
                form += "{{{field|%s|property=%s|input type=textarea|editor=wikieditor|rows=10}}}\n\n" % (prop.name, prop.name)
            elif prop.range == "boolean":
                form += "{{{field|%s|property=%s|input type=radiobutton| mandatory|default=false}}}\n\n" % (prop.name, prop.name)
            elif prop.range == "dateTime":
                form += "{{{field|%s|property=%s|input type=date}}}\n\n" % (prop.name, prop.name)                
            elif prop.range == "int":
                form += "{{{field|%s|property=%s|input type=text|size=10}}}\n\n" % (prop.name, prop.name)                
            else:
                form += "{{{field|%s|property=%s|input type=text}}}\n\n" % (prop.name, prop.name)
            # Link to attribute page
            form += "[%sProperty:%s %s]\n\n" % (self._manager.connector.baseURL, prop.name, prop.getLabel(language))

        # Add object properties as a listbox 
        for prop in sclass.objectProperties:
            form += "==%s==\n\n" % prop.getLabel(language)
            if prop.getComment(language):
                form += "''%s''\n\n" % prop.getComment(language)
            form += "{{{field|%s\n" % prop.range
            form += "   |property=%s\n" % prop.range
            form += "   |input type=listbox\n"
            form += "   | values from category=%s\n" % prop.range
            form += "   |size=10\n"
            form += "   |list\n"
            form += "   |delimiter=@\n"
            form += "}}}\n\n"
            form += "<div class=\"wt_toolbar\">[%sCategory:%s Add %s]</div>\n\n" % (self._manager.connector.baseURL, prop.range, prop.range)

        form += "{{{end template}}}\n\n"
        form += "{{{standard input|minor edit}}}\n"
        form += "{{{standard input|watch}}}{{{standard input|save}}}\n"
        form += "{{{standard input|changes}}} {{{standard input|cancel}}}\n"
        form += "__NOTOC__\n"
        form += "__NOEDITSECTION__\n"
        form += "</includeonly>\n"

        self.values["form"] = form

        # Markup for the category page
        category = "{{#default_form:%s}}" % sclass.name
        category += "{{#forminput:form=%s|autocomplete on category=%s}}" % (sclass.name, sclass.name)
        self.values["category"] = category

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
