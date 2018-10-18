import json


class Qualifier:
    """Collection of API functions for qualifiers

    Example function call::

        from wikibase_api import Wikibase

        wb = Wikibase(
            # Parameters
        )

        claim_id = "Q2$8C67587E-79D5-4E8C-972C-A3C5F7ED06B3"
        r = wb.qualifier.add(claim_id, "P585", "13700 million years BCE")
        print(r)
    """

    def __init__(self, api):
        self.api = api

    def add(self, claim_id, property_id, value):
        """Create a new qualifier for the specified claim

        :param claim_id: Claim identifier (e.g. ``"Q2$8C67587E-79D5-4E8C-972C-A3C5F7ED06B3"``)
        :type claim_id: str
        :param property_id: Property identifier (e.g. ``"P1"``)
        :type property_id: str
        :param value: Value of the qualifier
        :type value: any
        :return: Response
        :rtype: dict
        """
        value_encoded = json.dumps(value)
        params = {
            "action": "wbsetqualifier",
            "claim": claim_id,
            "property": property_id,
            "value": value_encoded,
            "snaktype": "value",
        }

        return self.api.post(params)

    def update(self, claim_id, qualifier_id, property_id, new_value):
        """Update the value of the specified qualifier

        :param claim_id: Claim identifier (e.g. ``"Q2$8C67587E-79D5-4E8C-972C-A3C5F7ED06B3"``)
        :type claim_id: str
        :param property_id: Property identifier (e.g. ``"P1"``)
        :type property_id: str
        :param qualifier_id: Hash of the qualifier to be updated (e.g.
            ``"e3401fd064ec7c3cb7169aca6efff7419d95312a"``)
        :type qualifier_id: str
        :param new_value: Value of the qualifier
        :type new_value: any
        :return: Response
        :rtype: dict
        """
        value_encoded = json.dumps(new_value)
        params = {
            "action": "wbsetqualifier",
            "claim": claim_id,
            "property": property_id,
            "value": value_encoded,
            "snaktype": "value",
            "snakhash": qualifier_id,
        }

        return self.api.post(params)

    def remove(self, claim_id, qualifier_ids):
        """Delete the specified qualifier(s)

        :param claim_id: Claim identifier (e.g. ``"Q2$8C67587E-79D5-4E8C-972C-A3C5F7ED06B3"``)
        :type claim_id: str
        :param qualifier_ids: Hash(es) of the qualifier(s) to be deleted (e.g.
            ``"e3401fd064ec7c3cb7169aca6efff7419d95312a"``,
            ``["e3401fd064ec7c3cb7169aca6efff7419d95312a",
            "d86fda314abf561afca0d1fef97546ea050f3c1e"]``)
        :type qualifier_ids: str or list(str)
        :return: Response
        :rtype: dict
        """
        if isinstance(qualifier_ids, str):
            ids_encoded = qualifier_ids
        else:
            ids_encoded = "|".join(qualifier_ids)

        params = {"action": "wbremovequalifiers", "claim": claim_id, "qualifiers": ids_encoded}

        return self.api.post(params)
