claim_value = "Claim value"
qualifier_value_1 = "Qualifier 1"
qualifier_value_2 = "Qualifier 2"


def test_qualifier(wb, item_id, property_id):
    # Create claim
    r = wb.claim.add(item_id, property_id, claim_value)
    assert r["success"] == 1
    assert r["claim"]["mainsnak"]["property"] == property_id
    claim_id = r["claim"]["id"]

    # Create qualifier
    r = wb.qualifier.add(claim_id, property_id, qualifier_value_1)
    assert r["success"] == 1
    assert r["claim"]["qualifiers"][property_id][0]["datavalue"]["value"] == qualifier_value_1
    qualifier_id = r["claim"]["qualifiers"][property_id][0]["hash"]

    # Update qualifier
    r = wb.qualifier.update(claim_id, qualifier_id, property_id, qualifier_value_2)
    assert r["success"] == 1
    assert r["claim"]["qualifiers"][property_id][0]["datavalue"]["value"] == qualifier_value_2
    qualifier_id_updated = r["claim"]["qualifiers"][property_id][0]["hash"]

    # Delete qualifier
    r = wb.qualifier.remove(claim_id, qualifier_id_updated)
    assert r["success"] == 1
