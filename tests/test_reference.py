claim_value = "Claim value"
reference_value_1 = {"type": "string", "value": "Reference 1"}
reference_value_2 = {"type": "string", "value": "Reference 2"}


def test_reference(wb_with_auth, item_id, property_id):
    # Create claim
    r = wb_with_auth.claim.add(item_id, property_id, claim_value)
    assert r["success"] == 1
    assert r["claim"]["mainsnak"]["property"] == property_id
    assert r["claim"]["mainsnak"]["snaktype"] == "value"
    claim_id = r["claim"]["id"]

    # Create reference
    r = wb_with_auth.reference.add(claim_id, property_id, reference_value_1)
    assert r["success"] == 1
    assert r["reference"]["snaks"][property_id][0]["datavalue"] == reference_value_1
    assert r["reference"]["snaks"][property_id][0]["snaktype"] == "value"
    reference_id = r["reference"]["hash"]

    # Update reference
    r = wb_with_auth.reference.update(claim_id, property_id, reference_id, reference_value_2)
    assert r["success"] == 1
    assert r["reference"]["snaks"][property_id][0]["datavalue"] == reference_value_2
    assert r["reference"]["snaks"][property_id][0]["snaktype"] == "value"
    reference_id_updated = r["reference"]["hash"]

    # Delete reference
    r = wb_with_auth.reference.remove(claim_id, reference_id_updated)
    assert r["success"] == 1


def test_reference_no_value(wb_with_auth, item_id, property_id):
    # Create claim
    r = wb_with_auth.claim.add(item_id, property_id, claim_value)
    assert r["success"] == 1
    assert r["claim"]["mainsnak"]["property"] == property_id
    assert r["claim"]["mainsnak"]["snaktype"] == "value"
    claim_id = r["claim"]["id"]

    # Create reference
    r = wb_with_auth.reference.add(claim_id, property_id, None, "novalue")
    assert r["success"] == 1
    assert r["reference"]["snaks"][property_id][0]["snaktype"] == "novalue"
    reference_id = r["reference"]["hash"]

    # Update reference (use "somevalue")
    r = wb_with_auth.reference.update(claim_id, property_id, reference_id, None, "somevalue")
    assert r["success"] == 1
    assert r["reference"]["snaks"][property_id][0]["snaktype"] == "somevalue"
    reference_id_updated = r["reference"]["hash"]

    # Delete reference
    r = wb_with_auth.reference.remove(claim_id, reference_id_updated)
    assert r["success"] == 1


def test_reference_some_value(wb_with_auth, item_id, property_id):
    # Create claim
    r = wb_with_auth.claim.add(item_id, property_id, claim_value)
    assert r["success"] == 1
    assert r["claim"]["mainsnak"]["property"] == property_id
    assert r["claim"]["mainsnak"]["snaktype"] == "value"
    claim_id = r["claim"]["id"]

    # Create reference
    r = wb_with_auth.reference.add(claim_id, property_id, None, "somevalue")
    assert r["success"] == 1
    assert r["reference"]["snaks"][property_id][0]["snaktype"] == "somevalue"
    reference_id = r["reference"]["hash"]

    # Update reference (use "novalue")
    r = wb_with_auth.reference.update(claim_id, property_id, reference_id, None, "novalue")
    assert r["success"] == 1
    assert r["reference"]["snaks"][property_id][0]["snaktype"] == "novalue"
    reference_id_updated = r["reference"]["hash"]

    # Delete reference
    r = wb_with_auth.reference.remove(claim_id, reference_id_updated)
    assert r["success"] == 1
