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
    
    def getValues(self):
        '''Returns a dictionary of string representations of the queries used for persisting the in-memory object
        e.g. template->a template, form->a form
        '''
        raise NotImplementedError
        
