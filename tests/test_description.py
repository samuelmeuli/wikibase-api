description = "This is a description"
language = "en"


class TestDescription(object):
    def test_set_description(self, wb, item_id):
        r = wb.description.set(item_id, description, language)
        assert type(r) is dict
        assert r["success"] == 1
        assert r["entity"]["descriptions"][language]["value"] == description
