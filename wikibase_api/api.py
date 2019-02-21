import json

import requests
from requests_oauthlib import OAuth1

from wikibase_api.utils.exceptions import ApiError, AuthError


class Api:
    """Class for connecting to the Wikibase API"""

    def __init__(self, config):
        """Create a session with the Wikibase API on class creation and set the authorization header
        and params which remain the same for all future requests

        :param config: Configuration options
        :type config: dict
        """
        # Set up request session
        self.session = requests.Session()
        self.session.params = {"format": "json"}
        self.edit_token = None
        self.base_url = config["api_url"]
        self.is_bot = config["is_bot"]
        self.summary = config["summary"]

        if config["oauth_credentials"]:
            # OAuth
            oauth_config = config["oauth_credentials"]
            self.session.auth = OAuth1(
                oauth_config["consumer_key"],
                oauth_config["consumer_secret"],
                oauth_config["access_token"],
                oauth_config["access_secret"],
            )
            self.edit_token = self._get_token("csrf")  # Get edit token for POST requests
        elif config["login_credentials"]:
            # Bot login
            login_config = config["login_credentials"]
            login_token = self._get_token("login")  # Get login token
            self._login(login_config["bot_username"], login_config["bot_password"], login_token)
            self.edit_token = self._get_token("csrf")  # Get edit token for POST requests

    @staticmethod
    def _check_err(res_json):
        if "error" in res_json:
            raise ApiError(json.dumps(res_json["error"]))

    def get(self, params):
        """Make a GET request to the Wikibase API

        :param params: Query parameters to be encoded in the URL
        :type params: dict
        :return: Response object
        :rtype: dict
        """
        r = self.session.get(url=self.base_url, params=params)
        r.raise_for_status()  # Raise exception if status code indicates error
        json = r.json()
        self._check_err(json)
        return json

    def post(self, body):
        """Make a POST request to the Wikibase API

        :param body: Query parameters to be sent in the POST body
        :type body: dict
        :return: Response object
        :rtype: dict
        """
        if not self.edit_token:
            raise AuthError("You need to be authenticated to be able to make edits on Wikibase")

        data = {**body, "token": self.edit_token, "summary": self.summary}
        if self.is_bot:
            body["bot"] = True

        r = self.session.post(url=self.base_url, data=data)
        r.raise_for_status()  # Raise exception if status code indicates error
        json = r.json()
        self._check_err(json)
        return json

    def _get_token(self, token_type):
        """Request edit (CSRF) or login token

        :param token_type: Token type (either "csrf" or "login")
        :type token_type: str
        :return: token
        :rtype: str
        """
        if token_type != "csrf" and token_type != "login":
            raise ValueError('Token type must be either "csrf" or "login"')

        params = {"action": "query", "meta": "tokens", "type": token_type}
        data = self.get(params)

        if "query" not in data or "tokens" not in data["query"]:
            raise ValueError(
                f"Could not obtain {token_type} token due to authentication error: {data}"
            )

        return data["query"]["tokens"][token_type + "token"]

    def _login(self, bot_username, bot_password, token):
        """Log in user with bot username and bot password (alternative to OAuth) to set auth cookies

        :param bot_username: Bot username
        :type bot_username: str
        :param bot_password: Bot password
        :type bot_password: str
        :param token: Login token (see the :meth:`_get_token` function)
        :type token: str
        """
        params = {
            "action": "login",
            "lgname": bot_username,
            "lgpassword": bot_password,
            "lgtoken": token,
        }
        r = self.session.post(url=self.base_url, data=params)
        r.raise_for_status()  # Raise exception if status code indicates error
        data = r.json()

        if "login" not in data:
            raise ValueError("Login error: " + str(data))
        if data["login"]["result"] != "Success":
            raise ValueError("Login error: Incorrect username or password")
