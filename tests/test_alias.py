alias_1 = "Alias 1"
alias_2 = "Alias 2"
alias_3 = "Alias 3"
language = "en"


def test_alias(wb, item_id):
    # Add alias
    r = wb.alias.add(item_id, alias_1, language)
    assert r["success"] == 1
    assert r["entity"]["aliases"][language][0]["value"] == alias_1

    # Replace aliases
    r = wb.alias.replace(item_id, [alias_2, alias_3], language)
    assert r["success"] == 1
    assert r["entity"]["aliases"][language][0]["value"] == alias_2
    assert r["entity"]["aliases"][language][1]["value"] == alias_3

    # Remove alias
    r = wb.alias.remove(item_id, alias_2, language)
    assert r["success"] == 1
    assert r["entity"]["aliases"][language][0]["value"] == alias_3
