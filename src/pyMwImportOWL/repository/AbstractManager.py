'''
Created on 17.05.2016

@author: Alvaro.Ortiz
'''
class AbstractManager():
    
    def commit(self, name, values):
        raise NotImplementedError
