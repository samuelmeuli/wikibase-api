import os

from .api import Api
from .config import get_config


class Wikibase:
    current_dir = os.path.dirname(os.path.realpath(__file__))
    default_config_path = current_dir + "/../config/config.json"

    def __init__(self, config_path=default_config_path):
        config = get_config(config_path)
        self.api = Api(config)

    def get_entities(self, ids):
        ids_encoded = "|".join(ids)
        params = {
            "action": "wbgetentities",
            "ids": ids_encoded
        }
        self.api.get(params)
