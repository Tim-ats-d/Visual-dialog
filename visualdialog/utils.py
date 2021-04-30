# utils.py
# 2020 Timéo Arnouts <tim.arnouts@protonmail.com>

__all__ = ["TextAttr"]

from contextlib import ContextDecorator
from typing import Iterable, NoReturn, Sequence, Tuple, Union

from .type import CursesTextAttribute, CursesWindow


def chunked(seq: Sequence,
            chunk_length: int) -> Iterable:
    """Return a iterable that contains given sequence separated into
    ``chunk_length`` bundles.

    :returns: An iterator contains sequence separated into
        ``chunk_length`` bundles.
    """
    return (seq[chunk:chunk + chunk_length]
            for chunk in range(0, len(seq), chunk_length))


def to_tuple(obj: Union[object, Sequence]) -> Union[Tuple, Sequence]:
    """Check if the given object is a sequence, if so returns it,
    otherwise returns it as a tuple.

    This function is mainly used to work with sequences even if only one
    argument is passed.
    """
    if isinstance(obj, Sequence):
        return obj
    else:
        return (obj, )


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
