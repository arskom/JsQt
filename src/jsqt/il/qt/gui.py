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
import obj
from jsqt import il
from base import SimpleProp
from jsqt.xml import etree

class MGeometryProperties(object):
    hor_stretch_pol = "Expanding"
    ver_stretch_pol = "Expanding"
    hor_stretch_coef = 1
    ver_stretch_coef = 1

    def __init__(self):
        self.__margin_t = etree.fromstring("<number>1</number>")
        self.__margin_b = etree.fromstring("<number>1</number>")
        self.__margin_l = etree.fromstring("<number>1</number>")
        self.__margin_r = etree.fromstring("<number>1</number>")
        self.__margin = etree.fromstring("<number>1</number>")

        self.__min_width = etree.fromstring("<number>0</number>")
        self.__min_height = etree.fromstring("<number>0</number>")

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

    def __handle_size_policy(self, elt):
        if elt[0].tag == 'sizepolicy':
            tmp = self._decode_nested_prop(elt[0])

            self.hor_stretch_pol = elt[0].attrib['hsizetype']
            self.hor_stretch_coef = int(tmp['horstretch'].text)
            self.ver_stretch_pol = elt[0].attrib['vsizetype']
            self.ver_stretch_coef = int(tmp['verstretch'].text)

            if not self.hor_stretch_pol in ("Fixed", "Minimum"):
                if self.hor_stretch_coef == 0:
                    self.hor_stretch_coef = 1

            if not self.ver_stretch_pol in ("Fixed", "Minimum"):
                if self.ver_stretch_coef == 0:
                    self.ver_stretch_coef = 1

        else:
            jsqt.debug_print("\t\t", "WARNING: property 'sizePolicy' doesn't "
                                                      "have a 'sizepolicy' tag")

    #
    # hacking around qooxdoo bug 3075
    # http://bugzilla.qooxdoo.org/show_bug.cgi?id=3075
    #
    def __handle_minimum_size(self, elt):
        if elt[0].tag == 'size':
            tmp = {}
            for e in elt[0]:
                tmp[e.tag]=e

            self.__min_width = tmp['width']
            self.__min_height = tmp['height']
            self.simple_prop_data['geometry.width'] = self.__min_width
            self.simple_prop_data['geometry.height'] = self.__min_height

        else:
            jsqt.debug_print("\t\t", "WARNING: property 'minimumSize' doesn't "
                                                            "have a 'size' tag")

    def _compile_geometry(self, dialect, ret):
        if not self._compile_simple_prop(SimpleProp("setMargin", il.primitive.DecimalInteger, 0), self.__margin):
            self._compile_simple_prop(SimpleProp("setMarginTop", il.primitive.DecimalInteger, 0), self.__margin_t)
            self._compile_simple_prop(SimpleProp("setMarginLeft", il.primitive.DecimalInteger, 0), self.__margin_l)
            self._compile_simple_prop(SimpleProp("setMarginRight", il.primitive.DecimalInteger, 0), self.__margin_r)
            self._compile_simple_prop(SimpleProp("setMarginBottom", il.primitive.DecimalInteger, 0), self.__margin_b)

        self._compile_simple_prop(SimpleProp("setMinWidth", il.primitive.DecimalInteger, 0), self.__min_width)
        self._compile_simple_prop(SimpleProp("setMinHeight", il.primitive.DecimalInteger, 0), self.__min_height)

        xml_false = etree.fromstring("<bool>false</bool>")
        if self.hor_stretch_pol == "Fixed":
            self._compile_simple_prop(SimpleProp("setAllowGrowX",
                                               il.primitive.Boolean), xml_false)
        if self.ver_stretch_pol == "Fixed":
            self._compile_simple_prop(SimpleProp("setAllowGrowY",
                                               il.primitive.Boolean), xml_false)

    known_simple_props = {
        "geometry": {
            "x": SimpleProp("", il.primitive.DecimalInteger, 0),
            "y": SimpleProp("", il.primitive.DecimalInteger, 0),
            "width": SimpleProp("setWidth", il.primitive.DecimalInteger, 0),
            "height": SimpleProp("setHeight", il.primitive.DecimalInteger, 0),
        },
        "maximumSize": {
            "width": SimpleProp("setMaxWidth", il.primitive.DecimalInteger,
                                                                      16777215),
            "height": SimpleProp("setMaxHeight", il.primitive.DecimalInteger,
                                                                      16777215),
        }
    }

    known_complex_props = {
        "sizePolicy": __handle_size_policy,
        "minimumSize": __handle_minimum_size,
    }

class WidgetBase(obj.Base, MGeometryProperties):
    def __init__(self, elt, name=None):
        MGeometryProperties.__init__(self)
        obj.Base.__init__(self, elt, name)

    def compile(self, dialect, ret):
        obj.Base.compile(self, dialect, ret)
        self._compile_geometry(dialect, ret)

    def _decode_nested_prop(self, elt):
        retval = {}
        for e in elt:
            retval[e.tag] = e

        return retval

    @staticmethod
    def get_class(class_name):
        if class_name in widget_dict:
            return widget_dict[class_name]

        elif class_name in layout_dict:
            return layout_dict[class_name]

        elif class_name in custom_dict:
            return custom_dict[class_name]

        else:
            return Stub

    @staticmethod
    def get_instance(elt):
        if elt.tag == 'spacer':
            class_name = 'Spacer'
        else:
            class_name = elt.attrib['class']

        return WidgetBase.get_class(class_name)(elt)

class Stub(WidgetBase):
    real = False

    def __init__(self, elt, name=None):
        WidgetBase.__init__(self, elt, name)

        self.class_name = elt.attrib['class']

    def compile(self, dialect, ret=None):
        ret.ctor.add_statement(
           il.primitive.Comment("The instance named '%s' is of type '%s' which"
                     " is not supported (yet?)" % (self.name, self.class_name)))

class QSpacer(WidgetBase):
    type = "qx.ui.core.Spacer"

    known_simple_props = {
        "sizeHint": {
            "width": SimpleProp("setWidth", il.primitive.DecimalInteger, 0),
            "height": SimpleProp("setHeight", il.primitive.DecimalInteger, 0),
        },
    }
