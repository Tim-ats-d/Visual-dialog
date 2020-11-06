#!/usr/bin/python3
#  example.py

import curses

from visualdialog import *


def main(stdscr):
    text = (
        "Hello world",
        "How are you today ?",
        "Press a key to skip this dialog."
        )

    # Makes the cursor invisible.
    curses.curs_set(0)

    # Definition of several colors pairs.
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)

    textbox = DialogBox(
        20, 15,  # Position 20;15 in terminal.
        40, 6,  # Length and width (in character).
        title="Dogm", title_colors_pair_nb=3, # Title and color_pair used to colored title.
        end_dialog_indicator="►"
        delay=0.6) # Time in seconds between the writing of each character.

    # Display each sentence contains in text.
    for reply in text:
        textbox.framing_box(stdscr) # Display of the dialog box
        textbox.char_by_char(stdscr, reply, 2) # Display of the reply variable colored with color pair 2.

        stdscr.getch() # Waiting for a key press.
        stdscr.clear() # Clear the screen.

# Execution of the function.
curses.wrapper(main)
