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
        pass
 

    def testSimpleClass(self):
        simpleClass = self.model.classes[ 'Description' ]
        dao = self.factory.getSemanticClassDAO()
        dao.create( simpleClass ) 
        # the template should be in the wiki
        resp = self.connector.loadPage( "Template:" + simpleClass.name )
        self.assertTrue( resp )
        resp = self.connector.deletePage( "Template:" + simpleClass.name )
        self.assertTrue( resp )


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()