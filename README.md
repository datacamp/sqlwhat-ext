sqlwhat-ext
===========

[![Build Status](https://travis-ci.org/datacamp/sqlwhat-ext.svg?branch=master)](https://travis-ci.org/datacamp/sqlwhat-ext)

extensions (high-level SCTs) for sqlwhat.

Including in a DataCamp course
------------------------------

In the course's `requirements.sh`, add

```
# replace 0.0.1 with the appropriate release version
pip3 install sqlwhat-ext==0.0.1
```

To use the extensions in an exercise's SCT, import the function you want into the SCT block of the exercise.
For example,

```
from sqlwhat_ext import check_result2

Ex() >> check_result2()
```

Running tests
-------------

```
pip install -r requirements.txt
# may need to uncomment line below
#pip install -e .
py.test tests
```
