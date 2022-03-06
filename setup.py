# Copyright 2017 Louis Paternault
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Installer"""

import codecs
import os

from setuptools import setup


def readme():
    directory = os.path.dirname(os.path.join(os.getcwd(), __file__))
    with codecs.open(
        os.path.join(directory, "README.rst"),
        encoding="utf8",
        mode="r",
        errors="replace",
    ) as file:
        return file.read()


setup(
    name="sphinxcontrib-stuffcounter",
    version="0.0.0",
    packages=["sphinxcontrib.stuffcounter"],
    install_requires=["sphinx>=1.8.0"],
    author="Louis Paternault",
    author_email="spalax@gresille.org",
    description="A sphinx extension to illustrate the `add_enumerable_node()` method.",
    url="https://framagit.org/spalax/sphinxcontrib-stuffcounter",
    project_urls={
        "Documentation": "http://sphinxcontrib-stuffcounter.readthedocs.io",
        "Source": "https://framagit.org/spalax/sphinxcontrib-stuffcounter",
        "Tracker": "https://framagit.org/spalax/sphinxcontrib-stuffcounter/issues",
    },
    license="AGPLv3 or any later version",
    keywords="sphinx stuffcounter enumerable",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Sphinx :: Extension",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Documentation :: Sphinx",
        "Topic :: Utilities",
        "DO :: NOT :: UPLOAD :: TO :: PYPI",
    ],
    long_description=readme(),
    namespace_packages=["sphinxcontrib"],
)
