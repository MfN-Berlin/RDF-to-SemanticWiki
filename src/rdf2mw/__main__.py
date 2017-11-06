"""
Import an Ontology in OWL format into a semantic MediaWiki.

Created on 02.05.2016

@author: Alvaro.Ortiz
"""

import sys
import traceback
import ConfigParser
from rdf2mw.OWLImporter import OWLImporter
from rdf2mw.parser.OWLParser import OWLParser
from rdf2mw.repository.Factory import Factory
from rdf2mw.connector.MediaWikiApiConnector import MediaWikiApiConnector

configPath = "../../example/config.ini"
"""Path to configuration file."""


def run():
    """Run main function."""
    try:
        # Read the configuration file
        config = ConfigParser.ConfigParser()
        config.read(configPath)

        # A parser which can parse OWL
        parser = OWLParser()
        # A connector which can login to a MediaWiki through the API
        connector = MediaWikiApiConnector(config)
        # A factory for DAO objects which can persist a SemanticModel
        daoFactory = Factory(connector)
        # A wrapper for the import process
        importer = OWLImporter(parser, daoFactory)

        importer.run()

    except:
        traceback.print_exc(file=sys.stdout)


if __name__ == "__main__":
    run()
