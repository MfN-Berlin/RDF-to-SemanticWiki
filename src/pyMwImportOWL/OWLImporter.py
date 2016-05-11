'''
Created on 02.05.2016

@author: Alvaro.Ortiz
'''

class OWLImporter:
    '''
    Import an OWL file into a semantic MediaWiki
    '''
    _parser = None
    _daoFactory = None

    def __init__(self, parser, daoFactory ):
        '''
        Constructor
        @param parser: parses an OWL file into a dom object
        @param converter: converts a dom object into MediaWiki API calls
        @param connector: connects to the MediaWiki semantic API 
        '''
        self._parser = parser
        self._daoFactory = daoFactory


    def run(self, path):
        '''Import OWL file
        @param path: OWL file to import
        '''
        model = self._parser.parse( path )
        
        