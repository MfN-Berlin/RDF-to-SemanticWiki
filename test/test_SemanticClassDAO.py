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
    layoutpath = "testdata/layout.xml"

    def testSimpleClass(self):
        """Test that template markdown is correct."""
        factory = DummyDAOFactory()
        sclass = SemanticClass("test class")
        sprop = DatatypeProperty("test property")
        sclass.addProperty(sprop)
        classDAO = factory.getSemanticClassDAO()
        self.assertTrue(classDAO)
        classDAO.create(sclass)
        template = classDAO.getValues()['template']
        self.assertTrue("test class" in template)  # Class name is header 1
        self.assertTrue("==test property" in template)  # Properties names H2
        # properties are in semantic mediawiki syntax
        self.assertTrue("[[test property::{{{test property|}}}]]" in template)

    def testLayout(self):
        """Test that the layout file is read and interpreted correctly."""
        factory = DummyDAOFactory(layoutFile=test_SemanticClassDAO.layoutpath)
        # could the layout object be read from file
        self.assertTrue(factory.layout)

    @unittest.skip("Skip unions for now")
    def testUnionClass(self):
        """Test that markdown generated from class unions is correct."""
        factory = DummyDAOFactory()
        sclass = SemanticClass("test class")
        uclass = SemanticClass("test class 2")
        uclass.addProperty(DatatypeProperty("test property"))
        sclass.uniteWith(uclass)
        classDAO = factory.getSemanticClassDAO()
        classDAO.create(sclass)
        template = classDAO.getValues()['template']
        self.assertTrue("{{test class" in template)
        # union class names are header 2
        self.assertTrue("==test class 2" in template)
        # a call to the template of the union class
        self.assertTrue("{{test class 2" in template)
        # the property value is passed to the template
        self.assertTrue("| test property = {{{test property|}}}" in template)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
