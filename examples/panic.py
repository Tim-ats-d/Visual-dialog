# panic.py
# An example of the use of panic keys.

import curses

from visualdialog import DialogBox, PanicError


# Definition of curses key constants.
# 10, 32, 113 correspond to enter, space and "q" keys.
PASS_KEYS = (10, 32)
EXIT_KEYS = (113, )


def main(win):
    # Makes the cursor invisible.
    curses.curs_set(False)

    box = DialogBox(1, 1,
                    40, 6)

    # Definition of accepted key codes to pass a dialog.
    box.confirm_dialog_key = PASS_KEYS

    box.panic_key = EXIT_KEYS

    try:
        box.char_by_char(win,
                         "When a key contained in EXIT_KEY has been "
                         "pressed a PanicError exception is raised.")
    except PanicError:  # Catch PanicError.
        box.char_by_char(win,
                         "PanicError exception has been caught. "
                         "One of the keys contained in EXIT_CHAR has "
                         "been pressed.")
    else:
        box.char_by_char(win,
                         "None of the keys contained in EXIT_CHAR have "
                         "been pressed.")
    finally:  # Code executed in all cases.
        box.char_by_char(win,
                         "End of dialog.")


# Execution of main function.
curses.wrapper(main)
