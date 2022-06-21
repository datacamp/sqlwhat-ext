> :warning: **This repo has outdated tokens in its travisci config**
> To make new releases for this project it needs to be moved to circleci
 
 
sqlwhat-ext
===========

[![Build Status](https://travis-ci.org/datacamp/sqlwhat-ext.svg?branch=master)](https://travis-ci.org/datacamp/sqlwhat-ext)
[![codecov](https://codecov.io/gh/datacamp/sqlwhat-ext/branch/master/graph/badge.svg)](https://codecov.io/gh/datacamp/sqlwhat-ext)
[![PyPI version](https://badge.fury.io/py/sqlwhat-ext.svg)](https://badge.fury.io/py/sqlwhat-ext)
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fdatacamp%2Fsqlwhat-ext.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Fdatacamp%2Fsqlwhat-ext?ref=badge_shield)

Extensions (high-level SCTs) for sqlwhat.

[Documentation here](http://sqlwhat-ext.readthedocs.io/).

Including in a DataCamp course
------------------------------

In the course's `requirements.sh`, add

```
# replace 0.0.1 with the appropriate release version
pip3 install --no-deps sqlwhat-ext==0.0.1
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
pytest tests

# can also do: python -m pytest tests
```


## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fdatacamp%2Fsqlwhat-ext.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fdatacamp%2Fsqlwhat-ext?ref=badge_large)
