import os

import pytest

from wikibase_api import Wikibase

current_dir = os.path.dirname(os.path.realpath(__file__))
config_path = os.path.join(os.path.dirname(current_dir), "config-tests.json")

sample_item_content = {"labels": {"en": {"language": "en", "value": "Test item"}}}
sample_property_content = {
    "datatype": "string",
    "labels": {"en": {"language": "en", "value": "Test property"}},
}


@pytest.fixture(scope="session")
def wb_with_auth():
    """Return new instance of the API wrapper with OAuth authentication

    :return: API wrapper class
    :rtype: Wikibase
    """
    try:
        wikibase = Wikibase(config_path=config_path)
        return wikibase
    except Exception as e:
        pytest.exit("Could not create Wikibase class instance (with authentication): " + str(e))


@pytest.fixture(scope="session")
def wb_without_auth():
    """Return new instance of the API wrapper without authentication

    :return: API wrapper class
    :rtype: Wikibase
    """
    try:
        wikibase = Wikibase(api_url="http://localhost:8181/w/api.php")
        return wikibase
    except Exception as e:
        pytest.exit("Could not create Wikibase class instance (without authentication): " + str(e))


@pytest.fixture(scope="function")
def item_id(wb_with_auth):
    """Create a new Wikibase item and delete it after running the test

    :param wb_with_auth: API wrapper class (authenticated)
    :type wb_with_auth: Wikibase
    :return: Yield the item's ID
    :rtype: str
    """
    # Create item
    r = wb_with_auth.entity.add("item", content=sample_item_content)
    assert r["success"] == 1
    assert r["entity"]["labels"] == sample_item_content["labels"]
    entity_id = r["entity"]["id"]
    assert type(entity_id) is str

    # Pass entity_id to test function and wait for it to finish
    yield entity_id

    # Delete item
    title = "Item:" + entity_id
    r = wb_with_auth.entity.remove(title)
    assert "errors" not in r
    assert r["delete"]["title"] == title


@pytest.fixture(scope="function")
def property_id(wb_with_auth):
    """Create a new Wikibase property (of type string) and delete it after running the test

    :param wb_with_auth: API wrapper class (authenticated)
    :type wb_with_auth: Wikibase
    :return: Yield the property's ID
    :rtype: str
    """
    # Create property
    r = wb_with_auth.entity.add("property", content=sample_property_content)
    assert type(r) is dict
    assert r["success"] == 1
    entity_id = r["entity"]["id"]
    assert type(entity_id) is str

    # Pass entity_id to test function and wait for it to finish
    yield entity_id

    # Delete property
    title = "Property:" + entity_id
    r = wb_with_auth.entity.remove(title)
    assert "errors" not in r
    assert r["delete"]["title"] == title
