"""Trigger various errors in linters."""


def pydocstyle_issue():
    """A function with a pydocstyle issue"""
    pass


def pep8_issue(hello , world):
    """A function with a PEP8 spacing issue."""
    pass


def pyflake_issue():
    """A function with an unused variable."""
    a = 123


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
