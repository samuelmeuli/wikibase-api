import json

from wikibase_api.utils.validate_value import validate_snak


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

    def add(self, claim_id, property_id, value, snak_type="value"):
        """Create a new qualifier for the specified claim

        :param claim_id: Claim identifier (e.g. ``"Q2$8C67587E-79D5-4E8C-972C-A3C5F7ED06B3"``)
        :type claim_id: str
        :param property_id: Property identifier (e.g. ``"P1"``)
        :type property_id: str
        :param value: Value of the qualifier. If snak_type is set to "novalue" or "somevalue", value
            must be None
        :type value: any
        :param snak_type: Value type (one of ``["value", "novalue", "somevalue"]``. ``"value"``
            (default) is used for normal property-value pairs. ``"novalue"`` is used to indicate
            that an item has none of the property (e.g. a person has no children). ``"somevalue"``
            is used when it is known that a value exists, but the value itself is not known
        :type snak_type: str
        :return: Response
        :rtype: dict
        """
        validate_snak(value, snak_type)
        params = {
            "action": "wbsetqualifier",
            "claim": claim_id,
            "property": property_id,
            "snaktype": snak_type,
        }
        if value:
            value_str = json.dumps(value)
            params["value"] = value_str
        return self.api.post(params)

    def update(self, claim_id, qualifier_id, property_id, value, snak_type="value"):
        """Update the value of the specified qualifier

        :param claim_id: Claim identifier (e.g. ``"Q2$8C67587E-79D5-4E8C-972C-A3C5F7ED06B3"``)
        :type claim_id: str
        :param property_id: Property identifier (e.g. ``"P1"``)
        :type property_id: str
        :param qualifier_id: Hash of the qualifier to be updated (e.g.
            ``"e3401fd064ec7c3cb7169aca6efff7419d95312a"``)
        :type qualifier_id: str
        :param value: Value of the qualifier. If snak_type is set to "novalue" or "somevalue", value
            must be None
        :type value: any
        :param snak_type: Value type (one of ``["value", "novalue", "somevalue"]``. ``"value"``
            (default) is used for normal property-value pairs. ``"novalue"`` is used to indicate
            that an item has none of the property (e.g. a person has no children). ``"somevalue"``
            is used when it is known that a value exists, but the value itself is not known
        :type snak_type: str
        :return: Response
        :rtype: dict
        """
        validate_snak(value, snak_type)
        params = {
            "action": "wbsetqualifier",
            "claim": claim_id,
            "property": property_id,
            "snaktype": snak_type,
            "snakhash": qualifier_id,
        }
        if value:
            value_str = json.dumps(value)
            params["value"] = value_str
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
