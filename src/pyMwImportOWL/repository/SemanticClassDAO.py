'''
Created on 10.05.2016

@author: Alvaro.Ortiz
'''
from pyMwImportOWL.repository.AbstractDAO import AbstractDAO

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
        self.value = "=%s=\n" % sclass.name
        for name in sclass.getPropertyNames():
            self.value += "'''%s''': " % name
            self.value += "[[%s::{{{%s|}}}]] \n" % ( name, name )
            
        # Mark-down for the properties of union classes
        # Make a call to the template of the class
        for part in sclass.unionOf.values():
            self.value += "==%s==\n" % part.name
            self.value += "{{%s\n" % part.name
            for name in part.getPropertyNames():
                self.value += "| %s = {{{%s|}}}\n" % (name, name)
            self.value += "}}\n"
                
        # Send to MediaWiki    
        self._manager.commit( "template:" + sclass.name, self.value )


    def getValue(self):
        return self.value