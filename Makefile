.PHONY: install
install:
	poetry install
	git config core.hooksPath .hooks

.PHONY: test
test:
	poetry run pytest -s

.PHONY: build-docs
build-docs:
	poetry run make html -C docs

.PHONY: format
format:
	poetry run black wikibase_api --line-length=100

.PHONY: lint
lint:
	poetry run flake8 wikibase_api --max-line-length=100
