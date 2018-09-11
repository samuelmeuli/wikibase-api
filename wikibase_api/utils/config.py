import json


required_entires = ["consumerKey", "consumerSecret", "accessToken", "accessSecret", "apiUrl"]
optional_entries = {"isBot": False, "summary": "Modified using wikibase-api for Python"}


def get_config(config_path):
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
    for key in required_entires:
        if key not in user_config:
            raise KeyError('Entry "{}" is missing in configuration file'.format(key))
        else:
            config[key] = user_config[key]

    # Save values of optional entries if provided, otherwise fall back to defaults
    for key, value in optional_entries.items():
        config[key] = user_config.get(key, value)

    return config
