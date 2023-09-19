# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'neuromorpho-api'
copyright = '2023, Ross Barnowski (rossbar)'
author = 'Ross Barnowski (rossbar)'
release = '0.1.1'

# -- General configuration ---------------------------------------------------
extensions = ["myst_nb"]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_title = "neuromorpho-api"
html_theme_options = {
    "external_links": [
        {
            "url": "https://neuromorpho.org/",
            "name": "Neuromorpho.org",
        },
    ],
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/rossbar/neuromorpho-api",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "PyPI",
            "url": "https://pypi.org/project/neuromorpho-api/",
            "icon": "fas fa-box",
        },
    ],
    "use_edit_page_button": True,
}

html_context = {
    "github_user": "rossbar",
    "github_repo": "neuromorpho-api",
    "github_version": "main",
    "doc_path": "doc",
}
