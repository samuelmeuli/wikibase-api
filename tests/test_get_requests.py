import unittest

from wikibase_api import Wikibase

item_id_1 = "Q1"
item_id_2 = "Q2"
wikibase = Wikibase()


class TestGetRequests(unittest.TestCase):
    def test_get_entity(self):
        r = wikibase.get_entity(item_id_1)
        self.assertIsInstance(r, dict)
        self.assertEqual(r["success"], 1)
        self.assertIsInstance(r["entities"][item_id_1], dict)

    def test_get_entities(self):
        r = wikibase.get_entities([item_id_1, item_id_2])
        self.assertIsInstance(r, dict)
        self.assertEqual(r["success"], 1)
        self.assertIsInstance(r["entities"][item_id_1], dict)
        self.assertIsInstance(r["entities"][item_id_2], dict)
