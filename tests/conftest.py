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
def wb():
    # Return new instance of the API wrapper
    try:
        wikibase = Wikibase(config_path=config_path)
        return wikibase
    except Exception as e:
        pytest.exit("Could not create Wikibase object: " + str(e))


@pytest.fixture(scope="function")
def item_id(wb):
    # Create item
    r = wb.entity.add("item", content=sample_item_content)
    assert r["success"] == 1
    assert r["entity"]["labels"] == sample_item_content["labels"]
    entity_id = r["entity"]["id"]
    assert type(entity_id) is str

    # Pass entity_id to test function and wait for it to finish
    yield entity_id

    # Delete item
    title = "Item:" + entity_id
    r = wb.entity.remove(title)
    assert "errors" not in r
    assert r["delete"]["title"] == title


@pytest.fixture(scope="function")
def property_id(wb):
    # Create property
    r = wb.entity.add("property", content=sample_property_content)
    assert type(r) is dict
    assert r["success"] == 1
    entity_id = r["entity"]["id"]
    assert type(entity_id) is str

    # Pass entity_id to test function and wait for it to finish
    yield entity_id

    # Delete property
    title = "Property:" + entity_id
    r = wb.entity.remove(title)
    assert "errors" not in r
    assert r["delete"]["title"] == title
