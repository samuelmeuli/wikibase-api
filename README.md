# wikibase-api

**`wikibase-api` is a Python library for simple access to the [Wikibase API](https://www.wikidata.org/w/api.php?action=help).**

It simplifies the authentication process and can be used to query and edit information on Wikidata or any other Wikibase instance.

**For an simpler, object-oriented abstraction of the Wikibase API, have a look at [`python-wikibase`](https://github.com/samuelmeuli/python-wikibase).**

## Installation

```sh
pip install wikibase-api
```

## Usage

Simple example for getting all information about a Wikidata page:

```py
from wikibase_api import Wikibase

wb = Wikibase()
r = wb.entity.get("Q1")
print(r)
```

Output:

```python
{
  "entities": {
    "Q1": {
      # ...
    }
  },
  "success": 1,
}
```

**See the [documentation](https://wikibase-api.readthedocs.io) for descriptions and examples of all commands.**

## Development

### Setup

See [this guide](https://wikibase-api.readthedocs.io/en/latest/development/development.html) on how to set up a development environment for this package.

If you'd like to test this package with a local instance of Wikibase, see [this guide](https://wikibase-api.readthedocs.io/en/latest/guides/local_wikibase_instance.html) on how to set up a development instance with `wikibase-docker`.

### Contributing

Suggestions and contributions are always welcome! Please first discuss changes via issue before submitting a pull request.
