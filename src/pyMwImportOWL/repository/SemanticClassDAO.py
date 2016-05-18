'''
Created on 10.05.2016

@author: Alvaro.Ortiz
'''
from pyMwImportOWL.repository.AbstractDAO import AbstractDAO

class SemanticClassDAO( AbstractDAO ):
    _manager = None
    
    def __init__( self, manager ):
        '''Instantiate the DAO class and associate it with a DAO manager, which manages the connection
        @param manager: class implementing AbstractDAOManager 
        '''
        self._manager = manager
        self.values = {}


    def create( self, sclass ):
        '''Create a Semantic MediaWiki template for the class
        @param sprop: SemanticClass
        AbstractDAO.create(self, obj)
        '''
        
        # Mark-down for the class properties
        template = "=%s=\n" % sclass.name
        for name in sclass.getPropertyNames():
            template += "'''%s''': " % name
            template += "[[%s::{{{%s|}}}]] \n" % ( name, name )
            
        # Mark-down for the properties of union classes
        # Make a call to the template of the class
        for part in sclass.unionOf.values():
            template += "==%s==\n" % part.name
            template += "{{%s\n" % part.name
            for name in part.getPropertyNames():
                template += "| %s = {{{%s|}}}\n" % (name, name)
            template += "}}\n"
        
        self.values["template"] = template
        
        # Mark-down for the form
        form = "<noinclude>{{#forminput:form=%s}}</noinclude>" % sclass.name
        form += "<includeonly>{{{for template|%s}}}" % sclass.name
        form += "{{{end template}}}"
        form += "{{{standard input|minor edit}}} {{{standard input|watch}}}{{{standard input|save}}} {{{standard input|changes}}} {{{standard input|cancel}}}"
        form += "__NOTOC__"
        form += "__NOEDITSECTION__"
        form += "</includeonly>"
        
        self.values["form"] = form
        
        # Send to MediaWiki
        self._manager.commit( sclass.name, self.values )


    def getValues(self):
        '''
        @return dictionary
        '''
        return self.values
