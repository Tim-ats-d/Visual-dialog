#  confrontation.py
#
#  A concrete example exploiting the possibilities of Visual-dialog.

import curses

from visualdialog import DialogBox


# Definition of curses key constants.
# 10 and 32 correspond to enter and space keys.
ENTER_KEY, SPACE_KEY = 10, 32

def main(stdscr):
    # Makes the cursor invisible.
    curses.curs_set(False)

    # Definition of several colors pairs.
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)

    position = (1, 1)  # Position 1;1 in stdscr.
    width, length  = 6, 35  # Width and length (in character).

    max_y, max_x = stdscr.getmaxyx()

    left_x = 2  # Left alignment.
    right_x = max_x - length - 4 # Calculation of right alignment.
    center_x = max_x // 2 - length // 2  # Calculation of center alignment.
    bottom_y = max_y - width - 4  # Calculation of bottom alignment.

    phoenix_wright = DialogBox(left_x, bottom_y,
                               length, width,
                               title="Phoenix",
                               title_colors_pair_nb=1)  # Title and color_pair used to colored title.

    april_may = DialogBox(center_x, bottom_y,
                          length, width,
                          title="April",
                          title_colors_pair_nb=2)

    miles_edgeworth = DialogBox(right_x, bottom_y,
                                length, width,
                                title="Edgeworth",
                                title_colors_pair_nb=3)

    # Definition of accepted key codes to pass a dialog.
    phoenix_wright.confirm_dialog_key = (ENTER_KEY, SPACE_KEY)
    april_may.confirm_dialog_key = (ENTER_KEY, SPACE_KEY)
    miles_edgeworth.confirm_dialog_key = (ENTER_KEY, SPACE_KEY)

    phoenix_wright.char_by_char(stdscr,
                                "This testimony is a pure invention !",
                                delay=0.03)  # Set delay between writting each characters to 0.03 seconde.

    phoenix_wright.char_by_char(stdscr,
                                "You're lying April May !",
                                flash_screen=True,  # A short luminous glow will be displayed before writing the text.
                                delay=0.03,
                                text_attr=curses.A_BOLD)

    april_may.char_by_char(stdscr,
                           "Arghh !",
                           delay=0.02,
                           text_attr=curses.A_ITALIC)

    miles_edgeworth.char_by_char(stdscr,
                                 "OBJECTION !",
                                 flash_screen=True,
                                 delay=0.03,
                                 text_attr=curses.A_BOLD)

    miles_edgeworth.char_by_char(stdscr,
                                 "These accusations are irrelevant !",
                                 delay=0.03)


# Execution of main function.
curses.wrapper(main)
