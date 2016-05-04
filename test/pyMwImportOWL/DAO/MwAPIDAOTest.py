'''
Created on 04.05.2016

Tests the DAO classes without persisting to a back-end
(using DummyDAOManager)

@author: Alvaro.Ortiz
'''
import unittest
from pyMwImportOWL.DAO.MwAPIDAO import MwAPIDAOManager
from pyMwImportOWL.parser.SemanticModel import SemanticProperty

class DummyDAOManager(MwAPIDAOManager):
    key = None
    value = None
    
    '''A dummy class for testing'''
    def commit(self, key, value):
        self.key = key
        self.value = value 


class Test(unittest.TestCase):

    def testDatePropertyDAO(self):
        manager = DummyDAOManager(None)
        sprop = SemanticProperty( "test date" )
        sprop.type= "dateTime"
        propDAO = manager.getSemanticPropertyDAO()
        self.assertTrue( propDAO )
        propDAO.create( sprop )
        self.assertEqual( "This is a property of type [[Has type::Date]].\n", manager.value)
        
        
    def testOneOfPropertyDAO(self):
        manager = DummyDAOManager(None)
        sprop = SemanticProperty( "test oneOf" )
        sprop.type= "DataOneOf"
        sprop.allowedValues = ['#0000ff', '#00ff00', '#00ffff', '#ff0000', '#ff00ff', '#ffff00', '#ffffff']
        propDAO = manager.getSemanticPropertyDAO()
        self.assertTrue( propDAO )
        propDAO.create( sprop )
        self.assertTrue( "This is a property of type [[Has type::Text]].\n" in manager.value)
        self.assertTrue( "[[Allows value::#0000ff]]\n" in manager.value)
        self.assertTrue( "[[Allows value::#ffffff]]\n" in manager.value)


    def testDefaultTypePropertyDAO(self):
        manager = DummyDAOManager(None)
        sprop = SemanticProperty( "test date" )
        sprop.type= "xxx"
        propDAO = manager.getSemanticPropertyDAO()
        self.assertTrue( propDAO )
        propDAO.create( sprop )
        self.assertEqual( "This is a property of type [[Has type::Text]].\n", manager.value)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()