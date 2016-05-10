'''
Created on 10.05.2016

Tests the DAO classes without persisting to a back-end
(using DummyDAOManager)

@author: Alvaro.Ortiz
'''
import unittest
from test.pyMwImportOWL.MwDAO.DummyDAOManager import DummyDAOManager
from pyMwImportOWL.model.SemanticClass import SemanticClass
from pyMwImportOWL.model.SemanticProperty import SemanticProperty

class SemanticClassDAOTest(unittest.TestCase):

    def testSimpleClass(self):
        manager = DummyDAOManager( None )
        sclass = SemanticClass( "test class" )
        sprop = SemanticProperty( "test property" )
        sclass.addProperty( sprop )
        classDAO = manager.getSemanticClassDAO()
        self.assertTrue( classDAO )
        classDAO.create( sclass )
        self.assertTrue( "=test class=" in manager.value)
        self.assertTrue( "==test property==" in manager.value)
        self.assertTrue( "[[test property::{{{test property|}}}]]" in manager.value)

    '''
    def testUnionClass(self):
        manager = DummyDAOManager( None )
        sclass = SemanticClass( "test class" )
        sprop = SemanticProperty( "test property" )
        sclass.addProperty( sprop )
        classDAO = manager.getSemanticClassDAO()
        self.assertTrue( classDAO )
        classDAO.create( sclass )
        self.assertTrue( "{{test class" in manager.value)
        self.assertTrue( "| test property =" in manager.value)
        self.assertTrue( "}}" in manager.value)
    '''

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()