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
        self.session.auth = OAuth1(
            config["consumerKey"],
            config["consumerSecret"],
            config["accessToken"],
            config["accessSecret"],
        )
        self.session.params = {"format": "json"}

        # Generate base URL for requests
        self.base_url = config["wikibaseInstance"] + "/api.php"
        self.is_bot = config["isBot"]
        self.summary = config["summary"]

        # Fetch edit token for POST requests
        self.edit_token = self.get_edit_token()

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
        params["bot"] = self.is_bot
        params["summary"] = self.summary
        body = {"token": self.edit_token}
        r = self.session.post(url=self.base_url, params=params, data=body)
        r.raise_for_status()  # Raise exception if status code indicates error
        return r.json()

    def get_edit_token(self):
        """
        Authenticate with OAuth and request an edit token (required for future POST requests)
        :return: Edit token
        :rtype str
        """
        params = {"action": "query", "meta": "tokens"}
        r = self.get(params)
        return r["query"]["tokens"]["csrftoken"]
