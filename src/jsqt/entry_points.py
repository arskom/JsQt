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

import sys
import os
import stat

import jsqt

from jsqt.base import JsPp
from jsqt.base import NoTrailingSpace
from jsqt.parser import UiParser


def walktree(top = ".", depthfirst = False):
    names = os.listdir(top)
    if not depthfirst:
        yield top, names

    for name in names:
        try:
            st = os.lstat(os.path.join(top, name))
        except os.error:
            continue

        if stat.S_ISDIR(st.st_mode):
            for (newtop, children) in walktree (os.path.join(top, name), depthfirst):
                yield newtop, children

    if depthfirst:
        yield top, names

def usage_jsqt():
    print "Usage:", sys.argv[0], "xml_input_path js_output_path root_namespace [base_class]"

def compile(ui_file_name, js_file_name, root_namespace, base_class, dialect):
    print ui_file_name

    if js_file_name.rfind(root_namespace) == -1:
        raise Exception("root_namespace '%s' not found in class name '%s'" % (
                root_namespace, js_file_name))

    object_name= js_file_name[js_file_name.rfind(root_namespace):].replace(
                                    os.sep*2, os.sep).replace(os.sep, ".")[0:-3]
    parser = UiParser(object_name)
    parser.parse(ui_file_name, ui_file_name)
    parser.clazz.base_class = base_class

    jsqt.debug_print("")
    jsqt.debug_print("\tcompiling....")
    jsqt.debug_print("\t"+"="*20)
    compiled_object = parser.clazz.compile(dialect)

    f=open(js_file_name, 'w')
    for p in parser.clazz.preamble:
        p.compile(dialect).to_stream(f)
    compiled_object.to_stream(JsPp(NoTrailingSpace(f)))
    f.write(";\n") # FIXME: Hack!
    f.close()

def main_jsqt():
    argv = sys.argv

    print jsqt.header_string
    print "cwd:",os.getcwd()

    if len(argv) >= 4:
        if os.path.isdir(argv[1]):
            if not argv[1].endswith(os.sep):
                argv[1]+=os.sep
            if not argv[2].endswith(os.sep):
                argv[2]+=os.sep

            for (basepath, children) in walktree(argv[1]):
                for c in children:
                    if c[-3:] == '.ui':
                        ui_file_name=os.path.join(basepath, c)
                        js_file_name=ui_file_name.replace(argv[1],argv[2],1)[0:-3]+".js"
                        root_namespace = argv[3]

                        base_class = None
                        if len(argv) == 5:
                            base_class = argv[4]

                        try:
                            os.makedirs(os.path.dirname(js_file_name))
                        except OSError,e:
                            pass

                        compile(ui_file_name, js_file_name, root_namespace, base_class, 'javascript-qooxdoo-1.1')
        else:
            usage_jsqt()
            print '       First argument must be a directory!'
            print

    else:
        usage_jsqt()
        print

def usage_jsuic():
    sys.stderr.write(jsqt.header_string)
    print """
Usage: %s [options] <.ui file>"
    -o <file>                 place the output into <file>
    -v                        enable verbose output
    -b                        specify the base class (default: qx.core.Object)
    """ % sys.argv[0]
    #-tr <func>                use func() for i18n
    sys.exit(1)

def main_jsuic():
    argv = sys.argv
    input_file_name = "-"
    output_file_name = "-"
    base_class = None

    for i in range(len(sys.argv)):
        if sys.argv[i] == "-v":
            jsqt.loglevel = 1
            break

    for i in range(1,len(argv)):
        if argv[i] == "-o":
            if output_file_name == "-":
                try:
                    output_file_name = argv[i+1]
                except IndexError:
                    usage_jsuic()
            else:
                usage_jsuic()

            i+=1
  
        elif argv[i] == "-h":
            usage_jsuic()

        elif argv[i] == "-b":
            base_class = argv[i+1]

        elif argv[i][0] == "-":
            usage_jsuic()

        else:
            if input_file_name == "-":
                input_file_name = argv[i]
            else:
                usage_jsuic()

    if input_file_name == "-":
        input_file = sys.stdin
    else:
        input_file = open(input_file_name, 'r')


    parser = UiParser()
    parser.parse(input_file, input_file_name)
    parser.clazz.base_class = base_class
    compiled_object = parser.clazz.compile('javascript-qooxdoo-1.6')

    if output_file_name == "-":
        output_file = sys.stdout
    else:
        output_file = open(output_file_name, 'w')

    compiled_object.to_stream(JsPp(NoTrailingSpace(output_file)))
    output_file.write(";\n") # FIXME: Hack!

    if output_file_name != "-":
        output_file.close()
