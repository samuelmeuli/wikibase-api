from wikibase_api.utils.possible_values import possible_languages


class Alias:
    """Collection of API methods for aliases"""

    def __init__(self, api):
        self.api = api

    def add(self, entity_id, aliases, language):
        """Add one or multiple new aliases to the specified entity

        :param entity_id: Entity identifier (e.g. ``"Q1"``)
        :type entity_id: str
        :param aliases: Aliases to add to the existing ones
        :type aliases: str or list(str)
        :param language: Language of the description (e.g. ``"en"``)
        :type language: str
        :return: Response
        :rtype: dict
        """
        if language not in possible_languages:
            raise ValueError('"{}" is not in list of allowed languages'.format(language))

        if isinstance(aliases, str):
            aliases_encoded = aliases
        else:
            aliases_encoded = "|".join(aliases)

        params = {
            "action": "wbsetaliases",
            "id": entity_id,
            "add": aliases_encoded,
            "language": language,
        }
        return self.api.post(params)

    def remove(self, entity_id, aliases, language):
        """Remove one or multiple aliases from the specified entity

        :param entity_id: Entity identifier (e.g. ``"Q1"``)
        :type entity_id: str
        :param aliases: Existing aliases to remove
        :type aliases: str or list(str)
        :param language: Language of the description (e.g. ``"en"``)
        :type language: str
        :return: Response
        :rtype: dict
        """
        if language not in possible_languages:
            raise ValueError('"{}" is not in list of allowed languages'.format(language))

        if isinstance(aliases, str):
            aliases_encoded = aliases
        else:
            aliases_encoded = "|".join(aliases)

        params = {
            "action": "wbsetaliases",
            "id": entity_id,
            "remove": aliases_encoded,
            "language": language,
        }
        return self.api.post(params)

    def replace(self, entity_id, aliases, language):
        """Replace all existing aliases with the specified one(s) for an entity

        :param entity_id: Entity identifier (e.g. ``"Q1"``)
        :type entity_id: str
        :param aliases: Aliases to add after deleting all existing ones
        :type aliases: str or list(str)
        :param language: Language of the description (e.g. ``"en"``)
        :type language: str
        :return: Response
        :rtype: dict
        """
        if language not in possible_languages:
            raise ValueError('"{}" is not in list of allowed languages'.format(language))

        if isinstance(aliases, str):
            aliases_encoded = aliases
        else:
            aliases_encoded = "|".join(aliases)

        params = {
            "action": "wbsetaliases",
            "id": entity_id,
            "set": aliases_encoded,
            "language": language,
        }
        return self.api.post(params)
