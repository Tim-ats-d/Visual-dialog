# error.py
# 2020 Timéo Arnouts <tim.arnouts@protonmail.com>

__all__ = ["PanicError", "ValueNotInBound"]

from .type import CursesKey


class ValueNotInBound(ValueError):
    """Base ``ValueError``.

    Exception thrown when incorrect values are passed as parameters
    to the :class:`visualdialog.box.BaseTextBox` constructor.
    """
    pass


class PanicError(KeyboardInterrupt):
    """Base ``KeyboardInterrupt``.

    Exception thrown when a key contained in
    :attr:`visualdialog.box.BaseTextBox.panic_keys` is pressed.

    :param key: Key pressed that caused the exception to be thrown.
    """
    def __init__(self, key: CursesKey):
        self.key = key

    def __str__(self) -> str:
        return ("text box was aborted "
                + (f"keycode {self.key}"
                   if isinstance(self.key, int)
                   else f'by pressing "{self.key}" key'))
