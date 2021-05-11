Text boxes
==========

.. important::
  **Visual-dialog** provides two classes but only :class:`DialogBox` is destined to be instantiated.

BaseTextBox
-----------

.. autoclass:: visualdialog.box.BaseTextBox

  .. automethod:: __init__

  The following methods are public:

  .. autoproperty:: position

  .. autoproperty:: dimensions

  .. automethod:: framing_box

  .. automethod:: get_input

DialogBox
---------

.. autoclass:: visualdialog.dialog.DialogBox

  .. automethod:: __init__

  The following methods are public:

  .. automethod:: __repr__

  .. automethod:: __enter__

  .. automethod:: __exit__

  .. automethod:: char_by_char

  .. automethod:: word_by_word
