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
        self.factory = DummyDAOFactory(  ) # stores markdown in factory.value, does not create mediawiki pages


    def tearDown(self):
        pass


    def testProperty(self):
        # The "Event" class has a property called "Priority"
        prop = self.model.classes[ 'Entry' ].properties[ 'hasPriority' ]
        dao = self.factory.getSemanticPropertyDAO()
        dao.create( prop )
        self.assertTrue( "This is a property of type [[Has type::Text]].\n" in self.factory._manager.value)


    def testSimpleClass(self):
        simpleClass = self.model.classes[ 'Description' ]
        classDAO = self.factory.getSemanticClassDAO()
        classDAO.create( simpleClass )
        self.assertTrue( "=Description=" in self.factory._manager.value )
        self.assertTrue( "'''hasSubject''': [[hasSubject::{{{hasSubject|}}}]]" in classDAO.getValue() )
        self.assertTrue( "'''hasDetails''': [[hasDetails::{{{hasDetails|}}}]]" in classDAO.getValue() )
        # Don't create a "Location" template if doing a "Description" template (don't mix up class variables with instance variables)
        self.assertFalse( "{{Location" in classDAO.getValue() )


    def testUnionClass(self):
        uclass = self.model.classes[ 'Entry' ]
        classDAO = self.factory.getSemanticClassDAO()
        classDAO.create( uclass )
        self.assertTrue( "=Entry=" in classDAO.getValue() ) 
        self.assertTrue( "'''hasPriority''': [[hasPriority::{{{hasPriority|}}}]]" in classDAO.getValue() )
        self.assertTrue( "==Event==" in classDAO.getValue() ) 
        self.assertTrue( "==Description==" in classDAO.getValue() ) 
        self.assertTrue( "==Location==" in classDAO.getValue() ) 
        self.assertFalse( "==Calendar==" in classDAO.getValue() ) 
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()