label = "This is a label"
language = "en"


class TestLabel(object):
    def test_set_label(self, wb, item_id):
        r = wb.label.set(item_id, label, language)
        assert type(r) is dict
        assert r["success"] == 1
        assert r["entity"]["labels"][language]["value"] == label
