# utils.py
# 2020 Timéo Arnouts <tim.arnouts@protonmail.com>

__all__ = ["CursesWindow",
           "CursesTextAttributesConstant",
           "CursesTextAttributesConstants",
           "CursesKeyConstant",
           "CursesKeyConstants",
           "CursesWindow",
           "TextAttributes"]

from contextlib import ContextDecorator
import _curses
from typing import Generator, Iterable, NoReturn, Sequence, Union


CursesWindow = _curses.window

#: curses key constants are integers.
#: See https://docs.python.org/3/library/curses.html?#constants
CursesKeyConstant = Union[int, str]
CursesKeyConstants = Sequence[CursesKeyConstant]

#: curses text attribute constants are integers.
#: See https://docs.python.org/3/library/curses.html?#constants
CursesTextAttributesConstant = int
CursesTextAttributesConstants = Sequence[CursesTextAttributesConstant]


def _make_chunk(seq: Sequence,
                chunk_length: int) -> Generator:
    """Returns a tuple that contains given sequence separated into
    ``chunk_length`` bundles.

    :returns: Generator separated into ``chunk_length`` bundles.
    """
    return (seq[chunk:chunk + chunk_length]
                for chunk in range(0, len(seq), chunk_length))


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
