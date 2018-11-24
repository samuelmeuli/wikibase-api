content = {"labels": {"en": {"language": "en", "value": "Test item (updated)"}}}


def test_entity(wb_with_auth, wb_without_auth, item_id):
    # Update entity
    r = wb_with_auth.entity.update(item_id, content=content)
    assert r["success"] == 1
    assert r["entity"]["labels"] == content["labels"]
    assert type(r["entity"]["id"]) is str

    # Search entity
    r = wb_without_auth.entity.search("Test item", "en")
    assert r["success"] == 1

    # Get entity
    r = wb_without_auth.entity.get(item_id)
    assert r["success"] == 1
    assert r["entities"][item_id]["labels"] == content["labels"]
