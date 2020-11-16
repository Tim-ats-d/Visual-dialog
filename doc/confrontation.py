#!/usr/bin/env python3
# confrontation_example.py

import curses

from visualdialog import DialogBox


def main(stdscr):
    # Makes the cursor invisible.
    curses.curs_set(0)

    # Definition of several colors pairs.
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)

    textbox_position = (20, 15)  # Position 20;15 in terminal.
    textbox_dimension = (40, 6)  # Length and width (in character).

    phoenix_textbox = DialogBox(
        *textbox_position,
        *textbox_dimension,
        title="Phoenix", title_colors_pair_nb=1  # Title and color_pair used to colored title.
    )

    april_may_textbox = DialogBox(
        *textbox_position,
        *textbox_dimension,
        title="April", title_colors_pair_nb=2  # Title and color_pair used to colored title.
    )

    edgeworth_textbox = DialogBox(
        *textbox_position,
        *textbox_dimension,
        title="Edgeworth", title_colors_pair_nb=3
    )

    # Definition of accepted key codes to pass a dialog.
    # See documentation of curses constants for more informations.
    phoenix_textbox.confirm_dialog_key = (10, 32)     # Key Enter and Space.
    april_may_textbox.confirm_dialog_key = (10, 32)  # Key Enter and Space.
    edgeworth_textbox.confirm_dialog_key = (10, 32)   # Key Enter and Space.

    phoenix_textbox.char_by_char(stdscr,
        "This testimony is a pure invention !",
        colors_pair_nb=0,
        delay=0.03)

    phoenix_textbox.getkey(stdscr)  # Wait until a key in phoenix_textbox.confirm_dialog_key list is pressed.
    stdscr.clear()  # Clear the screen.

    phoenix_textbox.char_by_char(stdscr,
        "You're lying April May !",
        colors_pair_nb=0,
        flash_screen=True,
        delay=0.03)

    phoenix_textbox.getkey(stdscr)
    stdscr.clear()

    april_may_textbox.char_by_char(stdscr,
        "Arghh !",
        colors_pair_nb=0,
        delay=0.02)

    april_may_textbox.getkey(stdscr)  # Wait until a key in april_may_textbox.confirm_dialog_key list is pressed.
    stdscr.clear()

    edgeworth_textbox.char_by_char(stdscr,
        "OBJECTION !",
        colors_pair_nb=0,
        flash_screen=True,
        delay=0.03)

    edgeworth_textbox.getkey(stdscr)  # Wait until a key in edgeworth_textbox.confirm_dialog_key list is pressed.
    stdscr.clear()

    edgeworth_textbox.char_by_char(stdscr,
        "These accusations are irrelevant !",
        colors_pair_nb=0,
        delay=0.03)

    edgeworth_textbox.getkey(stdscr)
    stdscr.clear()


# Execution of the function.
curses.wrapper(main)
