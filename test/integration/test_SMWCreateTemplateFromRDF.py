"""
Test.

Created on 12.05.2016
Reads an ontology file, parses it and stores the correspondin templates in a wiki.

@author: Alvaro.Ortiz
"""
import unittest
import configparser
from rdf2mw.RDFParser import RDFParser
from smw.MediaWikiApiConnector import MediaWikiApiConnector
from smw.Factory import Factory


class test_SMWCreateTemplateFromRDF(unittest.TestCase):
    """
    Test.

    Test creating pages in the wiki (e.g. using a test wiki)
    The connector actually creates pages here
    """

    # path to configuration file
    configPath = "./test.ini"
    # path to example RDF file
    rdfpath = "testdata/Test.rdf"

    def setUp(self):
        """Setup."""
        # Read the configuration file
        config = configparser.ConfigParser()
        config.read(self.configPath)

        self.parser = RDFParser()
        self.model = self.parser.parse(self.rdfpath)
        self.connector = MediaWikiApiConnector(config)
        self.factory = Factory(self.connector, "/src/smw/templates")

    def tearDown(self):
        """Teardown."""
        self.connector.deletePage("Template:Entry")
        self.connector.deletePage("Template:Event")
        self.connector.deletePage("Template:Location")
        self.connector.deletePage("Template:Description")
        self.connector.deletePage("Form:Description")
        self.connector.deletePage("Property:hasPriority")

    def testProperty(self):
        """Test that a property page can be created."""
        # The "Event" class has a property called "Priority"
        prop = self.model.classes['Entry'].properties['hasPriority']
        dao = self.factory.getDatatypePropertyDAO()
        dao.create(prop)
        resp = self.connector.loadPage("Property:" + prop.name)
        self.assertTrue(resp)

    def testSimpleClass(self):
        """Test that a template can be created."""
        simpleClass = self.model.classes['Description']
        dao = self.factory.getSemanticClassDAO()
        dao.create(simpleClass)
        # the template should be in the wiki
        resp = self.connector.loadPage("Template:" + simpleClass.name)
        self.connector.deletePage("Template:" + simpleClass.name)
        self.assertTrue(resp)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
