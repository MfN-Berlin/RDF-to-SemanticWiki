"""
Import an Ontology in RDF or OWL format into a semantic MediaWiki.

Created on 02.05.2016

@author: Alvaro.Ortiz
"""

import sys
import configparser
from rdf2mw.Importer import Importer
from rdf2mw.mediawiki.Factory import Factory
from rdf2mw.mediawiki.MediaWikiApiConnector import MediaWikiApiConnector

configPath = "example/config.ini"
"""Path to configuration file."""

try:
    if len(sys.argv) != 2:
        raise Exception("Expected 1 argument: RDF or OWL input file")

    # Read the configuration file
    config = configparser.ConfigParser()
    config.read(configPath)

    modelPath = sys.argv[1]
    if ".rdf" in modelPath:
        # A parser which can parse RDF
        from rdf2mw.RDFParser import RDFParser
        parser = RDFParser()
    elif ".owl" in modelPath:
        # A parser which can parse OWL
        from rdf2mw.OWLParser import OWLParser
        parser = OWLParser()
    else:
        raise Exception("Unknown input file format.")

    # A connector which can login to a MediaWiki through the API
    connector = MediaWikiApiConnector(config)
    # A factory for DAO objects which can persist a SemanticModel
    daoFactory = Factory(connector)
    # A wrapper for the import process
    importer = Importer(parser, daoFactory)

    importer.run(modelPath)

except Exception as e:
    print(e)
