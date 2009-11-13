#!/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Burak Arslan"
__date__  = "$Nov 13, 2009 10:38:45 PM$"

from setuptools import setup,find_packages
import sys
sys.path.append("src")
import jsqt
setup(
    name = 'jsqt',
    version = jsqt.version,
    packages = find_packages('src'),
    package_dir = {'':'src'},

    install_requires=['lxml>=2.2.2'],
    entry_points = {
        'console_scripts': [
            'jsqt=jsqt.entry_points:main_jsqt',
            'jsuic=jsqt.entry_points:main_jsuic',
        ],
    },

    author = 'Burak Arslan',
    author_email = 'burak-jsqt@arskom.com.tr',

    summary = "A compiler that translates Qt Designer's .ui files into Qooxdoo code.",
    url = 'http://jsqt.org',
    license = 'GPLv2',
)

