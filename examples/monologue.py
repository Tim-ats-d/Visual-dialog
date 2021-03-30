# monologue.py
# A simple example of how to use Visual-dialog.

import curses

from visualdialog import DialogBox


# Definition of curses key constants.
# 10 and 32 correspond to enter and space keys.
ENTER_KEY = 10
SPACE_KEY = 32


def main(stdscr):
    replys = (
        "Hello world",
        "Press a key to skip this dialog.",
        "That is a basic example.",
        "See doc for more informations."
    )

    # Makes the cursor invisible.
    curses.curs_set(False)

    # Definition of several colors pairs.
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)

    textbox = DialogBox(1, 1,  # Position 1;1 in stdscr.
                        40, 6,  # Length and width of textbox (in character).
                        title="Tim-ats-d",  # Title of textbox.
                        title_colors_pair_nb=1)  # Curses color_pair used to colored title.

    # Definition of accepted key codes to pass a dialog.
    textbox.confirm_dialog_key = (ENTER_KEY, SPACE_KEY)

    # Iterate on each sentence contained in replys.
    for reply in replys:
        textbox.char_by_char(stdscr,
            reply,
            2,  # Display text colored with color pair 2.
            delay=0.04)  # Set delay between writting each characters to 0.04 seconde.


# Execution of main function.
curses.wrapper(main)
