"""
Abstract base class for all DAO objects.

Created on 04.05.2016
@author: Alvaro.Ortiz
"""


class AbstractDAO:
    """Abstract base class for all DAO objects."""

    def create(self, obj, language=None):
        """
        Create whatever string or query is necessary for persisting the in-memory object.

        This method should always call the commit method from the associated DAO manager.
        Note that an in-memory object may be stored using several queries 
        (e.g. a semantic class may me stored as a wiki template and a form).
        Example:

        class myDAO( AbstractDAO ):
           _manager = None

           __init__( self, myDAOManager ):
              self._manager = myDAOManager

           create( self, myObj ):
              queries = {}
              queries['data1']= "...put some SQL here..."
              queries['data2']= "...put some SQL here..."
              ...
              self._manager.commit( myObj.name, queries )

        """
        raise NotImplementedError

    def delete(self, obj):
        """
        Delete obj from persistent storage.

        Generally, you would want to call the delete method of the manager.
        Example:

        class myDAO( AbstractDAO ):
           _manager = None

           __init__( self, myDAOManager ):
              self._manager = myDAOManager

           delete( self, myObj ):
              # in this example, myObj is persisted as a template, a form and a category
              # (as would be using a MediaWiki backend.)
              pages = ['template', 'form', 'category']
              ...
              self._manager.delete( myObj.name, pages )
        """
        raise NotImplementedError

    def getValues(self):
        """
        Get a representation of the DAO object.

        Get a dictionary of string representations of the queries used
        for persisting the in-memory object.

        e.g. template->a template, form->a form
        """
        raise NotImplementedError

