"""
Describes an ontology as a simple object oriented model.

Created on 03.05.2016
@author: Alvaro.Ortiz
"""

from lxml import etree


class SemanticModel:
    """
    A class for representing a semantic model in an object oriented way.

    Classes are stored in a dictionary.
    """

    def __init__(self):
        """Construct a semantic model class."""
        # dictionary of name -> class
        self.classes = {}
        # dictionary of name -> enum
        self.enums = {}

    def addClass(self, sclass):
        """Add a semantic class to the model."""
        self.classes[sclass.name] = sclass

    def addEnum(self, enum):
        """Add an enumeration to the model."""
        self.enums[enum.name] = enum

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

    def __str__(self):
        resp = ""
        for e in self.enums:
            resp += self.enums[e].serialize()    
        for c in self.classes:
            resp += self.classes[c].serialize()
        return resp


class SemanticElement:
    """Base class for all semantic elements."""

    def __init__(self, name):
        """
        Construct.

        Usually, you'd want to instantiate one of the child classes.
        """
        self.name = name
        self._label = {}
        self._comment = {}

    def getLabel(self, lang=None):
        """Get the localized label of this element."""
        resp = self.name
        if lang is not None and lang in self._label:
            resp = self._label[lang]
        return resp

    def addLabel(self, value, lang):
        """Add a localized label to this element."""
        self._label[lang] = value

    def getComment(self, lang=None):
        """Get the localized comment of this element."""
        resp = None
        if lang is not None and lang in self._comment:
            resp = self._comment[lang]
        return resp

    def addComment(self, value, lang):
        """Add a localized comment to this element."""
        self._comment[lang] = value

    def asElementTree(self):
        """
        Get a representation of this semantic class as an XML element tree.

        @return etree
        """
        # name
        selm = etree.Element(self.__class__.__name__)
        selm.set('name', self.name)

        # labels
        labels = etree.Element('labels')
        for key, val in self._label.items():
            label = etree.Element('label')
            label.set('lang', key)
            label.text = val
            labels.append(label)
        selm.append(labels)

        # comments
        comments = etree.Element('comments')
        for key, val in self._comment.items():
            comment = etree.Element('comment')
            comment.set('lang', key)
            comment.text = val
            comments.append(comment)
        selm.append(comments)

        return(selm)

    def serialize(self):
        """
        Get a string representation of this semantic class as an XML string.

        @return String
        """
        stree = self.asElementTree()
        resp = etree.tostring(stree, encoding="utf8", method="xml")
        return(str(resp))


class SemanticClass(SemanticElement):
    """
    A class for representing a semantic class in an object oriented way.

    Class properties are stored in a dictionary.
    """

    def __init__(self, name):
        """
        Initialize a class with a given name.

        @param name: string
        """
        super().__init__(name)
        self.properties = {}

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

    def asElementTree(self):
        """Override."""
        selm = super().asElementTree()

        for prop in self.properties.values():
            selm.append(prop.asElementTree())

        return(selm)

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


class SemanticProperty(SemanticElement):
    """Represents a semantic property."""

    def __init__(self, name):
        """
        Construct.

        Usually, you'd want to instantiate one of the child classes.
        """
        super().__init__(name)
        self.domain = None
        self._range = None
        self._allowedValues = {}
        self._cardinality = None

    @property
    def range(self):
        """Getter for range property."""
        return self._range

    @range.setter
    def range(self, value):
        """Setter for range property."""
        self._range = value
        if self.range == "boolean":
            self.allowedValues = {'true', 'false'}

    @property
    def cardinality(self):
        """Getter for cardinality property."""
        return self._cardinality

    @cardinality.setter
    def cardinality(self, value):
        """
        Setter for cardinality property.

        Allowed values are None (no constraints apply) and 'FunctionalProperty' (there can be only one of).
        @see https://www.w3.org/TR/owl-ref/#FunctionalProperty-def
        """
        self._cardinality = value

    @property
    def allowedValues(self):
        """Getter for allowedValues."""
        return self._allowedValues

    @allowedValues.setter
    def allowedValues(self, values):
        """
        Setter for allowedValues property.

        Allowed values are None (no constraints apply) or an array of values.
        """
        self._allowedValues = values

    def asElementTree(self):
        """Override."""
        selm = super().asElementTree()
        if self._range:
            selm.set('range', self._range)
        if self.domain:
            selm.set('domain', self.domain)
        if self.allowedValues:
            allowedValues = etree.Element('allowedValues')
            for val in self.allowedValues:
                allowed = etree.Element('allowed')
                allowed.text = val
                allowedValues.append(allowed)
            selm.append(allowedValues)
        if self.cardinality:
            selm.set('cardinality', self.cardinality)

        return(selm)


class DatatypeProperty(SemanticProperty):
    """Represents a datatype property."""

    def __init__(self, name):
        """Constructor."""
        super().__init__(name)


class ObjectProperty(SemanticProperty):
    """Represents an object property."""

    def __init__(self, name):
        """Constructor."""
        super().__init__(name)


class Enumeration(SemanticProperty):
    """A class description of the enumeration kind."""

    def __init__(self, name):
        """Constructor."""
        super().__init__(name)
        self.items = []

    def add(self, item):
        """Append an item to the enumeration."""
        self.items.append(item)

    def asList(self):
        """Return a representation of the enumeration as list."""
        resp = []
        for item in self.items:
            resp.append(item.text)
        return resp

    def asElementTree(self):
        """Override."""
        selm = super().asElementTree()

        for item in self.items:
            selm.append(item)

        return(selm)
