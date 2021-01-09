#!/usr/bin/env python3
#
#  test.py
#
#  This file contains the tests used to debug the library.

import curses


__import__("sys").path.append("../visualdialog")
from dialog import DialogBox


def main(stdscr):
    text = (
        "Hello world, how are you today ? test",
        "Press a key to skip this dialog. ",
        "This is a basic example. See doc for more informations."
        " If you have a problem don't hesitate to open an issue.",
    )

    curses.curs_set(0)

    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)

    textbox = DialogBox(20, 15,
                        40, 6,
                        title="Tim-ats-d",
                        title_colors_pair_nb=3,
                        end_dialog_indicator="o")

    textbox.confirm_dialog_key = (32, 10)
    # ~ textbox.panic_key = (32, )

    special_words = {
        "test": (curses.A_BOLD, curses.A_ITALIC),
        "this": (curses.A_BLINK, curses.color_pair(1))
    }

    def func(text: str):
        stdscr.addstr(0, 0, text)


    for reply in text:
        textbox.char_by_char(stdscr,
                             reply,
                             cargs=(reply, ),
                             callback=func,
                             text_attr=(curses.A_ITALIC, curses.A_BOLD),
                             words_attr=special_words)
        # ~ textbox.word_by_word(stdscr,
                             # ~ reply,
                             # ~ 2,
                             # ~ words_attr=special_words)



if __name__ == "__main__":
    curses.wrapper(main)
