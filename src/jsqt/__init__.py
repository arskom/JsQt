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

version   = "trunk"
copyright = "(c) 2009 Arskom Ltd."
header_string = """
JsQt %s
%s
""" % (version, copyright)

from UserList import UserList

class TypedList(UserList):

    def __init__(self,attr_list):
        UserList.__init__(self)
        for a in attr_list:
            if type(a) != str:
                raise Exception("""TypedList accepts only an iterable of strings

                """)

        self.__attr_list = attr_list

    def append(self, x):
        for a in self.__attr_list:
            if not hasattr(x, a):
                raise TypeError, 'TypedList should have objects with a "%s" member' % a

        self.data.append(x)

class Base(object):
    type = None
    class qt_defaults:
        vsize_type = 'Expanding'
        hsize_type = 'Expanding'

    class qx_defaults:
        vsize_type = 'Expanding'
        hsize_type = 'Expanding'

    def __init__(self, caller, name, class_name):
        # TODO: name validation
        self.children = []
        self.__name = name
        if len(caller.stack) > 0:
            self.parent = caller.stack[-1]
        else:
            self.parent = None

        self.inst_line = None

        #
        # The three fields here represent:
        # [0]: the property name
        # [1]: a complex data type, None if the data type is simple
        # [2]: a primitive data type.
        #
        # A complex data type is one that contains more than one primitive
        # entries. for example <rect> tag has four primitive entries under
        # a property.
        #
        self.current = [None, None, None]

        self.text_handler = None
        self.item_properties = None

        self.vsize_type = None
        self.hsize_type = None
        self.vsize_type_property = None
        self.hsize_type_property = None

        self.tag_entry_handlers = {}
        self.tag_exit_handlers = {}
        self.xmltext_handlers = {}
        self.xmltext_handler = None

        self.caller = caller
        self.buffer = caller.buffer

        self.implicit = False
        self.inst_line = None

        self.in_layout = False

        self.class_name = class_name

        self.display()
        self.js_inst()
        self.init_defaults()
        self.bridge_defaults()

    def display(self):
        """
        This is the function that is called when showing the progresss report.
        """
        print "\t","  ok ",self.__name, self.class_name

    def close(self):
        pass

    def js_inst(self):
        """
            When called the first time, this function writes the instantiation line.
            When called more than once, it overwrites the previous instantiation. It
            is useful when a property value in Qt is represented with a different
            widget in Qooxdoo.
        """
        if self.type == None:
            return

        js_inst_str = '        this.%(self_name)s = new %(self_type)s(); // %(internal_type)s' % \
            {'self_name': self.name(), 'self_type': self.type, 'internal_type': self.__class__.__name__}

        if self.inst_line == None:
            self.caller.add_member("%(self_name)s : null" % {'self_name' : self.name()})
            self.buffer.append('')
            self.buffer.append(js_inst_str)
            self.inst_line = len(self.buffer) - 1

        else:
            self.buffer[self.inst_line] = js_inst_str

    def init_defaults(self): # FIXME: should be done introspectively
        self.vsize_type = self.qx_defaults.vsize_type
        self.hsize_type = self.qx_defaults.hsize_type

    def bridge_defaults(self):
        if self.vsize_type != self.qt_defaults.vsize_type:
            self.vsize_type = self.qt_defaults.vsize_type
            self.set_vsizepolicy()

        if self.hsize_type != self.qt_defaults.hsize_type:
            self.hsize_type = self.qt_defaults.hsize_type
            self.set_hsizepolicy()

    def register_handlers(self):
        tag_entry_handlers={
            "rect": self.rect_entry,
            "datetime": self.datetime_entry,
            "sizepolicy": self.sizepolicy_entry,
            "size": self.size_entry,
            "hour": self.prim_entry,
            "minute": self.prim_entry,
            "second": self.prim_entry,
            "year": self.prim_entry,
            "month": self.prim_entry,
            "day": self.prim_entry,
            "string": self.prim_entry,
            "x": self.prim_entry,
            "y": self.prim_entry,
            "width": self.prim_entry,
            "height": self.prim_entry,
            "horstretch": self.prim_entry,
            "verstretch": self.prim_entry,
            "enum": self.prim_entry,
            "set": self.prim_entry,
            "pointsize": self.prim_entry,
            "family": self.prim_entry,
            "weight": self.prim_entry,
            "bold": self.prim_entry,
            "bool": self.prim_entry,
            "number": self.prim_entry,
        }

        self.tag_exit_handlers = {
            "horstretch": self.prim_exit,
            "sizepolicy": self.sizepolicy_exit,
            "datetime": self.datetime_exit,
            "minute": self.prim_exit,
            "string": self.prim_exit,
            "second": self.prim_exit,
            "height": self.prim_exit,
            "width": self.prim_exit,
            "month": self.prim_exit,
            "hour": self.prim_exit,
            "rect": self.rect_exit,
            "size": self.size_exit,
            "year": self.prim_exit,
            "day": self.prim_exit,
            "x": self.prim_exit,
            "y": self.prim_exit,
            "number": self.prim_exit,
            "bool": self.prim_exit,
            "bold": self.prim_exit,
            "weight": self.prim_exit,
            "family": self.prim_exit,
            "enum": self.prim_exit,
            "verstretch": self.prim_exit,
            "set": self.prim_exit,
            "pointsize": self.prim_exit,
        }

        # property handlers
        self.xmltext_handlers = {
            ("geometry", "rect", "x"):  self.x_text,
            ("geometry", "rect", "y"):  self.y_text,
            ("geometry", "rect", "width"):  self.w_text,
            ("geometry", "rect", "height"):  self.h_text,

            ("sizeHint", "size", "width"):  self.w_text,
            ("sizeHint", "size", "height"):  self.h_text,

            ("minimumSize", "size", "width"):  self.set_minimum_width,
            ("minimumSize", "size", "height"):  self.set_minimum_height,
            ("maximumSize", "size", "width"):  self.set_maximum_width,
            ("maximumSize", "size", "height"):  self.set_maximum_height,

            ("bottomMargin", None, "number"):  self.set_margin_bottom,
            ("leftMargin", None, "number"):  self.set_margin_left,
            ("rightMargin", None, "number"):  self.set_margin_right,
            ("topMargin", None, "number"):  self.set_margin_top,
            ("margin", None, "number"):  self.set_margin,
        }

    def get_type(self):
        return self.__class__.__name__

    def name(self):
        return self.__name

    def set_current_property(self, name):
        self.current[0] = name

    def rect_entry(self, attrs, *args):
        self.current[1] = "rect"

    def rect_exit(self):
        self.current[1] = None

    def set_vsizepolicy(self):
        if self.vsize_type == 'Fixed':
            self.buffer.append("        this.%(self_name)s.setAllowGrowY(false);" % {'self_name': self.name()})
        else:
            self.buffer.append("        this.%(self_name)s.setAllowGrowY(true);" % {'self_name': self.name()})

    def set_hsizepolicy(self):
        if self.hsize_type == 'Fixed':
            self.buffer.append("        this.%(self_name)s.setAllowGrowX(false);" % {'self_name': self.name()})
        else:
            self.buffer.append("        this.%(self_name)s.setAllowGrowX(true);" % {'self_name': self.name()})


    def sizepolicy_entry(self, attrs, *args):
        self.vsize_type = attrs.get("vsizetype")
        self.hsize_type = attrs.get("hsizetype")

        self.vsize_type_property = attrs.get("vsizetype")
        self.hsize_type_property = attrs.get("hsizetype")

        self.set_vsizepolicy()
        self.set_hsizepolicy()

    def sizepolicy_exit(self):
        pass

    def datetime_entry(self, attrs, *args):
        self.current[1] = "datetime"

    def datetime_exit(self):
        self.current[1] = None


    def size_entry(self, attrs, *args):
        self.current[1] = "size"

    def size_exit(self):
        self.current[1] = None


    def prim_entry(self, attrs, what):
        """ Entry tag handler for the primitive data types """
        self.current[2] = what
        t = tuple(self.current)

        if self.xmltext_handlers.has_key(t):
            self.xmltext_handler = self.xmltext_handlers[t]
        else:
            self.buffer.append("        // WARNING: %s: property is ignored" % str(t))

    def prim_exit(self):
        """ Exit tag handler for the primitive data types """
        self.xmltext_handler = None
        self.current[2] = None


    def x_text(self, text, *args):
        self.x = text

    def y_text(self, text, *args):
        self.y = text

    def w_text(self, text, *args):
        self.buffer.append("        this.%(self_name)s.setWidth(%(text)s);" % {'self_name': self.name(), 'text': text})

    def h_text(self, text, *args):
        self.buffer.append("        this.%(self_name)s.setHeight(%(text)s);" % {'self_name': self.name(), 'text': text})

    def set_minimum_width(self, minWidth, *args):
        if int(minWidth) > 0:
            self.buffer.append('        this.%(self_name)s.setMinWidth(%(minWidth)s);' % {'self_name': self.name(), 'minWidth': minWidth})
    def set_minimum_height(self, minHeight, *args):
        if int(minHeight) > 0:
            self.buffer.append('        this.%(self_name)s.setMinHeight(%(minHeight)s);' % {'self_name': self.name(), 'minHeight': minHeight})
    def set_maximum_width(self, maxWidth, *args):
        if int(maxWidth) < 16777215:
            self.buffer.append('        this.%(self_name)s.setMaxWidth(%(maxWidth)s);' % {'self_name': self.name(), 'maxWidth': maxWidth})
    def set_maximum_height(self, maxHeight, *args):
        if int(maxHeight) < 16777215:
            self.buffer.append('        this.%(self_name)s.setMaxHeight(%(maxHeight)s);' % {'self_name': self.name(), 'maxHeight': maxHeight})

    def set_margin_bottom(self, marginBottom, *args):
        self.buffer.append('        this.%(self_name)s.setMarginBottom(%(marginBottom)s);' % {'self_name': self.name(), 'marginBottom': marginBottom})
    def set_margin_left(self, marginLeft, *args):
        self.buffer.append('        this.%(self_name)s.setMarginLeft(%(marginLeft)s);' % {'self_name': self.name(), 'marginLeft': marginLeft})
    def set_margin_right(self, marginRight, *args):
        self.buffer.append('        this.%(self_name)s.setMarginRight(%(marginRight)s);' % {'self_name': self.name(), 'marginRight': marginRight})
    def set_margin_top(self, marginTop, *args):
        self.buffer.append('        this.%(self_name)s.setMarginTop(%(marginTop)s);' % {'self_name': self.name(), 'marginTop': marginTop})
    def set_margin(self, margin, *args):
        self.buffer.append('        this.%(self_name)s.setMargin(%(margin)s);' % {'self_name': self.name(), 'margin': margin})

    def set_geometry_x(self, x):
        self.x = x
    def set_geometry_y(self, y):
        self.y = y
    def set_geometry_w(self, w):
        self.buffer.append('        this.%(self_name)s.setWidth(%(width)s);' % {'self_name': self.name(), 'width': w})
    def set_geometry_h(self, h):
        self.buffer.append('        this.%(self_name)s.setHeight(%(width)s);' % {'self_name': self.name(), 'width': h})


class Class(Base):
    def __init__(self, caller, name, class_name):
        Base.__init__(self, caller, name, class_name)
        self.xmltext_handler = self.__xmltext_handler

    def js_type(self):
        pass

    def __xmltext_handler(self, text, *args):
        self.buffer.append('qx.Class.define("%(class_name)s", { type : "abstract", extend : qx.core.Object ' % { "class_name": self.name() })
        self.buffer.append('    ,properties : {');
        self.buffer.append('        widget : { check : "Object" }');
        self.buffer.append('    }');
        self.buffer.append('    ,construct : function () {');

    def add_widget(self, *args, **kwargs):
        pass

class Dummy(Base):
    def js_inst(self):
        self.buffer.append('        // WARNING: %(class_name)s widget is not supported (yet?).' % {'class_name':self.class_name})

    def display(self):
        print "\t WARN", self.class_name, "is not supported (yet?)."

    def do_nothing(self,*args,**kwargs):
        pass

    def __getattr__(self,attr,default=None):
        pass

    set_layout = do_nothing
    add_widget = do_nothing

class NoQooxdooEquivalent(Dummy):
    def register_handlers(self):
        pass

    def js_inst(self):
        self.buffer.append('        // WARNING: %(class_name)s widget is not supported by Qooxdoo.' % {'class_name':self.class_name})

    def display(self):
        print "\t WARN", self.class_name, "is not supported by Qooxdoo."

