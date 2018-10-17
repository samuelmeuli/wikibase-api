from wikibase_api.utils.possible_values import possible_languages


class Description:
    """Collection of API methods for descriptions"""

    def __init__(self, api):
        self.api = api

    def set(self, entity_id, description, language):
        """Create a new claim for the specified entity

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
        if language not in possible_languages:
            raise ValueError('"{}" is not in list of allowed languages'.format(language))

        params = {
            "action": "wbsetdescription",
            "id": entity_id,
            "language": language,
            "value": description,
        }
        return self.api.post(params)
