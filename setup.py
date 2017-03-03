#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from setuptools import setup
from codecs import open


APP_NAME = 'legit'
APP_SCRIPT = './legit_r'
VERSION = '0.2.0'

required = [
    'clint>=0.4.1',
    'GitPython>=0.3.4',
    'six>=1.9.0'
]


settings = dict()


# Publish Helper.
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel upload')
    sys.exit()


if sys.argv[-1] == 'build_manpage':
    os.system('rst2man.py README.rst > extra/man/legit.1')
    sys.exit()

settings.update(
    name=APP_NAME,
    version=VERSION,
    description='Git for Humans.',
    long_description=open('README.rst').read(),
    author='Kenneth Reitz',
    author_email='me@kennethreitz.com',
    url='https://github.com/kennethreitz/legit',
    packages= ['legit',],
    install_requires=required,
    license='BSD',
    classifiers=(
        # 'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ),
    entry_points={
        'console_scripts': [
            'legit = legit.cli:main',
        ],
    }
)



setup(**settings)
