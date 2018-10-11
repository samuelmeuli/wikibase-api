from random import random


item_id_1 = "Q2"
item_id_2 = "Q3"
rand_str = random()
content = {"labels": {"en": {"language": "en", "value": str(rand_str)}}}


class TestEntities(object):
    def test_get_entity(self, wikibase):
        r = wikibase.entity.get(item_id_1)
        assert type(r) is dict
        assert r["success"] == 1
        assert type(r["entities"][item_id_1]) is dict

    def test_get_entities(self, wikibase):
        r = wikibase.entity.get([item_id_1, item_id_2])
        assert type(r) is dict
        assert r["success"] == 1
        assert type(r["entities"][item_id_1]) is dict
        assert type(r["entities"][item_id_2]) is dict

    def test_create_entity(self, wikibase):
        r = wikibase.entity.create("item", content=content)
        assert type(r) is dict
        assert r["success"] == 1
        assert r["entity"]["labels"] == content["labels"]
        assert type(r["entity"]["id"]) is str

    def test_edit_entity(self, wikibase):
        r = wikibase.entity.edit(item_id_1, content=content)
        assert type(r) is dict
        assert r["success"] == 1
        assert r["entity"]["labels"] == content["labels"]
        assert type(r["entity"]["id"]) is str
