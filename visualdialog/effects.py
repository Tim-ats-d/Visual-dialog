
from .effect import EachChar

import curses


class ScrollEffect(EachChar):

    def activate(self):
        curses.curs_set(True)

    def desactivate(self):
        curses.curs_set(False)
