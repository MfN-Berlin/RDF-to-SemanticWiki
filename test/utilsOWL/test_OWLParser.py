'''
Created on 02.05.2016

@author: Alvaro.Ortiz
'''
import unittest
from pyMwImportOWL.parser.OWLParser import OWLParser

class test_OWLParser(unittest.TestCase):
    parser = None
    owlpath = "../example/Calendar.owl"

    def setUp(self):
        self.parser = OWLParser()


    def tearDown(self):
        pass


    def testInstantiate(self):
        self.assertTrue( self.parser )


    def testLoadOWLFile(self):
        self.assertTrue( self.parser.parse( self.owlpath ) )


    def testParseClasses(self):
        model = self.parser.parse( self.owlpath )
        self.assertEqual( 5, model.countClasses() )
        classNames = model.getClassNames()
        self.assertTrue( "Calendar" in classNames )
        self.assertTrue( "Event" in classNames )
        self.assertTrue( "Entry" in classNames )
        self.assertTrue( "Location" in classNames )
        self.assertTrue( "Description" in classNames )


    def testParseUnion(self):
        model = self.parser.parse( self.owlpath )
        entry = model.classes["Entry"]
        self.assertEquals( 3, len( entry.unionOf ) ) # Entry is composed of classes Event, Description and Location


    def testParseNotUnion(self):
        model = self.parser.parse( self.owlpath )
        entry = model.classes["Description"]
        self.assertEquals( 0, len( entry.unionOf ) ) # Description doesn't have union classes


    def testParseDomains(self):
        model = self.parser.parse( self.owlpath )
        sclass = model.classes[ 'Event' ]
        propNames = sclass.getPropertyNames()
        self.assertTrue( "hasStartDate" in propNames )
        self.assertTrue( "hasEndDate" in propNames )
        self.assertTrue( "isWholeDay" in propNames )
        sclass = model.classes[ 'Description' ]
        propNames = sclass.getPropertyNames()
        self.assertTrue( "hasSubject" in propNames )
        self.assertTrue( "hasDetails" in propNames )
        sclass = model.classes[ 'Location' ]
        propNames = sclass.getPropertyNames()
        self.assertTrue( "hasName" in propNames )
        self.assertTrue( "hasDirections" in propNames )
        sclass = model.classes[ 'Entry' ]
        propNames = sclass.getPropertyNames()
        self.assertTrue( "hasPriority" in propNames )


    def testParseRanges(self):
        model = self.parser.parse( self.owlpath )
        sclass = model.classes[ 'Event' ]
        self.assertEqual( "dateTime", sclass.properties["hasEndDate"].type )
        self.assertEqual( "dateTime", sclass.properties["hasStartDate"].type )
        self.assertEqual( "boolean", sclass.properties["isWholeDay"].type )


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
