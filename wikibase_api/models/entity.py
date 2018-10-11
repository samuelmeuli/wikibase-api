import json

from wikibase_api.utils.values import possible_attributes, possible_entities, possible_languages


class Entity:
    """Collection of API methods for Wikibase entities (items, properties, ...)"""

    def __init__(self, api):
        self.api = api

    def get_entity(self, entity_id, attributes=None, languages=None):
        """Get the data of one Wikibase entity

        :param entity_id: Entity identifier (e.g. "Q1")
        :type entity_id: str
        :param attributes: Names of the attributes to be fetched from the entity (e.g. "claims")
        :type attributes: list(str)
        :param languages: Languages to return the fetched data in (e.g. "en")
        :type languages: list(str)
        :return: Response
        :rtype: dict
        """
        return self.get_entities([entity_id], attributes=attributes, languages=languages)

    def get_entities(self, entity_ids, attributes=None, languages=None):
        """Get the data of multiple Wikibase entities

        :param entity_ids: Entity identifiers (e.g. ["Q1", "Q2"])
        :type entity_ids: list(str)
        :param attributes: Names of the attributes to be fetched from each entity (e.g. "claims")
        :type attributes: list(str)
        :param languages: Languages to return the fetched data in (e.g. "en")
        :type languages: list(str)
        :return: Response
        :rtype: dict
        """
        ids_encoded = "|".join(entity_ids)
        params = {"action": "wbgetentities", "ids": ids_encoded}

        if languages is not None:
            for lang in languages:
                if lang not in possible_languages:
                    raise ValueError('"{}" is not in list of allowed languages'.format(lang))
            params["languages"] = "|".join(attributes)

        if attributes is not None:
            for prop in attributes:
                if prop not in possible_attributes:
                    raise ValueError('"{}" is not in list of allowed attributes'.format(prop))
            params["props"] = "|".join(attributes)

        return self.api.get(params)

    def create_entity(self, entity_type, content=None):
        """Create a new Wikibase entity

        :param entity_type: Type of entity to be created (e.g. "item")
        :type entity_type: str
        :param content: Content of the new entity
        :type content: dict
        :return: Response
        :rtype: dict
        """
        if entity_type not in possible_entities:
            raise ValueError('"entity_type" must be set to one of ' + ", ".join(possible_entities))
        if content is None:
            content = {}
        content_str = json.dumps(content)
        params = {"action": "wbeditentity", "new": entity_type, "data": content_str}
        return self.api.post(params)

    def edit_entity(self, entity_id, content):
        """Modify an existing Wikibase entity

        :param entity_id: Entity identifier (e.g. "Q1")
        :type entity_id: str
        :param content: Content to add to the entity
        :type content: dict
        :return: Response
        :rtype: dict
        """
        content_str = json.dumps(content)
        params = {"action": "wbeditentity", "id": entity_id, "data": content_str}
        return self.api.post(params)
