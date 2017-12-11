"""
Provides layout information to the ontology classes.

Created on 11.12.2017

@author: Alvaro.Ortiz
"""
from lxml import etree


class Layout:
    """
    Provides layout information to the ontology classes.

    e.g. order of the attributes on the class page (start comes before end)
    """

    def __init__(self, layoutFile):
        """
        Construct.

        @param layout: path to a XML layout file
        """
        # read the layout file
        self.layoutTree = etree.parse(layoutFile)
