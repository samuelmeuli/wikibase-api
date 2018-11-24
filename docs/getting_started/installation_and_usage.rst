.. _installation_and_usage:

Installation and Usage
======================

1. Installation
---------------

```
pip install wikibase-api
```


2. Authentication
-----------------

To access the API, simply create an instance of the :class:`.Wikibase` class::

    from wikibase_api import Wikibase

    wb = Wikibase(
        # Parameters
    )


.. note::
    The Wikibase instance which is accessed by default is Wikidata. To use another instance, e.g. a local one for testing, set the ``api_url`` parameter accordingly. You can find a guide on how to set up your own instance locally using Docker under :ref:`local_wikibase_instance`.

    Another way to test your edits is to query/modify Wikibase's `sandbox item <https://www.wikidata.org/wiki/Q4115189>`_.

Before being able to make requests, you need to authenticate yourself to the API. You have two options:

* Authentication using `OAuth <#a-oauth>`_
* Authentication with a `user account <#b-user-login>`_

OAuth is the `recommended method <https://www.mediawiki.org/wiki/API:Login>`_ as it is more secure than logging in with username and password. However, setting up OAuth is more complicated and requires you to apply for credentials.


a) OAuth
~~~~~~~~

To be able to use OAuth, you need to obtain credentials for an owner-only consumer. This information can be obtained at ``Special:OAuthConsumerRegistration/propose`` (i.e. https://meta.wikimedia.org/wiki/Special:OAuthConsumerRegistration/propose for Wikimedia or http://localhost:8181/wiki/Special:OAuthConsumerRegistration/propose on a local instance):

1. Log in using your username and password
2. Fill in the registration form:

    * Application name and description
    * Tick "This consumer is for use only by <username>"
    * Select the `grants <https://www.mediawiki.org/wiki/Special:ListGrants>`_ you need, e.g. "High-volume editing", "Edit existing pages", "Create, edit, and move pages", and "Delete pages, revisions, and log entries"

3. Click the "Propose consumer" button at the bottom of the page
4. Write down your OAuth consumer information

Now, you can create an instance of the :class:`.Wikibase` class using your newly obtained OAuth credentials::

    from wikibase_api import Wikibase

    oauth_credentials = {
        "consumer_key": "...",
        "consumer_secret": "...",
        "access_token": "...",
        "access_secret": "...",
    }

    wb = Wikibase(oauth_credentials=oauth_credentials)

.. note::
    Some additional steps are required when using OAuth on a local Wikibase instance (see :ref:`oauth_on_local_wikibase_instance`).


b) User Login
~~~~~~~~~~~~~

Bot passwords allow users to access the API without providing their account's main login credentials. You can generate a bot password under ``Special:BotPasswords`` (i.e. https://www.wikidata.org/wiki/Special:BotPasswords on Wikidata or http://localhost:8181/wiki/Special:BotPasswords on a local instance):

1. Log in using your username and password
2. Fill in the registration form:

    * Choose a bot name (this will be a suffix to your username)
    * Select the `grants <https://www.mediawiki.org/wiki/Special:ListGrants>`_ you need, e.g. "High-volume editing", "Edit existing pages", "Create, edit, and move pages", and "Delete pages, revisions, and log entries"

3. Click the "Create" button at the bottom of the page
4. Write down your bot username and password

Now, you can create an instance of the :class:`.Wikibase` class using your newly obtained bot credentials::

    from wikibase_api import Wikibase

    login_credentials = {
        "bot_username": "...",
        "bot_password": "...",
    }

    wb = Wikibase(login_credentials=login_credentials)


3. Usage
--------

You can now make calls to the Wikibase API. For instance, you can fetch all information about an item::

    r = wikibase.entity.get("Q1")
    print(r)

Output::

    {
      "entities": {
        "Q1": {
          # ...
        }
      },
      "success": 1,
    }

For a list of all available API functions, have a look at the :ref:`api_reference`.
