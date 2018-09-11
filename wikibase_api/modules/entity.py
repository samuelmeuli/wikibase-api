import json

from wikibase_api.utils.values import possible_entities, possible_languages, possible_properties


class Entity:
    def __init__(self, api):
        self.api = api

    def get_entity(self, entity_id, languages=None, properties=None):
        """
        Get the data of one Wikibase entity
        :param entity_id: Entity identifier (e.g. "Q1")
        :type entity_id: str
        :param properties: Names of the properties to be fetched from the entity (see
        possible_properties)
        :type properties: list(str)
        :param languages: Languages to return the fetched data in (see possible_languages)
        :type languages: list(str)
        :return: Response
        :rtype dict
        """
        return self.get_entities([entity_id], languages=languages, properties=properties)

    def get_entities(self, entity_ids, languages=None, properties=None):
        """
        Get the data of multiple Wikibase entities
        :param entity_ids: Entity identifiers (e.g. ["Q1", "Q2"])
        :type entity_ids: list(str)
        :param properties: Names of the properties to be fetched from each entity (see
        possible_properties)
        :type properties: list(str)
        :param languages: Languages to return the fetched data in (see possible_languages)
        :type languages: list(str)
        :return: Response
        :rtype dict
        """
        ids_encoded = "|".join(entity_ids)
        params = {"action": "wbgetentities", "ids": ids_encoded}

        if languages is not None:
            for lang in languages:
                if lang not in possible_languages:
                    raise ValueError('"{}" is not in list of allowed languages'.format(lang))
            params["languages"] = "|".join(properties)

        if properties is not None:
            for prop in properties:
                if prop not in possible_properties:
                    raise ValueError('"{}" is not in list of allowed properties'.format(prop))
            params["props"] = "|".join(properties)

        return self.api.get(params)

    def create_entity(self, entity_type, content=None):
        """
        Create a new Wikibase entity
        :param entity_type: Type of entity to be created (see possible_entities)
        :type entity_type: str
        :param content: Content of the new entity
        :type content: dict
        :return: Response
        :rtype dict
        """
        if entity_type not in possible_entities:
            raise ValueError('"entity_type" must be set to one of ' + ", ".join(possible_entities))
        if content is None:
            content = {}
        content_str = json.dumps(content)
        params = {"action": "wbeditentity", "new": entity_type, "data": content_str}
        return self.api.post(params)

    def edit_entity(self, entity_id, content, clear=False):
        """
        Modify an existing Wikibase entity
        :param entity_id: Entity identifier (e.g. "Q1")
        :type entity_id: str
        :param content: Content to add to the entity
        :type content: dict
        :param clear: If true, the existing entity is cleared before adding the content
        :type clear: bool
        :return:
        """
        content_str = json.dumps(content)
        params = {"action": "wbeditentity", "id": entity_id, "data": content_str, "clear": clear}
        return self.api.post(params)