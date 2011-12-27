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

import StringIO
from jsqt import DuckTypedDict
from jsqt import DuckTypedList

class Base(object):
    def __str__(self):
        retval = StringIO.StringIO()
        self.to_stream(retval)
        return retval.getvalue()

    def to_stream(self, os):
        raise NotImplementedError("Please inherit and override")

class Comment(Base):
    def __init__(self, comment):
        self.__comment=comment.replace("*/", "*_/")
            
    def to_stream(self, os):
        os.write(" /* %s */\n" % self.__comment)

class String(Base):
    def __init__(self, string):
        self.__string = string

    def to_stream(self, os):
        os.write('"')
        os.write(self.__string
                .replace("\\", "\\\\")
                .replace("\r","")
                .replace("\n","\\\n")
                .replace('"','\\"')
            )
        os.write('"')

class Concatenation(Base):
    def __init__(self, sub_strings):
        self.__sub_strings = sub_strings

    def to_stream(self, os):
        raise Exception("Not implemented") # FIXME
        for i in len(range(self.__sub_strings)):
            self.__sub_strings[i].to_stream(os)

        return javascript.Concatenation(compiled_sub_strings)

class Assignment(Base):
    def __init__(self, left=None, right=None):
        self.__left = left
        self.__right = right

    def set_left(self, left):
        self.__left = left

    def set_right(self, right):
        self.__right = right
        
    def to_stream(self, os):
        self.__left.to_stream(os)
        if self.__right:
            os.write("=")
            self.__right.to_stream(os)

class VariableDeclaration(Assignment):
    def __init__(self, left, right=None):
        Assignment.__init__(self, ObjectReference(left), right)

    def to_stream(self, os):
        os.write("var ")
        Assignment.to_stream(self, os)

class Return(Base):
    def __init__(self, what):
        Base.__init__(self)

        self.what = what

    def to_stream(self, os):
        os.write("return %s" % self.what)

class Instantiation(Base):
    def __init__(self, class_name, init_arguments):
        self.__class_name = class_name
        self.__args = init_arguments

    def to_stream(self, os):
        os.write("new ")
        fc = FunctionCall(self.__class_name,self.__args)
        fc.to_stream(os)

class ObjectReference(Base):
    def __init__(self, object_name):
        if len(object_name) == 0:
            raise Exception("Empty object name not allowed")
        self.__object_name = object_name

    def to_stream(self, os):
        os.write(self.__object_name)

class DecimalInteger(Base):
    def __init__(self, value):
        self.__value=value

    def to_stream(self, os):
        os.write(str(self.__value))

class Boolean(Base):
    def __init__(self, value):
        self.__value=value

    def to_stream(self, os):
        if self.__value:
            os.write("true")
        else:
            os.write("false")

class Null(Base):
    def to_stream(self, os):
        os.write("null")

class Object(Base):
    def __init__(self):
        self.__members = DuckTypedDict(['to_stream'])

    def set_member(self,key,value):
        self.__members[key]=value

    def del_member(self,key):
        del self.__members[key]

    def to_stream(self, os):
        os.write("{")
        i=0
        keys = self.__members.keys()
        keys.sort()
        for k in keys:
            os.write(k)
            os.write(":")
            self.__members[k].to_stream(os)
            if i != len(self.__members) -1:
                os.write(",")
            i+=1

        os.write("}")

class Array(Base):
    def __init__(self):
        self.__members = DuckTypedList(['to_stream'])

    def append(self, value):
        self.__members.append(value)

    def del_member(self,key):
        del self.__members[key]

    def to_stream(self, os):
        os.write("[")
        i=0
        for v in self.__members:
            v.to_stream(os)
            if i != len(self.__members) -1:
                os.write(",")
            i+=1

        os.write("]")

class FunctionCall(Base):
    def __init__(self, function_name, arguments=[]):
        self.__function_name = function_name
        self.__arguments = DuckTypedList(['to_stream'],arguments)

    def add_argument(self, argument):
        self.__arguments.append(argument)

    def to_stream(self, os):
        os.write(self.__function_name)
        os.write("(")
        for i in range(len(self.__arguments)):
            self.__arguments[i].to_stream(os)
            if i != len(self.__arguments) -1:
                os.write(",")

        os.write(")")

class FunctionDefinition(Base):
    def __init__(self, function_name, arguments=[], source=[]):
        self.__function_name = function_name
        self.__arguments = arguments
        self.__source=DuckTypedList(['to_stream'], source)

    def add_argument(self, argument):
        self.__arguments.append(argument)

    def add_statement(self, statement):
        self.__source.append(statement)

    def to_stream(self, os):
        os.write("function")
        if len(self.__function_name) > 0:
            os.write(" ")
            os.write(self.__function_name)
            
        os.write("(")
        for i in range(len(self.__arguments)):
            os.write(self.__arguments[i])
            if i != len(self.__arguments) -1:
                os.write(",")
        os.write(")")

        os.write("{")
        for st in self.__source:
            st.to_stream(os)
            if not isinstance(st, Comment):
                os.write(';')
        os.write("}")
