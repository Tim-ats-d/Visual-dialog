# context.py
# An example of how to use a text box as a context manager.

import curses

from visualdialog import DialogBox


replys = (
    "This text is displayed by an anonymous text box.",
    "Its behavior is the same as that of a normal dialog box.",
    "The advantage is that the verbosity is lighter."
)


def main(win):
    curses.curs_set(False)

    for reply in replys:
        # The keyword "as" allows to capture the returned DialogBox object.
        with DialogBox(1, 1,
                       30, 6) as db:
            db.confirm_keys.append("\n")  # To match enter key.
            db.char_by_char(reply, win)


# Execution of main function.
curses.wrapper(main)
