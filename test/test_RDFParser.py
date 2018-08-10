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
        """Test that the parser can be instantiated."""
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

    def testParseDataPropertyLabels(self):
        """Test parsing labels (localised property names) of data properties."""
        model = self.parser.parse(self.rdfpath)
        sclass = model.classes['Event']
        self.assertEqual("Enddatum", sclass.properties["hasEndDate"].getLabel('de'))
        self.assertEqual("Start date", sclass.properties["hasStartDate"].getLabel('en'))

    def testParseDataPropertyComments(self):
        """Test parsing labels (localised property names) of data properties."""
        model = self.parser.parse(self.rdfpath)
        sclass = model.classes['Description']
        propNames = sclass.getPropertyNames()
        self.assertTrue("hasDetails" in propNames)
        self.assertTrue("Das ist der Absatz" in sclass.properties["hasDetails"].getComment('de'))
        self.assertTrue("This is the section", sclass.properties["hasDetails"].getComment('en'))

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

    def testParseObjectPropertyCardinality(self):
        """Test that global cardinality constraints are parsed correctly and that default is used."""
        model = self.parser.parse(self.rdfpath)
        # Entry/hasDescription is functional
        sclass = model.classes['Entry']
        self.assertEqual("FunctionalProperty", sclass.properties["hasDescription"].cardinality)
        # Calendar/hasEntry is not functional
        sclass = model.classes['Calendar']
        self.assertFalse(sclass.properties["hasEntry"].cardinality)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
