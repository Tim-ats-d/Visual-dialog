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

from .utils import (CursesKeyConstants,
                    CursesTextAttributesConstants,
                    TextAttributes)


class PanicError(Exception):
    """Exception thrown when a key contained in ``TextBox.panic_key`` is
    pressed.

    :param key: Key pressed that caused the exception to be thrown.
    :type key: CursesKeyConstants
    """
    def __init__(self,
                 key: CursesKeyConstants):
        self.key = key

    def __str__(self):
        return f"text box was aborted by pressing the {self.key} key"


class TextBox:
    """This class provides attributs and methods to manage a text box.

    .. NOTE::
        This class provides a general API for text boxes, it does not need
        to be instantiated.

    :param pos_x: x position of the dialog box in ``curses`` window
        object on which methods will have effects.
    :type pos_x: int

    :param pos_y: y position of the dialog box in ``curses`` window
        object on which methods will have effects.
    :type pos_y: int

    :param length: Length of the dialog box in ``curses`` window object
        on which methods will have effects.
    :type length: int

    :param width: Width of the dialog box in ``curses`` window object on
        which methods will have effects.
    :type width: int

    :param title: String that will be displayed in the upper left corner
        of dialog box.
        If title is an empty string, the title will not be displayed.
        This defaults an empty string.
    :type title: Optional[str]

    :param title_colors_pair_nb:
        Number of the curses color pair that will be used to color the
        title. Zero corresponding to the pair of white color on black
        background initialized by ``curses``). This defaults to ``0``.
    :type title_colors_pair_nb: Optional[int]

    :param title_text_attr:
        Dialog box title text attributes. It should be a single curses
        text attribute or a tuple of curses text attribute. This
        defaults to ``curses.A_BOLD``.
    :type title_text_attr: Optional[Union[CursesTextAttributesConstants,Tuple[CursesTextAttributesConstants],List[CursesTextAttributesConstants]]]

    :param downtime_chars:
        List of characters that will trigger a ``downtime_chars_delay``
        time second between the writing of each character.
        This defaults to ``(",", ".", ":", ";", "!", "?")``.
    :type downtime_chars: Optional[Union[Tuple[str],List[str]]]

    :param downtime_chars_delay:
        Waiting time in seconds after writing a character contained in
        ``downtime_chars``.
        This defaults to ``0.6``.
    :type downtime_chars_delay: Optional[Union[int,float]]
    """
    #: List of accepted key codes to skip dialog. ``curses`` constants are supported. This defaults to an empty tuple.
    confirm_dialog_key: Union[Tuple[CursesKeyConstants],
                          List[CursesKeyConstants]] = ()
    #: List of accepted key codes to raise PanicError. ``curses`` constants are supported. This defaults to an empty tuple.
    panic_key: Union[Tuple[CursesKeyConstants],
                     List[CursesKeyConstants]] = ()

    def __init__(
        self,
        pos_x: int,
        pos_y: int,
        length: int,
        width: int,
        title: str = "",
        title_colors_pair_nb: CursesTextAttributesConstants = 0,
        title_text_attr: Union[CursesTextAttributesConstants,
                               Tuple[CursesTextAttributesConstants],
                               List[CursesTextAttributesConstants]] = curses.A_BOLD,
        downtime_chars: Union[Tuple[str],
                              List[str]] = (",", ".", ":", ";", "!", "?"),
        downtime_chars_delay: Union[int, float] = .6):
        self.pos_x, self.pos_y = pos_x, pos_y
        self.length, self.width = length, width

        self.title_offsetting_y = 2 if title else 0

        # Compensation for the left border of the dialog box.
        self.text_pos_x = pos_x + 2
        # Compensation for the upper border of the dialog box.
        self.text_pos_y = pos_y + self.title_offsetting_y + 1

        self.nb_char_max_line = length - 4
        self.nb_lines_max = width - 2

        self.title = title
        if title:
            self.title_colors = curses.color_pair(title_colors_pair_nb)

            # Test if only one argument is passed instead of a tuple
            if isinstance(title_text_attr, int):
                self.title_text_attr = (title_text_attr, )
            else:
                self.title_text_attr = title_text_attr

        self.downtime_chars = downtime_chars
        self.downtime_chars_delay = downtime_chars_delay

    @property
    def position(self) -> Tuple[int, int]:
        """Returns a tuple contains x;y position of ``TextBox``.

        :returns: x;y position of ``TextBox``.
        :rtype: Tuple[int, int]
        """
        return self.text_pos_x - 2, self.text_pos_y - 3

    @property
    def dimensions(self) -> Tuple[int, int]:
        """Returns a tuple contains dimensions of ``TextBox``.

        :returns: Length and width of ``TextBox``.
        :rtype: Tuple[int, int]
        """
        return self.length, self.width

    def framing_box(self, stdscr):
        """Displays dialog box borders and his title.

        If attribute ``self.title`` is empty doesn't display the title.

        :param stdscr: ``curses`` window object on which the method will
            have effect.
        """
        title_length = len(self.title) + 4
        title_width = 2

        # Displays the title and the title box.
        if self.title:
            attr = (self.title_colors, *self.title_text_attr)

            curses.textpad.rectangle(stdscr,
                                     self.pos_y,
                                     self.pos_x + 1,
                                     self.pos_y + title_width,
                                     self.pos_x + title_length)

            with TextAttributes(stdscr, *attr):
                stdscr.addstr(self.pos_y + 1,
                              self.pos_x + 3,
                              self.title)

        # Displays the borders of the dialog box.
        curses.textpad.rectangle(stdscr,
                                 self.pos_y + self.title_offsetting_y,
                                 self.pos_x,
                                 self.pos_y + self.title_offsetting_y + self.width,
                                 self.pos_x + self.length)

    def getkey(self, stdscr):
        """Blocks execution as long as a key contained in
        ``self.confirm_dialog_key`` is not detected.


        :param stdscr: ``curses`` window object on which the method will
            have effect.
        :raises PanicError: If a key contained in ``self.panic_key`` is
            pressed.

        .. NOTE::
            - To see the list of key constants please refer to
              `this curses documentation
              <https://docs.python.org/3/library/curses.html?#constants>`_.
            - This method uses ``window.getch`` method from ``curses``
              module. Please refer to `curses documentation
              <https://docs.python.org/3/library/curses.html?#curses.window.getch>`_
              for more informations.
        """
        while 1:
            key = stdscr.getch()

            if key in self.confirm_dialog_key:
                break
            elif key in self.panic_key:
                raise PanicError(key)
            else:
                # Ignore incorrect keys.
                ...
