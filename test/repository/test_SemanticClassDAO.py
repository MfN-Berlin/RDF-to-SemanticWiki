'''
Created on 10.05.2016

Tests the DAO classes without persisting to a back-end
(using DummyDAOManager)

@author: Alvaro.Ortiz
'''
import unittest
from repository.DummyDAOFactory import DummyDAOFactory
from pyMwImportOWL.model.SemanticClass import SemanticClass
from pyMwImportOWL.model.SemanticProperty import SemanticProperty

class test_SemanticClassDAO(unittest.TestCase):

    def testSimpleClass(self):
        factory = DummyDAOFactory(  )
        sclass = SemanticClass( "test class" )
        sprop = SemanticProperty( "test property" )
        sclass.addProperty( sprop )
        classDAO = factory.getSemanticClassDAO()
        self.assertTrue( classDAO )
        classDAO.create( sclass )
        template = classDAO.getValues()['template']
        self.assertTrue( "=test class=" in template) # Class name is header 1
        self.assertTrue( "'''test property'''" in template) # Properties names are in bold
        self.assertTrue( "[[test property::{{{test property|}}}]]" in template) # properties are in semantic mediawiki syntax


    def testUnionClass(self):
        factory = DummyDAOFactory(  )
        sclass = SemanticClass( "test class" )
        uclass = SemanticClass( "test class 2" )
        uclass.addProperty( SemanticProperty( "test property" ) )
        sclass.uniteWith( uclass )
        classDAO = factory.getSemanticClassDAO()
        classDAO.create( sclass )
        template = classDAO.getValues()['template']
        self.assertTrue( "{{test class" in template )
        self.assertTrue( "==test class 2==" in template ) # union class names are header 2
        self.assertTrue( "{{test class 2" in template ) # a call to the template of the union class
        self.assertTrue( "| test property = {{{test property|}}}" in template ) # the property value is passed to the template


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
