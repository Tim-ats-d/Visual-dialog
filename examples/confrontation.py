# confrontation.py
# A concrete example exploiting the possibilities of Visual-dialog.

import curses
from functools import partial

from visualdialog import DialogBox


pass_keys = (" ", "\n")
height, width = 35, 5


# It is preferable to create its own class derived from DialogBox for
# complex applications (or an instance factory like here).
def box_factory(win,
                x: int,
                y: int,
                title: int,
                title_colors_pair_nb: int,
                **kwargs) -> DialogBox:
    box = DialogBox(x, y,
                    height, width,
                    title, title_colors_pair_nb,
                    global_win=win,
                    # Use a default window to display text.
                    # Setting this parameter allows to avoid passing `win`
                    # parameter to `char_by_char` and `word_by_word` methods.
                    # Useful when dealing with many `DialogBox` methods calls.
                    **kwargs)

    # Definition of accepted key codes to pass a dialog.
    box.confirm_keys = pass_keys
    # Definition of a partial objet to reduce verbosity and accelerate
    # the time it takes to write the text on the screen.
    box.char_by_char = partial(box.char_by_char, delay=30)

    return box


def main(win):
    # Make the cursor invisible.
    curses.curs_set(False)

    # Definition of several colors pairs.
    curses.init_pair(1, curses.COLOR_BLUE, 0)
    curses.init_pair(2, curses.COLOR_MAGENTA, 0)
    curses.init_pair(3, curses.COLOR_RED, 0)

    max_y, max_x = win.getmaxyx()  # Get height and width of the window.

    left_x = 2  # Left alignment.
    right_x = max_x - height - 4  # Calculation of right alignment.
    center_x = max_x//2 - height//2  # Calculation of center alignment.
    bottom_y = max_y - width - 4  # Calculation of bottom alignment.

    phoenix_wright = box_factory(win,
                                 left_x, bottom_y,
                                 "Phoenix",  # Title of dialog box.
                                 1)  # Color pair used to colored title.

    april_may = box_factory(win,
                            center_x, bottom_y,
                            "April",
                            2)

    miles_edgeworth = box_factory(win,
                                  right_x, bottom_y,
                                  "Edgeworth",
                                  3)

    phoenix_wright.char_by_char("This testimony is a pure invention !",
                                delay=30)
    # Set delay between writting each characters to 30 milliseconds

    phoenix_wright.char_by_char("You're lying April May !",
                                flash_screen=True,  # A short luminous glow will be displayed before writing the text.
                                delay=30,
                                text_attr=curses.A_BOLD)

    april_may.char_by_char("Arghh !",
                           delay=30,
                           text_attr=curses.A_ITALIC)

    miles_edgeworth.char_by_char("OBJECTION !",
                                 flash_screen=True,
                                 delay=30,
                                 text_attr=curses.A_BOLD)

    miles_edgeworth.char_by_char("These accusations are irrelevant !",
                                 delay=30)


# Execution of main function.
curses.wrapper(main)
