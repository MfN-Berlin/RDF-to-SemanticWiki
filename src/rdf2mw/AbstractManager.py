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

        @param name: a string corresponding to a page name.
        @param values: a list of page names and page contents.
        """
        raise NotImplementedError
