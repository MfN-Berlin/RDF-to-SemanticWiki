'''
Created on 10.05.2016

@author: Alvaro.Ortiz
'''
from pyMwImportOWL.DAO.Abstract import AbstractDAO

class SemanticClassDAO( AbstractDAO ):
    _manager = None
    
    def __init__( self, manager ):
        '''Instantiate the DAO class and associate it with a DAO manager, which manages the connection
        @param manager: class implementing AbstractDAOManager 
        '''
        self._manager = manager


    def create( self, sclass ):
        '''Create a Semantic MediaWiki template for the class
        @param sprop: SemanticClass
        AbstractDAO.create(self, obj)
        '''
        '''
        response = "{{%s\n" % sclass.name
        for name in sclass.getPropertyNames():
            response += "| %s = \n" % name
        response += "}}\n"
        '''
        
        response = "=%s=\n" % sclass.name
        for name in sclass.getPropertyNames():
            response += "==%s== \n" % name
            response += "[[%s::{{{%s|}}}]] \n" % ( name, name )
                
        # Send to MediaWiki    
        self._manager.commit( sclass.name, response )

                 
        