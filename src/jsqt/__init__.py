# encoding: utf8
#
# This file is part of JsQt.
#
# Copyright (C) Arskom Ltd. www.arskom.com.tr
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.
#

__version__ = '0.5.0'

import sys

copyright = "(c) Arskom Ltd."
header_string = """JsQt %s
%s
""" % (__version__, copyright)

loglevel = 0

def debug_print(*args):
    if loglevel > 0:
        for i in range(len(args)):
            sys.stderr.write(str(args[i]))
            if i != len(args)-1:
                sys.stderr.write(" ")
        sys.stderr.write("\n")

from base import *
