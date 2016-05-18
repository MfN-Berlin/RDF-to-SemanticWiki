'''
Created on 17.05.2016

@author: Alvaro.Ortiz
'''
from pyMwImportOWL.repository.AbstractManager import AbstractManager

class Manager( AbstractManager ):
    _connector = None
    
    def __init__(self, connector ):
        self._connector = connector
    
    
    def commit( self, name, values ):
        '''
        Commit the operation in this case using MediaWiki API
        @param key: a string corresponding to a page name
        @param value: a string corresponding to page contents in markdown
        '''
        for key in values.keys():
            pageName = '%s:%s' % ( key, name )
            self._connector.createPage( pageName, values[key] )
