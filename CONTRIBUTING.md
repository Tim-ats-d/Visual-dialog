
# Contributing

## Setup your development environment

You need:

* `Python3.6`: you can install it by following [Python3's documentation](https://www.python.org/downloads/).
* `curses`: available in standard library of `Python` but it doesn't work out-of-the-box on `Windows`. See [this](https://www.devdungeon.com/content/curses-windows-python) explanations to install `curses` on Windows.

## Branches

* `main` : stable releases.
* `dev` : beta releases.

To fix a minor problem or add new features create a new branch in this form: `username-dev`.

## Conventions

When you make a pull request make sure to:

* Test your code with `Python3.6` to be sure not to break compatability.
* Format your code according [PEP 8](https://www.python.org/dev/peps/pep-0008/). [PEP8 Check](https://github.com/quentinguidee/actions-pep8) will ensure that your code is correctly formatted .
* Document your code following [Numpy documentation conventions](https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard) if you add new functionality.

If you add a feature that changes the API, notify it explicitly.

## Download

Download projet:
```bash
git clone https://github.com/Tim-ats-d/Visual-dialog
```

Install Visual-dialog using `pip` (The lib is not yet available on **pypy**):

```bash
python3 -m pip install git+git://github.com/Tim-ats-d/Visual-dialog
```
or update lib to the latest version:

```bash
python3 -m pip install git+git://github.com/Tim-ats-d/Visual-dialog --upgrade
```
The list of versions and their changelogs can be found [here](https://github.com/Tim-ats-d/Visual-dialog/releases/).

## Repository Structure

The following snippet describes Visual-dialog's repository structure.

```text
.
├── .github/
│   Contains Github specific files such as actions definitions and issue templates.
│
├── doc/
│   Contains the files related to the documentation.
│   │
│   ├── examples/
│   │   Contains several examples of use cases of Visual-dialog.
│   │
│   ├── generate-documentation.sh
│   │   A script to generate documentation of public API from the source code.
│   │   Produces two files: visualdialog-documentation.txt and visualdialog.core.html
│   │
│   └── tutorial.md
│       A tutorial to learn how to use Visual-dialog.
│
├── tests/
│   Contains tests for debugging libraries.
│   │
│   └── test.py
│
├── visualdialog/
│   Source for Visual-dialog's library.
│   │
│   ├── __init__.py
│   │
│   ├── box.py
│   │   Contains the parent class TextBox which serves as a basis for the implementation of the other classes.
│   │
│   ├── dialog.py
│   │   Contains the DialogBox class, which is the main class of the library.
│   │
│   └── utils.py
│       Contains the classes and functions used but not related to the libriarie.
│
├── LICENSE
│
├── CONTRIBUTING.md
│   This document.
│
├── MANIFEST.in
│   Contains list of non Python file.
│
├── README.md
│
└── setup.py
    Installation of the library.
```
