import json
import os

import pytest

from wikibase_api import Wikibase

current_dir = os.path.dirname(os.path.realpath(__file__))
config_path = os.path.join(current_dir, "config.json")


@pytest.fixture(scope="session", autouse=True)
def wb():
    # Load Wikibase class parameters from config.json file
    try:
        with open(config_path) as file:
            config = json.load(file)
    except FileNotFoundError:
        pytest.exit(
            "Configuration file with authentication information missing. Please create a "
            "config.json file in the project root."
        )
    except Exception as e:
        pytest.exit("Could not load config.json: " + str(e))

    # Prevent tests from being run on live Wikidata instance
    if config["api_url"] == "https://www.wikidata.org/w/api.php":
        pytest.exit(
            "Tests must not be run on the live Wikidata instance! Please specify a different "
            "api_url in the config.json file"
        )

    # Return new instance of the API wrapper
    try:
        wikibase = Wikibase(
            api_url=config["api_url"], oauth_credentials=config["oauth_credentials"]
        )
    except Exception as e:
        pytest.exit("Could not create Wikibase object: " + str(e))

    return wikibase
