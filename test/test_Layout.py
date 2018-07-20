"""
Test.

Created on 18.07.2018

Tests Layout class without persisting to a back-end
(using DummyDAOManager)

@author: Alvaro.Ortiz
"""
import unittest
from DummyDAOFactory import DummyDAOFactory
from rdf2mw.RDFParser import RDFParser


class test_Layout(unittest.TestCase):
    """Test."""

    layoutpath = "testdata/layout.xml"
    # path to example RDF file
    rdfpath = "testdata/Test.rdf"

    def testLayout(self):
        """Test that the layout file is read and interpreted correctly."""
        factory = DummyDAOFactory(layoutFile=test_Layout.layoutpath)
        # could the layout object be read from file
        self.assertTrue(factory.layout)

        sclass = factory.getSemanticClassDAO()
        # SemanticClassDAO has a Layout object
        self.assertTrue(sclass.layout)

        root = sclass.layout.layoutTree.getroot()
        expected = "hasName,hasSubject,hasStartDate,hasEndDate,isWholeDay,hasDetails,hasLocation,hasPriority"
        props = root.find("./page/properties")
        self.assertEqual(expected, props.attrib['order'])

    def testOrder(self):
        """Test that the attributes are rendered in the correct order."""
        parser = RDFParser()
        model = parser.parse(self.rdfpath)

        factory = DummyDAOFactory(layoutFile=test_Layout.layoutpath)
        
        # Description has the attributes: hasDetails and hasSubject
        simpleClass = model.classes['Description']
        dao = factory.getSemanticClassDAO()
        dao.create(simpleClass)

        # test the string generated for the template
        tplStr = dao._manager.values['template']
        self.assertNotEqual(-1, tplStr.find("hasDetails"))
        self.assertNotEqual(-1, tplStr.find("hasSubject"))
        # hasSubject should be rendered before hasDetails
        #self.assertTrue(tplStr.find("hasDetails") < tplStr.find("hasSubject"))

        # test the string generated for the form
        formStr = dao._manager.values['form']
        self.assertNotEqual(-1, formStr.find("hasDetails"))
        self.assertNotEqual(-1, formStr.find("hasSubject"))
        # hasSubject should be rendered before hasDetails
        self.assertTrue(formStr.find("hasDetails") < formStr.find("hasSubject"))

        # Event has the attributes: hasEndDate, hasStartDate, isWholeDay
        simpleClass = model.classes['Event']
        dao = factory.getSemanticClassDAO()
        dao.create(simpleClass)

        
        # test the string generated for the template
        tplStr = dao._manager.values['template']
        self.assertNotEqual(-1, tplStr.find("hasEndDate"))
        self.assertNotEqual(-1, tplStr.find("hasStartDate"))
        self.assertNotEqual(-1, tplStr.find("isWholeDay"))
        # hasStartDate should be rendered before hasEndDate etc
        #self.assertTrue(tplStr.find("hasStartDate") < tplStr.find("hasEndDate"))
        #self.assertTrue(tplStr.find("hasEndDate") < tplStr.find("isWholeDay"))

        # test the string generated for the form
        formStr = dao._manager.values['form']
        self.assertNotEqual(-1, formStr.find("hasEndDate"))
        self.assertNotEqual(-1, formStr.find("hasStartDate"))
        self.assertNotEqual(-1, formStr.find("isWholeDay"))
        # hasStartDate should be rendered before hasEndDate
        #self.assertTrue(formStr.find("hasStartDate") < formStr.find("hasEndDate"))
        #self.assertTrue(formStr.find("hasEndDate") < formStr.find("isWholeDay"))

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
