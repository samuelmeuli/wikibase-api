required_oauth_entries = ["consumer_key", "consumer_secret", "access_token", "access_secret"]
required_login_entries = ["bot_username", "bot_password"]


def verify_auth_info(oauth_credentials, login_credentials):
    """
    Verify that the provided authentication credentials are of the correct form (i.e. exactly one
    authentication method is specified and the corresponding parameter contains the correct keys)
    """
    if oauth_credentials is None and login_credentials is None:
        raise KeyError(
            'Authentication information missing: Either the "oauth_credentials" or the '
            '"login_credentials" parameter must be provided to the Wikibase class'
        )
    if oauth_credentials is not None and login_credentials is not None:
        raise KeyError(
            'Authentication information conflict: Only one of the "oauth_credentials" and the '
            '"login_credentials" parameters must be provided to the Wikibase class'
        )
    if oauth_credentials is not None:
        for key in required_oauth_entries:
            if key not in oauth_credentials:
                raise KeyError(
                    'Key "{}" is missing in the "oauth_credentials" parameter'.format(key)
                )
    else:
        for key in required_login_entries:
            if key not in login_credentials:
                raise KeyError(
                    'Key "{}" is missing in the "login_credentials" parameter'.format(key)
                )
