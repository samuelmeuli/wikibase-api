import os
import sys

sys.path.insert(0, os.path.abspath(".."))

from wikibase_api.__version__ import __version__  # noqa: E402


# Project information
author = "Samuel Meuli"
copyright = "2018, Samuel Meuli"
project = "wikibase-api"
release = __version__
version = __version__

# Build configuration
exclude_patterns = ["_build"]
extensions = ["sphinx.ext.autodoc"]
master_doc = "index"
source_suffix = ".rst"

# HTML output
html_theme = "sphinx_rtd_theme"
htmlhelp_basename = project
