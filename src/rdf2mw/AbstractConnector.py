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

    def loadPage(self, title):
        """
        Load a page (from a private wiki or not), using username and password.

        The page content can be obtained from MediaWikiApiConnector::content()

        @param title: title of the wiki page to load
        @return True (if page was loaded) or False (if page could not be loaded)
        """
        raise NotImplementedError

    def createPage(self, title, content):
        """
        Create a page.

        @param title: title of the wiki page to create
        @return True (if page was created) or False (if page could not be created)
        """
        raise NotImplementedError

    def protectPage(self, title):
        """
        Protect a page, e.g. if it was created automatically.

        @param title: title of the wiki page to create
        @return True (if page was protected) or False (if page could not be protected)
        """
        raise NotImplementedError

    def deletePage(self, title):
        """
        Delete a page.

        @param title: title of the wiki page to delete
        @return True (if page was deleted or did not exist) or False (if page could not be deleted)
        """
        raise NotImplementedError

    def content(self):
        """Get the content of a wiki page after it has been loaded with loadPage."""
        raise NotImplementedError


class ConnectionException(Exception):
    """Failed connection with the API."""

    pass


class PageDoesNotExistException(Exception):
    """Requested page does not exist."""

    pass
