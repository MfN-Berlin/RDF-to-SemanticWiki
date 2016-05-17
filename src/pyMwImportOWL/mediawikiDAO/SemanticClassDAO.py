'''
Created on 10.05.2016

@author: Alvaro.Ortiz
'''
from pyMwImportOWL.mediawikiDAO.AbstractDAO import AbstractDAO

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
        
        # Mark-down for the class properties
        response = "=%s=\n" % sclass.name
        for name in sclass.getPropertyNames():
            response += "'''%s''': " % name
            response += "[[%s::{{{%s|}}}]] \n" % ( name, name )
            
        # Mark-down for the properties of union classes
        # Make a call to the template of the class
        for part in sclass.unionOf.values():
            response += "==%s==\n" % part.name
            response += "{{%s\n" % part.name
            for name in part.getPropertyNames():
                response += "| %s = {{{%s|}}}\n" % (name, name)
            response += "}}\n"
                
        # Send to MediaWiki    
        self._manager.commit( "template:" + sclass.name, response )
