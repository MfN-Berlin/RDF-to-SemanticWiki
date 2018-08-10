"""
Test.

Created on 12.05.2016

@author: Alvaro.Ortiz
"""

import unittest
from rdf2mw.RDFParser import RDFParser
from DummyDAOFactory import DummyDAOFactory


class test_MakeMarkdownFromRDF(unittest.TestCase):
    """
    Test creating wiki markdown.

    The connector is a dummy which does not actually create pages
    """

    # path to example RDF file
    rdfpath = "testdata/Test.rdf"
    # class variables
    parser = None
    model = None
    factory = None

    def setUp(self):
        """Setup."""
        self.parser = RDFParser()
        self.model = self.parser.parse(self.rdfpath)
        # stores markdown in factory.value, does not create mediawiki pages
        self.factory = DummyDAOFactory()

    def testProperty(self):
        """Test that property markdown is correct."""
        # The "Event" class has a property called "Priority"
        prop = self.model.classes['Entry'].properties['hasPriority']
        dao = self.factory.getDatatypePropertyDAO()
        dao.create(prop)
        result = dao.getValues()['property']
        self.assertTrue("This is a property of type [[Has type::Text]].\n" in result)

    def testSimpleClass(self):
        """Test that template markdown is correct."""
        simpleClass = self.model.classes['Description']
        classDAO = self.factory.getSemanticClassDAO()
        classDAO.create(simpleClass)
        result = classDAO.getValues()['template']
        self.assertTrue("Description" in result)
        self.assertTrue("==Subject" in result)
        self.assertTrue("[[hasSubject::{{{hasSubject|}}}]]" in result)
        self.assertTrue("==Details" in result)
        self.assertTrue("[[hasDetails::{{{hasDetails|}}}]]" in result)

    def testClassWithObjectProperties(self):
        """Test that template markdown is correct."""
        sClass = self.model.classes['Calendar']
        classDAO = self.factory.getSemanticClassDAO()
        classDAO.create(sClass)
        result = classDAO.getValues()['template']
        self.assertTrue("=Entry" in result)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
