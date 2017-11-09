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
        # Mark-down for the class properties
        template = "=%s=\n" % sclass.name
        for name in sclass.getPropertyNames():
            template += "'''%s''': " % name
            template += "[[%s::{{{%s|}}}]] \n" % (name, name)

        # Mark-down for the properties of union classes
        # Make a call to the template of the class
        for part in sclass.unionOf.values():
            template += "==%s==\n" % part.name
            template += "{{%s\n" % part.name
            for name in part.getPropertyNames():
                template += "| %s = {{{%s|}}}\n" % (name, name)
            template += "}}\n"

        self.values["template"] = template

        # Mark-down for the form
        form = "<noinclude>{{#forminput:form=%s}}</noinclude>\n" % sclass.name
        form += "<includeonly>\n{{{for template|%s}}}\n" % sclass.name

        # Add form input fields
        for prop in sclass.datatypeProperties:
            form += "==%s==\n\n" % prop.name
            if prop.range is "Literal":
                form += "{{{field|%s|input type=textarea||editor=wikieditor|rows=10}}}\n" % prop.name
            else:
                form += "{{{field|%s|input type=text}}}\n" % prop.name

        form += "{{{end template}}}\n\n"
        form += "{{{standard input|minor edit}}}\n"
        form += "{{{standard input|watch}}}{{{standard input|save}}}\n"
        form += "{{{standard input|changes}}} {{{standard input|cancel}}}\n"
        form += "__NOTOC__\n"
        form += "__NOEDITSECTION__\n"
        form += "</includeonly>\n"

        self.values["form"] = form

        # Send to MediaWiki
        self._manager.commit(sclass.name, self.values)

    def getValues(self):
        """Override abstract method."""
        return self.values
