"""
Test.

Created on 02.05.2016

@author: Alvaro.Ortiz
"""
import unittest
from pyMwImportOWL.parser.OWLParser import OWLParser


class test_OWLParser(unittest.TestCase):
    """Test."""

    parser = None
    owlpath = "../example/Calendar.owl"

    def setUp(self):
        """Setup."""
        self.parser = OWLParser()

    def testInstantiate(self):
        """Test."""
        self.assertTrue(self.parser)

    def testLoadOWLFile(self):
        """Test thet a OWL file can be read."""
        self.assertTrue(self.parser.parse(self.owlpath))

    def testParseClasses(self):
        """Test parsng ontology classes."""
        model = self.parser.parse(self.owlpath)
        self.assertEqual(5, model.countClasses())
        classNames = model.getClassNames()
        self.assertTrue("Calendar" in classNames)
        self.assertTrue("Event" in classNames)
        self.assertTrue("Entry" in classNames)
        self.assertTrue("Location" in classNames)
        self.assertTrue("Description" in classNames)

    def testParseUnion(self):
        """Tset parsing united classes."""
        model = self.parser.parse(self.owlpath)
        entry = model.classes["Entry"]
        # Entry is composed of classes Event, Description and Location
        self.assertEquals(3, len(entry.unionOf))

    def testParseNotUnion(self):
        """Test."""
        model = self.parser.parse(self.owlpath)
        entry = model.classes["Description"]
        self.assertEquals(0, len(entry.unionOf))  # Description doesn't have union classes

    def testParseDomains(self):
        """Test parsing domains of properties."""
        model = self.parser.parse(self.owlpath)
        sclass = model.classes['Event']
        propNames = sclass.getPropertyNames()
        self.assertTrue("hasStartDate" in propNames)
        self.assertTrue("hasEndDate" in propNames)
        self.assertTrue("isWholeDay" in propNames)
        sclass = model.classes['Description']
        propNames = sclass.getPropertyNames()
        self.assertTrue("hasSubject" in propNames)
        self.assertTrue("hasDetails" in propNames)
        sclass = model.classes['Location']
        propNames = sclass.getPropertyNames()
        self.assertTrue("hasName" in propNames)
        self.assertTrue("hasDirections" in propNames)
        sclass = model.classes['Entry']
        propNames = sclass.getPropertyNames()
        self.assertTrue("hasPriority" in propNames)

    def testParseRanges(self):
        """Test parsing ranges of properties."""
        model = self.parser.parse(self.owlpath)
        sclass = model.classes['Event']
        self.assertEqual("dateTime", sclass.properties["hasEndDate"].type)
        self.assertEqual("dateTime", sclass.properties["hasStartDate"].type)
        self.assertEqual("boolean", sclass.properties["isWholeDay"].type)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
