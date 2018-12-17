.PHONY: install
install:
	poetry install
	git config core.hooksPath .hooks

.PHONY: test
test:
	poetry run pytest -s

.PHONY: docs-build
docs-build:
	poetry run make html -C docs

.PHONY: docs-open
docs-open:
	open docs/_build/html/index.html

.PHONY: format
format:
	poetry run black wikibase_api --line-length=100

.PHONY: lint
lint:
	poetry run flake8 wikibase_api --max-line-length=100
