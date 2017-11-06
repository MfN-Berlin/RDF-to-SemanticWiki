"""
Provides a class DAO object.

Created on 10.05.2016

@author: Alvaro.Ortiz
"""
from rdf2mw.repository.AbstractDAO import AbstractDAO


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
        form = "<noinclude>{{#forminput:form=%s}}</noinclude>" % sclass.name
        form += "<includeonly>{{{for template|%s}}}" % sclass.name
        form += "{{{end template}}}"
        form += "{{{standard input|minor edit}}}"
        form += "{{{standard input|watch}}}{{{standard input|save}}}"
        form += "{{{standard input|changes}}} {{{standard input|cancel}}}"
        form += "__NOTOC__"
        form += "__NOEDITSECTION__"
        form += "</includeonly>"

        self.values["form"] = form

        # Send to MediaWiki
        self._manager.commit(sclass.name, self.values)

    def getValues(self):
        """Override abstract method."""
        return self.values
