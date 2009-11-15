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

import jsqt
from jsqt import DuckTypedList
from jsqt import il
from jsqt.xml import etree

widget_dict = {}
layout_dict = {}
custom_dict = {}

class SimpleProp(object):
    def __init__(self, function_name, wrapper_type, default_value=None):
        self.function_name = function_name
        self.wrapper_type = wrapper_type
        self.default_value = default_value

class WidgetMeta(type):
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
                    raise Exception("'%s' already has a simple '%s' handler."%
                                                                      (name, k))
                if k in cls.known_complex_props:
                    raise Exception("'%s' already has a complex '%s' handler."%
                                                                      (name, k))
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
                    raise Exception("'%s' already has a simple '%s' handler."%
                                                                      (name, k))
                if k in cls.known_complex_props:
                    raise Exception("'%s' already has a complex '%s' handler."%
                                                                  (name, k))
                cls.known_complex_props[k] = v

class MGeometryProperties(object):
    def __init__(self):
        self.__margin_t = etree.fromstring("<number>1</number>")
        self.__margin_b = etree.fromstring("<number>1</number>")
        self.__margin_l = etree.fromstring("<number>1</number>")
        self.__margin_r = etree.fromstring("<number>1</number>")
        self.__margin = etree.fromstring("<number>1</number>")

        self.__h_stretch_pol = "Expanding"
        self.__h_stretch_coef = 1
        self.__v_stretch_pol = "Expanding"
        self.__v_stretch_coef = 1

    def get_geometry_top(self):
        if "geometry.y" in self.simple_prop_data:
            return int(self.simple_prop_data["geometry.y"].text)
        else:
            return 0
    geometry_top = property(get_geometry_top)

    def get_geometry_left(self):
        if "geometry.x" in self.simple_prop_data:
            return int(self.simple_prop_data["geometry.x"].text)
        else:
            return 0
    geometry_left = property(get_geometry_left)

    def get_hor_stretch_coef(self):
        return self.__h_stretch_coef
    hor_stretch_coef = property(get_hor_stretch_coef)

    def get_ver_stretch_coef(self):
        return self.__v_stretch_coef
    ver_stretch_coef = property(get_ver_stretch_coef)

    def get_hor_stretch_pol(self):
        return self.__h_stretch_pol
    hor_stretch_pol = property(get_hor_stretch_pol)

    def get_ver_stretch_pol(self):
        return self.__v_stretch_pol
    ver_stretch_pol = property(get_ver_stretch_pol)

    def __handle_size_policy(self, elt):
        if elt[0].tag == 'sizepolicy':
            tmp = self._decode_nested_prop(elt[0])

            self.__h_stretch_pol = elt[0].attrib['hsizetype']
            self.__h_stretch_coef = int(tmp['horstretch'].text)
            self.__v_stretch_pol = elt[0].attrib['vsizetype']
            self.__v_stretch_coef = int(tmp['verstretch'].text)

            if self.__h_stretch_pol != "Fixed":
                if self.__h_stretch_coef == 0:
                    self.__h_stretch_coef = 1

            if self.__v_stretch_pol != "Fixed":
                if self.__v_stretch_coef == 0:
                    self.__v_stretch_coef = 1

        else:
            jsqt.debug_print("\t\t", "WARNING: property 'geometry' doesn't have"
                                                            " 'sizepolicy' tag")

    def compile(self, dialect, ret):
        if not self._compile_simple_prop(SimpleProp("setMargin", il.primitive.DecimalInteger, 0), self.__margin):
            self._compile_simple_prop(SimpleProp("setMarginTop", il.primitive.DecimalInteger, 0), self.__margin_t)
            self._compile_simple_prop(SimpleProp("setMarginLeft", il.primitive.DecimalInteger, 0), self.__margin_l)
            self._compile_simple_prop(SimpleProp("setMarginRight", il.primitive.DecimalInteger, 0), self.__margin_r)
            self._compile_simple_prop(SimpleProp("setMarginBottom", il.primitive.DecimalInteger, 0), self.__margin_b)

    known_simple_props = {
        "geometry": {
            "x": SimpleProp("", il.primitive.DecimalInteger, 0),
            "y": SimpleProp("", il.primitive.DecimalInteger, 0),
            "width": SimpleProp("setWidth", il.primitive.DecimalInteger, 0),
            "height": SimpleProp("setHeight", il.primitive.DecimalInteger, 0),
        },
        "minimumSize": {
            "width": SimpleProp("setMinWidth", il.primitive.DecimalInteger, 0),
            "height": SimpleProp("setMinHeight", il.primitive.DecimalInteger, 0),
        },
        "maximumSize": {
            "width": SimpleProp("setMaxWidth", il.primitive.DecimalInteger, 16777215),
            "height": SimpleProp("setMaxHeight", il.primitive.DecimalInteger, 16777215),
        }
    }

    known_complex_props = {
        "sizePolicy": __handle_size_policy,
    }

class ObjectBase(il.primitive.MultiPartCompilable):
    type = None

    def __init__(self, elt, name=None):
        il.primitive.MultiPartCompilable.__init__(self)

        self.simple_prop_data={}

        self.children = DuckTypedList(['compile'])
        self.supported = True
        self.parent = None
        self.tag_handlers = {}

        self.tag_handlers["property"] = self._handle_property_tag
        self.tag_handlers["attribute"] = self._handle_property_tag

        if name != None:
            if elt != None:
                raise Exception("You should provide either name or elt"
                                                     "arguments, but not both.")

            self.name = name

        else:
            self.name = elt.attrib['name']

            jsqt.debug_print("\tQWidget.__init__:", elt.tag, elt.attrib)
            self._init_before_parse()
            self._loop_children(elt)

    def set_name(self, name):
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

    def set_property(self, elt):
        jsqt.debug_print("\t\t", elt.tag, elt.attrib)
        MGeometryProperties.set_property(self, elt)

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

    @staticmethod
    def get_class(class_name):
        if class_name in widget_dict:
            return widget_dict[class_name]
        elif class_name in layout_dict:
            return layout_dict[class_name]
        elif class_name in custom_dict:
            return custom_dict[class_name]
        else:
            return QWidgetStub

    @staticmethod
    def get_instance(elt):
        if elt.tag == 'spacer':
            class_name = 'Spacer'
        else:
            class_name = elt.attrib['class']

        return ObjectBase.get_class(class_name)(elt)

    def _compile_instantiation(self, dialect, ret):
        factory_function_retval = il.primitive.ObjectReference('retval')
        instantiation = il.primitive.Assignment()
        instantiation.set_left(il.primitive.ObjectReference('this.%s' % self.name))
        instantiation.set_right(il.primitive.Instantiation(self.type))

        self.factory_function.add_statement(instantiation)
        self.factory_function.add_statement(il.primitive.ObjectReference("var retval = this.%s" % self.name)) # FIXME: hack

        ret.set_member(self.factory_function.name, self.factory_function)
        self.factory_function.set_return_statement(
                            il.primitive.ObjectReference('retval'))

        ret.set_member(self.name, il.primitive.ObjectReference('null'))

    def _compile_simple_props(self, dialect, ret):
        keys = self.simple_prop_data.keys()
        keys.sort()
        for k in keys:
            if "." in k:
                tmp = k.split(".")
                prop = self.known_simple_props[tmp[0]][tmp[1]]
            else:
                prop = self.known_simple_props[k]

            self._compile_simple_prop(prop, self.simple_prop_data[k])

    def _compile_simple_prop(self, prop, data):
        data=prop.wrapper_type.from_elt(data)
        if prop.default_value != data and prop.function_name != "" :
            fc=il.primitive.FunctionCall("retval.%s"%(prop.function_name),[data])
            self.factory_function.add_statement(fc)
            return True
        else:
            return False

    def compile(self, dialect, ret):
        self._compile_instantiation(dialect, ret)
        self._compile_simple_props(dialect, ret)

    def set_parent(self, parent):
        self.parent = parent

    def is_primitive(self):
        return False

class WidgetBase(ObjectBase, MGeometryProperties):
    __metaclass__ = WidgetMeta

    def __init__(self, elt, name=None):
        MGeometryProperties.__init__(self)
        ObjectBase.__init__(self, elt, name)

    def compile(self, dialect, ret):
        ObjectBase.compile(self, dialect, ret)
        MGeometryProperties.compile(self, dialect, ret)

    def set_property(self, elt):
        prop_name = elt.attrib['name']

        if prop_name in self.known_simple_props:
            prop = self.known_simple_props[prop_name]
            if isinstance(prop,dict):
                tmp = self._decode_nested_prop(elt[0])
                for k in tmp:
                    self.simple_prop_data["%s.%s" % (prop_name,k)] = tmp[k]

            else:
                self.simple_prop_data[prop_name] = elt[0]

        elif prop_name in self.known_complex_props:
            self.known_complex_props[prop_name](self, elt)

    def _decode_nested_prop(self, elt):
        retval = {}
        for e in elt:
            retval[e.tag] = e

        return retval

class ContainerBase(WidgetBase):
    add_method_name = "add"

    def _init_before_parse(self):
        WidgetBase._init_before_parse(self)
        self.tag_handlers["widget"] = self._handle_widget_tag
        self.tag_handlers['layout'] = self._handle_layout_tag
        self.tag_handlers['item'] = self._handle_item_tag
        self.layout = il.qt.layout.CanvasLayout(None, "%s_il" % self.name)

    def _handle_widget_tag(self, elt):
        instance = self.get_instance(elt)
        self.add_child(instance)

    def _handle_item_tag(self, elt):
        if elt[0].tag == "layout":
            new_elt = etree.Element("widget")
            new_elt.set('name', "%s_implicit_container" % elt[0].attrib['name'])
            new_elt.set('class', "QWidget")
            new_elt.append(elt[0])
            elt.append(new_elt)

        instance = self.get_instance(elt[0])
        self.add_child(instance, elt)

    def add_child(self, instance, elt=None):
        instance.layout_properties = self.layout.get_properties(elt, instance)

        self.children.append(instance)
        instance.set_parent(self)

    def _compile_layout(self, dialect, ret):
        self.layout.compile(dialect, ret)
        set_layout = il.primitive.FunctionCall('retval.setLayout',
               [il.primitive.FunctionCall("this.create_%s" % self.layout.name)])

        self.factory_function.add_statement(set_layout)

    def __compile_children(self, dialect, ret):
        # children
        for c in self.children:
            c.compile(dialect, ret)

            if c.supported:
                args = [il.primitive.FunctionCall("this.create_%s" % c.name)]
                c.layout_properties = c.parent.layout.get_properties(
                                                          c._elt.getparent(), c)
                if c.layout_properties != None:
                    args.append(c.layout_properties)

                add_children=il.primitive.FunctionCall('retval.%s' % self.add_method_name, args)
                self.factory_function.add_statement(add_children)

    def compile(self, dialect, ret):
        WidgetBase.compile(self, dialect, ret)
        self._compile_layout(dialect, ret)
        self.__compile_children(dialect, ret)

    def _handle_layout_tag(self, elt):
        instance = self.get_instance(elt)
        self.set_layout(instance)
        self._loop_children(elt)

    def set_layout(self, layout):
        self.__layout = layout
        self.__layout.set_parent(self)
    
    def get_layout(self):
        return self.__layout

    layout = property(get_layout, set_layout)

class QWidget(ContainerBase):
    type = "qx.ui.container.Composite"

class QSpacer(WidgetBase):
    type = "qx.ui.core.Spacer"

    known_simple_props = {
        "sizeHint": {
            "width": SimpleProp("setWidth", il.primitive.DecimalInteger, 0),
            "height": SimpleProp("setHeight", il.primitive.DecimalInteger, 0),
        },
    }

class QWidgetStub(WidgetBase):
    def __init__(self, elt, name=None):
        WidgetBase.__init__(self, elt, name)

        self.class_name = elt.attrib['class']
        self.supported = False

    def compile(self, dialect, ret=None):
        ret.ctor.add_statement(
           il.primitive.Comment("The instance named '%s' is of type '%s' which"
                     " is not supported (yet?)" % (self.name, self.class_name)))

