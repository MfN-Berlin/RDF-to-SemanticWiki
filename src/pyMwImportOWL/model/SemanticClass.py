"""
A class for representing a semantic class in an object oriented way.

Created on 10.05.2016

@author: Alvaro.Ortiz
"""


class SemanticClass:
    """
    A class for representing a semantic class in an object oriented way.

    Class properties are stored in a dictionary.
    """

    def __init__(self, name):
        """
        Initialize a class with a given name.

        @param name: string
        """
        self.name = name
        self.properties = {}
        self.unionOf = {}

    def addProperty(self, prop):
        """
        Add a property to the class.

        @param prop: SemanticProperty
        """
        self.properties[prop.name] = prop

    def getPropertyNames(self):
        """
        Get a list of the semantic properties of this class.

        @return array of strings
        """
        return self.properties.keys()

    def uniteWith(self, sclass):
        """Unite this class with another class."""
        self.unionOf[sclass.name] = sclass
