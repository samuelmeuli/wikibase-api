label = "This is a label"
language = "en"


def test_label(wb, item_id):
    # Set label
    r = wb.label.set(item_id, label, language)
    assert r["success"] == 1
    assert r["entity"]["labels"][language]["value"] == label
