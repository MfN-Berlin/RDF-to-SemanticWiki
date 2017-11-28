"""
Factory for DAO objects.

Created on 11.05.2016

@author: Alvaro.Ortiz
"""


class AbstractFactory:
    """Factory for DAO objects."""

    def getDAOManager(self):
        """Get a manager object for managing commits and connection scope."""
        raise NotImplementedError

    def getDatatypePropertyDAO(self):
        """Create a DAO object for the corresponding datatype property class."""
        raise NotImplementedError

    def getObjectPropertyDAO(self):
        """Create a DAO object for the corresponding object property class."""
        raise NotImplementedError

    def getSemanticClassDAO(self):
        """Create a DAO object for the corresponding semantic class."""
        raise NotImplementedError
