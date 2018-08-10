"""
Import an RDF file into a semantic MediaWiki.

Created on 02.05.2016

@author: Alvaro.Ortiz
"""
from rdf2mw.SemanticModel import DatatypeProperty

class Importer:
    """Import an RDF file into a data sink (e.g. semantic MediaWiki API)."""

    _parser = None
    _daoFactory = None

    def __init__(self, parser, daoFactory):
        """
        Construct.

        @param parser: parses an RDF file into a dom object
        @param daoFactory: a factory of DAO objects (that persist e.g. in semantic MediaWiki API)
        """
        self._parser = parser
        self._daoFactory = daoFactory

    def run(self, modelPath, language=None):
        """
        Import RDF  file.

        @param modelPath: ontology file to import
        @param language: string language code
        """
        # parse the file
        model = self._parser.parse(modelPath)

        # create DAO objects
        classDao = self._daoFactory.getSemanticClassDAO()
        dataPropDao = self._daoFactory.getDatatypePropertyDAO()
        objectPropDao = self._daoFactory.getObjectPropertyDAO()

        # create all the class pages
        for sclass in model.classes.values():
            classDao.create(sclass, language)
            print("Created pages for class %s" % sclass.name)
            # Create data property pages for this class
            for sprop in sclass.datatypeProperties:
                dataPropDao.create(sprop, language)
            # Create object property pages for this class
            for sprop in sclass.objectProperties:
                objectPropDao.create(sprop, language)

    def delete(self, modelPath):
        """
        Remove an ontology.

        @param modelPath: ontology file to remove
        """
        # parse the file
        model = self._parser.parse(modelPath)

        # create DAO objects
        classDao = self._daoFactory.getSemanticClassDAO()
        propDao = self._daoFactory.getDatatypePropertyDAO()

        # delete all the class pages
        for sclass in model.classes.values():
            classDao.delete(sclass)
            print("Deleted pages for class %s" % sclass.name)

            # delete all the property pages
            for sprop in sclass.properties.values():
                propDao.delete(sprop)
                # if isinstance(sprop, DatatypeProperty):
                #    propDao.delete(sprop)


class ImporterException(Exception):
    """Failed importer operation."""

    pass
