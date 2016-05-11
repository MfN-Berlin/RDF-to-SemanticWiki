'''
Created on 15.03.2016

@author: Alvaro.Ortiz
'''
import unittest
import ConfigParser
from pyMwImportOWL.connector.MediaWikiApiConnector import MediaWikiApiConnector

class Test(unittest.TestCase):
    '''Path to configuration file'''
    configPath =  "../../../example/config.ini"
    config = None
    connector = None

    def setUp(self):
        # Read the configuration file
        self.config = ConfigParser.ConfigParser()
        self.config.read( self.configPath )
        
        # Instantiate the connector
        self.connector = MediaWikiApiConnector( self.config )


    def tearDown(self):
        pass


    def testReadConfigFile(self):
        self.assertEqual( 'http://test.biowikifarm.net/test26wmf5/', self.config.get( 'defaults', 'baseMwURL' ) )


    def testInstantiate(self):
        self.assertTrue( self.connector )
        

    def testLogin(self):
        self.assertTrue( self.connector.login() )
        
        
    def testCreatePage(self):
        # Note: page has to be regular content page for this test, not a special page
        self.assertTrue( self.connector.createPage( 'Test', 'Test content' ) )
        self.assertTrue( self.connector.loadPage( 'Test' ) )
        self.assertTrue( self.connector.deletePage( 'Test' ) )


if __name__ == "__main__":
    unittest.main()