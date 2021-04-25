# utils.py
# 2020 Timéo Arnouts <tim.arnouts@protonmail.com>

__all__ = ["CursesWindow",
           "CursesTextAttribute",
           "CursesTextAttributes",
           "CursesKey",
           "CursesKeys",
           "CursesWindow",
           "TextAttr"]

from contextlib import ContextDecorator
from typing import Iterable, NoReturn, Sequence, Union

import _curses

CursesWindow = _curses.window

#: curses key constants are integers or strings depending on input method used..
#: See https://docs.python.org/3/library/curses.html?#constants
CursesKey = Union[int, str]
CursesKeys = Sequence[CursesKey]

#: curses text attribute constants are integers.
#: See https://docs.python.org/3/library/curses.html?#constants
CursesTextAttribute = int
CursesTextAttributes = Sequence[CursesTextAttribute]


def chunked(seq: Sequence,
            chunk_length: int) -> Iterable:
    """Return a iterable that contains given sequence separated into
    ``chunk_length`` bundles.

    :returns: An iterator contains sequence separated into
        ``chunk_length`` bundles.
    """
    return (seq[chunk:chunk + chunk_length]
            for chunk in range(0, len(seq), chunk_length))


class TextAttr(ContextDecorator):
    """A context manager to manage ``curses`` text attributes.

    :param win: ``curses`` window object for which the attributes will
        be managed.

    :param attributes: Iterable of ``curses`` text attributes to activate
        and desactivate.
    """
    def __init__(self,
                 win: CursesWindow,
                 *attributes: CursesTextAttribute):
        self.win = win
        self.attributes = attributes

    def __enter__(self) -> NoReturn:
        """Activate one by one attributes contained in self.attributes
        on ``self.win``.
        """
        for attr in self.attributes:
            self.win.attron(attr)

    def __exit__(self, type, value, traceback) -> NoReturn:
        """Disable one by one attributes contained in self.attributes
        on ``self.win``.
        """
        for attr in self.attributes:
            self.win.attroff(attr)
