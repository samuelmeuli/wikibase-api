import os

from .api import Api
from .models import Entity
from .utils.config import get_config


class Wikibase:
    """
    Wrapper library for the Wikibase API::

        wikibase = new Wikibase()
    """

    def __init__(self, config_path=None):
        """Parse the config object and start a request session with the Wikidata API

        :param config_path: Path to the configuration file (in case the user does not want to save
        it at ../config/config.json)
        :type config_path: str
        """
        # Use default config path if param is not provided
        if config_path is None:
            current_dir = os.path.dirname(os.path.realpath(__file__))
            config_path = current_dir + "/../config/config.json"

        # Load options from config file
        self.config = get_config(config_path)

        # Set up API session
        api = Api(self.config)

        self.entity = Entity(api)
        """An instance of :class:`.Entity`. See the documentation of the class for all available
        entity functions.::

           r = wikibase.entity.get_entity("Q1")
           print(r)
        """
