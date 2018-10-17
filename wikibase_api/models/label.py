from wikibase_api.utils.possible_values import possible_languages


class Label:
    """Collection of API methods for labels"""

    def __init__(self, api):
        self.api = api

    def set(self, entity_id, label, language):
        """Create a new claim for the specified entity

        :param entity_id: Entity identifier (e.g. ``"Q1"``)
        :type entity_id: str
        :param label: Value to set the label (site title) to (e.g. ``"Universe"``)
        :type label: str
        :param language: Language of the description (e.g. ``"en"``)
        :type language: str
        :return: Response
        :rtype: dict
        """
        if language not in possible_languages:
            raise ValueError('"{}" is not in list of allowed languages'.format(language))

        params = {"action": "wbsetlabel", "id": entity_id, "language": language, "value": label}
        return self.api.post(params)
