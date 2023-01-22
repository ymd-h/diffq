project = "diffqc"
author = "Hiroyuki Yamada"
copyright = "2023, Hiroyuki Yamada"

extensions = [
    'sphinx.ext.napoleon',
    "sphinx_automodapi.automodapi",
    'sphinx_automodapi.smart_resolver',
    'myst_parser'
]

html_theme = "furo"
html_logo = ""
html_favicon = ""
html_show_sourcelink = False

napoleon_include_init_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = True

numpydoc_show_class_members=False

autodoc_default_options = {
    'member-order': 'bysource',
    'class-doc-from':'both',
    'exclude-members': '__dict__, __weakref__, __module__, __new__, __reduce__, __setstate__'
}
