# type.py
# 2020 Timéo Arnouts <tim.arnouts@protonmail.com>

__all__ = [
    "CursesWindow",
    "CursesTextAttribute",
    "CursesTextAttributes",
    "CursesKey",
    "CursesKeys",
    "CursesWindow"
]

from typing import Sequence, Union

import _curses


CursesWindow = _curses.window

#: curses key constants are integers or strings depending on input method used.
#: See https://docs.python.org/3/library/curses.html?#constants
CursesKey = Union[int, str]
CursesKeys = Sequence[CursesKey]

#: curses text attribute constants are integers.
#: See https://docs.python.org/3/library/curses.html?#constants
CursesTextAttribute = int
CursesTextAttributes = Sequence[CursesTextAttribute]
