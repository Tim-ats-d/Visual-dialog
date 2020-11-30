#!/usr/bin/env python3
#
#  visualdialog.py
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

__all__ = ["DialogBox"]
__version__ = 0.6
__author__ = "Arnouts Timéo"

import curses
import curses.textpad
import random
import textwrap
import time

from typing import Callable, Generator, Iterable, Tuple


def _make_chunk(iterable: Iterable, chunk_length: int) -> Generator:
    """Returns a generator that contains the given iterator separated into
    chunk_length bundles."""
    return (iterable[chunk:chunk + chunk_length]
            for chunk in range(0, len(iterable), chunk_length))


class TextAttributes:
    """A context manager to manage curses text attributs.

    Attributes
    ----------
    window
        `curses` window object for which the attributes will be managed.
    attributes
        List of attributes to activate and deactivate.
    """

    def __init__(self, stdscr, *attributes):
        self.window = stdscr
        self.attributes = attributes

    def __enter__(self):
        """Activates one by the attributes contained in self.attributes."""
        for attribute in self.attributes:
            self.window.attron(attribute)

    def __exit__(self, type, value, traceback):
        """Disable one by the attributes contained in self.attributes."""
        for attribute in self.attributes:
            self.window.attroff(attribute)


class DialogBox:
    """This class provides methods and attributs to manage a dialog text
    box.

    Attributes
    ----------
    pos_x : int
        x position of the dialog box in the terminal.
    pos_y : int
        y position of the dialog box in the terminal
    box_length : int,
        Length of the dialog box in the terminal.
    box_width : int,
        Width of the dialog box in the terminal.
    title : str,
        String that will be displayed in the upper left corner of dialog box.
    title_colors_pair_nb : int,
        Number of the curses color pair that will be used to color the title.
    title_text_attributes : list of str or tuple of str, optional
        Dialog box title text attributes (by default (curses.A_BOLD, )).
    downtime_chars : Tuple[str], optional
        List of characters that will trigger a `downtime_chars_delay` time second between the
        writing of each character (by default (",", ".", ":", ";", "!", "?")).
        `word_by_word` method was not effected by this parameter.
    downtime_chars_delay : float, optional
        Waiting time in seconds after writing a character contained in `downtime_chars` (by
        default 0.6).
        `word_by_word` method was not effected by this parameter.
    end_dialog_indicator : str
        Character that will be displayed in the lower right corner the character once all the
        characters have been completed (by default "►").
        String with a length of more than 1 character can lead to an overflow of the dialog
        box frame.

    Class attributes
    ----------------
    confirm_dialog_key : tuple
        List of accepted key codes to skip dialog curses constants are supported.

        To see the list of key constants please refer to `curse` module documentation
        (https://docs.python.org/3/library/curses.html?#constants).
    """
    confirm_dialog_key: Tuple = ()

    def __init__(self,
                 pos_x: int,
                 pos_y: int,
                 box_length: int,
                 box_width: int,
                 title: str,
                 title_colors_pair_nb: int,
                 title_text_attributes: Tuple = (curses.A_BOLD, ),
                 downtime_chars: Tuple[str] = (",", ".", ":", ";", "!", "?"),
                 downtime_chars_delay: float = 0.6,
                 end_dialog_indicator: str = "►"):
        self.pos_x, self.pos_y = pos_x, pos_y
        self.box_length, self.box_width = box_length, box_width

        self.text_pos_x = pos_x + 2  # Compensation for the left border of the dialog box.
        self.text_pos_y = pos_y + 3  # Compensation for the upper border of the dialog box.

        self.nb_char_max_line = box_length - 7
        self.nb_lines_max = box_width - 2

        self.title = title
        self.title_colors = curses.color_pair(title_colors_pair_nb)
        self.title_text_attributes = title_text_attributes

        self.end_dialog_indicator_pos_x = pos_x + box_length - 2
        self.end_dialog_indicator_pos_y = pos_y + box_width + 1

        self.downtime_chars = downtime_chars
        self.downtime_chars_delay = downtime_chars_delay

        self.end_dialog_indicator_char = end_dialog_indicator

    def __enter__(self):
        """Returns self."""
        return self

    def __exit__(self, type, value, traceback):
        """Returns None."""
        ...

    def framing_box(self, stdscr):
        """Displays dialog box and his title.

        Displayed dialog box have for position self.pos_x;self.pos_y and for size
        `self.box_length` × `self.box_width`.

        Parameters
        ---------
        stdscr
            `curses` window object on which the method will have effect.

        Returns
        -------
        None.

        Notes
        -----
        Method flow:
            - Display title frame box.
            - Display title .
            - Display text frame box.
        """
        title_box_length = len(self.title) + 4
        title_box_width = 2

        attr = (self.title_colors, *self.title_text_attributes)

        curses.textpad.rectangle(stdscr, self.pos_y, self.pos_x + 1,
                                 self.pos_y + title_box_width,
                                 self.pos_x + title_box_length)

        with TextAttributes(stdscr, *attr):
            stdscr.addstr(self.pos_y + 1, self.pos_x + 3, self.title)

        curses.textpad.rectangle(stdscr, self.pos_y + 2, self.pos_x,
                                 self.pos_y + 2 + self.box_width,
                                 self.pos_x + self.box_length)

    def getkey(self, stdscr):
        """Blocks execution as long as a key contained in `self.confirm_dialog_key` is
        not detected.

        Parameters
        ---------
        stdscr
            `curses` window object on which the method will have effect.

        Returns
        -------
        None.

        See also
        --------
            - To see the list of key constants please refer to `curse` module documentation
            (https://docs.python.org/3/library/curses.html?#constants).
            - Documentation of `window.getch` method from `curses` module
            (https://docs.python.org/3/library/curses.html?#curses.window.getch).
        """
        while 1:
            if stdscr.getch() in self.confirm_dialog_key:
                break

    def _display_end_dialog_indicator(self,
                                      stdscr,
                                      text_attributes: Tuple = (curses.A_BOLD, curses.A_BLINK)):
        """Displays an end of dialog indicator in the lower right corner of textbox.

        Parameters
        ----------
        stdscr
            `curses` window object on which the method will have effect.
        text_attributes : tuple of curses text attribute constants, optional
           Text attributes of `end_dialog_indicator` method
           (by default (curses.A_BOLD, curses.A_BLINK)).

        Returns
        -------
        None.

        See also
        --------
        """
        if self.end_dialog_indicator_char:
            with TextAttributes(stdscr, *text_attributes):
                stdscr.addch(self.end_dialog_indicator_pos_y,
                             self.end_dialog_indicator_pos_x,
                             self.end_dialog_indicator_char)

    def char_by_char(self,
                     stdscr,
                     text: str,
                     colors_pair_nb: int,
                     text_attributes: Tuple = (),
                     flash_screen: bool = False,
                     delay: float = .05,
                     random_delay: Tuple[int, int] = (0, 0),
                     callback: Callable = None,
                     cargs=()):
        """Writes the given text character by character at position in the current dialog box.

        Parameters
        ----------
        stdscr
            `curses` window object on which the method will have effect.
        text : str
            Text that will be displayed character by character in the dialog box. This text can
            be wrapped to fit the proportions of the dialog box. See Notes section for more
            informations.
        colors_pair_nb : int,
            Number of the curses color pair that will be used to color the text.
        text_attributes : tuple of curses text attribute constants, optional
            Dialog box text attributes (by default an empty tuple).
        flash_screen : bool, optional
            Allows or not to flash screen with a short light effect done before writing the first
            character via `flash` function from `curses` module (by default False).
        delay : int or float, optional
            Waiting time between the writing of each character of text in second (by default 0.05).
        random_delay : list of two number or tuple of two number, optional
            Waiting time between the writing of each character in seconds where time waited is a
            random number generated in `random_delay` interval (by default (0, 0)).
        callback : callable, optional
            Callable called after writing a character and the delay time has elapsed
            (by default None).
        cargs : list or tuple, optional
            All the arguments that will be passed to callback (by default an empty tuple).

        Returns
        -------
        None.

        Notes
        -----
        Method flow:
            - Calling `framing_box` method.
            - Flash screen depending `flash_screen` parameter.
            - Cutting text into line via `wrap` function from `textwrap` module (to stay within the
            dialog box frame).
            - Writing paragraph by paragraph.
            - Writing each line of the current paragraph, character by character.
            - Calling `_display_end_dialog_indicator` method.

        Notes
        -----
            If the volume of text displayed is too large to be contained in a dialog box, text
            will be automatically cut into paragraphs. The screen will be completely cleaned when
            writing each paragraph via `window.clear()` method of `curses` module.

        See Also
        --------
            - Documentation of `wrap` function from `textwrap` module for more information
            of the behavior of text wrap
            (https://docs.python.org/fr/3.8/library/textwrap.html#textwrap.wrap).
            - Documentation of `flash` function from `curses` module
            (https://docs.python.org/3/library/curses.html?#curses.flash).
            - Documentation of `window.clear()` method from `curses` module
            (https://docs.python.org/3/library/curses.html?#curses.window.clear).
        """
        self.framing_box(stdscr)

        if flash_screen:
            curses.flash()

        wrapped_text = textwrap.wrap(text, self.nb_char_max_line - 1)
        wrapped_text = _make_chunk(wrapped_text, self.nb_lines_max)

        for paragraph in wrapped_text:
            stdscr.clear()
            self.framing_box(stdscr)
            for y, line in enumerate(paragraph):
                for x, char in enumerate(line):
                    attr = (curses.color_pair(colors_pair_nb),
                            *text_attributes)

                    with TextAttributes(stdscr, *attr):
                        stdscr.addstr(self.text_pos_y + y, self.text_pos_x + x,
                                      char)
                        stdscr.refresh()

                        if char in self.downtime_chars:
                            time.sleep(self.downtime_chars_delay +
                                       random.uniform(*random_delay))
                        else:
                            time.sleep(delay + random.uniform(*random_delay))

                    if callback:
                        callback(*cargs)

        self._display_end_dialog_indicator(stdscr)

    def word_by_word(self,
                     stdscr,
                     text: str,
                     colors_pair_nb: int,
                     cut_char: str = " ",
                     text_attributes: Tuple = (),
                     flash_screen: bool = False,
                     delay: float = .15,
                     random_delay: Tuple[int, int] = (0, 0),
                     callback: Callable = None,
                     cargs=()):
        """Writes the given text word by word at position at position in the current dialog box.

        Parameters
        ----------
        stdscr
            `curses` window object on which the method will have effect.
        text : str
            Text that will be displayed word by word in the dialog box. This text can be wrapped
            to fit the proportions of the dialog box. See Notes section for more informations.
        colors_pair_nb : int
            Number of the curses color pair that will be used to color the text.
        cut_char : str, optional
            The delimiter according which to split the text in word (by default a space).
        flash_screen : bool, optional
            Allows or not to flash screen with a short light effect done before writing the first
            word via `flash` function from `curses` module (by default False).
        delay : int or float, optional
            Waiting time between the writing of each character of text in second (by default 0.15).
        random_delay : list of two number or tuple of two number, optional
            Waiting time between the writing of each character in seconds where time waited is a
            random number generated in `random_delay` interval (by default (0, 0)).
        callback : callable, optional
            Callable called after writing a character and the `delay` time has elapsed
            (by default None).
        cargs : list or tuple, optional
            All the arguments that will be passed to callback (by default an empty tuple).

        Returns
        -------
        None.

        Notes
        -----
            Method flow:
                - Calling `framing_box` method.
                - Flash screen depending `flash_screen` parameter.
                - Cutting text into line via `textwrap.wrap` function from `textwrap` module (to
                stay within the dialog box frame).
                - Writing each line of the current paragraph, word by word.
                - Calling `_display_end_dialog_indicator` method.

        Notes
        -----
            If the volume of text displayed is too large to be contained in a dialog box, text
            will be automatically cut into paragraphs. The screen will be completely cleaned when
            writing each paragraph via `window.clear` method from `curses` module.

        See Also
        --------
            - Documentation of `wrap` function from `textwrap` module for more information
            on the behavior of text wrap
            (https://docs.python.org/fr/3.8/library/textwrap.html#textwrap.wrap).
            - Documentation of `flash` function from `curses` module
            (https://docs.python.org/3/library/curses.html?#curses.flash).
            - Documentation of `window.clear()` method from `curses` module
            (https://docs.python.org/3/library/curses.html?#curses.window.clear).
        """
        self.framing_box(stdscr)

        if flash_screen:
            curses.flash()

        attr = (curses.color_pair(colors_pair_nb),
                *text_attributes)

        wrapped_text = textwrap.wrap(text, self.nb_char_max_line - 1)
        wrapped_text = _make_chunk(wrapped_text, self.nb_lines_max)

        for paragraph in wrapped_text:
            stdscr.clear()
            self.framing_box(stdscr)
            for y, line in enumerate(paragraph):
                offsetting_x = 0
                for word in line.split(cut_char):
                    attr = (curses.color_pair(colors_pair_nb),
                            *text_attributes)

                    with TextAttributes(stdscr, *attr):
                        stdscr.addstr(self.text_pos_y + y, self.text_pos_x + offsetting_x,
                                      word)
                        stdscr.refresh()

                    offsetting_x += len(word) + 1  # Compensates for the space between words.
                    time.sleep(delay + random.uniform(*random_delay))

                if callback:
                    callback(*cargs)

        self._display_end_dialog_indicator(stdscr)


def main(stdscr):
    text = ("Hello world, how are you today ? ",
            "Press a key to skip this dialog. "
            "This is a basic example. See doc for more informations. "
            "If you have a problem don't hesitate to open an issue.",)

    curses.curs_set(0)

    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)


    textbox = DialogBox(20, 15,
                        40, 6,
                        title="Tim-ats-d",
                        title_colors_pair_nb=3,
                        end_dialog_indicator="►")

    textbox.confirm_dialog_key = (10, 32)

    def func(reply: str):
        stdscr.addstr(0, 0, reply)

    for reply in text:
        textbox.char_by_char(stdscr,
                             reply,
                             2,
                             cargs=(reply, ),
                             callback=func,
                             text_attributes=(curses.A_ITALIC, curses.A_BOLD))

        textbox.getkey(stdscr)
        stdscr.clear()


if __name__ == "__main__":
    curses.wrapper(main)

