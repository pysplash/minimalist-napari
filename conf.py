# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'minimalist-napari'
copyright = '2025, Carol Willing'
author = 'Carol Willing'
release = '0.6.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "myst_nb",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.venv']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']

intersphinx_mapping = {
    "python": ["https://docs.python.org/3", None],
    "numpy": ["https://numpy.org/doc/stable/", None],
    "napari_plugin_engine": [
        "https://napari-plugin-engine.readthedocs.io/en/latest/",
        "https://napari-plugin-engine.readthedocs.io/en/latest/objects.inv",
    ],
    "magicgui": [
        "https://pyapp-kit.github.io/magicgui/",
        "https://pyapp-kit.github.io/magicgui/objects.inv",
    ],
    "app-model": [
        "http://app-model.readthedocs.io/en/latest/",
        "http://app-model.readthedocs.io/en/latest/objects.inv",
    ],
    "vispy": [
        "https://vispy.org/",
        "https://vispy.org/objects.inv",
    ],
}

myst_enable_extensions = [
    "colon_fence",
    "dollarmath",
    "substitution",
    "tasklist",
    "attrs_inline",
    "linkify",
]
myst_footnote_transition = False
myst_heading_anchors = 4

exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    ".jupyter_cache",
    "jupyter_execute",
    "plugins/_*.md",
    "plugins/building_a_plugin/_layer_data_guide.md",
    "gallery/index.rst",
    ".venv"
]


autosummary_generate = True
autosummary_ignore_module_all = False
autosummary_imported_members = True
