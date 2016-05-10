'''
Created on 02.05.2016
Import an Ontology in OWL format into a semantic MediaWiki

@author: Alvaro.Ortiz
'''
import sys, traceback
from pyMwImportOWL.utilsOWL.OWLImporter import OWLImporter
from pyMwImportOWL.utilsOWL.OWLParser import OWLParser

def run():
    try:
        parser =  OWLParser()
        converter = None
        connector = None
        importer = OWLImporter( parser, converter, connector )
        importer.run()
        
    except:
        traceback.print_exc( file=sys.stdout )
        
if __name__ == "__main__":
    run()