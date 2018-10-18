from wikibase_api.utils.validate_value import validate_value


class Description:
    """Collection of API functions for descriptions

     Example function call::

        from wikibase_api import Wikibase

        wb = Wikibase(
            # Parameters
        )

        r = wb.description.set("Q1", "totality of space and all matter and radiation in it")
        print(r)
    """

    def __init__(self, api):
        self.api = api

    def set(self, entity_id, description, language):
        """Set the title in the specified language for an entity

        :param entity_id: Entity identifier (e.g. ``"Q1"``)
        :type entity_id: str
        :param description: Value to set the description to (e.g. ``"third planet from the Sun in
            the Solar System"``)
        :type description: str
        :param language: Language of the description (e.g. ``"en"``)
        :type language: str
        :return: Response
        :rtype: dict
        """
        validate_value(language, "language")

        params = {
            "action": "wbsetdescription",
            "id": entity_id,
            "language": language,
            "value": description,
        }
        return self.api.post(params)
