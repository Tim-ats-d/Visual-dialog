# words.py
# An example of using the word_by_word method from text boxes.

import curses

from visualdialog import DialogBox


instructions = (
    "Instead of the char_by_char method, word_by_word displays the "
    "given text word by word.",
    "It can be useful to make robots talk for example."
)


def main(win):
    # Make the cursor invisible.
    curses.curs_set(False)

    textbox = DialogBox(1, 1,  # Position 1;1 in win.
                        40, 6,  # Height and width of textbox.
                        "Robot")  # Title of textbox.

    # Definition of accepted key codes to pass a dialog.
    # This defaults to [" "] to match space key.
    textbox.confirm_keys.append("\n")

    # Iterate on each sentence contained in instructions.
    for instruction in instructions:
        textbox.word_by_word(instruction,
                             win,
                             delay=200)
        # Set delay between writting each words to 200 milliseconds.


# Execution of main function.
curses.wrapper(main)
