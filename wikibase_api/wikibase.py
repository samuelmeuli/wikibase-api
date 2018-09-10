import os

from .api import Api
from .config import get_config


class Wikibase:
    """
    Wrapper library for the Wikibase API
    """

    def __init__(self, config_path=None):
        """
        Parse the config object and start a request session with the Wikidata
        API
        :param config_path: Path to the configuration file (in case the user
        does not want to save it at ../config/config.json)
        :type config_path: str
        """
        # Use default config path if param is not provided
        if config_path is None:
            current_dir = os.path.dirname(os.path.realpath(__file__))
            config_path = current_dir + "/../config/config.json"

        # Load options from config file
        config = get_config(config_path)

        # Set up API session
        self.api = Api(config)

    def get_entity(self, item_id):
        """
        Get the data of one Wikibase entity
        :param item_id: Item identifier
        :type item_id: str (e.g. "Q1")
        :return: Response
        :rtype dict
        """
        return self.get_entities([item_id])

    def get_entities(self, item_ids):
        """
        Get the data of multiple Wikibase entities
        :param item_ids: Item identifiers
        :type item_ids: list(str) (e.g. ["Q1", "Q2"])
        :return: Response
        :rtype dict
        """
        ids_encoded = "|".join(item_ids)
        params = {
            "action": "wbgetentities",
            "ids": ids_encoded
        }
        return self.api.get(params)
