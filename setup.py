#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2012 by Łukasz Langa
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""mudmafia
   --------

   Managing extortion."""

import os
import sys
from setuptools import setup, find_packages

reload(sys)
sys.setdefaultencoding('utf8')

ld_file = open(os.path.join(os.path.dirname(__file__), 'README.rst'))
try:
    long_description = ld_file.read()
finally:
    ld_file.close()
# We let it die a horrible tracebacking death if reading the file fails.
# We couldn't sensibly recover anyway: we need the long description.

setup (
    name = 'mudmafia',
    version = '0.9',
    author = 'Łukasz Langa',
    author_email = 'lukasz@langa.pl',
    description = "Managing extortion.",
    long_description = long_description,
    keywords = '',
    platforms = ['any'],
    license = 'MIT',
    package_dir = {'': 'src/mudmafia'},
    include_package_data = True,
    zip_safe = False, # if only because of the readme file
    install_requires = [
        'django_evolution',
        'gunicorn',
        'lck.django>=0.7.5',
        'pytz',
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ]
)
