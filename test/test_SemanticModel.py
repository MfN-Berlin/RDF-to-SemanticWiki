"""
Test.

Created on 10.11.2017

Tests Semantic Classes and Properties

@author: Alvaro.Ortiz
"""
import unittest
from rdf2mw.SemanticModel import SemanticModel, SemanticClass, DatatypeProperty, ObjectProperty


class test_SemanticModel(unittest.TestCase):
    """Test."""

    def test_GetDatatypeProperties(self):
        """Test that getter for datatype properties returns only datatype properties."""
        sclass = SemanticClass("test")
        dtp = DatatypeProperty("dtp")
        op = ObjectProperty("op")
        sclass.addProperty(dtp)
        sclass.addProperty(op)
        self.assertEqual(1, len(sclass.datatypeProperties))

    def test_GetObjectProperties(self):
        """Test that getter for object properties returns only object properties."""
        sclass = SemanticClass("test")
        dtp = DatatypeProperty("dtp")
        op = ObjectProperty("op")
        sclass.addProperty(dtp)
        sclass.addProperty(op)
        self.assertEqual(1, len(sclass.objectProperties))
    
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
