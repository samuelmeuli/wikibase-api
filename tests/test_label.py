label = "This is a label"
language = "en"


def test_label(wb_with_auth, item_id):
    # Set label
    r = wb_with_auth.label.set(item_id, label, language)
    assert r["success"] == 1
    assert r["entity"]["labels"][language]["value"] == label
