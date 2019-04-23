# -*- coding: utf-8 -*-
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
from smw.Factory import Factory
from smw.MediaWikiApiConnector import MediaWikiApiConnector


class test_SMWImporter(unittest.TestCase):
    """
    Test.

    Test importing the example ontology (example/Calendar.rdf) in a wiki (e.g. using a test wiki)
    The importer actually creates pages here
    """

    # path to configuration file
    configPath = "./test.ini"
    # path to the ontology example
    modelPath = "testdata/Test.rdf"

    def setUp(self):
        """Setup."""
        # Read the configuration file
        config = configparser.ConfigParser()
        config.read(test_SMWImporter.configPath)
        # A parser which can parse RDF
        self.parser = RDFParser()
        # A connector which can login to a MediaWiki through the API
        self.connector = MediaWikiApiConnector(config)
        # A factory for DAO objects which can persist a SemanticModel
        self.daoFactory = Factory(self.connector, "templates")
        # A wrapper for the import process
        self.importer = Importer(self.parser, self.daoFactory)

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

    def test_CategoryPagesCreated(self):
        """Test that a Category: page was created for each class in the example ontology."""
        self.importer.run(self.modelPath)
        self.assertTrue(self.connector.loadPage("Category:Entry"))
        self.assertTrue(self.connector.loadPage("Category:Event"))
        self.assertTrue(self.connector.loadPage("Category:Location"))
        self.assertTrue(self.connector.loadPage("Category:Description"))
        self.assertTrue(self.connector.loadPage("Category:Calendar"))

    def test_DataPropertyPagesCreated(self):
        """Test that a property: page was created for each datatype property in the example ontology."""
        self.importer.run(self.modelPath)
        self.assertTrue(self.connector.loadPage("Property:hasDetails"))
        self.assertTrue(self.connector.loadPage("Property:hasDirections"))
        self.assertTrue(self.connector.loadPage("Property:hasName"))
        self.assertTrue(self.connector.loadPage("Property:hasPriority"))
        self.assertTrue(self.connector.loadPage("Property:hasStartDate"))
        self.assertTrue(self.connector.loadPage("Property:hasSubject"))
        self.assertTrue(self.connector.loadPage("Property:isWholeDay"))

    def test_ObjectPropertyPagesCreated(self):
        """Test that a property: page was created for each object property in the example ontology."""
        self.importer.run(self.modelPath)
        self.assertTrue(self.connector.loadPage("Property:hasLocation"))

    def test_PropertiesAddedToClassTemplates(self):
        """Test that the property markup is added to the template pages."""
        self.importer.run(self.modelPath)

        self.connector.loadPage("Template:Entry")
        self.assertTrue("hasPriority" in self.connector.content)

        self.connector.loadPage("Template:Location")
        self.assertTrue("hasDirections" in self.connector.content)
        self.assertTrue("hasName" in self.connector.content)

        self.connector.loadPage("Template:Description")
        self.assertTrue("hasDetails" in self.connector.content)
        self.assertTrue("hasSubject" in self.connector.content)

        self.connector.loadPage("Template:Event")
        self.assertTrue("hasStartDate" in self.connector.content)
        self.assertTrue("hasEndDate" in self.connector.content)
        self.assertTrue("isWholeDay" in self.connector.content)

    def test_PropertyLocalization(self):
        """Test that the localized property labels are added to the template pages."""
        self.importer.run(self.modelPath, language='de')

        self.connector.loadPage("Template:Description")
        # datatype property
        self.assertTrue("Details" in self.connector.content)

        self.connector.loadPage("Template:Event")
        # datatype property
        self.assertTrue("Enddatum" in self.connector.content)

        self.connector.loadPage("Template:Entry")
        # object property
        self.assertTrue("Beschreibung" in self.connector.content)

        self.connector.loadPage("Template:Description")
        # datatype property
        self.assertTrue("Das ist der Absatz mit den ganzen Details." in self.connector.content)

    def test_deleteOntologyFromWiki(self):
        """Test that an ontology can be deleted from the wiki."""
        self.importer.run(self.modelPath)

        self.assertTrue(self.connector.loadPage("Template:Entry"))
        self.assertTrue(self.connector.loadPage("Form:Entry"))
        self.assertTrue(self.connector.loadPage("Category:Entry"))
        # test a data property
        self.assertTrue(self.connector.loadPage("Property:hasDetails"))
        # test an object property
        self.assertTrue(self.connector.loadPage("Property:hasLocation"))

        self.importer.delete(self.modelPath)

        self.assertFalse(self.connector.loadPage("Template:Entry"))
        self.assertFalse(self.connector.loadPage("Form:Entry"))
        self.assertFalse(self.connector.loadPage("Category:Entry"))
        # test a data property
        self.assertFalse(self.connector.loadPage("Property:hasDetails"))
        # test an object property
        self.assertFalse(self.connector.loadPage("Property:hasLocation"))

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

        self.connector.deletePage("Category:Entry")
        self.connector.deletePage("Category:Event")
        self.connector.deletePage("Category:Location")
        self.connector.deletePage("Category:Description")
        self.connector.deletePage("Category:Calendar")

        self.connector.deletePage("Property:hasDetails")
        self.connector.deletePage("Property:hasDirections")
        self.connector.deletePage("Property:hasName")
        self.connector.deletePage("Property:hasPriority")
        self.connector.deletePage("Property:hasStartDate")
        self.connector.deletePage("Property:hasEndDate")
        self.connector.deletePage("Property:hasSubject")
        self.connector.deletePage("Property:isWholeDay")
        self.connector.deletePage("Property:hasLocation")

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
