#  text_attributes.py
#
#  An example showing the possibilities of text formatting.

import curses

from visualdialog import DialogBox


# Definition of curses key constants.
# 10 and 32 correspond to enter and space keys.
ENTER_KEY = 10
SPACE_KEY = 32

def main(stdscr):
    # Makes the cursor invisible.
    curses.curs_set(False)

    # Definition of several colors pairs.
    curses.start_color()
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_BLACK)

    demo_textbox = DialogBox(1, 1,
                             40, 6,
                             title="Demonstration",
                             title_colors_pair_nb=1,  # Display title colored with color pair 1.
                             title_text_attr=curses.A_UNDERLINE)  # curse text attributes that will be applied to the title.
    demo_textbox.confirm_dialog_key = (ENTER_KEY, SPACE_KEY)

    # A key/value dictionary containing the text and the attributes
    # with which it will be displayed.
    # You can pass one or more curses text attributes arguments as a tuple.
    sentences = {
        "An important text.": curses.A_BOLD,
        "An action performed by a character.": curses.A_ITALIC,
        "An underlined text.": curses.A_UNDERLINE,
        "A very important text.": (curses.A_BOLD, curses.A_ITALIC),
        "Incomprehensible gibberish.": curses.A_ALTCHARSET,
        "A blinking text.": curses.A_BLINK,
        "The colors of the front and the background reversed.": curses.A_REVERSE,
    }

    for text, attributs in sentences.items():
        demo_textbox.char_by_char(stdscr,
                                  text,
                                  2,  # Display text colored with color pair 2.
                                  text_attr=attributs)  # Pass the attributes to the text.


# Execution of main function.
curses.wrapper(main)
