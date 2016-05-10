'''
Created on 03.05.2016
Describes an ontology as a simple object oriented model
@author: Alvaro.Ortiz
'''

class SemanticModel:
    '''
    A class for representing a semantic model in an object oriented way.
    Classes are stored in a dictionary.
    '''
    classes = {}
    
    def addClass(self, sclass):
        self.classes[ sclass.name ] = sclass
    
    
    def countClasses(self):
        '''
        @return: 
        '''
        return len( self.classes )
    
    
    def  getClassNames(self):
        '''
        @return array of strings
        '''
        return self.classes.keys()
    

        


        
    
    