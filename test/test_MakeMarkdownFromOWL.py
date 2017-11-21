"""
Test.

Created on 12.05.2016

@author: Alvaro.Ortiz
"""

import unittest
from rdf2mw.OWLParser import OWLParser
from DummyDAOFactory import DummyDAOFactory


class test_MakeMarkdownFromOWL(unittest.TestCase):
    """
    Test creating wiki markdown.

    The connector is a dummy which does not actually create pages
    """

    # path to example OWL file
    owlpath = "testdata/Test.owl"
    # class variables
    parser = None
    model = None
    factory = None

    def setUp(self):
        """Setup."""
        self.parser = OWLParser()
        self.model = self.parser.parse(self.owlpath)
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

        # Localized labels and comments are not implemented in OWLParser

        self.assertTrue("==hasSubject==" in result)
        self.assertTrue("[[hasSubject::{{{hasSubject|}}}]]" in result)
        self.assertTrue("==hasDetails==" in result)
        self.assertTrue("[[hasDetails::{{{hasDetails|}}}]]" in result)
        # Don't create a "Location" template if doing a "Description" template
        # (don't mix up class variables with instance variables)
        self.assertFalse("{{hasLocation" in result)

    @unittest.skip("Skip unions for now")
    def testUnionClass(self):
        """Test that pages creted from uniting classes have correct markdown."""
        uclass = self.model.classes['Entry']
        classDAO = self.factory.getSemanticClassDAO()
        classDAO.create(uclass)
        result = classDAO.getValues()['template']
        self.assertTrue("=Entry=" in result)
        self.assertTrue("'''hasPriority''': [[hasPriority::{{{hasPriority|}}}]]" in result)
        self.assertTrue("==Event==" in result)
        self.assertTrue("==Description==" in result)
        self.assertTrue("==Location==" in result)
        self.assertFalse("==Calendar==" in result)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
