"""
Represents a semantic object property.

Created on 07.11.2017

@author: Alvaro.Ortiz
"""


class SemanticObjectProperty:
    """Represents a semantic object property."""

    def __init__(self, name):
        """Construct the class."""
        self.name = name
        self.domain = None
        self.range = None
