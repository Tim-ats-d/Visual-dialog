#!/usr/bin/env python3
#
#  utils.py
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
#

from typing import List, NewType, Tuple, Union


# curses text attribute constants are integers.
# See https://docs.python.org/3/library/curses.html?#constants
CursesTextAttributesConstants = NewType("CursesTextAttributesConstants", int)


def _make_chunk(iterable: Union[Tuple, List], chunk_length: int) -> Tuple:
    """Returns a generator that contains the given iterator separated into
    chunk_length bundles."""
    return (iterable[chunk:chunk + chunk_length]
            for chunk in range(0, len(iterable), chunk_length))


class TextAttributes:
    """A context manager to manage curses text attributs.

    Attributes
    ----------
    win
        `curses` window object for which the attributes will be managed.
    attributes : CursesTextAttributesConstants
        List of attributes to activate and desactivate.
    """
    def __init__(self, stdscr, *attributes: CursesTextAttributesConstants):
        self.win = stdscr
        self.attributes = attributes

    def __enter__(self):
        """Activates one by one the attributes contained in self.attributes."""
        for attribute in self.attributes:
            self.win.attron(attribute)

    def __exit__(self, type, value, traceback):
        """Disable one by one the attributes contained in self.attributes."""
        for attribute in self.attributes:
            self.win.attroff(attribute)
