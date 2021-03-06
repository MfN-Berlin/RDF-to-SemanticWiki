"""
Test.

Created on 10.05.2016

Tests the DAO classes without persisting to a back-end
(using DummyDAOManager)

@author: Alvaro.Ortiz
"""
import unittest

from DummyDAOFactory import DummyDAOFactory
from rdf2mw.SemanticModel import SemanticClass, DatatypeProperty


class test_SemanticClassDAO(unittest.TestCase):
    """Test."""

    def testSimpleClass(self):
        """Test that template markdown is correct."""
        factory = DummyDAOFactory()
        sclass = SemanticClass("test class")
        sprop = DatatypeProperty("test property")
        sprop.cardinality = 'FunctionalProperty'
        sclass.addProperty(sprop)
        classDAO = factory.getSemanticClassDAO()
        self.assertTrue(classDAO)
        classDAO.create(sclass)
        template = classDAO.getValues()['template']
        self.assertTrue("test class" in template)  # Class name is header 1
        self.assertTrue("==test property" in template)  # Properties names H2
        # properties are in semantic mediawiki syntax
        self.assertTrue("[[test property::{{{test property|}}}]]" in template)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
