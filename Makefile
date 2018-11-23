init:
	git config core.hooksPath .hooks

test:
	poetry run pytest -s

build-docs:
	poetry run make html -C docs

format:
	poetry run black wikibase_api --line-length=100

lint:
	poetry run flake8 wikibase_api --max-line-length=100
