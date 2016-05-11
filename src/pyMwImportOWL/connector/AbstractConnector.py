'''
Created on 15.03.2016
Abstract base class for all connectors
@author: Alvaro.Ortiz
'''
class AbstractConnector:
    
    def login(self):
        raise NotImplementedError        
        
    def loadPage(self, title, content):
        raise NotImplementedError
    
    def createPage(self, title, content):
        raise NotImplementedError
    
    def deletePage(self, title):
        raise NotImplementedError
    
    def content(self):
        raise NotImplementedError
        