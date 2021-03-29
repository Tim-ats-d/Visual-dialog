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

from contextlib import ContextDecorator
import _curses
from typing import (Generator, Iterable, List, NoReturn, Tuple, TypeVar,
					Union)


Numeric = TypeVar("Numeric", int, float)

CursesWindow = _curses.window

#: curses text attribute constants are integers.
#: See https://docs.python.org/3/library/curses.html?#constants
CursesTextAttributesConstant = int
CursesTextAttributesConstants = Union[Tuple[int], List[int]]

#: curses key constants are integers.
#: See https://docs.python.org/3/library/curses.html?#constants
CursesKeyConstant = int
CursesKeyConstants = Union[Tuple[int], List[int]]


def _make_chunk(iterable: Union[Tuple, List],
                chunk_length: int) -> Generator:
    """Returns a tuple that contains given iterable separated into
    ``chunk_length`` bundles.

    :returns: Generator separated into ``chunk_length`` bundles.
    """
    return (iterable[chunk:chunk + chunk_length]
				for chunk in range(0, len(iterable), chunk_length))


class TextAttributes(ContextDecorator):
    """A context manager to manage ``curses`` text attributes.

    :param win: ``curses`` window object for which the attributes will
		be managed.

    :param attributes: Iterable of ``curses`` text attributes to activate
		and desactivate.
    """
    def __init__(self,
                 win: CursesWindow,
                 *attributes: Iterable[CursesTextAttributesConstant]):
        self.win = win
        self.attributes = attributes

    def __enter__(self) -> NoReturn:
        """Activate one by one attributes contained in self.attributes
        on ``self.win``.
        """
        for attr in self.attributes:
            self.win.attron(attr)

    def __exit__(self, type, value, traceback) -> NoReturn:
        """Disable one by one attributes contained in
        ``self.attributes`` on ``self.win``.
        """
        for attr in self.attributes:
            self.win.attroff(attr)
