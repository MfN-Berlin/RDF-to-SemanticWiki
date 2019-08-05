"""
Import an Ontology in RDF format into a semantic MediaWiki.

Created on 02.05.2016

@author: Alvaro.Ortiz
"""

import sys
import os
import configparser
from optparse import OptionParser
from rdf2mw.Importer import Importer, ImporterException
from smw.Factory import Factory
from smw.MediaWikiApiConnector import MediaWikiApiConnector

configPath = "/rdf/config.ini"
"""Path to configuration file."""

try:
    # Read the configuration file
    config = configparser.ConfigParser()
    config.read(configPath)

    # Parse command-line options
    optionsParser = OptionParser()
    command = None
    optionsParser.add_option("-a", "--action", default="import", dest="command", help="Action can be one of import, remove or test")
    modelPath = None
    optionsParser.add_option("-i", "--input", dest="modelPath", help="Path to ontology file")
    language = None
    optionsParser.add_option("-l", "--language", default="en", dest="language", help="Language of the wiki")
    templateDir = None
    optionsParser.add_option("-t", "--templates", default="src/smw/templates", dest="templateDir", help="Path to template directory")

    (options, args) = optionsParser.parse_args()

    # Check file type
    if not (".rdf" in options.modelPath or ".owl" in options.modelPath):
        raise ImporterException("Unknown file type")
    # A parser which can parse RDF
    from rdf2mw.RDFParser import RDFParser
    parser = RDFParser()

    # Check command
    if options.command not in ['remove', 'import', 'test']:
        raise ImporterException("Unknown command")

    # Path to templates directory
    if options.templateDir is not None:
        tplDir = options.templateDir
    else:
        tplDir = config.get('defaults', 'tplDir')
    if not os.path.isdir(tplDir):
        raise ImporterException("Template directory not found")

    # A connector which can login to a MediaWiki through the API
    connector = MediaWikiApiConnector(config)
    # A factory for DAO objects which can persist a SemanticModel
    daoFactory = Factory(connector, tplDir)
    # A wrapper for the import process
    importer = Importer(parser, daoFactory)

    # Run the importer
    if options.command == "import":
        importer.run(options.modelPath, options.language)
    elif options.command == "remove":
        importer.delete(options.modelPath)
    elif options.command == "test":
        parser.parse(options.modelPath)
        print(str(parser._model))
    else:
        raise ImporterException("Unknown error")

    # return to bash
    sys.exit(0)

except ImporterException as e:
    print(e)
    optionsParser.print_help()
    sys.exit(1)
