.. _development:

Development
===========

Make sure you have Python 3 and `Poetry <https://github.com/sdispater/poetry>`_ installed.

1. Clone the repository
2. Run ``poetry install`` to install the project dependencies
3. Rename the ``config-example.json`` file to ``config-tests.json``. This is the configuration file that will be used for testing. Fill in either the ``oauth_credentials`` or the ``login_credentials`` parameters and delete the other. In this file, you can also specify other parameters you want to pass to the :class:`.Wikibase` class when running the tests.
4. Make your changes to the code.
5. Execute the tests using ``make test``.
