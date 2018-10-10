import pytest

from wikibase_api import Wikibase


@pytest.fixture(scope="session", autouse=True)
def wikibase():
    # Return new instance of the API wrapper
    try:
        wb = Wikibase()
    except Exception as e:
        pytest.exit("Could not create Wikibase object: " + str(e))

    # Prevent tests from being run on live Wikidata instance
    if wb.config["apiUrl"] == "https://www.wikidata.org/w/api.php":
        pytest.exit("Tests must not be run on the live Wikidata instance!")

    return wb
