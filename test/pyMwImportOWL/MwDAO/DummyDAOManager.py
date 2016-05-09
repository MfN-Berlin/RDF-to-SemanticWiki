'''
Created on 09.05.2016
A DAO Manager which doesn't persist, for testing.

@author: Alvaro.Ortiz
'''
from pyMwImportOWL.MwDAO.DAOManager import DAOManager

class DummyDAOManager(DAOManager):
    key = None
    value = None
    
    '''A dummy class for testing'''
    def commit(self, key, value):
        self.key = key
        self.value = value 
