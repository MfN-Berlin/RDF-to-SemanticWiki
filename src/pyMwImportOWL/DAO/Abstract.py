'''
Created on 04.05.2016
@author: Alvaro.Ortiz
'''

class AbstractDAOManager():
    def commit(self, key, value):
        raise NotImplementedError
    
    def getSemanticPropertyDAO(self):
        raise NotImplementedError
    
    def getSemanticClassDAO(self):
        raise NotImplementedError

class AbstractDAO:
    def create(self, obj):
        '''
        This method creates whatever string or query is necessary for persisting the in-memory object.
        This method should always call the commit method from the associated DAO manager
        
        Example:
        
        class myDAO( AbstractDAO ):
           manager = None
           
           __init__( self, myDAOManagermanager ):
              self.manager = myDAOManager
        
           create( self, myObj ):
              query = "...put some SQL here..."
              self.manager.commit( myObj.name, query ) 
        
        '''
        raise NotImplementedError

