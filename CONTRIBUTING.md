
# Contributing

## Setup your development environment

You need:

* `Python 3.7`: you can install it by following [Python3's documentation](https://www.python.org/downloads/).
* `curses`: available in standard library of `Python` but it doesn't work out-of-the-box on `Windows`. See [this](https://www.devdungeon.com/content/curses-windows-python) explanations to install `curses` on Windows.
* [`Sphinx`](https://www.sphinx-doc.org/en/master/usage/installation.html): to generate documentation.

## Branches

* `main` : stable releases.
* `dev` : beta releases.

To fix a minor problem or add new features create a new branch in this form: `username-dev`.
Please push on the `dev` branch, any pull request on the `main` branch will be refused.

## Conventions

When you make a pull request make sure to:

* Test your code with `Python3.7` to be sure not to break compatability.
* Format your code according [PEP 8](https://www.python.org/dev/peps/pep-0008/). [PEP8 Check](https://github.com/quentinguidee/actions-pep8) will ensure that your code is correctly formatted .
* Document your code with [reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html) if you add new functionality.

If you add a feature that changes the API, notify it explicitly.

## Download

Download the `dev` branch of the project:
```sh
git clone -b dev https://github.com/Tim-ats-d/Visual-dialog.git
```

Install Visual-dialog using `pip` (The lib is not yet available on **pypi**):
```sh
python3 -m pip install git+git://github.com/Tim-ats-d/Visual-dialog
```
or update lib to the latest version:

```sh
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
│   ├── images/
│   │    Contains images used in documentation.
│   │
│   ├── conf.py
│   │   Sphinx's configuration file.
│   │
│   ├── index.rst
│   │   Documentation home page.
│   │
│   └── visualdialog.rst
│         Documentation of all the public classes and methods in Visual-dialog.
│
├── examples/
│    Contains several examples of use cases of Visual-dialog.
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
├── make.bat
│   To generate documentation on Windows.
│
├── Makefile
│   To generate documentation on GNU/Linux or MacOS.
│
├── MANIFEST.in
│   Contains list of non Python file.
│
├── README.md
│
└── setup.py
   Installation of the library.
```
