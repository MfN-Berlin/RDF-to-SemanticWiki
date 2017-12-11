"""
A DAO Manager which doesn't persist, for testing.

Created on 09.05.2016

@author: Alvaro.Ortiz
"""
from smw.Factory import Factory
from rdf2mw.AbstractConnector import AbstractConnector
from smw.Manager import Manager


class DummyDAOFactory(Factory):
    """
    A factory for testing.

    Create a normal factory and replace
    the manager object with a dummy manager
    """

    def __init__(self, lang=None, layoutFile=None):
        """Construct."""
        Factory.__init__(self, lang, layoutFile)
        self._manager = DummyManager(DummyConnector(), self.layout)


class DummyManager(Manager):
    """
    A dummy class for testing.

    Values are stored in the value property, not saved to a back-end
    """

    def commit(self, name, values):
        """Override abstract method."""
        self.values = values


class DummyConnector(AbstractConnector):
    """A dummy class for testing."""

    @property
    def baseURL(self):
        """Get the base URL of the wiki."""
        return "dummy"
