"""
Import an Ontology in RDF or OWL format into a semantic MediaWiki.

Created on 02.05.2016

@author: Alvaro.Ortiz
"""

import sys
import configparser
from optparse import OptionParser
from rdf2mw.Importer import Importer
from rdf2mw.mediawiki.Factory import Factory
from rdf2mw.mediawiki.MediaWikiApiConnector import MediaWikiApiConnector

configPath = "example/config.ini"
"""Path to configuration file."""

try:
    # Parse command-line options
    optionsParser = OptionParser()
    command = None
    optionsParser.add_option("-a", "--action", dest="command", help="Action can be one of import or remove")
    modelPath = None
    optionsParser.add_option("-i", "--input", dest="modelPath", help="Path to ontology file")
    language = None
    optionsParser.add_option("-l", "--language", dest="language", help="Language of the wiki")
    (options, args) = optionsParser.parse_args()

    # Check file type
    if not (".rdf" in options.modelPath or ".owl" in options.modelPath):
        raise Exception("Unknown file type")
    if ".rdf" in options.modelPath:
        # A parser which can parse RDF
        from rdf2mw.RDFParser import RDFParser
        parser = RDFParser()
    elif ".owl" in options.modelPath:
        # A parser which can parse OWL
        from rdf2mw.OWLParser import OWLParser
        parser = OWLParser()
    else:
        raise Exception("Unknown input file format.")

    # Check command
    if options.command not in ['remove', 'import']:
        raise Exception("Unknown command")

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
    if options.command == "import":
        importer.run(options.modelPath, options.language)
    elif options.command == "remove":
        importer.delete(options.modelPath)
    else:
        raise Exception("Unknown error")

    # return to bash
    sys.exit(0)

except Exception as e:
    print(e)
    optionsParser.print_help()
    sys.exit(1)
