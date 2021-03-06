#  confrontation.py

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

    textbox_position = (10, 10)  # Position 10;10 in terminal.
    textbox_dimension = (40, 6)  # Length and width (in character).

    phoenix_wright = DialogBox(
        *textbox_position,
        *textbox_dimension,
        title="Phoenix", title_colors_pair_nb=1  # Title and color_pair used to colored title.
    )

    april_may = DialogBox(
        *textbox_position,
        *textbox_dimension,
        title="April", title_colors_pair_nb=2  # Title and color_pair used to colored title.
    )

    miles_edgeworth = DialogBox(
        *textbox_position,
        *textbox_dimension,
        title="Edgeworth", title_colors_pair_nb=3  # Title and color_pair used to colored title.
    )

    # Definition of accepted key codes to pass a dialog.
    # See documentation of curses constants for more informations.
    phoenix_wright.confirm_dialog_key = (10, 32)     # Key Enter and Space.
    april_may.confirm_dialog_key = (10, 32)  # Key Enter and Space.
    miles_edgeworth.confirm_dialog_key = (10, 32)   # Key Enter and Space.

    phoenix_wright.char_by_char(stdscr,
        "This testimony is a pure invention !",
        colors_pair_nb=0,
        delay=0.03)

    stdscr.clear()  # Clear entierely current window object.

    phoenix_wright.char_by_char(stdscr,
        "You're lying April May !",
        colors_pair_nb=0,
        flash_screen=True,
        delay=0.03,
        text_attributes=(curses.A_BOLD,))

    stdscr.clear()

    april_may.char_by_char(stdscr,
        "Arghh !",
        colors_pair_nb=0,
        delay=0.02,
        text_attributes=(curses.A_ITALIC,))

    stdscr.clear()

    miles_edgeworth.char_by_char(stdscr,
        "OBJECTION !",
        colors_pair_nb=0,
        flash_screen=True,
        delay=0.03,
        text_attributes=(curses.A_BOLD,)
        )

    stdscr.clear()

    miles_edgeworth.char_by_char(stdscr,
        "These accusations are irrelevant !",
        colors_pair_nb=0,
        delay=0.03)

    stdscr.clear()


# Execution of main function.
curses.wrapper(main)
