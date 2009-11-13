#!/bin/env python
# encoding: utf-8

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

    description = "A tool to compile Qt Designer's .ui files to qooxdoo code.",
    long_description = """
JsQt is a tool to compile Qt Designer's .ui files to javascript code, 
which is targeted to work with the Qooxdoo framework.
""",

    url = 'http://jsqt.org',
    license = 'GPLv2',
    platforms = ['Linux','Mac OSX','Windows 7/Vista/XP/2000/NT','Windows 95/98/ME']
)

