"""
Represents a semantic property.

Created on 10.05.2016

@author: Alvaro.Ortiz
"""


class SemanticProperty:
    """Represents a semantic property."""

    def __init__(self, name):
        """Construct the class."""
        self.name = name
        self.type = None
        self.allowedValues = None
