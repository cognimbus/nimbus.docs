# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Cogniteam Cloud Platform'
copyright = '2021, Cogniteam'
author = 'Cogniteam'

release = '0.1'
version = '0.1.0'

master_doc = 'index'

# -- General configuration
htmltitle = "CogniteamCloud Platform"

html_theme_options = {
    'logo_only': True,
    # ...
}

html_static_path = ["_static"]

html_css_files = [
    'css/rtd_dark.css',
]

html_logo = "_static/img/cogniteam-logo.webp"

extensions = [
    'myst_parser',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

source_suffix = [
    ".rst",
    ".md",
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

html_favicon = 'favicon.ico'

def get_edit_url():
    return "https://github.com/cognimbus/nimbus.docs"

html_context = {
    "display_github": True, # Integrate GitHub
    "github_user": "cognimbus", # Username
    "github_repo": "nimbus.docs", # Repo name
    "github_version": "main", # Version
    "edit_on_github": True,
    "edit_on_github_name": "Edit on GitHub",
    "edit_on_github_project": "cognimbus/nimbus.docs",
    "edit_on_github_branch": "main",
    "edit_on_github_src_path": "README.md", # Path in the checkout to the docs root
    "get_edit_on_github_url": get_edit_url,
}
