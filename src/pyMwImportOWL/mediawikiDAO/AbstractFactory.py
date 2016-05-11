'''
Created on 11.05.2016

@author: Alvaro.Ortiz
'''

class AbstractFactory:
    
    def getSemanticPropertyDAO(self):
        raise NotImplementedError
    
    def getSemanticClassDAO(self):
        raise NotImplementedError

    def getSemanticModelDAO(self):
        raise NotImplementedError
