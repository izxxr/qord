# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys
sys.path.insert(0, os.path.abspath('../../'))


# -- Project information -----------------------------------------------------

project = 'Qord'
copyright = '2022, izxxr'
author = 'izxxr'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# RST Prolog
embed_restricted_field = "This field can only be returned by embeds from API responses " \
                         "that are created by external sources. This field is not available " \
                         "to be set by bots or webhooks. As such you should never set this " \
                         "field manually, setting it will either have no effect on the embed " \
                         "or you will run into unexpected issues." # type: ignore

supports_comparison = "This class supports equality comparison between instances of this class " \
                      "by the :attr:`.id` attribute." # type: ignore

rst_prolog = f"""
.. |embed-restricted-field| replace:: {embed_restricted_field}
.. |supports-comparison| replace:: {supports_comparison}
.. |discord-guild-invite| replace:: https://discord.gg/nE9cGtzayA
"""

autodoc_type_aliases = {
    "MessageChannelT": "Union[TextChannel, DMChannel, VoiceChannel]",
    "_OverwriteValue": "Optional[bool]",
}

autodoc_member_order = 'bysource'
