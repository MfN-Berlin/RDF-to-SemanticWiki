"""
Base class for DAO managers.

Created on 17.05.2016

@author: Alvaro.Ortiz
"""


class AbstractManager():
    """Base class for DAO managers."""

    def commit(self, name, values):
        """
        Commit the operation to persistent storage.

        @param name: string name of the semantic object to store
        @param values: a list of pages and page contents.
        """
        raise NotImplementedError

    def delete(self, name, pages):
        """
        Delete the backend representation of a semantic object.

        @param name: string name of the semantic object to delete
        @param values: a list of pages.
        """
        raise NotImplementedError


