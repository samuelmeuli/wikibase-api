MODULE_PATH="wikibase_api"

# Install dependencies and Git hooks
.PHONY: install
install:
	poetry install
	git config core.hooksPath .hooks

# Update dependencies
.PHONY: update
update:
	poetry update
	poetry export --format requirements.txt --output ./docs/requirements.txt

# Run tests
.PHONY: test
test:
	poetry run pytest -s

# Build docs using Sphinx
.PHONY: docs-build
docs-build:
	poetry run sphinx-build ./docs ./docs/_build

# Open built docs
.PHONY: docs-open
docs-open:
	open docs/_build/index.html

# Format Python code using Black and isort
.PHONY: format
format:
	poetry run black ${MODULE_PATH} ${BLACK_FLAGS}
	poetry run isort ${MODULE_PATH} --recursive ${ISORT_FLAGS}

# Lint Python code using flake8
.PHONY: lint
lint:
	poetry run flake8 ${MODULE_PATH} --max-line-length=100
