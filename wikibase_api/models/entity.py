import json

from wikibase_api.utils.validate_value import validate_value


class Entity:
    """Collection of API functions for Wikibase entities (items, properties, ...)

    Example function call::

        from wikibase_api import Wikibase

        wb = Wikibase(
            # Parameters
        )

        content = {"labels": {"en": {"language": "en", "value": "Updated label"}}}
        r = wb.entity.update("Q1", content=content)
        print(r)
    """

    def __init__(self, api):
        self.api = api

    def get(self, entity_ids, attributes=None, languages=None):
        """Get the data of one or multiple Wikibase entities

        :param entity_ids: Entity identifier(s) (e.g. ``"Q1"`` or ``["Q1", "Q2"]``)
        :type entity_ids: str or list(str)
        :param attributes: Names of the attributes to be fetched from each entity (e.g.
            ``"claims"``)
        :type attributes: list(str)
        :param languages: Languages to return the fetched data in (e.g. ``"en"``)
        :type languages: list(str)
        :return: Response
        :rtype: dict
        """
        if isinstance(entity_ids, str):
            ids_encoded = entity_ids
        else:
            ids_encoded = "|".join(entity_ids)
        params = {"action": "wbgetentities", "ids": ids_encoded}

        if languages is not None:
            for lang in languages:
                validate_value(lang, "language")
            params["languages"] = "|".join(attributes)

        if attributes is not None:
            for prop in attributes:
                validate_value(prop, "attribute")
            params["props"] = "|".join(attributes)

        return self.api.get(params)

    def add(self, entity_type, content=None):
        """Create a new Wikibase entity

        :param entity_type: Type of entity to be created (e.g. ``"item"``)
        :type entity_type: str
        :param content: Content of the new entity
        :type content: dict
        :return: Response
        :rtype: dict
        """
        validate_value(entity_type, "entity")
        if content is None:
            content = {}
        content_str = json.dumps(content)
        params = {"action": "wbeditentity", "new": entity_type, "data": content_str}
        return self.api.post(params)

    def update(self, entity_id, content):
        """Modify the specified Wikibase entity

        :param entity_id: Entity identifier (e.g. ``"Q1"``)
        :type entity_id: str
        :param content: Content to add to the entity
        :type content: dict
        :return: Response
        :rtype: dict
        """
        content_str = json.dumps(content)
        params = {"action": "wbeditentity", "id": entity_id, "data": content_str}
        return self.api.post(params)

    def remove(self, title, reason=None):
        """Delete the specified Wikibase entity

        :param title: Entity title (e.g. ``"Item:Q1"`` or ``"Property:P1"``)
        :type title: str
        :param reason: Reason for the deletion (if not set, Wikibase will use an automatically
            generated reason)
        :return: Response
        :rtype: dict
        """
        params = {"action": "delete", "title": title}
        if reason is not None:
            params["reason"] = reason
        return self.api.post(params)

    def search(self, search_key, language, entity_type="item", limit=10, offset=0):
        """Search for entities based on their labels and aliases

        :param search_key: String for which Wikibase entities' labels and aliases are searched
        :type search_key: str
        :param language: Languages to search in (e.g. ``"en"``)
        :type language: str
        :param entity_type: Type of entities to search for. Default: "item"
        :type entity_type: str
        :param limit: Maximum number of results to return. Default: 10
        :type limit: int
        :param offset: Offset where to continue a search. Default: 0
        :type offset: int
        :return: Response
        :rtype: dict
        """
        validate_value(language, "language")
        if entity_type is not None:
            validate_value(entity_type, "entity")

        params = {
            "action": "wbsearchentities",
            "search": search_key,
            "language": language,
            "limit": str(limit),
        }

        if entity_type is not None:
            params["type"] = entity_type
        if offset is not None:
            params["offset"] = str(offset)

        return self.api.get(params)
