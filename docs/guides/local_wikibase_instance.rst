.. _local_wikibase_instance:

Local Wikibase Instance
=======================

The following is an introduction on how to build your own Wikibase instance using Docker. This instance can then be used for testing modifications using the Wikibase API without risking unwanted changes to the live instance.


Requirements
------------

Install `Docker <https://docs.docker.com/install>`_ if you don't have it already.


Setting up Wikibase
-------------------

Next, use `wikibase-docker <https://github.com/wmde/wikibase-docker>`_ to set up Wikibase and its query service on your machine:

1. Create an empty directory: ``mkdir wikibase-docker && cd wikibase-docker``
2. Download the ``docker-compose.yml`` file from the `wikibase-docker <https://github.com/wmde/wikibase-docker>`_ repo to the directory: ``wget https://raw.githubusercontent.com/wmde/wikibase-docker/master/docker-compose.yml``
3. Set up the Docker containers: ``docker-compose pull``
4. Start the containers: ``docker-compose up``

After a while, you should have the Wikibase instance up and running. The MediaWiki can be accessed on http://localhost:8181 and the UI for the SPARQL query service at http://localhost:8282.


Adding content
--------------

Right now, your Wikibase instance doesn't contain any data, so most API methods won't be useful yet. A good way to fill your Wikibase with some data is to copy parts of Wikidata to your local instance. This can be done using `WikibaseImport <https://github.com/filbertkm/WikibaseImport>`_, which comes bundled in your Wikibase installation:

1. List your Docker containers using ``docker ps``. Copy the ID of the ``wikibase/wikibase`` container
2. Use ``docker exec -t -i CONTAINER_ID /bin/bash`` to execute commands in the running Wikibase container
3. To import all Wikibase properties into your local instance, run ``php extensions/WikibaseImport/maintenance/importEntities.php --all-properties``. This will take a while
4. To import some Wikibase entities, run a command like ``php extensions/WikibaseImport/maintenance/importEntities.php --range Q1:Q20``

After that, you can view the imported entities in your local MediaWiki, e.g. entity ``Q10`` on http://localhost:8181/wiki/Item:Q10.


.. _oauth_on_local_wikibase_instance:

OAuth on local Wikibase instance
--------------------------------

To use OAuth on the local Wikibase instance, some additional steps are required.

1. Create a user account on the MediaWiki interface (http://localhost:8181)
2. List your Docker containers using ``docker ps``. Copy the ID of the ``wikibase/wikibase`` container
3. Use ``docker exec -t -i CONTAINER_ID /bin/bash`` to execute the following commands in the running Wikibase container:

    * Verify the user's password using ``php maintenance/resetUserEmail.php --no-reset-password YOUR_USERNAME YOUR_EMAIL``
    * Grant your user admin rights: ``php maintenance/createAndPromote.php --sysop YOUR_USERNAME --force``

4. Navigate to http://localhost:8181/wiki/Special:OAuthConsumerRegistration and continue with the steps described under :ref:`installation_and_usage`.
