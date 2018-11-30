# wikibase-api

`wikibase-api` is a Python library for simple access to the Wikibase API. For example, it can be used to query and edit information on Wikidata.


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

The documentation for this library can be found at [TODO URL](TODO URL).
