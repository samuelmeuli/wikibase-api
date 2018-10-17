property_id = "P245"
claim_geo = {"latitude": 40.748433, "longitude": -73.985656, "precision": 0.000001}


class TestClaim(object):
    def test_create_claim(self, wb, item_id):
        r = wb.claim.create(item_id, property_id, value=claim_geo)
        assert type(r) is dict
        assert r["success"] == 1
        assert r["claim"]["mainsnak"]["property"] == property_id

    def test_get_claims(self, wb, item_id):
        r = wb.claim.get(item_id)
        assert type(r) is dict
        assert "claims" in r
