"""
Test.

Created on 02.05.2016

@author: Alvaro.Ortiz
"""
import unittest
from rdf2mw.RDFParser import RDFParser


class test_inheritance(unittest.TestCase):
    """Test."""

    parser = None
    rdfpath = "testdata/Test3.rdf"

    def setUp(self):
        """Setup."""
        self.parser = RDFParser()

    def test01(self):
        """Tst that subclass inherits all properties from superclass."""
        model = self.parser.parse(self.rdfpath)
        superclass = model.classes["Superclass"]
        subclass = model.classes["Subclass"]
        self.assertTrue(len(subclass.getPropertyNames()) > 0)
        self.assertEqual(superclass.getPropertyNames(), subclass.getPropertyNames())
