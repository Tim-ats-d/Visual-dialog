
from typing import Union

from .utils import CursesWindow


class Effect:

    def __init__(self, cls, win: CursesWindow):
        self.cls = cls
        self.win = win

    def __enter__(self):
        for effect in (EachChar, EachWord, EachParagraph):
            if isinstance(self, effect) and self.cls == effect:
                self.activate()

    def __exit__(self, type, value, traceback):
        for effect in (EachChar, EachWord, EachParagraph):
            if isinstance(self, effect) and self.cls == effect:
                self.desactivate()

    def activate(self):
        ...

    def desactivate(self):
        ...


class EachChar(Effect):
    ...


class EachWord(Effect):
    ...


class EachParagraph(Effect):
    ...
