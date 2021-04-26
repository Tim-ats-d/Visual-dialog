
from setuptools import find_packages, setup

from visualdialog import __author__, __doc__, __version__


setup(
    name="visualdialog",
    version=__version__,
    packages=find_packages(),
    author=__author__,
    author_email="tim.arnouts@protonmail.com",
    description=__doc__,
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    install_requires=["windows-curses; platform_system=='Windows'"],
    extras_require={"doc": ["sphinx", "sphinx-rtd-theme"]},
    include_package_data=True,
    url="https://github.com/Tim-ats-d/Visual-dialog",
    requires_python=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console :: Curses",
        "Intended Audience :: Developers",
        "Typing :: Typed",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Natural Language :: English", "Natural Language :: French",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation",
        "Topic :: Software Development :: User Interfaces",
        "Topic :: Games/Entertainment :: Role-Playing",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    keywords="curses, ncurses, ui, dialogbox")
