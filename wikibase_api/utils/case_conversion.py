import re


def camel_to_snake_case(var_name):
    """Convert a variable name from camel case to snake case

    :param var_name: Variable name in camel case
    :type var_name: str
    :return: Variable name in snake case
    :rtype: str
    """
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", var_name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


def dict_to_snake_case(content):
    """Convert all camel-case keys and sub-keys in a dict to snake case

    :param content: Dict with keys in camel case
    :type content: dict
    :return: Dict with keys in snake case
    :rtype: dict
    """
    out = {}
    for key in content:
        new_key = camel_to_snake_case(key)
        if isinstance(content[key], dict):
            out[new_key] = dict_to_snake_case(content[key])
        else:
            out[new_key] = content[key]
    return out
