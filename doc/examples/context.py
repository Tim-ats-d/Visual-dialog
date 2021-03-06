#  context.py

import curses

from visualdialog import DialogBox


def main(stdscr):
    # Makes the cursor invisible.
    curses.curs_set(0)

    # Definition of several colors pairs.
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)

    textbox = DialogBox(
        0, 0,  # Position 0;0 in terminal.
        40, 6,  # Length and width (in character).
        title="Tim-ats-d",
        title_colors_pair_nb=1,  # Title and color_pair used to colored title.
        title_text_attributes=(curses.A_UNDERLINE, ))  # Attribute to underline the title.
    # It is necessary to think of passing a tuple even if it contains only one element
    # (see doc for more informations).

    # Definition of accepted key codes to pass a dialog.
    # See documentation of the curses constants for more informations.
    textbox.confirm_dialog_key = (10, 32)  # Key Enter and Space.

    sentences = {
        "An important text.": (curses.A_BOLD, ),
        "An action performed by a character.": (curses.A_ITALIC, ),
        "An underlined text.": (curses.A_UNDERLINE, ),
        "A very important text.": (curses.A_BOLD, curses.A_ITALIC),
        "Incomprehensible gibberish ": (curses.A_ALTCHARSET, ),
        "The colors of the front and the background reversed.":
        (curses.A_REVERSE, ),
    }

    for text, attributs in sentences.items():
        textbox.char_by_char(
            stdscr,
            text,
            2,  # Display of the reply variable colored with color pair 2.
            text_attributes=attributs)  # Pass the attributes to the text.

        stdscr.clear()  # Clear entierely current window object.


# Execution of main function.
curses.wrapper(main)
