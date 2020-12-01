
# Contributing

## Setup your development environment

You need:
* `Python3.6`: you can install it by following [Python3's documentation](https://www.python.org/downloads/).
* `curses`: available in standard library of `Python` but it doesn't work out-of-the-box on Windows. See [this](https://www.devdungeon.com/content/curses-windows-python) explanations to install `curses` on Windows.

## Branches

* main : stable releases.

To fix a minor problem or add new features create a new branch in this form: `username-dev`.
Please test your code with `Python3.6` version before **pull request** to be sure not to break compatability.

## Download

Download projet:
```bash
git clone https://github.com/Tim-ats-d/Visual-dialog
```

Install Visual-dialog using `pip`:
```bash
python3 -m pip install git+git://github.com/Tim-ats-d/Visual-dialog
```
or update lib to the latest version:
```bash
python3 -m pip install git+git://github.com/Tim-ats-d/Visual-dialog --upgrade
```
The list of versions and their changelogs can be found [here](https://github.com/Tim-ats-d/Visual-dialog/releases/).

## Repository Structure

The following snippet describes Visual-dialog's repository structure.

```text
.
├── .github/
|   Contains Github specific files such as actions definitions and issue templates.
│
├── doc/
|   Contains documentation.
│   │
│   ├── examples/
│   │   Contains several examples of how to use Visual-dialog.
│   │
│   └── documentation.md
│       Documentation of public API (coming soon).
│
├── visualdialog/
|   Source for Visual-dialog's library.
│   │
|   ├── __init__.py
│   │
|   └── core.py
|       Contains Visual-dialog's core functionnalities.
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
