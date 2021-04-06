# context.py
# An example of how to use a text box as a context manager.

import curses

from visualdialog import DialogBox


# Definition of curses key constants.
# 10 and 32 correspond to enter and space keys.
PASS_KEYS = (10, 32)

replys = (
    "This text is displayed by an anonymous text box.",
    "Its behavior is the same as that of a normal dialog box.",
    "The advantage is that the verbosity is lighter."
)


def main(win):
    # Makes the cursor invisible.
    curses.curs_set(False)

    for reply in replys:
        # The keyword "as" allows to capture the returned DialogBox object.
        with DialogBox(1, 1,
                       30, 6) as db:
            db.confirm_dialog_keys = PASS_KEYS
            db.char_by_char(win,
                            reply)


# Execution of main function.
curses.wrapper(main)
