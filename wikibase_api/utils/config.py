import json
import sys

from wikibase_api.utils.case_conversion import dict_to_snake_case

OAUTH_PARAMS = ["consumer_key", "consumer_secret", "access_token", "access_secret"]
LOGIN_PARAMS = ["bot_username", "bot_password"]
WIKIDATA_API = "https://www.wikidata.org/w/api.php"


def load_config_file(config_path, default_config):
    """Load the parameters from the config.json file at the specified path. Fall back to the
    default_config values for missing parameters

    :param config_path: Path to the config.json file
    :type config_path: str
    :param default_config: Default values to use when a parameter is not specified in config.json
    :type default_config: dict
    """
    with open(config_path) as file:
        # Load default config
        config = default_config

        # Override defaults with user config
        user_config = json.load(file)
        user_config_snake_case = dict_to_snake_case(user_config)
        config.update(user_config_snake_case)
        return config


def verify_auth_info(oauth_credentials, login_credentials):
    """Verify that the provided authentication credentials are of the correct form (i.e. exactly one
    authentication method is specified and the corresponding parameter contains the correct keys)

    :param oauth_credentials: OAuth credentials for Wikibase (None if not specified)
    :type oauth_credentials: str
    :param login_credentials: Bot login credentials for Wikibase (None if not specified)
    :type login_credentials: str
    """
    if oauth_credentials and login_credentials:
        raise KeyError(
            'Authentication information conflict: Only one of the "oauth_credentials" and the '
            '"login_credentials" parameters must be provided to the Wikibase class'
        )
    if oauth_credentials:
        for key in OAUTH_PARAMS:
            if key not in oauth_credentials:
                raise KeyError(f'Key "{key}" is missing in the "oauth_credentials" parameter')
    elif login_credentials:
        for key in LOGIN_PARAMS:
            if key not in login_credentials:
                raise KeyError(f'Key "{key}" is missing in the "login_credentials" parameter')


def verify_api_url(api_url):
    """Raise an exception if the api_url parameter is pointing to Wikidata during testing

    :param api_url: URL to the API of the relevant Wikibase instance
    :type api_url: str
    """
    is_test_mode = "pytest" in sys.modules
    if is_test_mode and api_url == WIKIDATA_API:
        raise Exception(
            "Tests must not be run on the live Wikidata instance! Please specify a different "
            "api_url"
        )
