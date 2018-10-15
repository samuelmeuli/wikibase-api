content = {"labels": {"en": {"language": "en", "value": "Test item (updated)"}}}


class TestEntity(object):
    def test_get_entity(self, wb, item):
        r = wb.entity.get(item)
        assert type(r) is dict
        assert r["success"] == 1
        assert type(r["entities"][item]) is dict

    def test_update_entity(self, wb, item):
        r = wb.entity.update(item, content=content)
        assert type(r) is dict
        assert r["success"] == 1
        assert r["entity"]["labels"] == content["labels"]
        assert type(r["entity"]["id"]) is str
