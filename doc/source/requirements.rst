Requirements
============

Python version
--------------

- `Python 3.7 or more <https://www.python.org/downloads/>`_.

Curses
------

**Visual-dialog** works with ``curses`` Python module.
It is available in the standard **Python** library on **UNIX** but it doesn't work out-of-the-box on **Windows**.

To install ``curses`` on **Windows**, you need the ``windows-curses`` module:

.. code-block::

  pip install curses-windows

To build the documentation
--------------------------

- `Sphinx <https://www.sphinx-doc.org/en/master/usage/installation.html>`_ to generate the documentation of library.
- `sphinx-rtd-theme <https://pypi.org/project/sphinx-rtd-theme/>`_ used as documentation theme.

.. code-block::

  pip install sphinx sphinx_rtd_theme
