'''
Created on 12.05.2016
Reads an OWL file, parses it and stores the correspondin templates in a wiki.

@author: Alvaro.Ortiz
'''
import unittest, ConfigParser
from pyMwImportOWL.parser.OWLParser import OWLParser
from pyMwImportOWL.connector.MediaWikiApiConnector import MediaWikiApiConnector
from pyMwImportOWL.mediawikiDAO.Factory import Factory


class CreateTemplateFromOWLTest(unittest.TestCase):
    '''
    Test creating pages in the wiki (e.g. using a test wiki)
    The connector actually creates pages here
    '''
    # path to configuration file
    configPath = "../../example/config.ini"
    # path to example OWL file
    owlpath = "../../example/Calendar.owl"
    # class variables
    parser = None
    model = None
    factory = None

    def setUp(self):
        #Read the configuration file
        config = ConfigParser.ConfigParser()
        config.read( self.configPath )        
        
        self.parser = OWLParser()
        self.model = self.parser.parse( self.owlpath )
        self.connector = MediaWikiApiConnector( config )
        self.factory = Factory( self.connector )


    def tearDown(self):
        self.connector.deletePage( "Template:Entry" )
        self.connector.deletePage( "Template:Event" )
        self.connector.deletePage( "Template:Location" )
        self.connector.deletePage( "Template:Description" )
        self.connector.deletePage( "Property:hasPriority" )

 
    def testProperty(self):
        # The "Event" class has a property called "Priority"
        prop = self.model.classes[ 'Entry' ].properties[ 'hasPriority' ]
        dao = self.factory.getSemanticPropertyDAO()
        dao.create( prop )
        resp = self.connector.loadPage( "Property:" + prop.name )
        self.assertTrue( resp )


    def testSimpleClass(self):
        simpleClass = self.model.classes[ 'Description' ]
        dao = self.factory.getSemanticClassDAO()
        dao.create( simpleClass ) 
        # the template should be in the wiki
        resp = self.connector.loadPage( "Template:" + simpleClass.name )
        self.assertTrue( resp )


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()