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

from typing import Generator, List, Tuple, TypeVar, Union


Numeric = TypeVar("Numeric", int, float)

# curses text attribute constants are integers.
# See https://docs.python.org/3/library/curses.html?#constants
CursesTextAttributesConstant = int
CursesTextAttributesConstants = Union[Tuple[int], List[int]]

# curses key constants are integers.
# See https://docs.python.org/3/library/curses.html?#constants
CursesKeyConstant = int
CursesKeyConstants = Union[Tuple[int], List[int]]


def _make_chunk(iterable: Union[Tuple, List],
                chunk_length: int) -> Generator:
    """Returns a tuple that contains the given iterator separated
    into chunk_length bundles.

    :returns: Iterator separated into chunk_length bundles.
    :rtype: Generator
    """
    return (iterable[chunk:chunk + chunk_length]
            for chunk in range(0, len(iterable), chunk_length))


class TextAttributes:
    """A context manager to manage curses text attributs.

    :param win: `curses` window object for which the attributes will be
        managed.

    :param attributes: List of attributes to activate and desactivate.
    :type attributes: Union[tuple[CursesTextAttributesConstants],list[CursesTextAttributesConstants]]
    """
    def __init__(self,
                 stdscr,
                 *attributes: CursesTextAttributesConstants):
        self.win = stdscr
        self.attributes = attributes

    def __enter__(self):
        """Activates one by one the attributes contained in
        self.attributes.
        """
        for attr in self.attributes:
            self.win.attron(attr)

    def __exit__(self, type, value, traceback):
        """Disable one by one the attributes contained in
        self.attributes.
        """
        for attr in self.attributes:
            self.win.attroff(attr)
