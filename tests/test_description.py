from random import randint

# Generate description with random number because there cannot be two items with the same label and
# description
description = "This is a description ({})".format(str(randint(0, 100000000)))
language = "en"


def test_description(wb, item_id):
    # Set description
    r = wb.description.set(item_id, description, language)
    assert r["success"] == 1
    assert r["entity"]["descriptions"][language]["value"] == description
