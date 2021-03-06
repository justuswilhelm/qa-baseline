# QA Baseline

A small example on how to compare the current amount of syntax issues in a
project against a known baseline. This uses flake8 to drive five different
linters:

- isort
- mccabe
- pep8
- pydocstyle
- pyflakes

## Quickstart

```bash
pyvenv env  # create virtual environment
source env/bin/activate  # enter virtual environment
pip3 install -r requirements.txt  # install linter tools
script/test # run tests
```

will output 5 issues from 5 different linters. The linters in this example are
(in order) _isort_, _pydocstyle_, _pep8_, _pyflakes_, and _mccabe_.

```
INFO:root:flake8:
---
./src/__init__.py:3:1: I001 isort found an import in the wrong position
./src/__init__.py:6:1: D400 First line should end with a period
./src/__init__.py:11:21: E203 whitespace before ','
./src/__init__.py:18:5: F841 local variable 'a' is assigned to but never used
./src/__init__.py:21:1: C901 'mccabe_issue' is too complex (7)
---
```

This can also be seen on
[CircleCI](https://circleci.com/gh/justuswilhelm/qa-baseline/7)

Running

```bash
echo "print()" >> src/__init__.py # append faulty code
# run tests again
script/test
```

will not exit cleanly with

```
INFO:root:flake8:
---
./src/__init__.py:3:1: I001 isort found an import in the wrong position
./src/__init__.py:6:1: D400 First line should end with a period
./src/__init__.py:11:21: E203 whitespace before ','
./src/__init__.py:18:5: F841 local variable 'a' is assigned to but never used
./src/__init__.py:21:1: C901 'mccabe_issue' is too complex (7)
./src/__init__.py:35:1: E305 expected 2 blank lines after class or function definition, found 0
---
Traceback (most recent call last):
  File "script/test", line 36, in <module>
    main()
  File "script/test", line 32, in main
    baseline, current))
AssertionError: More errors than acceptable. Baseline 5, current 6
```

This can also be seen on
[CircleCI](https://circleci.com/gh/justuswilhelm/qa-baseline/8)

The baseline is set in the `setup.cfg` file in the `[qa]` section. It is
currently set to `5` and `script/test` will exit without an error if the same
amount of issues is detected in subsequent tests. Should the amount of issues
increase, `script/test` will exit with an error.

Therefore, project maintainers can verify that the current code quality will
never worsen. If used in a Continuous Integration environment, the
`baseline` value can be gradually decreased as code cleanup happens.

## Requirements

- Python >= 3.3

## Tools used to test code quality

- [flake8-docstrings](https://gitlab.com/pycqa/flake8-docstrings), to use pydocstyle from flake8
- [isort](https://github.com/timothycrosley/isort) to ensure imports are sorted correctly
- [flake8-isort](https://github.com/gforcada/flake8-isort), to use isort from flake8
- [McCabe](https://github.com/PyCQA/mccabe), for mccabe complexity
- [pep8](http://pep8.readthedocs.io/en/release-1.7.x/), for PEP8 compliance
- [pydocstyle](http://www.pydocstyle.org), for PEP257 compliance
- [pyflakes](https://pypi.python.org/pypi/pyflakes), for pyflakes compliance

## Configuration

The amount of acceptable issues can be set in `setup.cfg` under the `[qa]`
section.

## Caveat

In order to check `src/__init__.py` using isort, the `setup.cfg` has to include
a `not_skip=__init__.py` entry for isort as it would otherwise skip any
`__init__.py` file.
