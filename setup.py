#!/usr/bin/env python

import re
import ast
from setuptools import setup

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('sqlwhat_ext.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
	name = 'sqlwhat-ext',
	version = version,
        py_modules= ['sqlwhat_ext'],
        install_requires = ['sqlwhat>=1.11'],
        description = 'sqlwhat extensions - high level SCTs',
        author = 'Michael Chow',
        author_email = 'michael@datacamp.com',
        url = 'https://github.com/datacamp/sqlwhat-ext')
