import json


class Reference:
    """Collection of API functions for references

    Example function call::

        from wikibase_api import Wikibase

        wb = Wikibase(
            # Parameters
        )

        claim_id = "Q2$8C67587E-79D5-4E8C-972C-A3C5F7ED06B3"
        r = wb.reference.add(claim_id, "P854", "https://example.com")
        print(r)
    """

    def __init__(self, api):
        self.api = api

    def add(self, claim_id, property_id, value, index=None):
        """Create a new reference for the specified claim

        :param claim_id: Claim identifier (e.g. ``"Q2$8C67587E-79D5-4E8C-972C-A3C5F7ED06B3"``)
        :type claim_id: str
        :param property_id: Property identifier (e.g. ``"P1"``)
        :type property_id: str
        :param value: Value of the reference
        :type value: any
        :param index: Position of the new reference within the list of references (e.g. ``0`` to add
            the reference to the top of the list)
        :type index: int
        :return: Response
        :rtype: dict
        """
        snak = {property_id: [{"snaktype": "value", "property": property_id, "datavalue": value}]}
        snak_encoded = json.dumps(snak)

        params = {"action": "wbsetreference", "statement": claim_id, "snaks": snak_encoded}

        if index is not None:
            params["index"] = str(index)

        return self.api.post(params)

    def update(self, claim_id, property_id, reference_id, new_value, index=None):
        """Update the value of the specified reference

        :param claim_id: Claim identifier (e.g. ``"Q2$8C67587E-79D5-4E8C-972C-A3C5F7ED06B3"``)
        :type claim_id: str
        :param property_id: Property identifier (e.g. ``"P1"``)
        :type property_id: str
        :param reference_id: Hash of the reference to be updated (e.g.
            ``"9d5f29a997ad9ced2b1138556a896734148c4a0c"``)
        :type reference_id: str
        :param new_value: Value of the reference
        :type new_value: any
        :param index: Position of the new reference within the list of references (e.g. ``0`` to add
            the reference to the top of the list)
        :type index: int
        :return: Response
        :rtype: dict
        """
        snak = {
            property_id: [{"snaktype": "value", "property": property_id, "datavalue": new_value}]
        }
        snak_encoded = json.dumps(snak)

        params = {
            "action": "wbsetreference",
            "statement": claim_id,
            "reference": reference_id,
            "snaks": snak_encoded,
        }

        if index is not None:
            params["index"] = str(index)

        return self.api.post(params)

    def remove(self, claim_id, reference_ids):
        """Delete the specified reference(s)

        :param claim_id: Claim identifier (e.g. ``"Q2$8C67587E-79D5-4E8C-972C-A3C5F7ED06B3"``)
        :type claim_id: str
        :param reference_ids: Hash(es) of the reference(s) to be deleted (e.g.
            ``"9d5f29a997ad9ced2b1138556a896734148c4a0c"``,
            ``["9d5f29a997ad9ced2b1138556a896734148c4a0c",
            "0b0ca37729a3f637c100832d2a30fe9d867ef385"]``)
        :type reference_ids: str or list(str)
        :return: Response
        :rtype: dict
        """
        if isinstance(reference_ids, str):
            ids_encoded = reference_ids
        else:
            ids_encoded = "|".join(reference_ids)

        params = {"action": "wbremovereferences", "statement": claim_id, "references": ids_encoded}

        return self.api.post(params)
