# test.py
# This file contains the tests used to debug the library.

import curses

from visualdialog import DialogBox
import visualdialog


def main(win):
    text = (
        "Hello world, how are\n you today ? test",
        "Press a key to skip this dialog. ",
        "This is a basic example. See doc for more informations."
        " If you have a problem don't hesitate to open an issue.",
    )

    curses.curs_set(0)

    curses.init_pair(1, curses.COLOR_RED, 0)
    curses.init_pair(2, curses.COLOR_CYAN, 0)
    curses.init_pair(3, curses.COLOR_GREEN, 0)

    textbox = DialogBox(0, 0,
                        40, 6,
                        # title="Tim-ats-d",
                        # title_colors_pair_nb=3,
                        end_indicator="o")

    textbox.confirm_dialog_keys = (32, )
    textbox.panic_keys = (10, )

    special_words = {
        "test": (curses.A_BOLD, curses.A_ITALIC),
        "this": (curses.A_BLINK, curses.color_pair(1))
    }

    def display_position(self: DialogBox,
                         char: str,
                         char_index: int):
        win.addstr(0, 0, char + str(char_index))
        win.refresh()

    def display_char_info(self: DialogBox,
                          char: str,
                          char_index: str):
        win.addstr(5, 0, char + str(char_index))
        win.refresh()

    for reply in text:
        textbox.char_by_char(win,
                             reply,
                             callbacks=(display_position, display_char_info),
                             text_attr=(curses.A_ITALIC, curses.A_BOLD),
                             words_attr=special_words)

    with visualdialog.TextAttr(win, curses.A_BOLD, curses.A_ITALIC):
        ...


if __name__ == "__main__":
    curses.wrapper(main)
