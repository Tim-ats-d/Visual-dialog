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
        box.char_by_char("When a key contained in EXIT_KEY is pressed "
                         "at end of dialog PanicError exception is raised.",
                         win)
    except PanicError:  # Catch PanicError.
        box.char_by_char("PanicError exception has been caught. "
                         "One of the keys contained in EXIT_CHAR has "
                         "been pressed.",
                         win)
    else:
        box.char_by_char("None of the keys contained in EXIT_CHAR have "
                         "been pressed.",
                         win)
    finally:  # Code executed in all cases.
        box.char_by_char("End of dialog.", win)


# Execution of main function.
curses.wrapper(main)
