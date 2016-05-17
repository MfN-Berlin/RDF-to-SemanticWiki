'''
Created on 12.05.2016

@author: Alvaro.Ortiz
'''
import unittest
from pyMwImportOWL.parser.OWLParser import OWLParser
from test.pyMwImportOWL.mediawikiDAO.DummyDAOFactory import DummyDAOFactory

class MakeMarkdownFromOWLTest(unittest.TestCase):
    '''
    Test creating wiki markdown
    The connector is a dummy which does not actually create pages
    '''

    # path to example OWL file
    owlpath = "../../example/Calendar.owl"
    # class variables
    parser = None
    model = None
    factory = None


    def setUp(self):
        self.parser = OWLParser()
        self.model = self.parser.parse( self.owlpath )
        self.factory = DummyDAOFactory( None ) # stores markdown in factory.value, does not create mediawiki pages


    def tearDown(self):
        pass


    def testProperty(self):
        # The "Event" class has a property called "Priority"
        prop = self.model.classes[ 'Entry' ].properties[ 'hasPriority' ]
        dao = self.factory.getSemanticPropertyDAO()
        dao.create( prop )
        self.assertTrue( "This is a property of type [[Has type::Text]].\n" in self.factory.value)


    def testSimpleClass(self):
        simpleClass = self.model.classes[ 'Description' ]
        dao = self.factory.getSemanticClassDAO()
        dao.create( simpleClass )
        self.assertTrue( "=Description=" in self.factory.value )
        self.assertTrue( "'''hasSubject''': [[hasSubject::{{{hasSubject|}}}]]" in self.factory.value )
        self.assertTrue( "'''hasDetails''': [[hasDetails::{{{hasDetails|}}}]]" in self.factory.value )
        # Don't create a "Location" template if doing a "Description" template (don't mix up class variables with instance variables)
        self.assertFalse( "{{Location" in self.factory.value )


    def testUnionClass(self):
        uclass = self.model.classes[ 'Entry' ]
        dao = self.factory.getSemanticClassDAO()
        dao.create( uclass )
        self.assertTrue( "=Entry=" in self.factory.value ) 
        self.assertTrue( "'''hasPriority''': [[hasPriority::{{{hasPriority|}}}]]" in self.factory.value )
        self.assertTrue( "==Event==" in self.factory.value ) 
        self.assertTrue( "==Description==" in self.factory.value ) 
        self.assertTrue( "==Location==" in self.factory.value ) 
        self.assertFalse( "==Calendar==" in self.factory.value ) 
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()