
# Visual-dialog

<p align="center">
  <img width="300" src="https://user-images.githubusercontent.com/59396366/113866239-5f5d0480-97ad-11eb-879f-fa7d4098b689.png" alt="Visual-dialog">
  <br>
  A library to make easier dialog box in a terminal.
</p>

## Features

📃 Automatic text scrolling.

🔖 Text coloring and formatting.

⚙️ Hackable and configurable.

⚠️ This library is still under development. API can change.

## Installation

### Using pip

Install Visual-dialog using `pip` (The lib is not yet available on **pypi**):

```sh
pip install git+git://github.com/Tim-ats-d/Visual-dialog
```
or update lib to the latest version:

```sh
pip install git+git://github.com/Tim-ats-d/Visual-dialog --upgrade
```

### From source

```sh
git clone https://github.com/Tim-ats-d/Visual-dialog.git
cd Visual-dialog
pip install .
```

## Requirements

### Python version

* [**Python 3.8**](https://www.python.org/downloads/) or more.

### Curses

**Visual-dialog** works with `curses` Python module. It is available in the standard **Python** library on **UNIX** but it doesn’t work out-of-the-box on **Windows**.

To install `curses` on **Windows**, you need `windows-curses` module:

```sh
pip install curses-windows
```

### To build the documentation

* [**Sphinx**](https://www.sphinx-doc.org/en/master/usage/installation.html) to generate the documentation of library.
* [**sphinx-rtd-theme**](https://pypi.org/project/sphinx-rtd-theme/) used as documentation theme.

```sh
pip install sphinx sphinx_rtd_theme
```

## Quick-start

### Hello world with **Visual-dialog**

```python3
import curses

from visualdialog import DialogBox


x, y = 0, 0
height, width = 35, 6

def main(win):
    curses.curs_set(False)

    textbox = DialogBox(x, y,
                        height, width,
                        title="Demo")
    textbox.char_by_char(win,
                         "Hello world")


curses.wrapper(main)
```

### Examples

Other various examples showing the capabilities of **Visual-dialog** can be found in  [examples](examples/).

## Documentation

Visualdialog's documentation is automatically generated from the source code by **Sphinx**.
To build it on **GNU/Linux** or **MacOS**:
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

You can also generate the documentation in **Latex**, **Texinfo** or **man-pages**.

## Contributing

We would love for you to contribute to improve **Visual-dialog**.

For major changes, please open an issue first to discuss what you would like to change.

Take a look at our [contributing guide](CONTRIBUTING.md) to get started.
You can also help by reporting **bugs**.

## License

Distributed under the **GPL-2.0 License**. See [license](LICENSE) for more information.


## Acknowledgements

Thanks to all those who contributed to **Visual-dialog** !
