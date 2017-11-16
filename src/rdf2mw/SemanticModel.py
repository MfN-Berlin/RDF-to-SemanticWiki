"""
Describes an ontology as a simple object oriented model.

Created on 03.05.2016
@author: Alvaro.Ortiz
"""


class SemanticModel:
    """
    A class for representing a semantic model in an object oriented way.

    Classes are stored in a dictionary.
    """

    def __init__(self):
        """Construct a semantic model class."""
        # dictionary of name -> class
        self.classes = {}

    def addClass(self, sclass):
        """Add a semantic class to the model."""
        self.classes[sclass.name] = sclass

    def countClasses(self):
        """
        Count semantic classes in the model.

        @return: count
        """
        return len(self.classes)

    def getClassNames(self):
        """
        Get the names of the semantic classes in the model.

        @return array of strings
        """
        return self.classes.keys()


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

    @property
    def datatypeProperties(self):
        """
        Get the datatype properties of this class.

        @return a list of DatatypeProperty objects
        """
        resp = []
        for prop in self.properties.values():
            if isinstance(prop, DatatypeProperty):
                resp.append(prop)
        return resp

    @property
    def objectProperties(self):
        """
        Get the object properties of this class.

        @return a list of ObjectProperty objects
        """
        resp = []
        for prop in self.properties.values():
            if isinstance(prop, ObjectProperty):
                resp.append(prop)
        return resp


class SemanticProperty:
    """Represents a semantic property."""

    def __init__(self):
        """Make this class abstract."""
        raise NotImplementedError


class DatatypeProperty(SemanticProperty):
    """Represents a datatype property."""

    def __init__(self, name):
        """Constructor."""
        self.name = name
        self.domain = None
        self.range = None
        self.label = {}
        self.allowedValues = None


class ObjectProperty(SemanticProperty):
    """Represents an object property property."""

    def __init__(self, name):
        """Constructor."""
        self.name = name
        self.domain = None
        self.range = None
        self.label = {}
