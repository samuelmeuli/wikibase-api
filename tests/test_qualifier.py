claim_value = "Claim value"
qualifier_value_1 = "Qualifier 1"
qualifier_value_2 = "Qualifier 2"


def test_qualifier(wb_with_auth, item_id, property_id):
    # Create claim
    r = wb_with_auth.claim.add(item_id, property_id, claim_value)
    assert r["success"] == 1
    assert r["claim"]["mainsnak"]["property"] == property_id
    assert r["claim"]["mainsnak"]["snaktype"] == "value"
    claim_id = r["claim"]["id"]

    # Create qualifier
    r = wb_with_auth.qualifier.add(claim_id, property_id, qualifier_value_1)
    assert r["success"] == 1
    assert r["claim"]["qualifiers"][property_id][0]["datavalue"]["value"] == qualifier_value_1
    assert r["claim"]["qualifiers"][property_id][0]["snaktype"] == "value"
    qualifier_id = r["claim"]["qualifiers"][property_id][0]["hash"]

    # Update qualifier
    r = wb_with_auth.qualifier.update(claim_id, qualifier_id, property_id, qualifier_value_2)
    assert r["success"] == 1
    assert r["claim"]["qualifiers"][property_id][0]["datavalue"]["value"] == qualifier_value_2
    assert r["claim"]["qualifiers"][property_id][0]["snaktype"] == "value"
    qualifier_id_updated = r["claim"]["qualifiers"][property_id][0]["hash"]

    # Delete qualifier
    r = wb_with_auth.qualifier.remove(claim_id, qualifier_id_updated)
    assert r["success"] == 1


def test_qualifier_no_value(wb_with_auth, item_id, property_id):
    # Create claim
    r = wb_with_auth.claim.add(item_id, property_id, claim_value)
    assert r["success"] == 1
    assert r["claim"]["mainsnak"]["property"] == property_id
    assert r["claim"]["mainsnak"]["snaktype"] == "value"
    claim_id = r["claim"]["id"]

    # Create qualifier
    r = wb_with_auth.qualifier.add(claim_id, property_id, None, snak_type="novalue")
    assert r["success"] == 1
    assert r["claim"]["qualifiers"][property_id][0]["snaktype"] == "novalue"
    qualifier_id = r["claim"]["qualifiers"][property_id][0]["hash"]

    # Update qualifier (use "somevalue")
    r = wb_with_auth.qualifier.update(
        claim_id, qualifier_id, property_id, None, snak_type="somevalue"
    )
    assert r["success"] == 1
    assert r["claim"]["qualifiers"][property_id][0]["snaktype"] == "somevalue"
    qualifier_id_updated = r["claim"]["qualifiers"][property_id][0]["hash"]

    # Delete qualifier
    r = wb_with_auth.qualifier.remove(claim_id, qualifier_id_updated)
    assert r["success"] == 1


def test_qualifier_some_value(wb_with_auth, item_id, property_id):
    # Create claim
    r = wb_with_auth.claim.add(item_id, property_id, claim_value)
    assert r["success"] == 1
    assert r["claim"]["mainsnak"]["property"] == property_id
    assert r["claim"]["mainsnak"]["snaktype"] == "value"
    claim_id = r["claim"]["id"]

    # Create qualifier
    r = wb_with_auth.qualifier.add(claim_id, property_id, None, snak_type="somevalue")
    assert r["success"] == 1
    assert r["claim"]["qualifiers"][property_id][0]["snaktype"] == "somevalue"
    qualifier_id = r["claim"]["qualifiers"][property_id][0]["hash"]

    # Update qualifier (use "novalue")
    r = wb_with_auth.qualifier.update(
        claim_id, qualifier_id, property_id, None, snak_type="novalue"
    )
    assert r["success"] == 1
    assert r["claim"]["qualifiers"][property_id][0]["snaktype"] == "novalue"
    qualifier_id_updated = r["claim"]["qualifiers"][property_id][0]["hash"]

    # Delete qualifier
    r = wb_with_auth.qualifier.remove(claim_id, qualifier_id_updated)
    assert r["success"] == 1
