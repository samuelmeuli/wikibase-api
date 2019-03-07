# wikibase-api

`wikibase-api` is a Python library for simple access to the [Wikibase API](https://www.wikidata.org/w/api.php?action=help). It simplifies the authentication process and can be used to query and edit information on Wikidata or any other Wikibase instance.

For an simpler, object-oriented abstraction of the Wikibase API, have a look at [`python-wikibase`](https://github.com/samuelmeuli/python-wikibase).

## Installation

```sh
pip install wikibase-api
```

## Usage

Simple example for getting all information about a Wikidata page:

```python
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

## Documentation

The documentation for this library can be built using the following commands:

```sh
git clone REPO_URL
make docs-build
make docs-open
```
