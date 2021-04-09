
from setuptools import find_packages, setup

from visualdialog import __author__, __doc__, __version__


setup(
    name="visualdialog",
    version=__version__,
    packages=find_packages(),
    author=__author__,
    author_email="tim.arnouts@protonmail.com",
    description=__doc__,
    long_description=open("README.md").read(),
    include_package_data=True,
    url="https://github.com/Tim-ats-d/Visual-dialog",
    requires_python=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console :: Curses",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Natural Language :: English", "Natural Language :: French",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation",
        "Topic :: Games/Entertainment :: Role-Playing",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    keywords="curses, ncurses, ui, dialogbox")
