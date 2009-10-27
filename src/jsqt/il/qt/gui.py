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

from jsqt import DuckTypedList
from jsqt import il
from jsqt.xml import etree

import tidy

widget_dict = {}
layout_dict = {}

class MPropertyManager(object):
    def __init__(self):
        self.geometry_t = 0
        self.geometry_l = 0
        self.geometry_w = 0
        self.geometry_h = 0

        self.geometry_min_w = 0
        self.geometry_min_h = 0
        self.geometry_max_w = 16777215
        self.geometry_max_h = 16777215
        self.margin_t = 1
        self.margin_b = 1
        self.margin_l = 1
        self.margin_r = 1

        self.known_props = {
            "geometry": self._handle_prop_geometry,
            "text": self._handle_prop_text,
        }

        self.primitive_prop_types = {
            'x': int,
            'y': int,
            'width': int,
            'height': int,
            'string': str,
        }

    def _handle_prop_type_rect(self, elt):
        retval = {}
        for e in elt:
            retval[e.tag] = self.primitive_prop_types[e.tag](e.text)

        return retval

    def _compile_props(self, dialect, ret):
        self._compile_geometry(dialect, ret)

    def _compile_geometry(self, dialect, ret):
        if self.geometry_w > 0:
            fc = il.primitive.FunctionCall("this.%s.setWidth" % self.name,
                                 [il.primitive.DecimalInteger(self.geometry_w)])
            self.factory_function.add_statement(fc)

        if self.geometry_h > 0:
            fc = il.primitive.FunctionCall("this.%s.setHeight" % self.name,
                                 [il.primitive.DecimalInteger(self.geometry_h)])
            self.factory_function.add_statement(fc)

        if self.geometry_min_w > 0:
            fc = il.primitive.FunctionCall("this.%s.setMinWidth" % self.name,
                             [il.primitive.DecimalInteger(self.geometry_min_w)])
            self.factory_function.add_statement(fc)

        if self.geometry_min_h > 0:
            fc = il.primitive.FunctionCall("this.%s.setMinHeight" % self.name,
                             [il.primitive.DecimalInteger(self.geometry_min_h)])
            self.factory_function.add_statement(fc)

        if self.geometry_max_w < 16777215:
            fc = il.primitive.FunctionCall("this.%s.setMaxWidth" % self.name,
                             [il.primitive.DecimalInteger(self.geometry_max_w)])
            self.factory_function.add_statement(fc)

        if self.geometry_max_h < 16777215:
            fc = il.primitive.FunctionCall("this.%s.setMaxHeight" % self.name,
                             [il.primitive.DecimalInteger(self.geometry_max_h)])
            self.factory_function.add_statement(fc)

        if self.margin_b != 0:
            fc = il.primitive.FunctionCall("this.%s.setMarginBottom" % self.name,
                                   [il.primitive.DecimalInteger(self.margin_b)])
            self.factory_function.add_statement(fc)

        if self.margin_t != 0:
            fc = il.primitive.FunctionCall("this.%s.setMarginTop" % self.name,
                                   [il.primitive.DecimalInteger(self.margin_t)])
            self.factory_function.add_statement(fc)

        if self.margin_l != 0:
            fc = il.primitive.FunctionCall("this.%s.setMarginLeft" % self.name,
                                   [il.primitive.DecimalInteger(self.margin_l)])
            self.factory_function.add_statement(fc)

        if self.margin_r != 0:
            fc = il.primitive.FunctionCall("this.%s.setMarginRight" % self.name,
                                   [il.primitive.DecimalInteger(self.margin_r)])
            self.factory_function.add_statement(fc)

    def _handle_prop_geometry(self, elt):
        if elt[0].tag == 'rect':
            retval = self._handle_prop_type_rect(elt[0])

            self.geometry_l = retval['x']
            self.geometry_t = retval['y']
            self.geometry_w = retval['width']
            self.geometry_h = retval['width']

        else:
            print "\t\t", "WARNING: property 'geometry' doesn't have 'rect' tag"

    def _handle_prop_text(self, elt):
        self.text = self.primitive_prop_types[elt[0].tag](elt[0].text)

class ObjectBase(il.primitive.MultiPartCompilable):
    def __init__(self, elt, name=None):
        il.primitive.MultiPartCompilable.__init__(self)
        
        self.children = DuckTypedList(['compile'])
        self.supported = True
        self.parent = None
        try:
            self.tag_handlers
        except:
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
            print "\tQWidget.__init__:", elt.tag, elt.attrib

            self._loop_children(elt)

        self.factory_function = il.primitive.FunctionDefinition(
                                                        "create_%s" % self.name)

    def _handle_property_tag(self, elt):
        self.set_property(elt)

    def _loop_children(self, elt):
        for e in elt:
            self.tag_handlers[e.tag](e)

    def get_instance(self, elt):
        if elt.tag == 'spacer':
            return widget_dict['Spacer'](elt)
        
        else:
            class_name = elt.attrib['class']
            if class_name in widget_dict:
                return widget_dict[class_name](elt)
            elif class_name in layout_dict:
                return layout_dict[class_name](elt)
            else:
                return QWidgetStub(elt)

    def compile(self, dialect, ret):
        factory_function_retval = il.primitive.ObjectReference('this.%s'
                                                               % self.name)
        instantiation = il.primitive.Assignment()
        instantiation.set_left(factory_function_retval)
        instantiation.set_right(il.primitive.Instantiation(self.type))

        self.factory_function.add_statement(instantiation)

        self._compile_layout(dialect, ret)
        self._compile_props(dialect, ret)

        # children
        for c in self.children:
            c.compile(dialect, ret)

            if c.supported:
                args = [il.primitive.FunctionCall("this.create_%s" % c.name)]
                if c.layout_properties != None:
                    args.append(il.primitive.AssociativeArrayInitialization(
                                c.layout_properties))

                add_children=il.primitive.FunctionCall('this.%s.add'% self.name,
                                                         args)
                self.factory_function.add_statement(add_children)

        ret.set_member(self.factory_function.name, self.factory_function)
        self.factory_function.add_statement(il.primitive.Return(
                                            factory_function_retval))

        ret.set_member(self.name, il.primitive.ObjectReference('null'))

    def set_parent(self, parent):
        self.parent = parent

    def is_primitive(self):
        return False

    def set_property(self, elt):
        print "\t\t", elt.tag, elt.attrib

        prop_name = elt.attrib['name']
        if prop_name in self.known_props:
            self.known_props[prop_name](elt)

    def _compile_layout(self, dialect, ret):
        pass

class WidgetBase(ObjectBase, MPropertyManager):
    def __init__(self, elt, name=None):
        MPropertyManager.__init__(self)
        ObjectBase.__init__(self, elt, name)

class ContainerBase(WidgetBase):
    def _loop_children(self, elt):
        self.tag_handlers["widget"] = self._handle_widget_tag
        self.tag_handlers['item'] = self._handle_item_tag
        self.tag_handlers['layout'] = self._handle_layout_tag
        try:
            self.layout
        except:
            self.layout = il.qt.layout.CanvasLayout(None, "%s_il" % self.name)
            
        WidgetBase._loop_children(self, elt)

    def _handle_widget_tag(self, elt):
        instance = self.get_instance(elt)
        self.add_child(instance)

    def _handle_item_tag(self, elt):
        if elt[0].tag == "layout":
            #print tidy.parseString(etree.tostring(elt), output_xml=1, input_xml=1, add_xml_decl=1, indent=1, tidy_mark=0)
            new_elt = etree.Element("widget")
            new_elt.set('name', "%s_implicit_container" % elt[0].attrib['name'])
            new_elt.set('class', "QWidget")
            new_elt.append(elt[0])
            elt.append(new_elt)
            #print "+++++++++++++++++++++++++"
            #print tidy.parseString(etree.tostring(elt), output_xml=1, input_xml=1, add_xml_decl=1, indent=1, tidy_mark=0)

        instance = self.get_instance(elt[0])

        if isinstance(self.layout, il.qt.layout.QGridLayout):
            instance.layout_properties = dict(elt.attrib)
            for k in instance.layout_properties:
                instance.layout_properties[k]=int(instance.layout_properties[k])

        elif (isinstance(self.layout, il.qt.layout.QHBoxLayout) or
              isinstance(self.layout, il.qt.layout.QVBoxLayout)):

            instance.layout_properties = {'flex': 1}

        else: # FIXME: unsupported layout
            instance.layout_properties = {}

        self.add_child(instance)

    def add_child(self, instance):
        self.children.append(instance)

        if isinstance(self.layout, il.qt.layout.CanvasLayout):
            instance.layout_properties = {
                "top": instance.geometry_t,
                "left": instance.geometry_l,
            }

        instance.set_parent(self)

    def _compile_layout(self, dialect, ret):
        self.layout.compile(dialect, ret)
        set_layout = il.primitive.FunctionCall('this.%s.setLayout' % self.name,
               [il.primitive.FunctionCall("this.create_%s" % self.layout.name)])

        self.factory_function.add_statement(set_layout)

    def _handle_layout_tag(self, elt):
        instance = self.get_instance(elt)
        self.set_layout(instance)
        self._loop_children(elt)

    def set_layout(self, layout):
        self.layout = layout
        layout.set_parent(self)

class QWidget(ContainerBase):
    def __init__(self, elt, name=None):
        ContainerBase.__init__(self, elt, name)

        self.type = "qx.ui.container.Composite"

class QSpacer(WidgetBase):
    def __init__(self, elt, name=None):
        WidgetBase.__init__(self, elt, name)

        self.type = "qx.ui.core.Spacer"

class QWidgetStub(ContainerBase):
    def __init__(self, elt, name=None):
        WidgetBase.__init__(self, elt, name)

        self.class_name = elt.attrib['class']
        self.supported = False

    def compile(self, dialect, ret=None):
        ret.ctor.add_statement(
           il.primitive.Comment("The instance named '%s' is of type '%s' which"
           " is not supported (yet?)" % (self.name, self.class_name)))

