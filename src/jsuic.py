#!/usr/bin/python -tt
# encoding: utf8

#
# This file is part of JsQt.
#
# Copyright (C) 2009 Arskom Ltd. www.arskom.com.tr
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

import sys

import jsqt
import logging

for i in range(len(sys.argv)):
    if sys.argv[i] == "-v":
        jsqt.loglevel = 1
        break

from jsqt import JsPp
from jsqt.parser import UiParser

def usage():
    sys.stderr.write(jsqt.header_string)
    print """
Usage: %s [options] <.ui file>"
    -o <file>                 place the output into <file>
    -v                        enable verbose output
    """ % sys.argv[0]
    #-tr <func>                use func() for i18n
    sys.exit(1)


def main(argv):
    input_file_name = "-"
    output_file_name = "-"
    i18n_function = ""

    for i in range(1,len(argv)):
        if argv[i] == "-o":
            if output_file_name == "-":
                try:
                    output_file_name = argv[i+1]
                except IndexError:
                    usage()
            else:
                usage()
                
            i+=1
  
        elif argv[i] == "-h":
            usage()

        elif argv[i] == "-v":
            pass

        elif argv[i] == "-tr":
            try:
                i18n_function = argv[i+1]
            except IndexError:
                usage()
            i+=1

        elif argv[i][0] == "-":
            usage()

        else:
            if input_file_name == "-":
                input_file_name = argv[i]
            else:
                usage()

    if input_file_name == "-":
        input_file = sys.stdin
    else:
        input_file = open(input_file_name, 'r')


    parser = UiParser()
    parser.parse(input_file)
    compiled_object = parser.clazz.compile('javascript-qooxdoo-0.8.3')

    if output_file_name == "-":
        output_file = sys.stdout
    else:
        output_file = open(output_file_name, 'w')

    compiled_object.to_stream(JsPp(output_file))
    output_file.write(";\n") # FIXME: Hack!

    if output_file_name != "-":
        output_file.close()

if __name__ == "__main__":
    main(sys.argv)

