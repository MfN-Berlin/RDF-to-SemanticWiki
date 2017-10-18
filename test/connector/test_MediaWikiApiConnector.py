'''
Created on 15.03.2016

@author: Alvaro.Ortiz
'''
import unittest
import configparser
from src.pyMwImportOWL.connector.MediaWikiApiConnector import MediaWikiApiConnector

class test_MediaWikiApiConnector(unittest.TestCase):
    '''Path to configuration file'''
    configPath =  "../example/config.ini"
    config = None
    connector = None

    def setUp(self):
        # Read the configuration file
        self.config = configparser.ConfigParser()
        self.config.read( self.configPath )

        # Instantiate the connector
        self.connector = MediaWikiApiConnector( self.config )


    def tearDown(self):
        self.connector.deletePage( 'Test' )


    def testReadConfigFile(self):
        self.assertIsNotNone( self.config.get( 'defaults', 'baseMwURL' ) )


    def testInstantiate(self):
        self.assertTrue( self.connector )


    def testLogin(self):
        self.assertTrue( self.connector.login() )


    @unittest.skip("needs more work")
    def testCreatePage(self):
        # Note: page has to be regular content page for this test, not a special page
        self.assertTrue( self.connector.createPage( 'Test', 'Test content' ) )
        self.assertTrue( self.connector.loadPage( 'Test' ) )


if __name__ == "__main__":
    unittest.main()
