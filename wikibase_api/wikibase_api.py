from wikibase_api.api import Api
from wikibase_api.models import Alias, Claim, Description, Entity, Label, Qualifier, Reference
from wikibase_api.utils.config import load_config_file, verify_api_url, verify_auth_info

DEFAULT_CONFIG = {
    "api_url": "https://www.wikidata.org/w/api.php",
    "oauth_credentials": None,
    "login_credentials": None,
    "is_bot": False,
    "summary": "Modified using wikibase-api for Python",
}


class Wikibase:
    """This is the Wikibase API wrapper class.

    :param api_url: URL to the API of the relevant Wikibase instance. Default:
        ``"https://www.wikidata.org/w/api.php"``. For a local instance, you might use
        ``"http://localhost:8181/w/api.php"``
    :type api_url: str
    :param oauth_credentials: Dictionary with the keys ``consumer_key``, ``consumer_secret``,
        ``access_token``, and ``access_secret``
    :type oauth_credentials: dict
    :param login_credentials: Dictionary with the keys ``bot_username`` and ``bot_password``
    :type login_credentials: dict
    :param is_bot: Mark edits as created by a bot. Default: ``false``
    :type is_bot: bool
    :param summary: Summary for edits. An auto-generated comment will be added before the summary.
        Together, they cannot be longer than 260 characters. Default: ``"Modified using wikibase-api
        for Python"``
    :type summary: str
    :param config_path: Path to a config.json configuration file. If specified, the other parameters
        are loaded from this file. The default values are the same as above
    :type config_path: str
    """

    def __init__(
        self,
        # Option 1: Parameters
        api_url=DEFAULT_CONFIG["api_url"],
        oauth_credentials=DEFAULT_CONFIG["oauth_credentials"],
        login_credentials=DEFAULT_CONFIG["login_credentials"],
        is_bot=DEFAULT_CONFIG["is_bot"],
        summary=DEFAULT_CONFIG["summary"],
        # Option 2: Config file
        config_path=None,
    ):
        # Load configuration from parameters or file
        if config_path:
            config = load_config_file(config_path, DEFAULT_CONFIG)
        else:
            config = {
                "api_url": api_url,
                "oauth_credentials": oauth_credentials,
                "login_credentials": login_credentials,
                "is_bot": is_bot,
                "summary": summary,
            }

        # Verify configuration parameters
        if config["oauth_credentials"] or config["login_credentials"]:
            verify_auth_info(config["oauth_credentials"], config["login_credentials"])
            verify_api_url(config["api_url"])

        # Set up API session
        api = Api(config)

        # Expose API functions to allow custom API calls
        self.api = api

        # API functions
        self.alias = Alias(api)
        self.claim = Claim(api)
        self.description = Description(api)
        self.entity = Entity(api)
        self.label = Label(api)
        self.qualifier = Qualifier(api)
        self.reference = Reference(api)
