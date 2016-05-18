'''
Created on 04.05.2016

Tests the DAO classes without persisting to a back-end
(using DummyDAOManager)

@author: Alvaro.Ortiz
'''
import unittest
from test.pyMwImportOWL.repository.DummyDAOFactory import DummyDAOFactory
from test.pyMwImportOWL.repository.DummyDAOFactory import DummyManager
from pyMwImportOWL.model.SemanticProperty import SemanticProperty


class SemanticPropertyDAOTest(unittest.TestCase):

    def testDatePropertyDAO(self):
        factory = DummyDAOFactory(  )
        sprop = SemanticProperty( "testDate" )
        sprop.type= "dateTime"
        propDAO = factory.getSemanticPropertyDAO()
        self.assertTrue( propDAO )
        propDAO.create( sprop )
        result = propDAO.getValues()['property']
        self.assertEqual( "This is a property of type [[Has type::Date]].\n", result )
        
        
    def testOneOfPropertyDAO(self):
        factory = DummyDAOFactory(  )
        sprop = SemanticProperty( "testOneOf" )
        sprop.type= "DataOneOf"
        sprop.allowedValues = ['#0000ff', '#00ff00', '#00ffff', '#ff0000', '#ff00ff', '#ffff00', '#ffffff']
        propDAO = factory.getSemanticPropertyDAO()
        self.assertTrue( propDAO )
        propDAO.create( sprop )
        result = propDAO.getValues()['property']
        self.assertTrue( "This is a property of type [[Has type::Text]].\n" in result )
        self.assertTrue( "[[Allows value::#0000ff]]\n" in result )
        self.assertTrue( "[[Allows value::#ffffff]]\n" in result )


    def testDefaultTypePropertyDAO(self):
        factory = DummyDAOFactory(  )
        sprop = SemanticProperty( "testDate" )
        sprop.type= "xxx"
        propDAO = factory.getSemanticPropertyDAO()
        self.assertTrue( propDAO )
        propDAO.create( sprop )
        result = propDAO.getValues()['property']
        self.assertEqual( "This is a property of type [[Has type::Text]].\n", result )
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()