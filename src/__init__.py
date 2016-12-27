"""Trigger various errors in linters."""
import sys
from os import path, getenv


def pydocstyle_issue():
    """A function with a pydocstyle issue"""
    path


def pep8_issue(hello , world):
    """A function with a PEP8 spacing issue."""
    getenv


def pyflake_issue():
    """A function with an unused variable."""
    a = sys


def mccabe_issue():
    """A function with a high McCabe complexity."""
    while True:
        pass
    while True:
        pass
    while True:
        pass
    while True:
        pass
    while True:
        pass
    while True:
        pass
