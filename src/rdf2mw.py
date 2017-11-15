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

usage = "Usage:\nImport an ontology:\n\t./rdf2mw.sh path-to-rdf-file\nRemove an ontology:\n\t./rdf2mw.sh --remove path-to-rdf-file\n"

try:
    # Check number of arguments
    if not(len(sys.argv) == 2 or len(sys.argv) == 3):
        raise Exception("Wrong number of arguments")

    # Check file type
    modelPath = sys.argv[len(sys.argv)-1]  # path to ontology file is last argument
    if not (".rdf" in modelPath or ".owl" in modelPath):
        raise Exception("Unknown file type")
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

    # Check command
    command = None
    if len(sys.argv) == 3 and not sys.argv[1] in ['remove', 'import']:
        raise Exception("Unknown command")
    if len(sys.argv) == 3:
        command = sys.argv[1]
    else:
        command = "import"

    # Read the configuration file
    config = configparser.ConfigParser()
    config.read(configPath)

    # A connector which can login to a MediaWiki through the API
    connector = MediaWikiApiConnector(config)
    # A factory for DAO objects which can persist a SemanticModel
    daoFactory = Factory(connector)
    # A wrapper for the import process
    importer = Importer(parser, daoFactory)

    # Run the importer
    if command == "import":
        importer.run(modelPath)
    elif command == "remove":
        importer.delete(modelPath)
    else:
        raise Exception("Unknown error")

    # return to bash
    sys.exit(0)

except Exception as e:
    print(e)
    sys.exit(1)
