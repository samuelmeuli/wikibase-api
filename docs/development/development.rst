.. _development:

Development
===========

Make sure you have Python 3 and `Pipenv <https://github.com/pypa/pipenv>`_ installed.

1. Clone the repository
2. Run ``pipenv install --dev`` to install the project dependencies
3. In the ``tests`` folder, rename the ``config-sample.json`` file to ``config.json``. This is the configuration file that will be used for testing. Fill in either the ``oauth_credentials`` or the ``login_credentials`` parameters and delete the other. In this file, you can also specify other parameters you want to pass to the :class:`.Wikibase` class when running the tests.
4. Execute the tests using ``pipenv run test``.
