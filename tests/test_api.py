import unittest
from random import random

from wikibase_api import Wikibase

wikibase = Wikibase()

item_id_1 = "Q2"
item_id_2 = "Q3"
rand_str = random()
content = {"labels": {"en": {"language": "en", "value": str(rand_str)}}}


class TestApi(unittest.TestCase):
    def test_get_entity(self):
        r = wikibase.entity.get_entity(item_id_1)
        self.assertIsInstance(r, dict)
        self.assertEqual(r["success"], 1)
        self.assertIsInstance(r["entities"][item_id_1], dict)

    def test_get_entities(self):
        r = wikibase.entity.get_entities([item_id_1, item_id_2])
        self.assertIsInstance(r, dict)
        self.assertEqual(r["success"], 1)
        self.assertIsInstance(r["entities"][item_id_1], dict)
        self.assertIsInstance(r["entities"][item_id_2], dict)

    def test_create_entity(self):
        r = wikibase.entity.create_entity("item", content=content)
        self.assertIsInstance(r, dict)
        self.assertEqual(r["success"], 1)
        self.assertEqual(r["entity"]["labels"], content["labels"])
        self.assertIsInstance(r["entity"]["id"], str)

    def test_edit_entity(self):
        r = wikibase.entity.edit_entity(item_id_1, content=content)
        self.assertIsInstance(r, dict)
        self.assertEqual(r["success"], 1)
        self.assertEqual(r["entity"]["labels"], content["labels"])
        self.assertIsInstance(r["entity"]["id"], str)
