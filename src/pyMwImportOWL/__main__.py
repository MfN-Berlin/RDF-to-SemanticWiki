'''
Created on 02.05.2016
Import an Ontology in OWL format into a semantic MediaWiki

@author: Alvaro.Ortiz
'''
import sys, traceback, ConfigParser
from pyMwImportOWL.OWLImporter import OWLImporter
from pyMwImportOWL.parser.OWLParser import OWLParser
from pyMwImportOWL.repository.Factory import Factory
from pyMwImportOWL.connector.MediaWikiApiConnector import MediaWikiApiConnector

'''Path to configuration file.'''
configPath =  "../../example/config.ini"

def run():
    try:
        #Read the configuration file
        config = ConfigParser.ConfigParser()
        config.read( configPath )

        parser =  OWLParser() # A parser which can parse OWL
        connector = MediaWikiApiConnector( config ) # A connector which can login to a MediaWiki through the API
        daoFactory = Factory( connector ) # A factory for DAO objects which can persist a SemanticModel
        
        importer = OWLImporter( parser, daoFactory ) # A wrapper for the import process
        importer.run()
        
    except:
        traceback.print_exc( file=sys.stdout )
        
if __name__ == "__main__":
    run()