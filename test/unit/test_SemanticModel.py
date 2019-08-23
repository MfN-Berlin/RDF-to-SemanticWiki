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

    def test_BooleanDatatype(self):
        """Test that Boolean dataytpe properties have the correct allowed values."""
        dtp = DatatypeProperty("dtp")
        dtp.range = "boolean"
        self.assertEqual(2, len(dtp.allowedValues))

    def testSerializeClass(self):
        """Test if the class can be seralized to XML string."""
        sclass = SemanticClass("test class")
        
        sclass.addLabel("en", "test class")
        sclass.addLabel("de", "Testklasse")
        
        sclass.addComment("en", "a comment")
        sclass.addComment("de", "ein Kommentar")
        
        serialized = sclass.serialize()
        self.assertEqual(1, serialized.count("<SemanticClass"))
        self.assertTrue('name="test class"' in serialized)
        self.assertEqual(2, serialized.count("<label lang"))
        self.assertEqual(2, serialized.count("<comment lang"))

        dtp1 = DatatypeProperty("dtp1")
        sclass.addProperty(dtp1)
        dtp2 = DatatypeProperty("dtp2")
        sclass.addProperty(dtp2)
        op1 = ObjectProperty("op1")
        sclass.addProperty(op1)
        op2 = ObjectProperty("op2")
        sclass.addProperty(op2)
        serialized = sclass.serialize()
        self.assertEqual(2, serialized.count("<DatatypeProperty"))
        self.assertEqual(2, serialized.count("<ObjectProperty"))

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
