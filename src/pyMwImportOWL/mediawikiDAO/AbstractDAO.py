'''
Created on 04.05.2016
@author: Alvaro.Ortiz
'''

class AbstractDAO:
    def create(self, obj):
        '''
        This method creates whatever string or query is necessary for persisting the in-memory object.
        This method should always call the commit method from the associated DAO manager
        
        Example:
        
        class myDAO( AbstractDAO ):
           _manager = None
           
           __init__( self, myDAOManagermanager ):
              self._manager = myDAOManager
        
           create( self, myObj ):
              query = "...put some SQL here..."
              self._manager.commit( myObj.name, query ) 
        
        '''
        raise NotImplementedError
    
    def getValue(self):
        '''Returns a string representation of the query used for persisting the in-memory object'''
        raise NotImplementedError
        
