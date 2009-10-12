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
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#

import sys
from jsqt import DuckTypedList, DuckTypedDict

from jsqt.lang_objects import javascript

class Compilable(object):
    def set_parent(self, parent):
        self.parent = parent
        #print "\t == parent: ", parent

class SinglePartCompilable(Compilable):
    """
    Objects that can be compiled into one language element
    """

    def compile(self, dialect):
        """
        Pure virtual method for invocation of the compilation task

        dialect -- a string representing the dialect of the output

        Returns the compiled language fragment

        """

        raise Exception("Please override for class '%s.%s'" % (self.__module__,self.__class__.__name__))

class MultiPartCompilable(Compilable):
    """
    Objects that require modifications to multiple parts of the object.
    """


    def compile(self, dialect, ret=None):
        """
        Pure virtual method for invocation of the compilation task

        dialect -- a string representing the dialect of the output
        ret -- an optional ClassDefinition object. If it's not
            supplied, it's created as a member and passed to the
            recursive invocations.

        Returns nothing
        
        """

        raise Exception("Please override for class '%s.%s'" % (self.__module__,self.__class__.__name__))

class ObjectReference(SinglePartCompilable):
    def __init__(self, object_name):
        if len(object_name) ==0:
            raise Exception("Empty object name not allowed")
        self.__object_name = object_name

    def compile(self, dialect):
        return javascript.ObjectReference(self.__object_name)

class Instantiation(object):
    def __init__(self, class_name):
        if len(class_name) ==0:
            raise Exception("Empty class name not allowed")
        self.__class_name = class_name

    def compile(self, dialect):
        return javascript.Instantiation(self.__class_name)

class Comment(SinglePartCompilable):
    def __init__(self, comment):
        SinglePartCompilable.__init__(self)

        if not isinstance(comment,str):
            raise Exception("Comments only accept strings")
        self.__comment = comment

    def compile(self, dialect):
        return javascript.Comment(self.__comment)

class Assignment(SinglePartCompilable):
    def __init__(self, left=None, right=None):
        self.__left = left
        self.__right = right

    def set_left(self, left):
        self.__left = left

    def set_right(self, right):
        self.__right = right

    def compile(self, dialect):
        return javascript.Assignment(self.__left.compile(dialect),
                                     self.__right.compile(dialect))

class FunctionCall(object):
    def __init__(self, function_name, arguments=[]):
        self.__function_name = function_name
        self.__arguments = DuckTypedList(['compile'],arguments)

    def add_argument(self, argument):
        self.__arguments.append(argument)

    def compile(self, dialect):
        return javascript.FunctionCall(self.__function_name, [a.compile(dialect) for a in self.__arguments])


class FunctionDefinition(SinglePartCompilable):
    def __init__(self, name):
        SinglePartCompilable.__init__(self)
        
        self._source = DuckTypedList(['compile'])
        self.name = name

    def add_statement(self, st):
        self._source.append(st)

    def insert_statement(self, pos, st):
        self._source.insert(pos, st)

    def compile(self, dialect):
        retval = javascript.FunctionDefinition(self.name)
        for st in self.source:
            retval.add_statement(st.compile(dialect))

        return retval

class ConstructorDefinition(FunctionDefinition):
    def __init__(self,class_name):
        FunctionDefinition.__init__(self,class_name)

    def compile(self, dialect):
        retval = javascript.FunctionDefinition("")
        for st in self._source:
            retval.add_statement(st.compile(dialect))

        return retval

class DestructorDefinition(FunctionDefinition):
    def __init__(self,class_name):
        FunctionDefinition.__init__(self,class_name)

    def compile(self, dialect):
        retval = javascript.FunctionDefinition("")
        for st in self._source:
            retval.add_statement(st.compile(dialect))

        return retval

class ClassDefinition(SinglePartCompilable):
    def __init__(self,name):
        SinglePartCompilable.__init__(self)

        if len(name) == 0:
            raise Exception("Empty name not allowed")
        self.name = name

        self.members = DuckTypedDict(['compile'])
        self.statics = DuckTypedDict(['compile'])
        self.ctor = ConstructorDefinition(self.name)
        self.dtor = DestructorDefinition(self.name)
        self.preamble = DuckTypedList(['compile'])
        self.base_class = None

    def set_member(self, key, val):
        self.members[key]=val
        val.set_parent(self)

    def get_member(self, key, val, default=None):
        return self.__elts['members'].get(key, default)

    def compile(self, dialect, ret=None):
        lang = javascript.FunctionCall("qx.Class.define")
        lang.add_argument(javascript.String(self.name))

        if self.base_class == None:
            base_class = javascript.ObjectReference('qx.core.Object')
        else:
            base_class = self.base_class

        class_members = javascript.Object()
        for k,v in self.members.items():
            if isinstance(v, MultiPartCompilable): # FIXME!
                v.compile(dialect,self)

        for k,v in self.members.items():
            if isinstance(v, SinglePartCompilable): # FIXME!
                class_members.set_member(k,v.compile(dialect))

        st = FunctionCall('this.base')
        st.add_argument(ObjectReference('arguments'))
        self.ctor.insert_statement(0,st)

        properties = javascript.Object()
        widget_property = javascript.Object()
        widget_property.set_member("check", javascript.String('qx.ui.Layout.Composite'))
        properties.set_member("widget", widget_property)

        class_dict = javascript.Object()
        class_dict.set_member("members", class_members)
        class_dict.set_member("extend", base_class)
        class_dict.set_member("construct", self.ctor.compile(dialect))
        class_dict.set_member("destruct", self.dtor.compile(dialect))
        class_dict.set_member("properties", properties)

        lang.add_argument(class_dict)

        return lang
        

