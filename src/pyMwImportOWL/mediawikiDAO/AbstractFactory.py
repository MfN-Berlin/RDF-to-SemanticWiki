'''
Created on 11.05.2016

@author: Alvaro.Ortiz
'''

class AbstractFactory:
    
    def commit(self):
        raise NotImplementedError
    
    def getSemanticPropertyDAO(self):
        raise NotImplementedError
    
    def getSemanticClassDAO(self):
        raise NotImplementedError

