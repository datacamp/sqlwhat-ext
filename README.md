sqlwhat-ext
===========

[![Build Status](https://travis-ci.org/datacamp/sqlwhat-ext.svg?branch=master)](https://travis-ci.org/datacamp/sqlwhat-ext)
[![PyPI version](https://badge.fury.io/py/sqlwhat-ext.svg)](https://badge.fury.io/py/sqlwhat-ext)

extensions (high-level SCTs) for sqlwhat.

Including in a DataCamp course
------------------------------

In the course's `requirements.sh`, add

```
# replace 0.0.1 with the appropriate release version
pip3 install sqlwhat-ext==0.0.1
```

To use the extensions in an exercise's SCT, import the function you want into the SCT block of the exercise:

```
from sqlwhat_ext import check_result2

Ex() >> check_result2()
```

Deploying to PyPI
----------------------------

Follow these steps

1. Open a PR, merge into master when appropriate.
2. Once merged, increment `__version__ = 0.0.1` to reflect changes ([see semver for guidance](http://semver.org/)).
3. Create a github release labeled `vVERSION`. E.g. `v0.0.1`. (see [here](https://help.github.com/articles/creating-releases/)).


Running tests
-------------

```
pip install -r requirements.txt
# may need to uncomment line below
#pip install -e .
py.test tests
```
