"""
Test.

Created on 02.05.2016

@author: Alvaro.Ortiz
"""
import unittest
from rdf2mw.RDFParser import RDFParser


class test_RDFParser(unittest.TestCase):
    """Test."""

    parser = None
    rdfpath = "testdata/Test.rdf"

    def setUp(self):
        """Setup."""
        self.parser = RDFParser()

    def testInstantiate(self):
        """Test."""
        self.assertTrue(self.parser)

    def testLoadOWLFile(self):
        """Test thet a OWL file can be read."""
        self.assertTrue(self.parser.parse(self.rdfpath))

    def testParseClasses(self):
        """Test parsng ontology classes."""
        model = self.parser.parse(self.rdfpath)
        self.assertEqual(5, model.countClasses())
        classNames = model.getClassNames()
        self.assertTrue("Calendar" in classNames)
        self.assertTrue("Event" in classNames)
        self.assertTrue("Entry" in classNames)
        self.assertTrue("Location" in classNames)
        self.assertTrue("Description" in classNames)

    def testParseDataPropertyDomains(self):
        """Test parsing domains of data properties."""
        model = self.parser.parse(self.rdfpath)
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

    def testParseDataPropertyRanges(self):
        """Test parsing ranges of data properties."""
        model = self.parser.parse(self.rdfpath)
        sclass = model.classes['Event']
        self.assertEqual("dateTime", sclass.properties["hasEndDate"].range)
        self.assertEqual("dateTime", sclass.properties["hasStartDate"].range)
        self.assertEqual("boolean", sclass.properties["isWholeDay"].range)

    def testParseObjectProperties(self):
        """Test parsing object properties."""
        model = self.parser.parse(self.rdfpath)
        # Entry -> Description
        sclass = model.classes['Entry']
        propNames = sclass.getPropertyNames()
        self.assertTrue("hasDescription" in propNames)
        # Calendar -> Entry
        sclass = model.classes['Calendar']
        propNames = sclass.getPropertyNames()
        self.assertTrue("hasEntry" in propNames)
        # Entry -> Event
        sclass = model.classes['Entry']
        propNames = sclass.getPropertyNames()
        self.assertTrue("hasEvent" in propNames)

    def testParseObjectPropertyRanges(self):
        """Test parsing ranges of object properties."""
        model = self.parser.parse(self.rdfpath)
        # Entry -> Description
        sclass = model.classes['Entry']
        self.assertEqual("Description", sclass.properties["hasDescription"].range)
        # Calendar -> Entry
        sclass = model.classes['Calendar']
        self.assertEqual("Entry", sclass.properties["hasEntry"].range)
        # Entry -> Event
        sclass = model.classes['Entry']
        self.assertEqual("Event", sclass.properties["hasEvent"].range)

    @unittest.skip("Skipping RDF union for now")
    def testParseUnion(self):
        """Tset parsing united classes."""
        model = self.parser.parse(self.rdfpath)
        entry = model.classes["Entry"]
        # Entry is composed of classes Event, Description and Location
        self.assertEquals(3, len(entry.unionOf))

    @unittest.skip("Skipping RDF union for now")
    def testParseNotUnion(self):
        """Test."""
        model = self.parser.parse(self.rdfpath)
        entry = model.classes["Description"]
        self.assertEquals(0, len(entry.unionOf))  # Description doesn't have union classes

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
