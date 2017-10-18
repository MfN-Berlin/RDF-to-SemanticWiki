"""
Abstract base class for all connectors.

Created on 15.03.2016
@author: Alvaro.Ortiz
"""


class AbstractConnector:
    """Abstract base class for all connectors."""

    def login(self):
        """Login to a wiki."""
        raise NotImplementedError

    def loadPage(self, title, content):
        """
        Load a page (from a private wiki or not), using username and password.

        The page content can be obtained from MediaWikiApiConnector::content()

        @param title: title of the wiki page to load
        """
        raise NotImplementedError

    def createPage(self, title, content):
        """
        Create a page.

        @param title: title of the wiki page to create
        """
        raise NotImplementedError

    def deletePage(self, title):
        """
        Delete a page.

        @param title: title of the wiki page to delete
        """
        raise NotImplementedError

    def content(self):
        """Get the content of a wiki page after it has been loaded with loadPage."""
        raise NotImplementedError
