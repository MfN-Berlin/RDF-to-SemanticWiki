"""
Test.

Created on 15.03.2016

@author: Alvaro.Ortiz
"""
import unittest
import configparser
from smw.MediaWikiApiConnector import MediaWikiApiConnector


class test_SMWMediaWikiApiConnector(unittest.TestCase):
    """Test."""

    configPath = "./test.ini"
    """Path to configuration file"""

    config = None
    connector = None

    def setUp(self):
        """Setup."""
        # Read the configuration file
        self.config = configparser.ConfigParser()
        self.config.read(self.configPath)

        # Instantiate the connector
        self.connector = MediaWikiApiConnector(self.config)

    def tearDown(self):
        """Tear down."""
        self.connector.deletePage('Test')

    def testReadConfigFile(self):
        """Test that the config file can be read."""
        self.assertIsNotNone(self.config.get('defaults', 'BASE_MW_URL'))

    def testInstantiate(self):
        """Test that a connector can be instantiated."""
        self.assertTrue(self.connector)

    def testLogin(self):
        """Test that login succeeds."""
        self.assertTrue(self.connector.login())

    def testCreatePage(self):
        """Test that a page can be created."""
        # Note: page has to be regular content page for this test, not a special page
        self.assertTrue(self.connector.createPage('Test', 'Test content'))
        self.assertTrue(self.connector.loadPage('Test'))

    def testProtectPage(self):
        """Test that a page can be protected."""
        # Note: page has to be regular content page for this test, not a special page
        self.assertTrue(self.connector.createPage('Test2', 'Test2 content'))
        self.assertTrue(self.connector.protectPage('Test2'))


if __name__ == "__main__":
    unittest.main()
