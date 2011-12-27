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

from jsqt import DuckTypedList, DuckTypedDict

from jsqt import js

class Compilable(object):
    def set_parent(self, parent):
        self.parent = parent

class SinglePartCompilable(Compilable):
    """Objects that can be compiled into one language element"""

    def compile(self, dialect):
        """Pure virtual method for invocation of the compilation task

        dialect -- a string representing the dialect of the output

        Returns the compiled language fragment
        """

        raise NotImplementedError("Please override for class '%s.%s'" % (self.__module__,
                                                       self.__class__.__name__))

class MultiPartCompilable(Compilable):
    """Objects that require modifications to multiple parts of the object."""


    def compile(self, dialect, ret=None):
        """Pure virtual method for invocation of the compilation task

        dialect -- a string representing the dialect of the output
        ret -- an optional ClassDefinition object. If it's not
            supplied, it's created as a member and passed to the
            recursive invocations.

        Returns nothing
        """

        raise NotImplementedError("Please override for class '%s.%s'" %
                                      (self.__module__,self.__class__.__name__))

class DecimalInteger(SinglePartCompilable):
    def __init__(self, value):
        SinglePartCompilable.__init__(self)

        self.value = int(value)

    @staticmethod
    def from_elt(elt):
        return DecimalInteger(int(elt.text))

    def __eq__(self, other):
        if isinstance(other, int):
            return self.value == other
        else:
            return id(self) == id(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return "<il.DecimalInteger(%d)>" % self.value

    def compile(self, dialect):
        return js.primitive.DecimalInteger(self.value)

class Boolean(SinglePartCompilable):
    def __init__(self, value):
        SinglePartCompilable.__init__(self)

        self.__value = bool(value)

    @staticmethod
    def from_elt(elt):
        return Boolean(elt.text.lower() == "true")

    def __eq__(self, other):
        if isinstance(other, bool):
            return self.__value == other
        else:
            return id(self) == id(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return "<il.Boolean(%d)>" % self.__value

    def compile(self, dialect):
        return js.primitive.Boolean(self.__value)

class Enum(SinglePartCompilable):
    """You need to sublass this and add mapping values."""
    value_map = None
    
    def __init__(self, value):
        SinglePartCompilable.__init__(self)

        self.__value = self.value_map[value]

    def get_value(self):
        return self.__value

    @classmethod
    def from_elt(cls, elt):
        return cls(elt.text)

    def __eq__(self, other):
        if isinstance(other, str) or isinstance(other, unicode):
            return self.__value == other
        else:
            return id(self) == id(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return "<il.Enum(%r)>" % self.__value

    def compile(self, dialect):
        return self.__value.compile(dialect)

class Null(SinglePartCompilable):
    def __init__(self):
        SinglePartCompilable.__init__(self)

    def __eq__(self, other):
        if isinstance(other, Null):
            return True
        else:
            return (other is None)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return "<il.None()>"

    def compile(self, dialect):
        return js.primitive.Null()

class ObjectReference(SinglePartCompilable):
    def __init__(self, object_name):
        SinglePartCompilable.__init__(self)

        if len(object_name) ==0:
            raise Exception("Empty object name not allowed")
        self.__object_name = object_name

    def __repr__(self):
        return "<il.ObjectReference(%s)>" % self.__object_name
    
    def compile(self, dialect):
        return js.primitive.ObjectReference(self.__object_name)

class String(SinglePartCompilable):
    def __init__(self, string):
        SinglePartCompilable.__init__(self)

        self._string = str(string)

    @staticmethod
    def from_elt(elt):
        return String(elt.text)

    def __eq__(self, other):
        if isinstance(other, str) or isinstance(other, unicode):
            return self._string == other
        else:
            return id(self) == id(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def compile(self, dialect):
        return js.primitive.String(self._string.replace("\n","\\n"))

class TranslatableString(String):
    def __init__(self, string):
        SinglePartCompilable.__init__(self)

        self._string=unicode(string)

    def __repr__(self):
        return "<il.TranslatableString('%s')>" % self._string

    @staticmethod
    def from_elt(elt):
        if elt.attrib.get('notr', None) == 'true':
            return String.from_elt(elt)
        elif elt.text is None:
            return TranslatableString("")
        else:
            return TranslatableString(elt.text)

    def compile(self, dialect):
        return js.primitive.FunctionCall("this.tr",[
                       js.primitive.String(self._string.replace("\n","\\n")) ])

class Comment(SinglePartCompilable):
    def __init__(self, comment):
        SinglePartCompilable.__init__(self)

        self.__comment = str(comment)

    def compile(self, dialect):
        return js.primitive.Comment(self.__comment)

class Instantiation(SinglePartCompilable):
    def __init__(self, class_name, init_arguments=[]):
        SinglePartCompilable.__init__(self)

        if len(class_name) ==0:
            raise Exception("Empty class name not allowed")
        self.__class_name = class_name
        self.args = DuckTypedList(['compile'],init_arguments)

    def compile(self, dialect):
        return js.primitive.Instantiation(self.__class_name,
                                      [a.compile(dialect) for a in self.args])

class Concatenation(SinglePartCompilable):
    def __init__(self, sub_strings):
        SinglePartCompilable.__init__(self)

        self.__sub_strings = sub_strings

    def compile(self, dialect):
        compiled_sub_strings = [s.compile(dialect) for s in self.__sub_strings]
        return js.primitive.Concatenation(compiled_sub_strings)

class Assignment(SinglePartCompilable):
    def __init__(self, left=None, right=None):
        SinglePartCompilable.__init__(self)

        self.left = left
        self.right = right

    def compile(self, dialect):
        return js.primitive.Assignment(self.left.compile(dialect),
                                                    self.right.compile(dialect))
class VariableDeclaration(SinglePartCompilable):
    def __init__(self, var_name, initializer=None):
        SinglePartCompilable.__init__(self)

        self.left = var_name
        self.right = initializer

    def compile(self, dialect):
        return js.primitive.VariableDeclaration(self.left, self.right.compile(dialect))

class FunctionCall(object):
    def __init__(self, function_name, arguments=[]):
        SinglePartCompilable.__init__(self)

        self.__function_name = function_name
        self.__arguments = DuckTypedList(['compile'],arguments)

    def add_argument(self, argument):
        self.__arguments.append(argument)

    def __repr__(self):
        return '<il.FunctionCall("%s", %s)>' %(self.__function_name,
                                                               self.__arguments)

    def compile(self, dialect):
        return js.primitive.FunctionCall(self.__function_name,
                                 [a.compile(dialect) for a in self.__arguments])

class Return(SinglePartCompilable):
    def __init__(self, what):
        SinglePartCompilable.__init__(self)

        self.what = what

    def compile(self, dialect):
        return js.primitive.Return(self.what.compile(dialect))

class FunctionDefinition(SinglePartCompilable):
    def __init__(self, name, args=[], source=[]):
        SinglePartCompilable.__init__(self)

        self._source = DuckTypedList(['compile'], source)
        self.name = name
        self.args = args
        self.return_statement = None

    def add_statement(self, st):
        self._source.append(st)

    def insert_statement(self, pos, st):
        self._source.insert(pos, st)

    def set_return_statement(self, st):
        self.return_statement = Return(st)

    def compile(self, dialect):
        retval = js.primitive.FunctionDefinition(self.name,self.args)
        for st in self._source:
            retval.add_statement(st.compile(dialect))

        if self.return_statement != None:
            retval.add_statement(self.return_statement.compile(dialect))

        return retval

class ConstructorDefinition(FunctionDefinition):
    def __init__(self,class_name):
        FunctionDefinition.__init__(self,class_name)

    def compile(self, dialect):
        retval = js.primitive.FunctionDefinition("")
        for st in self._source:
            retval.add_statement(st.compile(dialect))

        return retval

class DestructorDefinition(FunctionDefinition):
    def __init__(self,class_name):
        FunctionDefinition.__init__(self,class_name)

    def compile(self, dialect):
        retval = js.primitive.FunctionDefinition("")
        for st in self._source:
            retval.add_statement(st.compile(dialect))

        return retval

class ClassDefinition(SinglePartCompilable):
    def __init__(self,name):
        SinglePartCompilable.__init__(self)

        self.__name = name
        self.members = DuckTypedDict(['compile'])
        self.statics = DuckTypedDict(['compile'])
        self.ctor = ConstructorDefinition(self.name)
        self.dtor = DestructorDefinition(self.name)
        self.preamble = DuckTypedList(['compile'])
        self.mixins = DuckTypedList(['compile'])
        self.mixins.append(ObjectReference("qx.locale.MTranslation"))
        self.base_class = None
        self.assets = set()

    def set_name(self, name):
        self.__name = name
        self.ctor.name = name
        self.dtor.name = name

    def get_name(self):
        return self.__name

    name = property(get_name,set_name)

    def set_member(self, key, val):
        self.members[key]=val
        val.set_parent(self)

    def get_member(self, key, val, default=None):
        return self.__elts['members'].get(key, default)

    def compile(self, dialect):
        lang = js.primitive.FunctionCall("qx.Class.define")
        lang.add_argument(js.primitive.String(self.name))

        if self.base_class == None:
            base_class = js.primitive.ObjectReference('qx.core.Object')
        else:
            base_class = js.primitive.ObjectReference(self.base_class)

        class_members = js.primitive.Object()

        # MPC gets compiled first because they can make changes 
        # anywhere, including members dict.
        for k,v in self.members.items():
            if isinstance(v, MultiPartCompilable): # FIXME!
                v.compile(dialect, self)

        for k,v in self.members.items():
            if isinstance(v, SinglePartCompilable): # FIXME!
                class_members.set_member(k, v.compile(dialect))

        st = FunctionCall('this.base')
        st.add_argument(ObjectReference('arguments'))
        self.ctor.insert_statement(0,st)

        properties = js.primitive.Object()
        widget_property = js.primitive.Object()
        widget_property.set_member("check",
                               js.primitive.String('qx.ui.core.Widget'))
        properties.set_member("widget", widget_property)

        mixins = js.primitive.Array()
        for m in self.mixins:
            mixins.append(m.compile(dialect))

        class_dict = js.primitive.Object()
        class_dict.set_member("members", class_members)
        class_dict.set_member("extend", base_class)
        class_dict.set_member("construct", self.ctor.compile(dialect))
        class_dict.set_member("destruct", self.dtor.compile(dialect))
        class_dict.set_member("properties", properties)
        class_dict.set_member("include", mixins)

        lang.add_argument(class_dict)
        if len(self.assets) > 0:
            self.preamble.insert(0, Comment("".join(
                    ["\n#asset(%s)" % a for a in sorted(self.assets)]) + "\n"))

        return lang

class AssociativeArrayInitialization(SinglePartCompilable):
    type_map={
        int: DecimalInteger,
        str: String,
    }

    def __init__(self, aai):
        SinglePartCompilable.__init__(self)
        self.value = DuckTypedDict(['compile'])
        for k,v in aai.items():
            if isinstance(v, SinglePartCompilable):
                self.value[k] = v
            else:
                self.value[k] = self.type_map[type(v)](v)

    def __len__(self):
        return len(self.value)

    def compile(self, dialect):
        retval = js.primitive.Object()

        for k,v in self.value.items():
            retval.set_member(k, v.compile(dialect))

        return retval

class ContiguousArrayInitialization(SinglePartCompilable):
    type_map={
        int: DecimalInteger,
        str: String,
        unicode: TranslatableString,
    }

    def __init__(self, cai):
        SinglePartCompilable.__init__(self)
        self.__cai = DuckTypedList(['compile'])
        for v in cai.items():
            if isinstance(v, SinglePartCompilable):
                self.__aai.append(v)
            else:
                self.__aai.append(self.type_map[type(v)](v))

    def compile(self, dialect):
        retval = js.primitive.Array()

        for k,v in self.__aai.items():
            retval.append(v.compile(dialect))

        return retval
