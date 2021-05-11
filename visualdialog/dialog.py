# dialog.py
# 2020 Timéo Arnouts <tim.arnouts@protonmail.com>

__all__ = ["DialogBox"]

import curses
import random
import textwrap
from typing import (Any, Callable, Iterable, List, Mapping, Optional, Sequence,
                    Tuple, Union)

from .box import BaseTextBox
from .type import CursesTextAttribute, CursesTextAttributes, CursesWindow
from .utils import TextAttr, chunked, to_tuple


class DialogBox(BaseTextBox):
    """This class provides methods and attributs to manage a dialog box.

    Base :class:`BaseTextBox`.

    :param end_dialog_indicator: Character that will be displayed in the
        lower right corner the character once all the characters have
        been completed. String with a length of more than one character
        can lead to an overflow of the dialog box frame. This defaults
        to ``"►"``.

    :param global_win: `curses` window object where the text is written
        by default when the win argument of the :meth:`char_by_char` and
        :meth:`word_by_word` methods is omitted.

    :param args: Constructor arguments of :class:`BaseTextBox`.

    :param kwargs: Constructor keyword arguments of
        :class:`BaseTextBox`.

    .. note::
        This class can be used as a context manager.
    """
    def __init__(
            self,
            pos_x: int,
            pos_y: int,
            height: int,
            width: int,
            title: str = "",
            title_colors_pair_nb: int = 0,
            title_text_attr: Union[CursesTextAttribute,
                                   CursesTextAttributes] = curses.A_BOLD,
            downtime_chars: Sequence[str] = (",", ".", ":", ";", "!", "?"),
            downtime_chars_delay: int = 600,
            end_indicator: str = "►",
            global_win: Optional[CursesWindow] = None):
        """Initializes instance of :class:`DialogBox`."""
        BaseTextBox.__init__(self,
                             pos_x, pos_y,
                             height, width,
                             title,
                             title_colors_pair_nb, title_text_attr,
                             downtime_chars, downtime_chars_delay)

        self.text_wrapper = textwrap.TextWrapper(width=self.nb_char_max_line)

        self.end_indicator_char = end_indicator
        self.end_indicator_pos_x = self.pos_x + self.height - 2

        if self.title:
            self.end_indicator_pos_y = self.pos_y + self.width + 1
        else:
            self.end_indicator_pos_y = self.pos_y + self.width - 1

        self.global_win = global_win

    def __repr__(self) -> str:
        """Return repr(self)."""
        return f"DialogBox(title={self.title})"

    def __enter__(self) -> "DialogBox":
        """Return self."""
        return self

    def __exit__(self, type, value, traceback):
        """Return None."""
        return None

    def char_by_char(self,
                     text: str,
                     win: CursesWindow = None,
                     colors_pair_nb: int = 0,
                     text_attr: Union[CursesTextAttribute,
                                      CursesTextAttributes] = (),
                     words_attr: Mapping[Sequence[str],
                                         Union[CursesTextAttribute,
                                               CursesTextAttributes]] = {},
                     word_delimiter: str = " ",
                     flash_screen: bool = False,
                     delay: int = 40,
                     random_delay: Sequence[int] = (0, 0),
                     callbacks: Iterable[Callable[["DialogBox", str],
                                                  Optional[Any]]] = ()) -> str:
        """Write the given text character by character. Return the
        ``text`` passed argument without any treatment.

        :param text: Text that will be displayed character by character
            in the dialog box. This text can be wrapped to fit the
            proportions of the dialog box.

        :param win: ``curses`` window object on which the method will
            have effect. If omitted, ``self.global_win`` is chosen.

        :param colors_pair_nb: Number of the curses color pair that
            will be used to color the text. The number zero
            corresponding to the pair of white color on black
            background initialized by ``curses``). This defaults to
            ``0``.

        :param text_attr: Dialog box curses text attributes. It should
            be a single curses text attribute or a tuple of curses text
            attribute. This defaults an empty tuple.

        :param words_attr: Mapping composed of string as a key and a
            single curses text attribute or tuple as a value. Each key
            is colored with its associated values This defaults to an
            empty dictionary.

        :param word_delimiter: The delimiter according which to
            split the text in word. This defaults to ``" "``.

        :param flash_screen: Allows or not to flash screen with a short
            light effect done before writing the first character by
            ``flash`` function from ``curses`` module. This defaults to
            ``False``.

        :param delay: Waiting time between the writing of each character
            of text in milliseconds. This defaults to ``40``.

        :param random_delay: Waiting time between the writing of each
            character in milliseconds where time waited is a random
            number generated in ``random_delay`` interval. This defaults
            to ``(0, 0)``.

        :param callbacks: Iterable of callable called one by one after
            writing a character and the delay time has elapsed. This
            defaults to an empty tuple.
            The arguments passed to the given callables are:

            * the current instance (``self``).
            * the character previously written.
            * the index of the character previously written in the
              word being written.

        .. note::
            See implementation for more informations on method flow.

        .. note::
            If the volume of text displayed is too large to be contained
            in a dialog box, text will be automatically cut into
            paragraphs using ``textwrap.wrap`` function. See
            `textwrap module documentation
            <https://docs.python.org/fr/3.8/library/textwrap.html#textwrap.wrap>`_.
            for more information of the behavior of text wrap.

        .. warning::
            ``win`` will be completely cleaned when writing each
            paragraph by ``window.clear`` method of ``curses`` module.
        """
        self._one_by_one(self._write_word_char_by_char,
                         text,
                         win,
                         colors_pair_nb,
                         text_attr,
                         words_attr,
                         word_delimiter,
                         flash_screen,
                         delay,
                         random_delay,
                         callbacks)

        return text

    def word_by_word(self,
                     text: str,
                     win: CursesWindow = None,
                     colors_pair_nb: int = 0,
                     text_attr: Union[CursesTextAttribute,
                                      CursesTextAttributes] = (),
                     words_attr: Mapping[Sequence[str],
                                         Union[CursesTextAttribute,
                                               CursesTextAttributes]] = {},
                     word_delimiter: str = " ",
                     flash_screen: bool = False,
                     delay: int = 150,
                     random_delay: Sequence[int] = (0, 0),
                     callbacks: Iterable[Callable[["DialogBox", str],
                                                  Optional[Any]]] = ()) -> str:
        """Write the given text word by word. Return the ``text`` passed
        argument without any treatment.

        :param text: Text that will be displayed word by word in the
            dialog box. This text can be wrapped to fit the proportions
            of the dialog box.

        :param win: ``curses`` window object on which the method will
            have effect. If omitted, ``self.global_win`` is chosen.

        :param colors_pair_nb:
            Number of the curses color pair that will be used to color
            the text. The number zero corresponding to the pair of
            white color on black background initialized by ``curses``).
            This defaults to ``0``.

        :param text_attr: Dialog box curses text attributes. It should
            be a single curses text attribute or a tuple of curses text
            attribute. This defaults an empty tuple.

        :param words_attr: Mapping composed of string as a key and a
            single curses text attribute or tuple as a value. Each key
            is colored with its associated values This defaults to an
            empty dictionary.

        :param word_delimiter: The delimiter according which to
            split the text in word. This defaults to ``" "``.

        :param flash_screen: Allows or not to flash screen with a short
            light effect done before writing the first character by
            ``flash`` function from ``curses`` module. This defaults to
            ``False``.

        :param delay: Waiting time between the writing of each word of
            ``text`` in second. This defaults to ``150``.

        :param random_delay: Waiting time between the writing of each
            word in milliseconds where time waited is a random number
            generated in ``random_delay`` interval. This defaults to
            ``(0, 0)``.

        :param callbacks: Iterable of callable called one by one after
            writing a word and the delay time has elapsed. This defaults
            to an empty tuple.
            The arguments passed to the given callables are:

            * the current instance (``self``).
            * the word previously written.

        .. note::
            See implementation for more informations on method flow.

        .. note::
            If the volume of text displayed is too large to be contained
            in a dialog box, text will be automatically cut into
            paragraphs using ``textwrap.wrap`` function. See
            `textwrap module documentation
            <https://docs.python.org/fr/3.8/library/textwrap.html#textwrap.wrap>`_
            for more information of the behavior of text wrap.

        .. warning::
            ``win`` will be completely cleaned when writing each
            paragraph by ``window.clear`` method of ``curses`` module.

        .. warning::
            ``self.downtime_chars`` and ``self.downtime_chars_delay`` do
            not affect this method.
        """
        self._one_by_one(self._write_word,
                         text,
                         win,
                         colors_pair_nb,
                         text_attr,
                         words_attr,
                         word_delimiter,
                         flash_screen,
                         delay,
                         random_delay,
                         callbacks)

        return text

    def _display_end_indicator(self,
                               win: CursesWindow,
                               text_attr: CursesTextAttributes = (
                                   curses.A_BOLD,
                                   curses.A_BLINK)):
        """Displays an end indicator in the lower right corner of
        text box.

        :param win: ``curses`` window object on which the method
            will have effect.

        :param text_attr: Text attributes used to display
            ``end_indicator``. This defaults to
            ``(curses.A_BOLD, curses.A_BLINK)``.
        """
        if self.end_indicator_char:
            with TextAttr(win, *text_attr):
                win.addch(self.end_indicator_pos_y,
                          self.end_indicator_pos_x,
                          self.end_indicator_char)

    def _one_by_one(self,
                    write_method: Callable,
                    text: str,
                    win: CursesWindow,
                    colors_pair_nb: int,
                    text_attr: Union[CursesTextAttribute,
                                     CursesTextAttributes],
                    words_attr: Mapping[Sequence[str],
                                        Union[CursesTextAttribute,
                                              CursesTextAttributes]],
                    word_delimiter: str,
                    flash_screen: bool,
                    delay: int,
                    random_delay: Sequence[int],
                    callbacks: Iterable[Callable[["DialogBox",
                                                  CursesWindow,
                                                  str],
                                                 Optional[Any]]]):
        """This method offers a general purpose API to display text
        regardless of whether it is written word by word or character by
        character.
        """
        win = self.global_win or win
        text_attr = to_tuple(text_attr)
        colors_pair = curses.color_pair(colors_pair_nb)

        wrapped_text = self.text_wrapper.wrap(text)
        wrapped_text = chunked(wrapped_text, self.nb_lines_max)

        if flash_screen:
            curses.flash()

        for paragraph in wrapped_text:
            win.clear()
            self.framing_box(win)

            for y, line in enumerate(paragraph):
                offsetting_x = 0
                for word in line.split(word_delimiter):
                    if word in words_attr:
                        attr = to_tuple(words_attr[word])
                    else:
                        attr = (colors_pair, *text_attr)

                    with TextAttr(win, *attr):
                        write_method = getattr(self, write_method.__name__)
                        write_method(win,
                                     self.text_pos_x + offsetting_x,
                                     self.text_pos_y + y,
                                     word,
                                     delay,
                                     random_delay,
                                     callbacks)

                        # Waiting for space character.
                        curses.napms(delay)
                        # Compensate for the space between words.
                        offsetting_x += len(word) + 1

            self._display_end_indicator(win)
            self.get_input(win)

    def _write_word_char_by_char(self,
                                 win: CursesWindow,
                                 pos_x: int,
                                 pos_y: int,
                                 word: str,
                                 delay: int,
                                 random_delay: Sequence[int],
                                 callbacks: Iterable[
                                     Callable[[BaseTextBox,
                                               CursesWindow,
                                               str,
                                               int],
                                     Optional[Any]]]):
        """Write word char by char at given positon."""
        for x, char in enumerate(word):
            win.addstr(pos_y,
                       pos_x + x,
                       char)
            win.refresh()

            rand_delay = int(random.uniform(*random_delay))

            if char in self.downtime_chars:
                curses.napms(self.downtime_chars_delay
                             + rand_delay)
            else:
                curses.napms(rand_delay)

            curses.napms(delay)

            for callback in callbacks:
                callback(self, win, char, x)

    def _write_word(self,
                    win: CursesWindow,
                    pos_x: int,
                    pos_y: int,
                    word: str,
                    delay: int,
                    random_delay: Sequence[int],
                    callbacks: Iterable[Callable[["DialogBox",
                                                  CursesWindow,
                                                  str],
                                                 Optional[Any]]]):
        """Write word at given position."""
        win.addstr(pos_y,
                   pos_x,
                   word)
        win.refresh()

        rand_delay = int(random.uniform(*random_delay))
        curses.napms(delay
                     + rand_delay)

        for callback in callbacks:
            callback(self, win, word)