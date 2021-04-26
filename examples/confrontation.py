# confrontation.py
# A concrete example exploiting the possibilities of Visual-dialog.

import curses

from visualdialog import DialogBox


PASS_KEYS = (" ", "\n")
HEIGHT, WIDTH = 35, 6


# It is preferable to create its own class derived from DialogBox for
# complex applications.
class CustomDialogBox(DialogBox):

    def __init__(self,
                 pos_x: int,
                 pos_y: int,
                 title: str,
                 title_colors_pair_nb: int,
                 **kwargs):
        super().__init__(pos_x=pos_x,
                         pos_y=pos_y,
                         height=HEIGHT,
                         width=WIDTH,
                         title=title,
                         title_colors_pair_nb=title_colors_pair_nb,
                         **kwargs)

        # Definition of accepted key codes to pass a dialog.
        self.confirm_keys = PASS_KEYS


def main(win):
    # Make the cursor invisible.
    curses.curs_set(False)

    # Definition of several colors pairs.
    curses.init_pair(1, curses.COLOR_BLUE, 0)
    curses.init_pair(2, curses.COLOR_MAGENTA, 0)
    curses.init_pair(3, curses.COLOR_RED, 0)

    max_y, max_x = win.getmaxyx()  # Get height and width of the window.

    left_x = 2  # Left alignment.
    right_x = max_x - HEIGHT - 4  # Calculation of right alignment.
    center_x = max_x//2 - HEIGHT//2  # Calculation of center alignment.
    bottom_y = max_y - WIDTH - 4  # Calculation of bottom alignment.

    phoenix_wright = CustomDialogBox(left_x, bottom_y,
                                     "Phoenix",  # Title of dialog box.
                                     1)  # Color pair used to colored title.

    april_may = CustomDialogBox(center_x, bottom_y,
                                "April",
                                2)

    miles_edgeworth = CustomDialogBox(right_x, bottom_y,
                                      "Edgeworth",
                                      3)

    phoenix_wright.char_by_char(win,
                                "This testimony is a pure invention !",
                                delay=30)
    # Set delay between writting each characters to 30 milliseconds

    phoenix_wright.char_by_char(win,
                                "You're lying April May !",
                                flash_screen=True,  # A short luminous glow will be displayed before writing the text.
                                delay=30,
                                text_attr=curses.A_BOLD)

    april_may.char_by_char(win,
                           "Arghh !",
                           delay=30,
                           text_attr=curses.A_ITALIC)

    miles_edgeworth.char_by_char(win,
                                 "OBJECTION !",
                                 flash_screen=True,
                                 delay=30,
                                 text_attr=curses.A_BOLD)

    miles_edgeworth.char_by_char(win,
                                 "These accusations are irrelevant !",
                                 delay=30)


# Execution of main function.
curses.wrapper(main)
