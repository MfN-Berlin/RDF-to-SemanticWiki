"""
Test.

Tests the DAO classes without persisting to a back-end
(using DummyDAOManager)

Created on 04.05.2016

@author: Alvaro.Ortiz
"""
import unittest
from DummyDAOFactory import DummyDAOFactory
from rdf2mw.SemanticModel import DatatypeProperty


class test_DatatypePropertyDAO(unittest.TestCase):
    """Tests the DAO classes without persisting to a back-end (using DummyDAOManager)."""

    def testDatePropertyDAO(self):
        """Test a date property."""
        factory = DummyDAOFactory()
        sprop = DatatypeProperty("testDate")
        sprop.type = "dateTime"
        propDAO = factory.getSemanticPropertyDAO()
        self.assertTrue(propDAO)
        propDAO.create(sprop)
        result = propDAO.getValues()['property']
        self.assertEqual("This is a property of type [[Has type::Date]].\n", result)

    def testOneOfPropertyDAO(self):
        """Test a one-off propety (an enum)."""
        factory = DummyDAOFactory()
        sprop = DatatypeProperty("testOneOf")
        sprop.type = "DataOneOf"
        sprop.allowedValues = [
            '#0000ff', '#00ff00', '#00ffff', '#ff0000', '#ff00ff', '#ffff00', '#ffffff']
        propDAO = factory.getSemanticPropertyDAO()
        self.assertTrue(propDAO)
        propDAO.create(sprop)
        result = propDAO.getValues()['property']
        self.assertTrue("This is a property of type [[Has type::Text]].\n" in result)
        self.assertTrue("[[Allows value::#0000ff]]\n" in result)
        self.assertTrue("[[Allows value::#ffffff]]\n" in result)

    def testDefaultTypePropertyDAO(self):
        """Test a default (text) property."""
        factory = DummyDAOFactory()
        sprop = DatatypeProperty("testDate")
        sprop.type = "xxx"
        propDAO = factory.getSemanticPropertyDAO()
        self.assertTrue(propDAO)
        propDAO.create(sprop)
        result = propDAO.getValues()['property']
        self.assertEqual("This is a property of type [[Has type::Text]].\n", result)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
