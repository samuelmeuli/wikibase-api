import json


required_root_entries = ["apiUrl"]
required_oauth_entries = ["consumerKey", "consumerSecret", "accessToken", "accessSecret"]
required_login_entries = ["botUsername", "botPassword"]
optional_entries = {"isBot": False, "summary": "Modified using wikibase-api for Python"}


def get_config(config_path):
    """Load values from configuration file; make sure required values are present and fall back to
    defaults for optional ones

    :param config_path: Path to config.json file
    :type config_path: str
    :return: config
    :rtype: dict
    """
    config = {}

    # Load config.json into user_config dict
    try:
        with open(config_path) as file:
            user_config = json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(
            'Config file missing. Please create a config file at "{}" or specify the correct '
            "config path".format(config_path)
        )

    # Save values of required entries, raise exception if missing
    for key in required_root_entries:
        config[key] = _get_property(key, user_config)

    # Save values of optional entries if provided, otherwise fall back to defaults
    for key, value in optional_entries.items():
        config[key] = user_config.get(key, value)

    # Check that information about exactly one authentication method is present and save the values
    if "oauth" not in user_config and "login" not in user_config:
        raise KeyError(
            'Authentication information missing in the configuration file (either "oauth" or '
            '"login" entries)'
        )
    if "oauth" in user_config and "login" in user_config:
        raise KeyError(
            "Only one authentication method may be present in the configuration file (either "
            '"oauth" or "login")'
        )
    if "oauth" in user_config:
        config["oauth"] = {}
        for key in required_oauth_entries:
            config["oauth"][key] = _get_property(key, user_config["oauth"])
    else:
        config["login"] = {}
        for key in required_login_entries:
            config["login"][key] = _get_property(key, user_config["login"])

    return config


def _get_property(key, config):
    if key not in config:
        raise KeyError('Key "{}" is missing in configuration file'.format(key))
    return config[key]
