# box.py
# 2020 Timéo Arnouts <tim.arnouts@protonmail.com>

__all__ = ["BaseTextBox",
           "PanicError"]

import curses
import curses.textpad
from typing import Callable, List, Literal, Sequence, Tuple, Union

from .error import PanicError, ValueNotInBound
from .type import CursesKey, CursesTextAttribute, CursesTextAttributes, CursesWindow
from .utils import TextAttr, to_tuple


def value_checker(initializer: Callable) -> Callable:
    """A decorator which ensures that correct values are passed to
    ``BaseTextBox`` to avoid unexpected behavior.
    """
    def __init__(self,
                 pos_x, pos_y,
                 height, width,
                 title,
                 *args, **kwargs):
        minimum_box_width = 4

        title_box_borders_total_height = 5
        minimum_box_height = len(title) + title_box_borders_total_height

        if width < minimum_box_width:
            raise ValueNotInBound(f"width must be less than {minimum_box_width}")
        elif height < minimum_box_height:
            raise ValueNotInBound("height must be less than len(title) + 5")

        initializer(self,
                    pos_x, pos_y,
                    height, width,
                    title,
                    *args, **kwargs)

    return __init__


class BaseTextBox:
    """This class provides attributs and methods to manage a text box.

    .. NOTE::
        This class provides a general API for text boxes, it is not
        intended to be instantiated.

    :param pos_x: x position of the dialog box in ``curses`` window
        object on which methods will have effects.

    :param pos_y: y position of the dialog box in ``curses`` window
        object on which methods will have effects.

    :param height: Height of the dialog box in ``curses`` window object
        on which methods will have effects.

    :param width: Width of the dialog box in ``curses`` window object on
        which methods will have effects.

    :param title: String that will be displayed in the upper left corner
        of dialog box.
        If title is an empty string, the title will not be displayed.
        This defaults an empty string.

    :param title_colors_pair_nb:
        Number of the curses color pair that will be used to color the
        title. Zero corresponding to the pair of white color on black
        background initialized by ``curses``). This defaults to ``0``.

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
    """
    @value_checker
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
        self.pos_x, self.pos_y = pos_x, pos_y
        self.height, self.width = height - 1, width - 1

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

        self.downtime_chars = downtime_chars
        self.downtime_chars_delay = downtime_chars_delay

        #: Keystroke acquisition curses method for BaseTextBox.get_input.
        self.key_detection: Literal["getkey",
                                    "getch",
                                    "get_wch"] = "getkey"

        #: List of accepted key to skip dialog.
        #: This defaults to a list contains " ".
        self.confirm_keys: List[CursesKey] = [" "]
        #: List of accepted key to raise PanicError.
        #: This defaults to an empty list.
        self.panic_keys: List[CursesKey] = []

    @property
    def position(self) -> Tuple[int]:
        """Return a tuple contains x;y position of ``TextBox``.

        The position represents the x;y coordinates of the top left
        corner of text box.

        :returns: x;y position of ``TextBox``.
        """
        return self.pos_x, self.pos_y

    @property
    def dimensions(self) -> Tuple[int]:
        """Return a tuple contains dimensions of ``TextBox``.

        :returns: Height and width of ``TextBox``.
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
                                 self.pos_y
                                 + self.title_offsetting_y
                                 + self.width,
                                 self.pos_x + self.height)

    def get_input(self, win: CursesWindow):
        """Block execution as long as a key contained in
        ``self.confirm_keys`` is not detected.

        The method of key detection depends on the variable
        ``self.key_detection_mode``. ``"key"`` will acquire the key as
        a character and ``"code"`` as a key code. This is default to
        ``"key"``.

        :param win: ``curses`` window object on which the method will
            have effect.

        :raises PanicError: If a key contained in ``self.panic_keys`` is
            pressed.

        .. NOTE::
            - This method uses ``window.getch`` method from ``curses``
              module. Please refer to `curses documentation
              <https://docs.python.org/3/library/curses.html?#curses.window.getch>`_
              for more informations.
            - This method uses ``window.getkey`` method from ``curses``
              module. Please refer to `curses documentation
              <https://docs.python.org/3/library/curses.html?#curses.window.getkey>`_
              for more informations.
        """
        curses.flushinp()

        while 1:
            key = getattr(win, self.key_detection)()

            if key in self.confirm_keys:
                break
            elif key in self.panic_keys:
                raise PanicError(key)
