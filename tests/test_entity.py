content = {"labels": {"en": {"language": "en", "value": "Test item (updated)"}}}


def test_entity(wb, item_id):
    # Update entity
    r = wb.entity.update(item_id, content=content)
    assert r["success"] == 1
    assert r["entity"]["labels"] == content["labels"]
    assert type(r["entity"]["id"]) is str

    # Get entity
    r = wb.entity.get(item_id)
    assert r["success"] == 1
    assert r["entities"][item_id]["labels"] == content["labels"]
