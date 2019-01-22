claim_value_1 = "Claim value 1"
claim_value_2 = "Claim value 2"


def test_claim(wb_with_auth, item_id, property_id):
    # Create claim
    r = wb_with_auth.claim.add(item_id, property_id, claim_value_1)
    assert r["success"] == 1
    assert r["claim"]["mainsnak"]["property"] == property_id
    assert r["claim"]["mainsnak"]["snaktype"] == "value"
    claim_id = r["claim"]["id"]

    # Update claim
    r = wb_with_auth.claim.update(claim_id, claim_value_2)
    assert r["success"] == 1
    assert r["claim"]["mainsnak"]["property"] == property_id
    assert r["claim"]["mainsnak"]["datavalue"]["value"] == claim_value_2

    # Delete claim
    r = wb_with_auth.claim.remove(claim_id)
    assert r["success"] == 1
    assert r["claims"][0] == claim_id


def test_claim_no_value(wb_with_auth, item_id, property_id):
    # Create claim
    r = wb_with_auth.claim.add(item_id, property_id, None, snak_type="novalue")
    assert r["success"] == 1
    assert r["claim"]["mainsnak"]["property"] == property_id
    assert r["claim"]["mainsnak"]["snaktype"] == "novalue"
    claim_id = r["claim"]["id"]

    # Update claim
    r = wb_with_auth.claim.update(claim_id, None, snak_type="novalue")
    assert r["success"] == 1
    assert r["claim"]["mainsnak"]["property"] == property_id
    assert r["claim"]["mainsnak"]["snaktype"] == "novalue"

    # Delete claim
    r = wb_with_auth.claim.remove(claim_id)
    assert r["success"] == 1
    assert r["claims"][0] == claim_id


def test_claim_some_value(wb_with_auth, item_id, property_id):
    # Create claim
    r = wb_with_auth.claim.add(item_id, property_id, None, snak_type="somevalue")
    assert r["success"] == 1
    assert r["claim"]["mainsnak"]["property"] == property_id
    assert r["claim"]["mainsnak"]["snaktype"] == "somevalue"
    claim_id = r["claim"]["id"]

    # Update claim
    r = wb_with_auth.claim.update(claim_id, None, snak_type="somevalue")
    assert r["success"] == 1
    assert r["claim"]["mainsnak"]["property"] == property_id
    assert r["claim"]["mainsnak"]["snaktype"] == "somevalue"

    # Delete claim
    r = wb_with_auth.claim.remove(claim_id)
    assert r["success"] == 1
    assert r["claims"][0] == claim_id
