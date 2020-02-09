.. _development:

Development
===========

You can use the following steps to test and modify this library on your machine.

Requirements
------------

Make sure you have Python 3.6+ and `Poetry <https://github.com/sdispater/poetry>`_ installed.


Setup
-----

1. Clone the repository from GitHub.
2. Run ``make install`` to install the project's dependencies and Git hooks.
3. Set up ``wikibase-docker`` by following the ":ref:`local_wikibase_instance`" guide.
4. Rename the ``config-example.json`` file to ``config-tests.json``. This is the configuration file that will be used for testing. Fill in either the ``oauth_credentials`` or the ``login_credentials`` parameters and delete the other. If you didn't change ``wikibase-docker``'s configuration, you can use the following:

   .. code-block:: json

       {
         "apiUrl": "http://localhost:8181/w/api.php",
         "loginCredentials": {
           "botUsername": "WikibaseAdmin",
           "botPassword": "WikibaseDockerAdminPass"
         }
       }

   In ``config-tests.json``, you can also specify other parameters you want to pass to the :class:`.Wikibase` class during testing.
5. Make your changes to the code.
6. Make sure the tests are still passing (``make test``).
