#  box.py
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

__all__ = ["TextBox"]

import curses
import curses.textpad
from typing import List, NewType, Tuple, Union

from utils import (CursesKeyConstants, CursesTextAttributesConstants,
                   TextAttributes)


class PanicError(Exception):
    def __str__(self):
        return "text box was aborted"


class TextBox:
    """This class provides attributs and methods to manage a text box.

    This class provides a general API for text boxes, it does not need to be
    instantiated.

    Attributes
    ----------
    pos_x
        x position of the dialog box in the terminal.
    pos_y
        y position of the dialog box in the terminal
    box_length
        Length of the dialog box in the terminal.
    box_width
        Width of the dialog box in the terminal.
    title : optional
        String that will be displayed in the upper left corner of dialog box
        if title is an empty string, the title will not be displayed (by
        default an empty string).
    title_colors_pair_nb : optional
        Number of the curses color pair that will be used to color the title
        (by default 0. The number zero corresponding to the pair of white
        color on black background initialized by `curses`).
    title_text_attributes : optional
        Dialog box title text attributes (by default a tuple contains
        curses.A_BOLD).
    downtime_chars : optional
        List of characters that will trigger a `downtime_chars_delay` time
        second between the writing of each character (by
        default (",", ".", ":", ";", "!", "?")).
        `word_by_word` method was not effected by this parameter.
    downtime_chars_delay : optional
        Waiting time in seconds after writing a character contained in
        `downtime_chars` (by default 0.6).
        `word_by_word` method was not effected by this parameter.
    confirm_dialog_key
        List of accepted key codes to skip dialog. `curses` constants are
        supported.
    panic_key
        List of accepted key codes to raise PanicError. `curses` constants are
        supported.

    See also
    --------
    To see the list of key constants please refer to `curses` module
    documentation (https://docs.python.org/3/library/curses.html?#constants).
    """
    confirm_dialog_key: Union[Tuple[CursesKeyConstants],
                              List[CursesKeyConstants]] = ()
    panic_key: Union[Tuple[CursesKeyConstants], List[CursesKeyConstants]] = ()

    def __init__(
        self,
        pos_x: int,
        pos_y: int,
        box_length: int,
        box_width: int,
        title: str = "",
        title_colors_pair_nb: CursesTextAttributesConstants = 0,
        title_text_attributes: Union[Tuple[CursesTextAttributesConstants],
                                     List[CursesTextAttributesConstants]] = (
                                         curses.A_BOLD, ),
        downtime_chars: Union[Tuple[str],
                              List[str]] = (",", ".", ":", ";", "!", "?"),
        downtime_chars_delay: Union[int, float] = .6):
        self.pos_x, self.pos_y = pos_x, pos_y
        self.box_length, self.box_width = box_length, box_width

        # Compensation for the left border of the dialog box.
        self.text_pos_x = pos_x + 2
        # Compensation for the upper border of the dialog box.
        self.text_pos_y = pos_y + 3

        self.nb_char_max_line = box_length - 4
        self.nb_lines_max = box_width - 2

        self.title = title
        if self.title:
            self.title_colors = curses.color_pair(title_colors_pair_nb)
            self.title_text_attributes = title_text_attributes

        self.end_dialog_indicator_pos_x = pos_x + box_length - 2
        self.end_dialog_indicator_pos_y = pos_y + box_width + 1

        self.downtime_chars = downtime_chars
        self.downtime_chars_delay = downtime_chars_delay

    @property
    def position(self) -> Tuple[int, int]:
        """Returns a tuple contains x;y position.

        Returns
        -------
        position
            x;y position of TextBox.
        """
        return self.text_pos_x - 2, self.text_pos_y - 3

    @property
    def dimensions(self) -> Tuple[int, int]:
        """Returns a tuple contains dimensions of dialog box.

        Returns
        -------
        dimension
            TextBox length and width.
        """
        return self.box_length, self.box_width

    def framing_box(self, stdscr):
        """Displays dialog box borders and his title.
        If attribute self.title is empty doesn't display the title.

        Parameters
        ----------
        stdscr
            `curses` window object on which the method will have effect.

        Returns
        -------
        None.
        """
        title_box_length = len(self.title) + 4
        title_box_width = 2

        # Displays the title and the title box.
        if self.title:
            attr = (self.title_colors, *self.title_text_attributes)

            curses.textpad.rectangle(stdscr, self.pos_y, self.pos_x + 1,
                                     self.pos_y + title_box_width,
                                     self.pos_x + title_box_length)

            with TextAttributes(stdscr, *attr):
                stdscr.addstr(self.pos_y + 1, self.pos_x + 3, self.title)

        # Displays the borders of the dialog box.
        curses.textpad.rectangle(stdscr, self.pos_y + 2, self.pos_x,
                                 self.pos_y + 2 + self.box_width,
                                 self.pos_x + self.box_length)

    def getkey(self, stdscr):
        """Blocks execution as long as a key contained in
        `self.confirm_dialog_key` is not detected.

        Parameters
        ----------
        stdscr
            `curses` window object on which the method will have effect.

        Returns
        -------
        None.

        Raises
        ------
        PanicError
            If a key contained in self.panic_key is pressed.

        See also
        --------
            - To see the list of key constants please refer to `curses` module
            documentation
            (https://docs.python.org/3/library/curses.html?#constants).
            - Documentation of `window.getch` method from `curses` module
            (https://docs.python.org/3/library/curses.html?#curses.window.getch).
        """
        while 1:
            key = stdscr.getch()

            if key in self.confirm_dialog_key:
                break
            elif key in self.panic_key:
                raise PanicError
            else:
                # Ignore incorrect keys.
                ...
