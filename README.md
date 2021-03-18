
<p align="center">
  <a href="#features">Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#requirements">Requirements</a> •
  <a href="#documentation">Documentation</a> •
  <a href="#quick-start">Quick start</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#license">License</a>
</p>

<p align="center">
  <img width="300" src="https://user-images.githubusercontent.com/59396366/100594532-188c6900-32fa-11eb-8372-4796f53b122f.png" alt="Visual-dialog">
  <br>
  Library to make easier dialog box in terminal.
  <br>
  This library is still under development.
  API can change.
</p>

## Features

📃 Automatic text scrolling.

🔖 Text coloring and formatting.

⚙️ Hackable and configurable.

## Installation

### Using pip

Install Visual-dialog using `pip` (The lib is not yet available on **pypi**):

```sh
python3 -m pip install git+git://github.com/Tim-ats-d/Visual-dialog
```
or update lib to the latest version:

```sh
python3 -m pip install git+git://github.com/Tim-ats-d/Visual-dialog --upgrade
```

### From source

```sh
git clone https://github.com/Tim-ats-d/Visual-dialog.git
cd Visual-dialog
pip install .
```

## Requirements

### Curses

**Visual-dialog** works with `curses` Python module. It is available in the standard **Python** library on **UNIX** but it doesn’t work out-of-the-box on **Windows**.

See [this explanations](https://www.devdungeon.com/content/curses-windows-python) to install `curses` on **Windows** (untested).

### Other requirements
* [**Python 3.7**](https://www.python.org/downloads/) or more.
* [**Sphinx**](https://www.sphinx-doc.org/en/master/usage/installation.html) to generate the documentation of library.
* [**sphinx-rtd-theme**](https://pypi.org/project/sphinx-rtd-theme/) used as documentation theme.

## Quick-start

### Hello world with **Visual-dialog**

```python3
import curses

from visualdialog import DialogBox


def main(stdscr):
    curses.curs_set(False)

    textbox = DialogBox(0, 0,
                        35, 6,
                        title="Demo")
    textbox.char_by_char(stdscr,
                         "Hello world")


curses.wrapper(main)
```

### Examples

Other various examples showing the capabilities of **Visual-dialog** can be found in  [examples](examples/).

## Documentation

Visualdialog's documentation is automatically generated from the source code by **Sphinx**.
To build it in **HTML** on **GNU/Linux** or **MacOS**:
```sh
git clone https://github.com/Tim-ats-d/Visual-dialog.git
cd Visual-dialog/doc
make html
```
Or on **Windows** with **Git Bash**:
```sh
git clone https://github.com/Tim-ats-d/Visual-dialog.git
cd Visual-dialog/doc
./make.bat html
```

Once generated, the result will be in the `doc/build/html/` folder.
You can also generate documentation in **Latex**, **Texinfo** or **man-pages**.

## Contributing

We would love for you to contribute to improve **Visual-dialog**.

Take a look at our [contributing guide](CONTRIBUTING.md) to get started.
You can also help by reporting **bugs**.

## License

Distributed under the **GPL-2.0 License** . See [license](LICENSE) for more information.


## Acknowledgements

Thanks to all those who contributed to **Visual-dialog** !
