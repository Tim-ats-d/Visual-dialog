#!/usr/bin/env python3
#
#  dialog.py
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
import random
import textwrap
import time
from typing import Callable, Dict, Generator, List, NewType, Tuple, Union

import box
from utils import CursesTextAttributesConstants, TextAttributes, _make_chunk


__all__ = ["DialogBox"]


class DialogBox(box.TextBox):
    """This class provides methods and attributs to manage a dialog box.

    This class inherits all the methods and arguments of TextBox. See TextBox
    documentation for more informations.

    Attributes
    ----------
    end_dialog_indicator : str, optional
        Character that will be displayed in the lower right corner the
        character once all the characters have been completed (by default "►").
        String with a length of more than one character can lead to an overflow
        of the dialog box frame.
    """

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
            downtime_chars_delay: Union[int, float] = 0.6,
            end_dialog_indicator: str = "►"):
        super().__init__(pos_x,
                         pos_y,
                         box_length,
                         box_width,
                         title,
                         title_colors_pair_nb,
                         title_text_attributes,
                         downtime_chars,
                         downtime_chars_delay)

        self.end_dialog_indicator_char = end_dialog_indicator

    def __enter__(self):
        """Returns self."""
        return self

    def __exit__(self, type, value, traceback):
        """Returns None."""
        ...

    def _display_end_dialog_indicator(
            self,
            stdscr,
            text_attributes: Tuple[CursesTextAttributesConstants] = (
                curses.A_BOLD, curses.A_BLINK)):
        """Displays an end of dialog indicator in the lower right corner of
        textbox.

        Parameters
        ----------
        stdscr
            `curses` window object on which the method will have effect.
        text_attributes : tuple of curses text attribute constants, optional
           Text attributes of `end_dialog_indicator` method (by default
           (curses.A_BOLD, curses.A_BLINK)).

        Returns
        -------
        None.
        """
        if self.end_dialog_indicator_char:
            with TextAttributes(stdscr, *text_attributes):
                stdscr.addch(self.end_dialog_indicator_pos_y,
                             self.end_dialog_indicator_pos_x,
                             self.end_dialog_indicator_char)

    def char_by_char(
            self,
            stdscr,
            text: str,
            colors_pair_nb: int = 0,
            text_attr: Tuple[CursesTextAttributesConstants] = (),
            words_attr: Union[CursesTextAttributesConstants,
                              Dict[Tuple[str],
                                   Tuple[CursesTextAttributesConstants]]] = {},
            flash_screen: bool = False,
            delay: Union[int, float] = .04,
            random_delay: Tuple[int, int] = (0, 0),
            callback: Callable = None,
            cargs=()):
        """Writes the given text character by character in the
        current dialog box.

        Parameters
        ----------
        stdscr
            `curses` window object on which the method will have effect.
        text : str
            Text that will be displayed character by character in the dialog
            box. This text can be wrapped to fit the proportions of the dialog
            box.
        colors_pair_nb : int, optional
            Number of the curses color pair that will be used to color the
            text (by default 0. The number zero corresponding to the pair of
            white color on black background initialized by `curses`).
        text_attr : tuple or list of CursesTextAttributesConstants, optional
            Dialog box text attributes (by default an empty tuple).
        words_attr :

        flash_screen : bool, optional
            Allows or not to flash screen with a short light effect done
            before writing the first character via `flash` function from
            `curses` module (by default False).
        delay : int or float, optional
            Waiting time between the writing of each character of text in
            second (by default 0.04).
        random_delay : list of two number or tuple of two number, optional
            Waiting time between the writing of each character in seconds
            where time waited is a random number generated in `random_delay`
            interval (by default (0, 0)).
        callback : callable, optional
            Callable called after writing a character and the delay time has
            elapsed (by default None).
        cargs : list or tuple, optional
            All the arguments that will be passed to callback
            (by default an empty tuple).

        Returns
        -------
        None.

        Notes
        -----
        Method flow:
            - Calling `framing_box` method.
            - Flash screen depending `flash_screen` parameter.
            - Cutting text into line via `wrap` function from `textwrap`
            module (to stay within the dialog box frame).
            - Writing paragraph by paragraph.
            - Writing each line of the current paragraph, character by
            character.
            - Calling `_display_end_dialog_indicator` method.
            - Waits until a key contained in the class attribute
            `confirm_dialog_key` was pressed before writing the following
            paragraph.

        Notes
        -----
            If the volume of text displayed is too large to be contained in a
            dialog box, text will be automatically cut into paragraphs. The
            screen will be completely cleaned when writing each paragraph via
            `window.clear()` method of `curses` module.

        See Also
        --------
            - Documentation of `wrap` function from `textwrap` module for more
            information of the behavior of text wrap
            (https://docs.python.org/fr/3.8/library/textwrap.html#textwrap.wrap).
            - Documentation of `flash` function from `curses` module
            (https://docs.python.org/3/library/curses.html?#curses.flash).
            - Documentation of `window.clear()` method from `curses` module
            (https://docs.python.org/3/library/curses.html?#curses.window.clear).
        """
        self.framing_box(stdscr)

        if flash_screen:
            curses.flash()

        wrapped_text = textwrap.wrap(text, self.nb_char_max_line)
        wrapped_text = _make_chunk(wrapped_text, self.nb_lines_max)

        for paragraph in wrapped_text:
            stdscr.clear()
            super().framing_box(stdscr)

            for y, line in enumerate(paragraph):
                offsetting_x = 0
                for word in line.split():
                    if word in words_attr.keys():
                        attr = words_attr[word]

                        # Test if only one argument is passed.
                        if isinstance(attr, int):
                            attr = (attr, )
                    else:
                        attr = (curses.color_pair(colors_pair_nb),
                                *text_attr)

                    with TextAttributes(stdscr, *attr):
                        for x, char in enumerate(word):
                            stdscr.addstr(self.text_pos_y + y,
                                          self.text_pos_x + x + offsetting_x,
                                          char)
                            stdscr.refresh()

                            if char in self.downtime_chars:
                                time.sleep(self.downtime_chars_delay +
                                           random.uniform(*random_delay))
                            else:
                                time.sleep(delay +
                                           random.uniform(*random_delay))

                            if callback:
                                callback(*cargs)

                        # Waiting for space character.
                        time.sleep(delay)

                    # Compensates for the space between words.
                    offsetting_x += len(word) + 1

            self._display_end_dialog_indicator(stdscr)
            super().getkey(stdscr)

    def word_by_word(
            self,
            stdscr,
            text: str,
            colors_pair_nb: int,
            cut_char: str = " ",
            text_attr: Tuple[CursesTextAttributesConstants] = (),
            words_attr: Dict[str, Tuple[CursesTextAttributesConstants]] = {},
            flash_screen: bool = False,
            delay: Union[int, float] = .15,
            random_delay: Tuple[int, int] = (0, 0),
            callback: Callable = None,
            cargs=()):
        """Writes the given text word by word at position in the current
        dialog box.

        Parameters
        ----------
        stdscr
            `curses` window object on which the method will have effect.
        text : str
            Text that will be displayed word by word in the dialog box. This
            text can be wrapped to fit the proportions of the dialog box.
            See Notes section for more informations.
        colors_pair_nb : int, optional
            Number of the curses color pair that will be used to color the
            text (by default 1).
        text_attr : tuple or list of CursesTextAttributesConstants, optional
            Dialog box text attributes (by default an empty tuple).
        words_attr :

        cut_char : str, optional
            The delimiter according which to split the text in word
            (by default space character).
        flash_screen : bool, optional
            Allows or not to flash screen with a short light effect done
            before writing the first word via `flash` function from `curses`
            module (by default False).
        delay : int or float, optional
            Waiting time between the writing of each character of text in
            second (by default 0.15).
        random_delay : list of two number or tuple of two number, optional
            Waiting time between the writing of each character in seconds
            where time waited is a random number generated in `random_delay`
            interval (by default (0, 0)).
        callback : callable, optional
            Callable called after writing a character and the `delay` time has
            elapsed (by default None).
        cargs : list or tuple, optional
            All the arguments that will be passed to callback (by default
            an empty tuple).

        Returns
        -------
        None.

        Notes
        -----
            Method flow:
                - Calling `framing_box` method.
                - Flash screen depending `flash_screen` parameter.
                - Cutting text into line via `textwrap.wrap` function from
                `textwrap` module (to stay within the dialog box frame).
                - Writing each line of the current paragraph, word by word.
                - Calling `_display_end_dialog_indicator` method.
                - Waits until a key contained in the class attribute
                `confirm_dialog_key` was pressed before writing the following
                paragraph.

        Notes
        -----
            If the volume of text displayed is too large to be contained in a
            dialog box, text will be automatically cut into paragraphs.The
            screen will be completely cleaned when writing each paragraph via
            `window.clear` method from `curses`
            module.

        See Also
        --------
            - Documentation of `wrap` function from `textwrap` module for more
            information on the behavior of text wrap
            (https://docs.python.org/fr/3.8/library/textwrap.html#textwrap.wrap).
            - Documentation of `flash` function from `curses` module
            (https://docs.python.org/3/library/curses.html?#curses.flash).
            - Documentation of `window.clear()` method from `curses` module
            (https://docs.python.org/3/library/curses.html?#curses.window.clear).
        """
        super().framing_box(stdscr)

        if flash_screen:
            curses.flash()

        attr = (curses.color_pair(colors_pair_nb),
                *text_attr)

        wrapped_text = textwrap.wrap(text, self.nb_char_max_line)
        wrapped_text = _make_chunk(wrapped_text, self.nb_lines_max)

        for paragraph in wrapped_text:
            stdscr.clear()
            super().framing_box(stdscr)
            for y, line in enumerate(paragraph):
                offsetting_x = 0
                for word in line.split(cut_char):
                    if word in words_attr:
                        attr = words_attr[word]
                    else:
                        attr = (curses.color_pair(colors_pair_nb),
                        *text_attr)

                    with TextAttributes(stdscr, *attr):
                        stdscr.addstr(self.text_pos_y + y,
                                      self.text_pos_x + offsetting_x,
                                      word)
                        stdscr.refresh()

                    # Compensates for the space between words.
                    offsetting_x += len(word) + 1

                    time.sleep(delay + random.uniform(*random_delay))

                if callback:
                    callback(*cargs)

            self._display_end_dialog_indicator(stdscr)
            super().getkey(stdscr)
