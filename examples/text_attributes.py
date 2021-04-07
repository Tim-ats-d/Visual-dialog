# text_attributes.py
# An example showing the possibilities of text formatting.

import curses

from visualdialog import DialogBox


# Definition of keys to pass a dialog.
PASS_KEYS = (" ", "\n")

# A key/value dictionary containing the text and the attributes
# with which it will be displayed.
# You can pass one or more curses text attributes arguments as a tuple.
sentences = {
    "An important text.": curses.A_BOLD,
    "An action performed by a character.": curses.A_ITALIC,
    "An underlined text.": curses.A_UNDERLINE,
    "A very important text.": (curses.A_BOLD, curses.A_ITALIC),
    "Incomprehensible gibberish.": curses.A_ALTCHARSET,
    "A blinking text.": curses.A_BLINK,
    "The colors of the front and the background reversed.": curses.A_REVERSE,
}


def main(win):
    curses.curs_set(False)

    # Definition of several colors pairs.
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_BLACK)

    textbox = DialogBox(1, 1,
                        30, 6,
                        title="Demo",
                        title_colors_pair_nb=1,  # Display title colored with color pair 1.
                        title_text_attr=curses.A_UNDERLINE)  # curse text attributes that will be applied to the title.

    textbox.confirm_dialog_keys = PASS_KEYS

    for text, attributes in sentences.items():
        textbox.char_by_char(win,
                             text,
                             2,  # Display text colored with color pair 2.
                             attributes)  # Pass attributes to text.


# Execution of main function.
curses.wrapper(main)
