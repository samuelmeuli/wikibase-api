import pytest

from wikibase_api import Wikibase


@pytest.fixture(scope="session", autouse=True)
def wikibase():
    # Return new instance of the API wrapper
    try:
        wb = Wikibase()
    except Exception as e:
        pytest.exit("Could not create Wikibase object: " + str(e))

    return wb
