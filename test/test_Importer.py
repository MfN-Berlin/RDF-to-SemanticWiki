"""
Test.

Created on 08.11.2017
Reads the example ontology file, parses it and stores the corresponding pages in a wiki.

@author: Alvaro.Ortiz
"""
import unittest
import configparser
from rdf2mw.RDFParser import RDFParser
from rdf2mw.Importer import Importer
from rdf2mw.mediawiki.Factory import Factory
from rdf2mw.mediawiki.MediaWikiApiConnector import MediaWikiApiConnector


class test_Importer(unittest.TestCase):
    """
    Test.

    Test importing the example ontology (example/Calendar.rdf) in a wiki (e.g. using a test wiki)
    The importer actually creates pages here
    """

    # path to configuration file
    configPath = "../example/config.ini"
    # path to the ontology example
    modelPath = "../example/Calendar.rdf"


    def setUp(self):
        """Setup."""
        # Read the configuration file
        config = configparser.ConfigParser()
        config.read(test_Importer.configPath)
        # A parser which can parse RDF
        self.parser = RDFParser()
        # A connector which can login to a MediaWiki through the API
        self.connector = MediaWikiApiConnector(config)
        # A factory for DAO objects which can persist a SemanticModel
        self.daoFactory = Factory(self.connector)
        # A wrapper for the import process
        self.importer = Importer(self.parser, self.daoFactory)

    def tearDown(self):
        """Teardown."""
        self.connector.deletePage("Template:Entry")
        self.connector.deletePage("Template:Event")
        self.connector.deletePage("Template:Location")
        self.connector.deletePage("Template:Description")
        self.connector.deletePage("Template:Calendar")
        self.connector.deletePage("Form:Entry")
        self.connector.deletePage("Form:Event")
        self.connector.deletePage("Form:Location")
        self.connector.deletePage("Form:Description")
        self.connector.deletePage("Form:Calendar")

    def testImporterRun(self):
        """Test if the Importer runs at all."""
        try:
            self.importer.run(self.modelPath)
            self.assertTrue(True)
        except:
            self.assertFalse(True)

    def test_ClassPagesCreated(self):
        """Test that a form: and a template: page was created for each class in the example ontology."""
        self.importer.run(self.modelPath)
        self.assertTrue(self.connector.loadPage("Template:Entry"))
        self.assertTrue(self.connector.loadPage("Template:Event"))
        self.assertTrue(self.connector.loadPage("Template:Location"))
        self.assertTrue(self.connector.loadPage("Template:Description"))
        self.assertTrue(self.connector.loadPage("Template:Calendar"))
        self.assertTrue(self.connector.loadPage("Form:Entry"))
        self.assertTrue(self.connector.loadPage("Form:Event"))
        self.assertTrue(self.connector.loadPage("Form:Location"))
        self.assertTrue(self.connector.loadPage("Form:Description"))
        self.assertTrue(self.connector.loadPage("Form:Calendar"))


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()