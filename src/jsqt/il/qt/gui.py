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

class MGeometryProperties(object):
    def __init__(self):
        self.__top = 0
        self.__left = 0
        self.__width = 0
        self.__height = 0

        self.__min_w = 0
        self.__min_h = 0
        self.__max_w = 16777215
        self.__max_h = 16777215

        self.__margin_t = 1
        self.__margin_b = 1
        self.__margin_l = 1
        self.__margin_r = 1

        self.__h_stretch_pol = "Expanding"
        self.__h_stretch_coef = 1
        self.__v_stretch_pol = "Expanding"
        self.__v_stretch_coef = 1

        self.__known_props = {
            "text": self.__handle_prop_text,
            "geometry": self.__handle_prop_geometry,
            "minimumSize": self.__handle_prop_min_size,
            "maximumSize": self.__handle_prop_max_size,
            "sizePolicy": self.__handle_size_policy,
        }

        self.__primitive_prop_types = {
            'x': int,
            'y': int,
            'width': int,
            'height': int,
            'string': str,
            'horstretch': int,
            'verstretch': int,
        }

    def get_geometry_top(self):
        return self.__top
    geometry_top = property(get_geometry_top)

    def get_geometry_left(self):
        return self.__left
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
            tmp = self.__decode_complex_prop(elt[0])
            
            self.__h_stretch_pol = elt[0].attrib['hsizetype']
            self.__h_stretch_coef = tmp['horstretch']
            self.__v_stretch_pol = elt[0].attrib['vsizetype']
            self.__v_stretch_coef = tmp['verstretch']

            if self.__h_stretch_pol != "Fixed":
                if self.__h_stretch_coef == 0:
                    self.__h_stretch_coef = 1

            if self.__v_stretch_pol != "Fixed":
                if self.__v_stretch_coef == 0:
                    self.__v_stretch_coef = 1

        else:
            jsqt.debug_print("\t\t", "WARNING: property 'geometry' doesn't have"
                                                            " 'sizepolicy' tag")

    def __handle_prop_min_size(self, elt):
        if elt[0].tag == 'size':
            tmp = self.__decode_complex_prop(elt[0])

            self.__min_w = tmp['width']
            self.__min_h = tmp['height']

        else:
            jsqt.debug_print("\t\t", "WARNING: property 'geometry' doesn't have"
                                                                  " 'size' tag")

    def __handle_prop_max_size(self, elt):
        if elt[0].tag == 'size':
            retval = self.__decode_complex_prop(elt[0])

            self.__max_w = retval['width']
            self.__max_h = retval['height']

        else:
            jsqt.debug_print("\t\t", "WARNING: property 'geometry' doesn't have"
                                                                  " 'size' tag")

    def __handle_prop_geometry(self, elt):
        if elt[0].tag == 'rect':
            retval = self.__decode_complex_prop(elt[0])

            self.__top = retval['y']
            self.__left = retval['x']
            self.__width = retval['width']
            self.__height = retval['height']

        else:
            jsqt.debug_print("\t\t", "WARNING: property 'geometry' doesn't have"
                                                                  " 'rect' tag")

    def __handle_prop_text(self, elt):
        self.text = self.__primitive_prop_types[elt[0].tag](elt[0].text)

    def __decode_complex_prop(self, elt):
        retval = {}
        for e in elt:
            retval[e.tag] = self.__primitive_prop_types[e.tag](e.text)

        return retval

    def set_property(self, elt):
        prop_name = elt.attrib['name']
        if prop_name in self.__known_props:
            self.__known_props[prop_name](elt)

    def compile(self, dialect, ret):
        if self.__width != 0:
            fc = il.primitive.FunctionCall("this.%s.setWidth" % self.name,
                                    [il.primitive.DecimalInteger(self.__width)])
            self.factory_function.add_statement(fc)

        if self.__height != 0:
            fc = il.primitive.FunctionCall("this.%s.setHeight" % self.name,
                                   [il.primitive.DecimalInteger(self.__height)])
            self.factory_function.add_statement(fc)

        if self.__min_w != 0:
            fc = il.primitive.FunctionCall("this.%s.setMinWidth" % self.name,
                                    [il.primitive.DecimalInteger(self.__min_w)])
            self.factory_function.add_statement(fc)

        if self.__min_h != 0:
            fc = il.primitive.FunctionCall("this.%s.setMinHeight" % self.name,
                                    [il.primitive.DecimalInteger(self.__min_h)])
            self.factory_function.add_statement(fc)

        if self.__max_w != 16777215:
            fc = il.primitive.FunctionCall("this.%s.setMaxWidth" % self.name,
                                    [il.primitive.DecimalInteger(self.__max_w)])
            self.factory_function.add_statement(fc)

        if self.__max_h != 16777215:
            fc = il.primitive.FunctionCall("this.%s.setMaxHeight" % self.name,
                                    [il.primitive.DecimalInteger(self.__max_h)])
            self.factory_function.add_statement(fc)

        if self.__margin_b != 0:
            fc = il.primitive.FunctionCall("this.%s.setMarginBottom"% self.name,
                                 [il.primitive.DecimalInteger(self.__margin_b)])
            self.factory_function.add_statement(fc)

        if self.__margin_t != 0:
            fc = il.primitive.FunctionCall("this.%s.setMarginTop" % self.name,
                                 [il.primitive.DecimalInteger(self.__margin_t)])
            self.factory_function.add_statement(fc)

        if self.__margin_l != 0:
            fc = il.primitive.FunctionCall("this.%s.setMarginLeft" % self.name,
                                 [il.primitive.DecimalInteger(self.__margin_l)])
            self.factory_function.add_statement(fc)

        if self.__margin_r != 0:
            fc = il.primitive.FunctionCall("this.%s.setMarginRight" % self.name,
                                 [il.primitive.DecimalInteger(self.__margin_r)])
            self.factory_function.add_statement(fc)

class ObjectBase(il.primitive.MultiPartCompilable):
    type = None

    def __init__(self, elt, name=None):
        il.primitive.MultiPartCompilable.__init__(self)
        
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
        factory_function_retval = il.primitive.ObjectReference('this.%s'
                                                                    % self.name)
        instantiation = il.primitive.Assignment()
        instantiation.set_left(factory_function_retval)
        instantiation.set_right(il.primitive.Instantiation(self.type))

        self.factory_function.add_statement(instantiation)

        ret.set_member(self.factory_function.name, self.factory_function)
        self.factory_function.set_return_statement(
                            il.primitive.ObjectReference('this.%s' % self.name))

        ret.set_member(self.name, il.primitive.ObjectReference('null'))

    def compile(self, dialect, ret):
        self._compile_instantiation(dialect, ret)

    def set_parent(self, parent):
        self.parent = parent

    def is_primitive(self):
        return False

class WidgetBase(ObjectBase, MGeometryProperties):
    def __init__(self, elt, name=None):
        MGeometryProperties.__init__(self)
        ObjectBase.__init__(self, elt, name)

    def compile(self, dialect, ret):
        ObjectBase.compile(self, dialect, ret)
        MGeometryProperties.compile(self, dialect, ret)

class ContainerBase(WidgetBase):
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
        set_layout = il.primitive.FunctionCall('this.%s.setLayout' % self.name,
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

                if isinstance(c.layout_properties, dict):
                    args.append(il.primitive.AssociativeArrayInitialization(
                                c.layout_properties))
                                
                elif isinstance(c.layout_properties, int):
                    args.append(il.primitive.DecimalInteger(c.layout_properties))

                add_children=il.primitive.FunctionCall('this.%s.add'% self.name,
                                                                           args)
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

    def __init__(self, elt, name=None):
        ContainerBase.__init__(self, elt, name)

class QSpacer(WidgetBase):
    type = "qx.ui.core.Spacer"

    def __init__(self, elt, name=None):
        WidgetBase.__init__(self, elt, name)

class QWidgetStub(WidgetBase):
    def __init__(self, elt, name=None):
        WidgetBase.__init__(self, elt, name)

        self.class_name = elt.attrib['class']
        self.supported = False

    def compile(self, dialect, ret=None):
        ret.ctor.add_statement(
           il.primitive.Comment("The instance named '%s' is of type '%s' which"
                     " is not supported (yet?)" % (self.name, self.class_name)))

