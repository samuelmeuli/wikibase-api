import json

from wikibase_api.utils.possible_values import possible_ranks


class Claim:
    """Collection of API methods for claims"""

    def __init__(self, api):
        self.api = api

    def get(self, entity_id, property_id=None, rank=None):
        """Get the claims of the specified entity

        :param entity_id: Entity identifier (e.g. ``"Q1"``)
        :type entity_id: str
        :param property_id: Only return claims of the specified property (e.g. ``"P1"``)
        :type property_id: str
        :param rank: Only return claims of the specified rank (one of ``["preferred", "normal",
            "deprecated"]``)
        :type rank: str
        :return: Response
        :rtype: dict
        """
        params = {"action": "wbgetclaims", "entity": entity_id}

        if property_id is not None:
            params["property"] = property_id

        if rank is not None:
            if rank not in possible_ranks:
                raise ValueError('"rank" must be set to one of ' + ", ".join(possible_ranks))
            params["rank"] = rank

        return self.api.get(params)

    def create(self, entity_id, property_id, value):
        """Create a new claim for the specified entity

        :param entity_id: Entity identifier (e.g. ``"Q1"``)
        :type entity_id: str
        :param property_id: Property identifier (e.g. ``"P1"``)
        :type property_id: str
        :param value: Value of the claim
        :type value: any
        :return: Response
        :rtype: dict
        """
        value_str = json.dumps(value)
        params = {
            "action": "wbcreateclaim",
            "entity": entity_id,
            "property": property_id,
            "snaktype": "value",
            "value": value_str,
        }
        return self.api.post(params)

    def update(self, claim_id, new_value):
        """Update the value of the specified claim

        :param claim_id: Claim identifier (e.g. ``"Q2$8C67587E-79D5-4E8C-972C-A3C5F7ED06B3"``), can
            be obtained with :meth:`get`
        :type claim_id: str
        :param new_value: New value of the claim
        :type new_value: any
        :return: Response
        :rtype: dict
        """
        value_str = json.dumps(new_value)
        params = {
            "action": "wbsetclaimvalue",
            "claim": claim_id,
            "snaktype": "value",
            "value": value_str,
        }
        return self.api.post(params)

    def delete(self, claim_ids):
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
