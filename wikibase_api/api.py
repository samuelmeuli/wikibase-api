import requests
from requests_oauthlib import OAuth1


class Api:
    def __init__(self, config):
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
        r = self.session.get(url=self.base_url, params=params)
        print(r.status_code)
        print(r.text)

    def post(self, params, body):
        r = self.session.post(url=self.base_url, params=params, data=body)
        print(r.status_code)
        print(r.text)
