Utils
=====

.. NOTE::
  A sub-module of **Visual-dialog** (``visualdialog.utils``) contains
  functions and classes used by the private API. The context manager
  ``TextAttributes`` is used by the library to manage in a more
  pythonic way the textual ``curses`` attributes curses but you can
  also use it in your programs.

  ``visualdialog.utils`` is automatically imported when importing
  visualdialog so you can use its module functions and classes just like this::

    import visualdialog

    visualdialog.function(args)


.. autoclass:: visualdialog.utils.TextAttributes
    :members:
