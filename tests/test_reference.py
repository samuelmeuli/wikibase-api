claim_value = "Claim value"
reference_value_1 = {"type": "string", "value": "Reference 1"}
reference_value_2 = {"type": "string", "value": "Reference 2"}


def test_reference(wb, item_id, property_id):
    # Create claim
    r = wb.claim.add(item_id, property_id, claim_value)
    assert r["success"] == 1
    assert r["claim"]["mainsnak"]["property"] == property_id
    claim_id = r["claim"]["id"]

    # Create reference
    r = wb.reference.add(claim_id, property_id, reference_value_1)
    assert r["success"] == 1
    assert r["reference"]["snaks"][property_id][0]["datavalue"] == reference_value_1
    reference_id = r["reference"]["hash"]

    # Update reference
    r = wb.reference.update(claim_id, property_id, reference_id, reference_value_2)
    assert r["success"] == 1
    assert r["reference"]["snaks"][property_id][0]["datavalue"] == reference_value_2
    reference_id_updated = r["reference"]["hash"]

    # Delete reference
    r = wb.reference.remove(claim_id, reference_id_updated)
    assert r["success"] == 1
