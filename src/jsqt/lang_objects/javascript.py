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
import cStringIO
from jsqt import DuckTypedList,DuckTypedDict

class Base(object):
    def __str__(self):
        retval = StringIO.StringIO()
        self.to_stream(retval)
        return retval.getvalue()

    def to_stream(self, os=sys.stdout):
        raise Exception("Please inherit and override")


class Comment(Base):
    def __init__(self, comment):
        self.__comment=comment.replace("*/", "*_/")
            
    def to_stream(self, os=sys.stdout):
        os.write(" /* %s */ " % self.__comment)

class String(Base):
    def __init__(self, string):
        self.__string = string
        
    def to_stream(self, os=sys.stdout):
        os.write('"')
        os.write(self.__string)
        os.write('"')

class Assignment(Base):
    def __init__(self, left=None, right=None):
        self.__left = left
        self.__right = right

    def set_left(self, left):
        self.__left = left

    def set_right(self, right):
        self.__right = right
        
    def to_stream(self, os=sys.stdout):
        self.__left.to_stream(os)
        os.write("=")
        self.__right.to_stream(os)

class Instantiation(Base):
    def __init__(self, what):
        self.__what = what

    def to_stream(self, os=sys.stdout):
        os.write("new %s();" % self.__what)

class ObjectReference(Base):
    def __init__(self, object_name):
        if len(object_name) ==0:
            raise Exception("Empty object name not allowed")
        self.__object_name = object_name

    def to_stream(self, os=sys.stdout):
        os.write(self.__object_name)

class Object(Base):
    def __init__(self):
        self.__members = DuckTypedDict(['to_stream'])

    def set_member(self,key,value):
        self.__members[key]=value

    def del_member(self,key):
        del self.__members[key]
        
    def to_stream(self, os=sys.stdout):
        os.write("{")
        i=0
        for k in self.__members.keys():
            os.write(k)
            os.write(":")
            self.__members[k].to_stream(os)
            if i != len(self.__members) -1:
                os.write(",")
            i+=1

        os.write("}")

class FunctionCall(Base):
    def __init__(self, function_name, arguments=[]):
        self.__function_name = function_name
        self.__arguments = DuckTypedList(['to_stream'],arguments)

    def add_argument(self, argument):
        self.__arguments.append(argument)

    def to_stream(self, os=sys.stdout):
        os.write(self.__function_name)
        os.write("(")
        for i in range(len(self.__arguments)):
            self.__arguments[i].to_stream(os)
            if i != len(self.__arguments) -1:
                os.write(",")

        os.write(");")

class FunctionDefinition(Base):
    def __init__(self, function_name, arguments=None, source=None):

        self.__function_name = function_name
        if arguments == None:
            self.__arguments = DuckTypedList(['to_stream'])
        else:
            self.__arguments = arguments

        if source == None:
            self.__source=DuckTypedList(['to_stream'])
        else:
            self.__source = source

    def add_argument(self, argument):
        self.__arguments.append(argument)

    def add_statement(self, argument):
        self.__source.append(argument)

    def to_stream(self, os=sys.stdout):
        os.write("function")
        if len(self.__function_name) > 0:
            os.write(" ")
            os.write(self.__function_name)
            
        os.write("(")
        for i in range(len(self.__arguments)):
            self.__arguments[i].to_stream(os)
            if i != len(self.__arguments) -1:
                os.write(",")
        os.write(")")

        os.write("{")
        for st in self.__source:
            st.to_stream(os)
        os.write("}")


