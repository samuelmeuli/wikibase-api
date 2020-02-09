.. _local_wikibase_instance:

Local Wikibase Instance
=======================

The following is an introduction on how to build your own Wikibase instance using Docker. This instance can then be used for testing modifications using the Wikibase API without risking unwanted changes to the live instance.


Requirements
------------

Install `Docker <https://docs.docker.com/install>`_ and ``docker-compose`` if you don't have the tools already.


Setting up Wikibase
-------------------

Next, use `wikibase-docker <https://github.com/wmde/wikibase-docker>`_ to set up Wikibase and its query service on your machine:

1. Create an empty directory: ``mkdir wikibase-docker && cd wikibase-docker``
2. Download the ``docker-compose.yml`` file from the `wikibase-docker <https://github.com/wmde/wikibase-docker>`_ repo to the directory: ``wget https://raw.githubusercontent.com/wmde/wikibase-docker/master/docker-compose.yml``
3. Set up the Docker containers: ``docker-compose pull``
4. Start the containers: ``docker-compose up``

After a while, you should have a Wikibase instance up and running. MediaWiki can be accessed on http://localhost:8181 and the SPARQL UI at http://localhost:8282.
