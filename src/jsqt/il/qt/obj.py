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

import jsqt
from jsqt import il
from jsqt.base import DuckTypedList

widget_dict = {}
layout_dict = {}
custom_dict = {}

class _Meta(type):
    def __init__(cls, name, bases, members):
        try:
            cls.known_simple_props
        except AttributeError:
            cls.known_simple_props = {}

        try:
            cls.known_complex_props
        except AttributeError:
            cls.known_complex_props = {}

        for b in bases:
            try:
                b.known_simple_props
                if id(b.known_simple_props) == id(cls.known_simple_props):
                    continue

            except AttributeError:
                continue

            for k,v in b.known_simple_props.items():
                if k in cls.known_simple_props:
                    raise Exception("'%s(%r)' already has a simple '%s' handler."%
                                                          (name, cls, k))
                if k in cls.known_complex_props:
                    raise Exception("'%s(%r)' already has a complex '%s' handler."%
                                                          (name, cls, k))
                cls.known_simple_props[k] = v

        for b in bases:
            try:
                b.known_complex_props
                if id(b.known_complex_props) == id(cls.known_complex_props):
                    continue
            except AttributeError:
                continue

            for k,v in b.known_complex_props.items():
                if k in cls.known_simple_props:
                    raise Exception("'%s' already has a simple '%s' handler." %
                                                                      (name, k))
                if k in cls.known_complex_props:
                    raise Exception("'%s' already has a complex '%s' handler." %
                                                                      (name, k))
                cls.known_complex_props[k] = v

class Base(il.primitive.MultiPartCompilable):
    __metaclass__ = _Meta

    type = None
    likes_to_flex = True
    real = True

    def __init__(self, elt, name=None):
        class Icons(object):
            def __init__(self):
                self.base = None
                self.normaloff = None

        il.primitive.MultiPartCompilable.__init__(self)

        self.icons = Icons()
        self.simple_prop_data = {}

        self.children = DuckTypedList(['compile'])
        self.parent = None
        self.tag_handlers = {}

        self.tag_handlers["property"] = self._handle_property_tag
        self.tag_handlers["attribute"] = self._handle_property_tag
        self._elt = None
        self.layout_properties = {}
        self.parser = None

        if name != None:
            if elt != None:
                raise Exception("You should provide either name or elt"
                                                     "arguments, but not both.")

            self.name = name

        else:
            try:
                self.name = elt.attrib['name']

            except ValueError,e:
                from lxml import etree
                print etree.tostring(elt)
                raise

            jsqt.debug_print("\tQWidget.__init__:", elt.tag, elt.attrib)
            jsqt.debug_print("\t\treading xml...")
            self._init_before_parse()
            self._loop_children(elt)

    def set_name(self, name):
        if name is None or len(name) == 0:
            raise ValueError("the object name is empty")
        self.__name = name
        self.factory_function = il.primitive.FunctionDefinition(
                                                        "create_%s" % self.name)
    def get_name(self):
        return self.__name

    name = property(get_name, set_name)

    def _init_before_parse(self):
        pass

    def _handle_property_tag(self, elt):
        self.set_property(elt)

    def _loop_children(self, elt):
        self._elt = elt
        for e in elt:
            if e.tag in self.tag_handlers:
                self.tag_handlers[e.tag](e)
            else:
                self.factory_function.add_statement(
                    il.primitive.Comment("The '%s' tag for widget named '%s'"
                             "of type '%s' is not supported (yet?)"
                                        % (e.tag, self.name, type(self) )))

    def _compile_instantiation(self, dialect, ret):
        jsqt.debug_print("\t\tinstantiation")

        self.instantiation = il.primitive.Assignment()
        self.instantiation.left = il.primitive.ObjectReference('this.%s' %
                                                                      self.name)
        self.instantiation.right = il.primitive.Instantiation(self.type)

        self.factory_function.add_statement(self.instantiation)
        self.factory_function.add_statement(il.primitive.VariableDeclaration(
            "retval", il.primitive.ObjectReference("this.%s" % self.name)
        ))

        ret.set_member(self.factory_function.name, self.factory_function)
        self.factory_function.set_return_statement(
                                         il.primitive.ObjectReference('retval'))

        ret.set_member(self.name, il.primitive.ObjectReference('null'))

    def _compile_icon(self, dialect, ret):
        def _recurse_parent(arg):
            if getattr(arg, 'parser', None) is None:
                if getattr(arg, 'parent', None) is None:
                    arg.parser = arg
                else:
                    _recurse_parent(arg.parent)
                    arg.parser = arg.parent.parser

        if self.icons.base is not None:
            _recurse_parent(self)
            icon_uri = self.parser.resources[self.icons.base[0]][self.icons.base[1]]
            fc = il.primitive.FunctionCall("retval.setIcon",[
                                    il.primitive.String(str(icon_uri))])
            self.factory_function.add_statement(fc)
            self.parser.clazz.assets.add(icon_uri)

    def _compile_simple_props(self, dialect, ret):
        keys = self.simple_prop_data.keys()
        keys.sort()
        for k in keys:
            jsqt.debug_print("\t\tcompile simple prop: %s" % k)
            if "." in k:
                tmp = k.split(".")
                prop = self.known_simple_props[tmp[0]][tmp[1]]
            else:
                prop = self.known_simple_props[k]

            self._compile_simple_prop(prop, self.simple_prop_data[k])

    def _compile_simple_prop(self, prop, data):
        retval = False

        data = prop.wrapper_type.from_elt(data)
        if prop.default_value != data and prop.function_name != "" :
            fc = il.primitive.FunctionCall("retval.%s" % (prop.function_name),
                                                                         [data])
            self.factory_function.add_statement(fc)

            retval = True

        return retval

    def compile(self, dialect, ret):
        jsqt.debug_print("\tcompiling '%s'..." % self.name)
        self._compile_instantiation(dialect, ret)
        self._compile_simple_props(dialect, ret)
        self._compile_icon(dialect, ret)

    def set_parent(self, parent):
        self.parent = parent

    def set_property(self, elt):
        prop_name = elt.attrib['name']

        if prop_name in self.known_simple_props:
            jsqt.debug_print("\t\t\tread simple prop: %s" % prop_name)
            prop = self.known_simple_props[prop_name]
            if isinstance(prop,dict):
                tmp = self._decode_nested_prop(elt[0])
                for k in tmp:
                    self.simple_prop_data["%s.%s" % (prop_name,k)] = tmp[k]

            else:
                self.simple_prop_data[prop_name] = elt[0]

        elif prop_name in self.known_complex_props:
            jsqt.debug_print("\t\t\tread complex prop: %s" % prop_name)
            self.known_complex_props[prop_name](self, elt)

        else:
            self.factory_function.add_statement(
                    il.primitive.Comment("The '%s' property for widget named '%s'"
                             "of type '%s' is not supported (yet?)"
                                        % (prop_name, self.name, type(self)) ))

    def _handle_icon(self, elt):
        iconset = elt.find('iconset')
        if 'resource' in iconset.attrib:
            base_icon = [iconset.text]
            base_icon.extend([e.tail for e in iconset.getchildren()])
            base_icon = ''.join(base_icon).strip()
            assert base_icon[0] == ':',("JsQt only supports importing resources "
                                        "from resource (.qrc) files. Hey, at "
                                        "least I warned ya.")

            self.icons.base = (iconset.attrib['resource'], base_icon)

    known_complex_props = {
        "icon": _handle_icon,
    }


class Action(Base):
    def __init__(self, elt, name=None):
        self.checkable = False

        Base.__init__(self, elt, name)

    def _handle_text(self, elt):
        self.prop_text = elt[0]

    def _handle_checkable(self, elt):
        self.checkable = (elt.find('bool').text == 'true')

    known_complex_props = {
        "text": _handle_text,
        "checkable": _handle_checkable,
    }
