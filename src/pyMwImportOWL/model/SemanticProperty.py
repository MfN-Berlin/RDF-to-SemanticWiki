'''
Created on 10.05.2016

@author: Alvaro.Ortiz
'''
class SemanticProperty:
    name = None
    type = None
    allowedValues = None
    
    def __init__(self, name):
        self.name = name
