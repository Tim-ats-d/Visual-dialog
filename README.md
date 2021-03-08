<p align="center">
    <img width="300" src="https://user-images.githubusercontent.com/59396366/100594532-188c6900-32fa-11eb-8372-4796f53b122f.png" alt="Visual-dialog">
    <br><br>
    Library to make easier dialog box in terminal.
</p>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#documentation">Documentation</a> •
  <a href="#quick-start">Quick start</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#license">License</a>
</p>

<div align="center">
  <img src="https://user-images.githubusercontent.com/59396366/100640592-e3523c00-3336-11eb-8793-19a0543be8d0.gif" alt="Demo">
</div>

This library is still under development.
API can change.

## Features

📃 Automatic text scrolling.

🔖 Text coloring and formatting.

⚙️ Hackable and configurable .


## Installation

### Using pip

Install Visual-dialog using `pip` (The lib is not yet available on **pypy**):

```sh
python3 -m pip install git+git://github.com/Tim-ats-d/Visual-dialog
```
or update lib to the latest version:

```sh
python3 -m pip install git+git://github.com/Tim-ats-d/Visual-dialog --upgrade
```

### Requirements
* **Python 3.7** or more.
* [**Sphinx**](https://www.sphinx-doc.org/en/master/usage/installation.html) to generate the documentation of library.
* [`curses`](https://docs.python.org/3/library/curses.html) Python module (available in standard library of Python on **UNIX**).
* Knowledge of [`curses`](https://docs.python.org/3/library/curses.html) librairie.

## Quick-start

Coming soon.

Read these [examples](examples/).

## Documentation

Visualdialog's documentation is automatically generated from the source code by **Sphinx**.
To build it on **GNU/Linux** or **MacOS**:
```sh
git clone https://github.com/Tim-ats-d/Visual-dialog.git
cd Visual-dialog
make html
```
Or on **Windows** with **Git Bash**:
```sh
git clone https://github.com/Tim-ats-d/Visual-dialog.git
cd Visual-dialog
./make.bat html
```

Once generated, the result will be in the `build/html/` folder.

## Contributing

We would love for you to contribute to improve **Visual-dialog**.

Take a look at our [contributing guide](CONTRIBUTING.md) to get started.
You can also help by reporting bugs.

## License

Distributed under the **GPL-2.0 License** . See [License](LICENSE) for more information.


## Acknowledgements

Thanks to all those who contributed to **Visual-dialog** !
