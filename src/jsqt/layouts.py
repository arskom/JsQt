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

from jsqt import Base, Dummy

class Layout(Base):
    class qt_defaults(Base.qt_defaults):
        spacing_x = '9'
        spacing_y = '9'

    class qx_defaults(Base.qx_defaults):
        spacing_x = '0'
        spacing_y = '0'

    def init_defaults(self):
        Base.init_defaults(self)

        self.spacing_x = self.qx_defaults.spacing_x
        self.spacing_y = self.qx_defaults.spacing_y

    def __init__(self, caller, name, class_name):
        if len(caller.stack) > 0:
            self.parent = caller.stack[ - 1]
        if name == "":
            name = self.parent.name() + "_" + self.__class__.__name__.lower()
        Base.__init__(self, caller, name, class_name)

class CanvasLayout(Layout):
    implicit = False

    def __init__(self, caller, name, class_name=""):
        self.type = "qx.ui.layout.Canvas"
        Layout.__init__(self, caller, name, class_name)

        self.register_handlers()

    def add_widget(self, container, widget, **kwargs):
        props = []
        if hasattr(widget, 'x'):
            props.append('left: %s' % widget.x)
        if hasattr(widget, 'y'):
            props.append('top: %s' % widget.y)

        if isinstance(widget, Dummy):
            return

        container.children.append(widget)
        self.buffer.append('        this.%(container_name)s.add(this.%(widget_name)s,{%(props)s});' % {'container_name': container.name(), 'widget_name': widget.name(), 'props': ', '.join(props)})

class QVBoxLayout(Layout):
    def __init__(self, caller, name, class_name=""):
        self.type = "qx.ui.layout.VBox"
        Layout.__init__(self, caller, name, class_name)

        self.register_handlers()

    def bridge_defaults(self):
        Layout.bridge_defaults(self)

        if self.spacing_y != self.qt_defaults.spacing_y:
            self.spacing_y = self.qt_defaults.spacing_y
            self.buffer.append('        this.%(self_name)s.setSpacing(%(val)s);' % {'self_name': self.name(), 'val': self.qt_defaults.spacing_y})

    def add_widget(self, container, widget, **kwargs):
        if isinstance(widget, Dummy):
            return

        self.buffer.append('        this.%(container_name)s.add(this.%(widget_name)s,{flex:1});' % {'container_name': container.name(), 'widget_name': widget.name()})

class QHBoxLayout(Layout):
    def __init__(self, caller, name, class_name=""):
        self.type = "qx.ui.layout.HBox"
        Layout.__init__(self, caller, name, class_name)
        self.buffer.append('        this.%(self_name)s.setSpacing(9);' % {'self_name': self.name()})

        self.register_handlers()

    def bridge_defaults(self):
        Layout.bridge_defaults(self)

        if self.spacing_x != self.qt_defaults.spacing_x:
            self.spacing_x = self.qt_defaults.spacing_x
            self.buffer.append('        this.%(self_name)s.setSpacing(%(val)s);' % {'self_name': self.name(), 'val': self.qt_defaults.spacing_x})

    def add_widget(self, container, widget, **kwargs):
        if isinstance(widget, Dummy):
            return

        self.buffer.append('        this.%(container_name)s.add(this.%(widget_name)s,{flex:1});' % {'container_name': container.name(), 'widget_name': widget.name()})

class QGridLayout(Layout):
    def __init__(self, caller, name, class_name=""):
        self.type = "qx.ui.layout.Grid"
        Layout.__init__(self, caller, name, class_name)

        self.register_handlers()

        self.row_flex_flags = set()
        self.column_flex_flags = set()

    def bridge_defaults(self):
        Layout.bridge_defaults(self)

        if self.spacing_x != self.qt_defaults.spacing_x:
            self.spacing_x = self.qt_defaults.spacing_x
            self.buffer.append('        this.%(self_name)s.setSpacingX(%(val)s);' % {'self_name': self.name(), 'val': self.qt_defaults.spacing_x})

        if self.spacing_y != self.qt_defaults.spacing_y:
            self.spacing_y = self.qx_defaults.spacing_y
            self.buffer.append('        this.%(self_name)s.setSpacingY(%(val)s);' % {'self_name': self.name(), 'val': self.qt_defaults.spacing_y})

    def add_widget(self, container, widget, **kwargs):
        if isinstance(widget, Dummy):
            return

        row = widget.item_properties.get("row")
        column = widget.item_properties.get("column")

        hsizetype = widget.hsize_type

        self.buffer.append('        this.%(container_name)s.add(this.%(widget_name)s, {row: %(row)s, column: %(col)s });' % {
             'container_name': container.name()
            ,'widget_name': widget.name()
            ,'row': row
            ,'col': column
        })

        if not column in self.column_flex_flags:
            if widget.hsize_type == 'Expanding':
                print "\t\t\tcol expanding_widget:", widget.name()
                self.buffer.append('        this.%(self_name)s.setColumnFlex(%(column)s, 1);' % { 'self_name': self.name(), 'column': column } )
                self.column_flex_flags.add(column)

        if not row in self.row_flex_flags:
            if (widget.vsize_type == 'Expanding'):
                print "\t\t\trow expanding_widget:", widget.name()
                self.buffer.append('        this.%(self_name)s.setRowFlex(%(row)s, 1);' % { 'self_name': self.name(), 'row': row } )
                self.row_flex_flags.add(row)

class QFormLayout(QGridLayout):
    pass

