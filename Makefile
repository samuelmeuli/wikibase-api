# Install dependencies and Git hooks
.PHONY: install
install:
	poetry install
	git config core.hooksPath .hooks

# Run tests
.PHONY: test
test:
	poetry run pytest -s

# Build docs using Sphinx
.PHONY: docs-build
docs-build:
	poetry run make html -C docs

# Open built docs
.PHONY: docs-open
docs-open: docs-build
	open docs/_build/html/index.html

# Format Python code using Black
.PHONY: format
format:
	poetry run black wikibase_api --line-length=100 ${BLACK_FLAGS}

# Lint Python code using flake8
.PHONY: lint
lint:
	poetry run flake8 wikibase_api --max-line-length=100
