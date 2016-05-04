'''
Created on 04.05.2016
Provides a single point of access and connection scoping for the 
DAO objects accessing the MediaWiki API.
@author: Alvaro.Ortiz
'''

class AbstractDAOManager():
    def commit(self, key, value):
        pass
    
    def getSemanticPropertyDAO(self):
        pass

class AbstractDAO:
    def create(self, obj):
        raise NotImplementedError

