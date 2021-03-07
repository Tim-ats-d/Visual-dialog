#  monologue.py

import curses

from visualdialog import DialogBox


def main(stdscr):
    replys = (
        "Hello world, how are you today ?",
        "Press a key to skip this dialog.",
        "That is a basic example.",
        "See doc for more informations."
    )

    # Makes the cursor invisible.
    curses.curs_set(0)

    # Definition of several colors pairs.
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)

    textbox = DialogBox(
        20, 15,   # Position 20;15 in terminal.
        40, 6,   # Length and width of textbox (in character).
        title="Tim-ats-d", title_colors_pair_nb=3)
        # Title and color pair used to colored title.

    # Definition of accepted key codes to pass a dialog.
    # See documentation of the curses constants for more informations.
    textbox.confirm_dialog_key = (10, 32)  # Key Enter and Space.

    # We iterate on each sentence contained in replys.
    for reply in replys:
        textbox.char_by_char(stdscr,
            reply,
            2,  # Display of the reply variable colored with color pair 2.
            delay=0.04)  # Set delay between each characters to 0.04 seconde.

        stdscr.clear()  # Clear entierely current window object.


# Execution of main function.
curses.wrapper(main)
