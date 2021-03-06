# panic.py
# An example of the use of panic keys.

import curses

from visualdialog import DialogBox, PanicError


def main(win):
    curses.curs_set(False)

    box = DialogBox(1, 1,
                    40, 6)

    # Definition of keys to pass and exit a dialog.
    box.confirm_keys.append("\n")
    box.panic_keys = ("q", )

    try:
        box.char_by_char(win,
                         "When a key contained in EXIT_KEY has been "
                         "pressed a PanicError exception is raised.")
    except PanicError:  # Catch PanicError.
        box.char_by_char(win,
                         "PanicError exception has been caught. "
                         "One of the keys contained in EXIT_CHAR has "
                         "been pressed.")
    else:
        box.char_by_char(win,
                         "None of the keys contained in EXIT_CHAR have "
                         "been pressed.")
    finally:  # Code executed in all cases.
        box.char_by_char(win,
                         "End of dialog.")


# Execution of main function.
curses.wrapper(main)
