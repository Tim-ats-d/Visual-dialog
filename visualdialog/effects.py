
import curses

from .effect import EachChar


class ScrollEffect(EachChar):

    def activate(self):
        curses.curs_set(True)

    def desactivate(self):
        curses.curs_set(False)
