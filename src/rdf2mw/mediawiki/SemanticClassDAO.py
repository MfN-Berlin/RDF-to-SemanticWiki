"""
Provides a class DAO object.

Created on 10.05.2016

@author: Alvaro.Ortiz
"""
from rdf2mw.AbstractDAO import AbstractDAO


class SemanticClassDAO(AbstractDAO):
    """Provides a class DAO objects accessing the MediaWiki API."""

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

    def create(self, sclass):
        """Override abstract method."""
        # Markup for the class properties
        template = "=%s=\n" % sclass.name

        # Add datatype property fields
        for prop in sclass.datatypeProperties:
            template += "==%s==\n\n" % prop.name
            template += "[[%s::{{{%s|}}}]] \n" % (prop.name, prop.name)

        # Add object properties as semantic query for corresponding classes
        for prop in sclass.objectProperties:
            template += "==%s==\n" % prop.name
            template += "{{#ask: [[Category:%s]]" % prop.range
            template += "|format=ol"
            template += "}}"

        # Markup for the properties of union classes
        # Make a call to the template of the class
        # for part in sclass.unionOf.values():
        #    template += "==%s==\n" % part.name
        #    template += "{{%s\n" % part.name
        #    for name in part.getPropertyNames():
        #        template += "| %s = {{{%s|}}}\n" % (name, name)
        #    template += "}}\n"

        # Add a category for all classes using this template
        template += "<includeonly>[[category:%s]]</includeonly>" % sclass.name
        self.values["template"] = template

        # Markup for the form
        form = "<noinclude>{{#forminput:form=%s}}</noinclude>\n" % sclass.name
        form += "<includeonly>\n{{{for template|%s}}}\n" % sclass.name

        # Add form input fields
        for prop in sclass.datatypeProperties:
            form += "==%s==\n\n" % prop.name
            if prop.range is "Literal":
                form += "{{{field|%s|input type=textarea||editor=wikieditor|rows=10}}}\n" % prop.name
            else:
                form += "{{{field|%s|input type=text}}}\n" % prop.name

        # Add object properties as semantic query for corresponding classes
        # Add alink to create new entries of the object property
        for prop in sclass.objectProperties:
            form += "==%s==\n\n" % prop.name
            form += "{{#ask: [[Category:%s]]" % prop.range
            form += "|format=ol"
            form += "}}\n\n"
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
