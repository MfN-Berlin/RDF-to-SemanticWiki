"""
Abstract base class for all parsers.

Created on 15.03.2016
@author: Alvaro.Ortiz
"""


class AbstractParser:
    """Abstract base class for all parsers."""

    def parse(self, path):
        """
        Parse an ontology.

        @param path:string path to a file
        @return SemanticModel: a object representing the parsed OWL
        @raise exception: if parsing failed.
        """
        raise NotImplementedError
