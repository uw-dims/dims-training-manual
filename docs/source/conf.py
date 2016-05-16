#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sw=4 tw=0 noet :
#
# Document: dims-training-manual
# This documentation build configuration file was created from
# a cookiecutter template. It is based on output derived from
# the output of sphinx-quickstart.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
import shlex
from sphinx import __version__

# ReadTheDocs configuration setting:

on_rtd = os.environ.get('READTHEDOCS') == "True"
if on_rtd:
    html_theme = 'default'
else:
    html_theme = 'sphinx_rtd_theme'

# If extensions (or modules to document with autodoc) are in another
# directory, add these directories to sys.path here. If the directory is
# relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ---------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.graphviz',
    'sphinx.ext.coverage',
    'sphinx.ext.ifconfig', 
    'sphinx.ext.viewcode'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'DIMS Training Manual'
copyright = u'2014-2016, University of Washington'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.3.0'
# The full version, including alpha/beta/rc tags.
release = '0.3.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
show_authors = True

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.

if not on_rtd and os.environ.get('INCLUDETODOS') == "True":
    todo_include_todos = True
else:
    todo_include_todos = False

# -- Options for HTML output -------------------------------------------

# Theme options are theme-specific and customize the look and feel of a
# theme further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as
# html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the
# top of the sidebar.
html_logo = 'UW-logo.png'

# The name of an image file (within the static path) to use as favicon
# of the docs.  This file should be a Windows icon file (.ico) being
# 16x16 or 32x32 pixels large.
html_favicon = 'UW-logo-32x32.ico'

# Add any paths that contain custom static files (such as style sheets)
# here, relative to this directory. They are copied after the builtin
# static files, so a file named "default.css" will overwrite the builtin
# "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer.
# Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr'
#html_search_language = 'en'

# A dictionary with options for the search language support, empty by d    efault.
# Now only 'ja' uses this config value
#html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration director    y) that
# implements a search results scorer. If empty, the default will be use    d.
#html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'dims-training-manualdoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # The following comes from
    # https://github.com/rtfd/readthedocs.org/issues/416
    # and http://www.utf8-chartable.de/unicode-utf8-table.pl?start=9472&names=-
    #
    'preamble': "".join((
        '\usepackage{pifont}',                # To get Dingbats
        '\DeclareUnicodeCharacter{00A0}{ }',  # NO-BREAK SPACE
        '\DeclareUnicodeCharacter{2014}{\dash}', # LONG DASH
        '\DeclareUnicodeCharacter{251C}{+}',  # BOX DRAWINGS LIGHT VERTICAL AND RIGHT
        '\DeclareUnicodeCharacter{2514}{+}',  # BOX DRAWINGS LIGHT UP AND RIGHT
        '\DeclareUnicodeCharacter{1F37A}{ }', # Beer emoji (just turn into space for now)
        '\DeclareUnicodeCharacter{2588}{\textblock}',  # SOLID TEXT BLOCK
        '\DeclareUnicodeCharacter{25CF}{\ding{108}}',  # Dingbat 108 (black circle)
    )),
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc,
     'dims-training-manual.tex',
     u'DIMS Training Manual Documentation',
     u'Dave Dittrich', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = 'UW-logo.png'

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = ['appendices']

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc,
     'dims-training-manual',
     u'DIMS Training Manual Documentation',
     [u'Dave Dittrich'],
     1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output ----------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc,
     'dims-training-manual',
     u'DIMS Training Manual Documentation',
     'Dave Dittrich',
     'dims-training-manual',
     'DIMS Training Manual',
     'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False

git_branch = os.environ.get('GITBRANCH', "develop")
git_tag = os.environ.get('GITTAG', "latest")

#os.environ['DOCSURL'] = "file://{}".format(os.environ.get('GIT'))
if os.environ.get('DOCSURL') is None:
    if not on_rtd:
        os.environ['DOCSURL'] = "http://demo.prisem.washington.edu:8080/docs/{}/html".format(git_branch)

intersphinx_cache_limit = -1   # days to keep the cached inventories (0 == forever)
if on_rtd:
    intersphinx_mapping = {
            'dimsusermanual': ("https://dims-user-manual.readthedocs.io/en/{0}/".format(git_tag), None),
            'dimsjds': ("https://dims-jds.readthedocs.io/en/{0}/".format(git_tag), None),
    }
else:
    intersphinx_mapping = {
            'dimsusermanual': ("{}/dims-ocd".format(os.environ['DOCSURL']), None),
            'dimsjds': ("{}/dims-ocd".format(os.environ['DOCSURL']), None),
    }
