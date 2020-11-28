#!/usr/bin/env python3
# context.py

import curses

from visualdialog import DialogBox


def main(stdscr):
    monologue = (
        "I will be the narrator of this story.",
        "I will guide you throughout your adventure."
    )

    # Makes the cursor invisible.
    curses.curs_set(0)

    # Definition of several colors pairs.
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)

    with DialogBox(
            5, 5,  # Position 5;5 in terminal.
            40, 6,  # Length and width (in character).
            title="Narrator", title_colors_pair_nb=1) as narrator:  # We catch the dialog box with as.

        # Definition of accepted key codes to pass a dialog.
        # See documentation of the curses constants for more informations.
        narrator.confirm_dialog_key = (10, 32)  # Key Enter and Space.

        # We iterate on each sentence contained in monologue.
        for text in monologue:
            narrator.char_by_char(stdscr,
                text,
                2)  # Display of the reply variable colored with color pair 2.

            narrator.getkey(stdscr)  # Waiting for a key press.
            stdscr.clear()  # Clear the screen.


# Execution of the function.
curses.wrapper(main)
