import requests
from requests_oauthlib import OAuth1


class Api:
    """
    Class for connecting to the Wikibase API
    """

    def __init__(self, config):
        """
        Create a session with the Wikibase API on class creation and set the authorization header
        and params which remain the same for all future requests
        :param config: Configuration dict as defined in ./config.py
        """
        # Set up request session
        self.session = requests.Session()
        self.session.params = {"format": "json"}
        self.base_url = config["apiUrl"]
        self.is_bot = config["isBot"]
        self.summary = config["summary"]

        if "oauth" in config:
            # OAuth
            oauth_config = config["oauth"]
            self.session.auth = OAuth1(
                oauth_config["consumerKey"],
                oauth_config["consumerSecret"],
                oauth_config["accessToken"],
                oauth_config["accessSecret"],
            )
            self.edit_token = self.get_token("csrf")  # Get edit token for POST requests
        else:
            # Login
            login_config = config["login"]
            login_token = self.get_token("login")  # Get login token
            self.login(login_config["botUsername"], login_config["botPassword"], login_token)
            self.edit_token = self.get_token("csrf")  # Get edit token for POST requests

    def get(self, params):
        """
        Make a GET request to the Wikibase API
        :param params: Query parameters to be encoded in the URL
        :type params: dict
        :return: Response object
        :rtype dict
        """
        r = self.session.get(url=self.base_url, params=params)
        r.raise_for_status()  # Raise exception if status code indicates error
        return r.json()

    def post(self, params):
        """
        Make a POST request to the Wikibase API
        :param params: Query parameters to be encoded in the URL
        :type params: dict
        :return: Response object
        :rtype dict
        """
        if self.is_bot:
            params["bot"] = True
        params["summary"] = self.summary
        body = {"token": self.edit_token}
        r = self.session.post(url=self.base_url, params=params, data=body)
        r.raise_for_status()  # Raise exception if status code indicates error
        return r.json()

    def get_token(self, token_type):
        """
        Request edit (CSRF) or login token
        :param token_type: Token type (either "csrf" or "login")
        :type token_type: str
        :return: token
        :rtype: str
        """
        if token_type != "csrf" and token_type != "login":
            raise ValueError('Token type must be either "csrf" or "login"')

        params = {"action": "query", "meta": "tokens", "type": token_type}
        r = self.get(params)
        return r["query"]["tokens"][token_type + "token"]

    def login(self, bot_username, bot_password, token):
        """
        Log in user with bot username and bot password (alternative to OAuth) to set auth cookies
        :param bot_username: Bot username
        :type bot_username: str
        :param bot_password: Bot password
        :type bot_password: str
        :param token: Login token (see get_token function)
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
