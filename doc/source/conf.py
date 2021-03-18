#  choices.py
#
#  2020 Timéo Arnouts <tim.arnouts@protonmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#

import os
import sys
from datetime import datetime

from visualdialog import __version__


sys.path.insert(0, os.path.abspath("../../"))

project = "Visual-dialog"
copyright = f"2021-{datetime.now().year}, Timéo Arnouts"
author = "Timéo Arnouts"

extensions = [
    "sphinx.ext.autodoc"
]

master_doc = "index"
source_suffix = ".rst"
autodoc_member_order = "bysource"

version = str(__version__)
release = version

templates_path = ["_templates"]

exclude_patterns = []

pygments_style = "friendly"

html_title = "Visual-dialog Documentation"
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_show_sourcelink = True
html_theme_options = {
    "display_version": True
}

html_logo = "images/visual-dialog.png"

latex_logo = "images/visual-dialog.png"

latex_elements = {
    "pointsize": "12pt",
    "fontpkg": r"""
        \setmainfont{Open Sans}
        \setsansfont{Bitter}
        \setmonofont{Ubuntu Mono}
        """
}

latex_documents = [
    (master_doc, "Visual-dialog.tex", "Visual-dialog Documentation",
     "Arnouts Timéo", "manual"),
]

man_pages = [
    (master_doc, "visual-dialog", "Visual-dialog Documentation",
     [author], 1)
]

texinfo_documents = [
    (master_doc, "Visual-dialog", "Visual-dialog Documentation",
     author, "Visual-dialog", "One line description of project.",
     "Miscellaneous"),
]
