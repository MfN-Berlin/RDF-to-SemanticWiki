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
