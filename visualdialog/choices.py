# choices.py
#
# 2020 Timéo Arnouts <tim.arnouts@protonmail.com>

import curses
from typing import Any, Dict, Tuple, Union

from .dialog import DialogBox
from .utils import (CursesTextAttributesConstants,
                    TextAttributes,
                    _make_chunk)


class ChoiceBox(DialogBox):

    def __init__(self,
                 **kwargs):
        super().__init__(**kwargs)

    def chain(
            self,
            stdscr,
            *propositions: Dict[str, Any]) -> Any:
        """"""
        super().framing_box(stdscr)

        for y, proposition in enumerate(propositions):
            stdscr.addstr(self.pos_y + y*2,
                          self.pos_x,
                          proposition)
            stdscr.refresh()


def main(stdscr):
    choices_box = ChoiceBox(10, 10, 40, 4)

    choices_box.chain(stdscr,
                      "Quel âge as-tu ?"
                      "14",
                      "16",
                      "18")
    stdscr.getch()


curses.wrapper(main)
