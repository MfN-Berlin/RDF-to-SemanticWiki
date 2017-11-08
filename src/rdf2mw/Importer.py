"""
Import an RDF or OWL file into a semantic MediaWiki.

Created on 02.05.2016

@author: Alvaro.Ortiz
"""


class Importer:
    """Import an RDF or OWL file into a data sink (e.g. semantic MediaWiki API)."""

    _parser = None
    _daoFactory = None

    def __init__(self, parser, daoFactory):
        """
        Construct.

        @param parser: parses an RDF or OWL file into a dom object
        @param daoFactory: a factory of DAO objects (that persist e.g. in semantic MediaWiki API)
        """
        self._parser = parser
        self._daoFactory = daoFactory

    def run(self, path):
        """Import RDF or OWL file.

        @param path: file to import
        """
        # parse the file
        model = self._parser.parse(path)

        # create DAO objects
        classDao = self._daoFactory.getSemanticClassDAO()
#        propDao = self._daoFactory.getSemanticPropertyDAO()

        # create all the class pages
        for sclass in model.classes.values():
            classDao.create(sclass)
            print("Created page for class %s" % sclass.name)
                
            # create all the property pages
 #           for sprop in sclass.properties.values():
 #               propDao.create(sprop)

