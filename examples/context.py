#  context.py
#
#  An example of how to use a text box with a context manager.

import curses

from visualdialog import DialogBox


def main(stdscr):
    # Makes the cursor invisible.
    curses.curs_set(0)

    replys = (
        "This text is displayed by an anonymous text box.",
        "Its behavior is the same as that of a normal dialog box.",
        "The advantage is that the syntax is lighter."
    )

    for reply in replys:
        # The keyword "as" allows to capture the returned DialogBox object.
        with DialogBox(1, 1, 30, 6) as db:
            db.confirm_dialog_key = (10, 32)
            db.char_by_char(stdscr, reply)


# Execution of main function.
curses.wrapper(main)
