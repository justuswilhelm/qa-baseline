# QA Baseline

A small example on how to compare the current amount of syntax issues in a
project against a known baseline. This uses a flake8 to drive four different
linters:

- pydocstyle
- pyflakes
- mccabe
- pep8

## Quickstart

```bash
pyvenv env  # create virtual environment
source env/bin/activate  # enter virtual environment
pip3 install -r requirements.txt  # install linter tools
script/test # run tests
```

will output

```
./src/__init__.py:4:1: D400 First line should end with a period
./src/__init__.py:9:21: E203 whitespace before ','
./src/__init__.py:16:5: F841 local variable 'a' is assigned to but never used
./src/__init__.py:19:1: C901 'mccabe_issue' is too complex (7)
```

This can also be seen on [CircleCI](https://circleci.com/gh/justuswilhelm/qa-baseline/7)

But running

```bash
echo "print()" >> src/__init__.py # append faulty code
# run tests again
script/test
```

will throw an error with

```
INFO:root:flake8:
---
./src/__init__.py:4:1: D400 First line should end with a period
./src/__init__.py:9:21: E203 whitespace before ','
./src/__init__.py:16:5: F841 local variable 'a' is assigned to but never used
./src/__init__.py:19:1: C901 'mccabe_issue' is too complex (7)
./src/__init__.py:33:1: E305 expected 2 blank lines after class or function definition, found 0
---
Traceback (most recent call last):
  File "script/test", line 36, in <module>
    main()
  File "script/test", line 32, in main
    baseline, current))
AssertionError: More errors than acceptable. Baseline 4, current 5
```

This can also be seen on [CircleCI](https://circleci.com/gh/justuswilhelm/qa-baseline/8)

The baseline is set in the `setup.cfg` file in the `[qa]` section. It is
currently set to `4` and `script/test` will exit without an error if the same
amount of issues is detected in subsequent tests. Should the amount of issues
increase, `script/test` will exit with an error.

Therefore, project maintainers can verify that the current code quality will
never worsen. If used in a Continuous Integration environment, the
`baseline` value can be gradually decreased as code cleanup happens.

## Requirements

- Python >= 3.3

## Tools used to test code quality

- [McCabe](https://github.com/PyCQA/mccabe), for mccabe complexity
- [pyflakes](https://pypi.python.org/pypi/pyflakes), for pyflakes compliance
- [pydocstyle](http://www.pydocstyle.org), for PEP257 compliance
- [pep8](http://pep8.readthedocs.io/en/release-1.7.x/), for PEP8 compliance
- [flake8-docstrings](https://gitlab.com/pycqa/flake8-docstrings), to use pydocstyle from flake8

## Configuration

The amount of acceptable issues can be set in `setup.cfg` under the `[qa]`
section.
