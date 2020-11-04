#  main.py
#
#  Copyright 2020 Timéo Arnouts <dogm@dogm-s-pc>
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

"""
A librairie which provides class and functions to make easier dialog box in terminal.
"""

__all__ = ["DialogBox"]
__version__ = "0.1"
__author__ = "Arnouts Timéo"


import curses
import curses.textpad
import random
import time


class DialogBox :

    def __init__(self,
            pos_x: int, pos_y: int,
            box_length: int, box_width: int,
            title: str, title_colors_pair_nb: int,
            end_dialog_indicator: str = ""):

        self.pos_x, self.pos_y = pos_x, pos_y
        self.box_length, self.box_width = box_length, box_width

        self.text_pos_x = pos_x + 2
        self.text_pos_y = pos_y + 3

        self.nb_char_max_line = box_length - 2
        self.nb_lines_max = box_width - 2

        self.title = title
        self.title_colors = curses.color_pair(title_colors_pair_nb)

        self.end_dialog_indicator_pos_x = pos_x + box_length - 2
        self.end_dialog_indicator_pos_y = pos_y + box_width + 1

        # Doit être un seul caractère.
        self.end_dialog_indicator_char = end_dialog_indicator

    def framing_box(self, stdscr):
        """Displays dialog box and his title.

        The displayed dialog box have for position self.pos_x;self.pos_y and for size
        self.box_length × self.box_width.
        """
        title_box_length = len(self.title) + 4
        title_box_width = 2

        # Display of the framed title.
        curses.textpad.rectangle(stdscr,
            self.pos_y, self.pos_x + 1,
            self.pos_y + title_box_width, self.pos_x + title_box_length)
        stdscr.addstr(
            self.pos_y + 1, self.pos_x + 3,
            self.title, self.title_colors)

        # Display of the dialog box frame.
        curses.textpad.rectangle(stdscr,
            self.pos_y + 2, self.pos_x,
            self.pos_y + 2 + self.box_width, self.pos_x + self.box_length)

    def _display_end_dialog_indicator(self, stdscr, blink: bool = True):
        """ """
        if self.end_dialog_indicator_char:
            blink = curses.A_BLINK if blink else curses.A_NORMAL

            stdscr.addch(self.end_dialog_indicator_pos_y, self.end_dialog_indicator_pos_x,
                self.end_dialog_indicator_char, blink)

    def char_by_char(self, stdscr,
            text: str, colors_pair_nb: int,
            delay: int = .07, random_delay: tuple = (0, 0)):
        """Writes the given text character by character at position self.pos_x;self.pos_y.

        The delay parameter affects the waited time between the writing of each character in seconds
        (set by default on 0.7 seconde).

        The random_delay parameter affects time between the writing of each character in seconds where
        waited time is a number generated in the given interval (as a tuple).
        """
        for x, char in enumerate(text):
            stdscr.addstr(
                self.text_pos_y, self.text_pos_x + x,
                char, curses.color_pair(colors_pair_nb))

            stdscr.refresh()
            time.sleep(delay + random.uniform(*random_delay))

        self._display_end_dialog_indicator(stdscr)

    def word_by_word(self, stdscr,
            text: str, colors_pair_nb: int,
            cut_char: str = " ", delay: int = .07, random_delay: tuple = (0, 0)):
        """Writes the given text word by word at position at position self.pos_x;self.pos_y.

        The cut_char parameter is sentence break character (by defaut on a space).

        The delay parameter affects the waited time between the writing of each word in seconds
        (set by default on 0.7 seconde).

        The random_delay parameter affects time between the writing of each word in seconds where
        waited time is a number generated in the given interval (as a tuple).
        """
        offsetting_x = 0
        for word in text.split(cut_char):
            stdscr.addstr(
                self.text_pos_y, self.text_pos_x + offsetting_x,
                word, curses.color_pair(colors_pair_nb))

            stdscr.refresh()
            offsetting_x += len(word) + 1 # Compensates for the space between words.
            time.sleep(delay + random.uniform(*random_delay))

        self._display_end_dialog_indicator(stdscr)


def main(stdscr):
    text = (
        "Hello world",
        "How are you today ?"
        )

    curses.curs_set(0)

    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)

    textbox = DialogBox(
        20, 15,
        40, 6,
        title="Dogm", title_colors_pair_nb=3,
        end_dialog_indicator="►")

    for reply in text:
        textbox.framing_box(stdscr)
        textbox.char_by_char(stdscr, reply, 2)

        stdscr.getch()
        stdscr.clear()

if __name__ == "__main__":
    curses.wrapper(main)
