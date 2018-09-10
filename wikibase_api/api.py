import requests
from requests_oauthlib import OAuth1


class Api:
    """
    Class for connecting to the Wikibase API
    """

    def __init__(self, config):
        """
        Create a session with the Wikibase API on class creation and set the
        authorization header and params which remain the same for all future
        requests
        :param config: Configuration dict as defined in ./config.py
        """
        self.config = config
        self.base_url = config["wikibaseInstance"] + "/api.php"
        self.session = requests.Session()
        self.session.auth = OAuth1(
            config["consumerKey"],
            config["consumerSecret"],
            config["accessToken"],
            config["accessSecret"]
        )
        self.session.params = {
            "format": "json"
        }

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

    def post(self, params, body):
        """
        Make a POST request to the Wikibase API
        :param params: Query parameters to be encoded in the URL
        :type params: dict
        :return: Response object
        :rtype dict
        """
        r = self.session.post(url=self.base_url, params=params, data=body)
        r.raise_for_status()  # Raise exception if status code indicates error
        return r.json()
