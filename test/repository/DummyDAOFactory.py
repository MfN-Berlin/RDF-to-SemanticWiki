"""
A DAO Manager which doesn't persist, for testing.

Created on 09.05.2016

@author: Alvaro.Ortiz
"""
from rdf2mw.repository.Factory import Factory
from rdf2mw.repository.Manager import Manager


class DummyDAOFactory(Factory):
    """
    A factory for testing.

    Create a normal factory and replace
    the manager object with a dummy manager
    """

    def __init__(self):
        """Construct."""
        Factory.__init__(self, None)
        self._manager = DummyManager(None)


class DummyManager(Manager):
    """
    A dummy class for testing.

    Values are stored in the value property, not saved to a back-end
    """

    def commit(self, name, values):
        """Override abstract method."""
        self.values = values
