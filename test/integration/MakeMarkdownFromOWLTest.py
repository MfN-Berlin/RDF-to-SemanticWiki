'''
Created on 12.05.2016

@author: Alvaro.Ortiz
'''
import unittest
from pyMwImportOWL.parser.OWLParser import OWLParser
from test.pyMwImportOWL.mediawikiDAO.DummyDAOFactory import DummyDAOFactory

class MakeMarkdownFromOWLTest(unittest.TestCase):
    # path to example OWL file
    owlpath = "../../example/Calendar.owl"
    # class variables
    parser = None
    model = None
    factory = None


    def setUp(self):
        self.parser = OWLParser()
        self.model = self.parser.parse( self.owlpath )
        self.factory = DummyDAOFactory( None ) # stores markup in factory.value, does not create mediawik pages


    def tearDown(self):
        pass


    def testSimpleClass(self):
        simpleClass = self.model.classes[ 'Description' ]
        dao = self.factory.getSemanticClassDAO()
        dao.create( simpleClass )
        self.assertTrue( "=Description=" in self.factory.value )
        self.assertTrue( "'''hasSubject''': [[hasSubject::{{{hasSubject|}}}]]" in self.factory.value )
        self.assertTrue( "'''hasDetails''': [[hasDetails::{{{hasDetails|}}}]]" in self.factory.value )
        # Don't create a "Location" template if doing a "Description" template (don't mix up class variables with instance variables)
        self.assertFalse( "{{Location" in self.factory.value )


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()