
from setuptools import find_packages, setup

from visualdialog import __author__, __version__


setup(
    name="visualdialog",
    version=__version__,
    packages=find_packages(),
    author=__author__,
    author_email="tim.arnouts@protonmail.com",
    description="A library to make easier dialog box in terminal.",
    long_description=open("README.md", encoding="utf-8").read(),
    include_package_data=True,
    url="https://github.com/Tim-ats-d/Visual-dialog",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console :: Curses",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Natural Language :: English", "Natural Language :: French",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation",
        "Topic :: Games/Entertainment :: Role-Playing",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    keywords="curses, ncurses, ui, dialogbox")
