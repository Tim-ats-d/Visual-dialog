Frequently asked questions
==========================

Why is DialogBox a context manager?
-----------------------------------

You can use this behavior to avoid having to instantiate a new dialog box.

See the `dedicated example <https://github.com/Tim-ats-d/Visual-dialog/tree/main/examples/context.py>`_.

How can I continue to manage screen display while a DialogBox is writing text on the screen?
--------------------------------------------------------------------------------------------

``char_by_char`` and ``word_by_word`` methods of ``DialogBox`` class accept a callback in parameter.
You can also pass arguments to this callback via ``cargs`` parameter.

The past callback is executed after downtime delay between character or word display.
You can use this behavior to perform multiple tasks while ``DialogBox`` scrolling.

I am not satisfied with the behavior of DialogBox, how can I change it?
-----------------------------------------------------------------------

You can create your own derived class by inheriting from ``BaseTextBox``.
Additionally, you can override the methods of ``DialogBox``.
