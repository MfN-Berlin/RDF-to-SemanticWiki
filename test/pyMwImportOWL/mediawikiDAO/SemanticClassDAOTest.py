'''
Created on 10.05.2016

Tests the DAO classes without persisting to a back-end
(using DummyDAOManager)

@author: Alvaro.Ortiz
'''
import unittest
from test.pyMwImportOWL.mediawikiDAO.DummyDAOFactory import DummyDAOFactory
from pyMwImportOWL.model.SemanticClass import SemanticClass
from pyMwImportOWL.model.SemanticProperty import SemanticProperty

class SemanticClassDAOTest(unittest.TestCase):

    def testSimpleClass(self):
        factory = DummyDAOFactory(  )
        sclass = SemanticClass( "test class" )
        sprop = SemanticProperty( "test property" )
        sclass.addProperty( sprop )
        classDAO = factory.getSemanticClassDAO()
        self.assertTrue( classDAO )
        classDAO.create( sclass )
        self.assertTrue( "=test class=" in classDAO.getValue()) # Class name is header 1
        self.assertTrue( "'''test property'''" in classDAO.getValue()) # Properties names are in bold
        self.assertTrue( "[[test property::{{{test property|}}}]]" in classDAO.getValue()) # properties are in semantic mediawiki syntax


    def testUnionClass(self):
        factory = DummyDAOFactory(  )
        sclass = SemanticClass( "test class" )
        uclass = SemanticClass( "test class 2" )
        uclass.addProperty( SemanticProperty( "test property" ) )
        sclass.uniteWith( uclass )
        classDAO = factory.getSemanticClassDAO()
        classDAO.create( sclass )
        self.assertTrue( "{{test class" in classDAO.getValue())
        self.assertTrue( "==test class 2==" in classDAO.getValue()) # union class names are header 2
        self.assertTrue( "{{test class 2" in classDAO.getValue()) # a call to the template of the union class
        self.assertTrue( "| test property = {{{test property|}}}" in classDAO.getValue()) # the property value is passed to the template


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()