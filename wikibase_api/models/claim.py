import json

from wikibase_api.utils.validate_value import validate_value


class Claim:
    """Collection of API functions for claims

     Example function call::

        from wikibase_api import Wikibase

        wb = Wikibase(
            # Parameters
        )

        r = wb.claim.get("Q1")
        print(r)
    """

    def __init__(self, api):
        self.api = api

    def get(self, entity_id, property_id=None, rank="normal"):
        """Get the claims of the specified entity

        :param entity_id: Entity identifier (e.g. ``"Q1"``)
        :type entity_id: str
        :param property_id: Only return claims of the specified property (e.g. ``"P1"``)
        :type property_id: str
        :param rank: Only return claims of the specified rank (one of ``["preferred", "normal",
            "deprecated"]``). Default: "normal"
        :type rank: str
        :return: Response
        :rtype: dict
        """
        params = {"action": "wbgetclaims", "entity": entity_id}

        if property_id is not None:
            params["property"] = property_id

        if rank is not None:
            validate_value(rank, "rank")
            params["rank"] = rank

        return self.api.get(params)

    def add(self, entity_id, property_id, value, snak_type="value"):
        """Create a new claim for the specified entity

        :param entity_id: Entity identifier (e.g. ``"Q1"``)
        :type entity_id: str
        :param property_id: Property identifier (e.g. ``"P1"``)
        :type property_id: str
        :param value: Value of the claim
        :type value: any
        :param snak_type: Value type (one of ``["value", "novalue", "somevalue"]``. ``"value"``
            (default) is used for normal property-value pairs. ``"novalue"`` is used to indicate
            that an item has none of the property (e.g. a person has no children). ``"somevalue"``
            is used when it is known that a value exists, but the value itself is not known
        :type snak_type: str
        :return: Response
        :rtype: dict
        """
        value_str = json.dumps(value)
        validate_value(snak_type, "snak_type")
        params = {
            "action": "wbcreateclaim",
            "entity": entity_id,
            "property": property_id,
            "snaktype": snak_type,
            "value": value_str,
        }
        return self.api.post(params)

    def update(self, claim_id, new_value, snak_type="value"):
        """Update the value of the specified claim

        :param claim_id: Claim identifier (e.g. ``"Q2$8C67587E-79D5-4E8C-972C-A3C5F7ED06B3"``), can
            be obtained with :meth:`get`
        :type claim_id: str
        :param new_value: New value of the claim
        :type new_value: any
        :param snak_type: Value type (one of ``["value", "novalue", "somevalue"]``. ``"value"``
            (default) is used for normal property-value pairs. ``"novalue"`` is used to indicate
            that an item has none of the property (e.g. a person has no children). ``"somevalue"``
            is used when it is known that a value exists, but the value itself is not known
        :type snak_type: str
        :return: Response
        :rtype: dict
        """
        value_str = json.dumps(new_value)
        validate_value(snak_type, "snak_type")
        params = {
            "action": "wbsetclaimvalue",
            "claim": claim_id,
            "snaktype": snak_type,
            "value": value_str,
        }
        return self.api.post(params)

    def remove(self, claim_ids):
        """Delete one or multiple claims

        :param claim_ids: Claim identifier(s) (e.g. ``"Q2$8C67587E-79D5-4E8C-972C-A3C5F7ED06B3"`` or
            ``["Q2$8C67587E-79D5-4E8C-972C-A3C5F7ED06B3",
            "Q2$ACC73295-5CF2-4B6A-95AA-CF156AB2B036"]``), can be obtained with :meth:`get`
        :type claim_ids: str or list(str)
        :return: Response
        :rtype: dict
        """
        if isinstance(claim_ids, str):
            ids_encoded = claim_ids
        else:
            ids_encoded = "|".join(claim_ids)
        params = {"action": "wbremoveclaims", "claim": ids_encoded}
        return self.api.post(params)
