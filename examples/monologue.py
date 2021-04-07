# monologue.py
# A simple example of how to use Visual-dialog.

import curses

from visualdialog import DialogBox


# Definition of keys to pass a dialog.
PASS_KEYS = (" ", "\n")

replys = (
    "Hello world",
    "Press a key to skip this dialog.",
    "That is a basic example.",
    "See doc for more informations."
)


def main(win):
    # Make the cursor invisible.
    curses.curs_set(False)

    # Definition of several colors pairs.
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)

    textbox = DialogBox(1, 1,  # Position 1;1 in win.
                        30, 5,  # Height and width of textbox.
                        "Tim-ats",  # Title of textbox.
                        1)  # Curses color_pair used to colored title.

    # Definition of accepted key codes to pass a dialog.
    textbox.confirm_dialog_keys = PASS_KEYS

    # Iterate on each sentence contained in replys.
    for reply in replys:
        textbox.char_by_char(
            win,
            reply,
            2,  # Display text colored with color pair 2.
            delay=40)  # Set delay between writting each characters to 40 milliseconds.


# Execution of main function.
curses.wrapper(main)
