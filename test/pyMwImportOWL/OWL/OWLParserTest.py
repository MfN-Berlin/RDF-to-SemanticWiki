'''
Created on 02.05.2016

@author: Alvaro.Ortiz
'''
import unittest
from pyMwImportOWL.OWL.OWLParser import OWLParser

class OWLParserTest(unittest.TestCase):
    parser = None
    owlpath = "../../../example/Calendar.owl"

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
        self.assertTrue( "Display" in classNames )
        self.assertTrue( "Description" in classNames )


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
        sclass = model.classes[ 'Display' ]
        propNames = sclass.getPropertyNames()
        self.assertTrue( "hasColorValue" in propNames )
        sclass = model.classes[ 'Entry' ]
        propNames = sclass.getPropertyNames()
        self.assertTrue( "hasLocation" in propNames )
        
        
    def testParseRanges(self):
        model = self.parser.parse( self.owlpath )
        sclass = model.classes[ 'Event' ]
        self.assertEqual( "dateTime", sclass.properties["hasEndDate"].type )
        self.assertEqual( "dateTime", sclass.properties["hasStartDate"].type )
        self.assertEqual( "boolean", sclass.properties["isWholeDay"].type )

        
    def testParseRangeOneOf(self):
        model = self.parser.parse( self.owlpath )
        sclass = model.classes[ 'Display' ]
        self.assertEqual( "DataOneOf", sclass.properties["hasColorValue"].type )
        self.assertEqual( ['#0000ff', '#00ff00', '#00ffff', '#ff0000', '#ff00ff', '#ffff00', '#ffffff'], sclass.properties["hasColorValue"].allowedValues )
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()