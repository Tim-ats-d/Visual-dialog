# box.py
# 2020 Timéo Arnouts <tim.arnouts@protonmail.com>

__all__ = ["BaseTextBox"]

import curses
import curses.textpad
from typing import List, Literal, NoReturn, Sequence, Tuple, Union

from .error import PanicError, ValueNotInBound
from .type import (CursesKey, CursesTextAttribute, CursesTextAttributes,
                   CursesWindow)
from .utils import TextAttr, to_tuple


class BoundHeight:
    """A descriptor which ensures that correct value is setted to
    ``BaseTextBox.height`` to avoid unexpected behavior.
    """
    def __get__(self, obj: "BaseTextBox", objtype=None):
        return obj._height

    def __set__(self, obj: "BaseTextBox", value: int) -> NoReturn:
        title_box_borders_total_height = 5
        minimum_box_height = len(obj.title) + title_box_borders_total_height

        if value < minimum_box_height:
            raise ValueNotInBound("height must be more than title length + 5")
        else:
            obj._height = value


class BoundWidth:
    """A descriptor which ensures that correct value is setted to
    ``BaseTextBox.width`` to avoid unexpected behavior.
    """
    def __get__(self, obj: "BaseTextBox", objtype=None):
        return obj._width

    def __set__(self, obj: "BaseTextBox", value: int) -> NoReturn:
        minimum_box_width = 4

        if value < minimum_box_width:
            raise ValueNotInBound("width must be more than "
                                  f"{minimum_box_width}")
        else:
            obj._width = value


class BaseTextBox:
    """This class provides attributs and methods to manage a text box.

    .. note::
        This class provides a general API for text boxes, it is not
        intended to be instantiated.

    :param pos_x: x position of the dialog box in ``curses`` window
        object on which methods will have effects.

    :param pos_y: y position of the dialog box in ``curses`` window
        object on which methods will have effects.

    :param height: Height of the dialog box in ``curses`` window object
        on which methods will have effects.
        This value is covered by a descriptor to avoid unexpected behavior.
        Set this value to a value lower than title length and title box borders
        height (``len(self.title) + 5``) raises a ``ValueError``.

    :param width: Width of the dialog box in ``curses`` window object on
        which methods will have effects.
        This value is covered by a descriptor to avoid unexpected behavior.
        Set this value to a value lower than 4 (the minimum box width)
        raises a ``ValueError``.

    :param title: String that will be displayed in the upper left corner
        of dialog box.
        If title is an empty string, the title will not be displayed.
        This defaults an empty string.

    :param title_colors_pair_nb:
        Number of the curses color pair that will be used to color the
        title. Zero corresponding to the pair of white color on black
        background initialized by ``curses``. This defaults to ``0``.

    :param title_text_attr:
        Dialog box title text attributes. It should be a single curses
        text attribute or a tuple of curses text attribute. This
        defaults to ``curses.A_BOLD``.

    :param downtime_chars:
        List of characters that will trigger a ``downtime_chars_delay``
        time second between the writing of each character.
        This defaults to ``(",", ".", ":", ";", "!", "?")``.

    :param downtime_chars_delay:
        Waiting time in milliseconds after writing a character contained
        in ``downtime_chars``.
        This defaults to ``600``.

    :ivar key_detection: initial value: ["getkey", "getch", "get_wch"]:
        Keystroke acquisition ``curses`` method for
        :meth:`BaseTextBox.get_input`.

    :ivar confirm_keys: initial value: [" "]:
        List of accepted key to skip dialog.

    :ivar panic_keys: initial value: []:
        List of accepted key to raise :exc:`PanicError`.
    """
    height, width = BoundHeight(), BoundWidth()

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
            downtime_chars_delay: int = 600):
        """Initializes instance of :class:`BaseTextBox`."""
        self.title_offsetting_y = 2 if title else 0

        # Compensation for left and upper borders of text box.
        self.text_pos_x = pos_x + 2
        self.text_pos_y = pos_y + self.title_offsetting_y + 1

        # Text margins.
        self.nb_char_max_line = height - 5
        self.nb_lines_max = width - 3

        self.title = title
        if title:
            self.title_colors = curses.color_pair(title_colors_pair_nb)
            self.title_text_attr = to_tuple(title_text_attr)

        self.pos_x, self.pos_y = pos_x, pos_y
        self.height, self.width = height - 1, width - 1

        self.downtime_chars = downtime_chars
        self.downtime_chars_delay = downtime_chars_delay

        #: Keystroke acquisition curses method for BaseTextBox.get_input.
        self.key_detection: Literal["getkey",
                                    "getch",
                                    "get_wch"] = "getkey"

        #: List of accepted key to skip dialog.
        #: This defaults to a list contains ``" "``.
        self.confirm_keys: List[CursesKey] = [" "]
        #: List of accepted key to raise PanicError.
        #: This defaults to an empty list.
        self.panic_keys: List[CursesKey] = []

    @property
    def position(self) -> Tuple[int, int]:
        """A property that returns a tuple contains x;y position of
        :class:`BaseTextBox`.

        The position represents the x;y coordinates of the top left
        corner of text box.

        :returns: x;y position of :class:`BaseTextBox`.
        """
        return self.pos_x, self.pos_y

    @property
    def dimensions(self) -> Tuple[int, int]:
        """A property that return a tuple contains dimensions of
        :class:`BaseTextBox`.

        :returns: Height and width of :class:`BaseTextBox`.
        """
        return (self.height + 1,
                self.width + 1 + self.title_offsetting_y)

    def framing_box(self, win: CursesWindow):
        """Display dialog box borders and his title.

        If attribute ``self.title`` is empty doesn't display the title
        box.

        :param win: ``curses`` window object on which the method will
            have effect.
        """
        title_height = len(self.title) + 4
        title_width = 2

        # Display title and title box.
        if self.title:
            attr = (self.title_colors, *self.title_text_attr)

            curses.textpad.rectangle(win,
                                     self.pos_y,
                                     self.pos_x + 1,
                                     self.pos_y + title_width,
                                     self.pos_x + title_height)

            with TextAttr(win, *attr):
                win.addstr(self.pos_y + 1,
                           self.pos_x + 3,
                           self.title)

        # Display borders of text box.
        curses.textpad.rectangle(win,
                                 self.pos_y + self.title_offsetting_y,
                                 self.pos_x,
                                 (self.pos_y
                                  + self.title_offsetting_y
                                  + self.width),
                                 self.pos_x + self.height)

    def get_input(self, win: CursesWindow):
        """Block execution as long as a key contained in
        ``self.confirm_keys`` is not detected.

        The method of key detection depends on the variable
        ``self.key_detection``.

        :param win: ``curses`` window object on which the method will
            have effect.

        :raises PanicError: If a key contained in ``self.panic_keys`` is
            pressed.
        """
        curses.flushinp()

        while 1:
            key = getattr(win, self.key_detection)()

            if key in self.confirm_keys:
                break
            elif key in self.panic_keys:
                raise PanicError(key)
