from wikibase_api.utils.validate_value import validate_value


class Label:
    """Collection of API functions for labels

    Example function call::

        from wikibase_api import Wikibase

        wb = Wikibase(
            # Parameters
        )

        r = wb.label.set("Q1", "univers", "fr")
        print(r)
    """

    def __init__(self, api):
        self.api = api

    def set(self, entity_id, label, language):
        """Set the label in the specified language for an entity

        :param entity_id: Entity identifier (e.g. ``"Q1"``)
        :type entity_id: str
        :param label: Value to set the label (site title) to (e.g. ``"Universe"``)
        :type label: str
        :param language: Language of the description (e.g. ``"en"``)
        :type language: str
        :return: Response
        :rtype: dict
        """
        validate_value(language, "language")
        params = {"action": "wbsetlabel", "id": entity_id, "language": language, "value": label}
        return self.api.post(params)
