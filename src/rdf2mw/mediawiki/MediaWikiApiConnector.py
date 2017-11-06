"""
Connector for the MediaWiki http API.

Created on 15.03.2016
@author: Alvaro.Ortiz
"""
import requests
import urllib.parse
import sys
import traceback
from src.rdf2mw.AbstractConnector import AbstractConnector


class MediaWikiApiConnector(AbstractConnector):
    """Connect to the MediaWiki API."""

    # The URL to the Mediawiki API
    _apiUrl = None
    # The URL to MediaWiki pages
    _contentUrl = None
    # Authentication to the MediaWiki API
    _username = None
    _password = None
    # Token available after Login
    _loginToken = None
    # Cookie available after Login
    _cookies = None
    # The content of the page loaded
    _content = None

    def __init__(self, config):
        """Construct the connector."""
        baseMwUrl = config.get('defaults', 'baseMwURL')
        self._apiUrl = urllib.parse.urljoin(baseMwUrl, 'api.php')
        self._contentUrl = urllib.parse.urljoin(baseMwUrl, 'index.php')
        self._username = config.get('defaults', 'username')
        self._password = config.get('defaults', 'password')

    def login(self):
        """Override abstract method."""
        try:
            # PRE 1.27
            # Login request, pre 1.27
            payload = {
               'action': 'login', 'format': 'json',
               'lgname': self._username, 'lgpassword': self._password}

            # POST 1.27
            # Get a login token
            # payload = {
            #    'action': 'query', 'meta': 'tokens', 'type': 'login', 'format': 'json'}
            r1 = requests.post(self._apiUrl, data=payload)
            self._cookies = r1.cookies

            # Check http status
            self._checkRequest(r1)

            # store login token
            # pre 1.27
            self._loginToken = r1.json()['login']['token']
            # post 1.27
            # self._loginToken = r1.json()['query']['tokens']['logintoken']

            # Workaround MediaWiki bug
            # see https://www.mediawiki.org/wiki/API:Login
            # if r1.json()['login']['result'] == 'NeedToken':
            #    payload = {
            #        'action': 'login', 'format': 'json', 'utf8': '',
            #        'lgname': self._username, 'lgpassword': self._password,
            #        'lgtoken': self._loginToken}
            #    requests.post(self._apiUrl, data=payload, cookies=r1.cookies)

            # login
            payload['lgtoken'] = self._loginToken
            # payload['action'] = 'clientlogin'
            # payload['logintoken'] = self._loginToken
            # payload['username'] = self._username
            # payload['password'] = self._password
            # payload['loginreturnurl'] = self._contentUrl
            r2 = requests.post(self._apiUrl, data=payload, cookies=r1.cookies)

            # Check http status
            self._checkRequest(r2)

            # Store cookies
            self._cookies = r2.cookies

            return True

        except:
            traceback.print_exc(file=sys.stdout)
            return False

    def loadPage(self, title):
        """Override abstract method."""
        try:
            # Attempt to Login
            if not self.login():
                return False

            # Read a page
            payload = {'action': 'parse', 'page': title, 'format': 'json'}
            r1 = requests.post(self._apiUrl, data=payload, cookies=self._cookies)

            # Check http status
            self._checkRequest(r1)

            self._content = r1.content
            return True

        except:
            traceback.print_exc(file=sys.stdout)
            return False

    def createPage(self, title, content):
        """Override abstract method."""
        try:
            # Attempt to Login
            if not self.login():
                return False

            # Open the page to get the edit token
            payload = {
                'action': 'query', 'prop': 'info', 'titles': title,
                'intoken': 'edit', 'format': 'json'}
            r1 = requests.post(self._apiUrl, data=payload, cookies=self._cookies)

            # Check http status
            self._checkRequest(r1)

            # if page does not exist
            if "-1" in r1.json()['query']['pages']:
                # get the edit token
                edittoken = r1.json()['query']['pages']["-1"]['edittoken']
            else:
                # page exists, do not overwrite
                raise Exception('Page exists %s.' % title)

            payload = {
                'action': 'edit', 'title': title, 'text': content,
                'token': edittoken, 'format': 'json'}
            r1 = requests.post(self._apiUrl, data=payload, cookies=self._cookies)

            # Check http status
            self._checkRequest(r1)

            return True

        except:
            traceback.print_exc(file=sys.stdout)
            return False

    def deletePage(self, title):
        """Override abstract method."""
        try:
            # Attempt to Login
            if not self.login():
                return False

            # Open the page to get the edit token
            # payload = {
            #    'action': 'query', 'prop': 'info', 'titles': title,
            #    'intoken': 'edit', 'format': 'json'}
            payload = {
                'action': 'query', 'prop': 'info', 'titles': title,
                'meta': 'tokens', 'format': 'json'}
            r1 = requests.post(self._apiUrl, data=payload, cookies=self._cookies)

            # Check http status
            self._checkRequest(r1)

            # Assuming there is only one page, get the page id
            # pageId = list(r1.json()['query']['pages'].keys())[0]
            # get the edit token
            # edittoken = r1.json()['query']['pages'][pageId]['edittoken']
            edittoken = r1.json()['query']['tokens']['csrftoken']

            payload = {'action': 'delete', 'title': title, 'token': edittoken, 'format': 'json'}
            r2 = requests.post(self._apiUrl, data=payload, cookies=self._cookies)

            # Check http status
            self._checkRequest(r2)

            return True

        except:
            traceback.print_exc(file=sys.stdout)
            return False

    def _checkRequest(self, r):
        """Check if a http request was successful, throw an exception otherwise."""
        # Check http status
        if r.status_code != 200:
            raise Exception('Failed request url %s status %d' % (self._apiUrl, r.status_code))
        # Check response code
        if 'error' in r.json():
            if(r.json()['error']['code'] == 'missingtitle'):
                pass
                # print("Page %s doesn't exist, ignoring" % self._apiUrl)
            else:
                raise Exception(
                    'Failed request %s : %s' % (self._apiUrl, r.json()['error']['info']))

    def content(self):
        """Get the content of a wiki page after it has been loaded with loadPage."""
        return self._content