#  choices_box.py
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

import curses
from typing import Any, Dict, NewType, Tuple, Union

import box
from utils import CursesTextAttributesConstants, TextAttributes, _make_chunk


class ChoiceBox(box.TextBox):

    def __init__(
            self,
            pos_x: int,
            pos_y: int,
            box_length: int,
            box_width: int,
            title: str = "",
            title_colors_pair_nb: CursesTextAttributesConstants = 0,
            title_text_attributes: Tuple[CursesTextAttributesConstants] = (
                curses.A_BOLD, ),
            downtime_chars: Tuple[str] = (",", ".", ":", ";", "!", "?"),
            downtime_chars_delay: Union[int, float] = 0.6):
        super().__init__(pos_x,
                         pos_y,
                         box_length,
                         box_width,
                         title,
                         title_colors_pair_nb,
                         title_text_attributes,
                         downtime_chars,
                         downtime_chars_delay)

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
