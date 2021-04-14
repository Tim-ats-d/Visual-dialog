# choices.py
# 2020 Timéo Arnouts <tim.arnouts@protonmail.com>

import curses
from typing import Any, Dict, Tuple, Union

from .dialog import DialogBox
from .utils import CursesTextAttrConstants, TextAttr, chunked


class ChoiceBox(DialogBox):

    def __init__(self,
                 **kwargs):
        super().__init__(**kwargs)

    def chain(
            self,
            win,
            *propositions: Dict[str, Any]) -> Any:
        """"""
        super().framing_box(win)

        for y, proposition in enumerate(propositions):
            win.addstr(self.pos_y + y*2,
                       self.pos_x,
                       proposition)
            win.refresh()
