"""
Provides a property DAO object.

Created on 09.05.2016

@author: Alvaro.Ortiz
"""

from rdf2mw.AbstractDAO import AbstractDAO


class SemanticPropertyDAO(AbstractDAO):
    """Provides a property DAO object."""

    def __init__(self, manager):
        """
        Construct.

        Instantiate the DAO class and associate it with a DAO manager,
        which manages the connection.

        @param manager: class implementing AbstractManager
        """
        self._manager = manager
        self.values = {}

    def create(self, sprop):
        """Override abstract method."""
        datatype = "Text"  # default
        if sprop.type == "dateTime":
            datatype = "Date"
        elif sprop.type == "boolean":
            datatype = "Boolean"
        elif sprop.type == "string":
            datatype = "Text"
        elif sprop.type == "DataOneOf":
            datatype = "Text"

        # markdown goes in the MediaWiki page
        markdown = "This is a property of type [[Has type::%s]].\n" % datatype

        if sprop.type == "DataOneOf":
            markdown += "The allowed values for this property are:\n"
            for item in sprop.allowedValues:
                markdown += "[[Allows value::%s]]\n" % item

        self.values['property'] = markdown

        # Send to MediaWiki
        self._manager.commit(sprop.name, self.values)

    def getValues(self):
        """Override abstract method."""
        return self.values
