# encoding: utf8

#
# This file is part of JsQT.
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

from jsqt import Base, Dummy

class Layout(Base):
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
        self.buffer.append('        this.%(self_name)s.setSpacing(9);' % {'self_name': self.name()})

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

    def add_widget(self, container, widget, **kwargs):
        if isinstance(widget, Dummy):
            return

        self.buffer.append('        this.%(container_name)s.add(this.%(widget_name)s,{flex:1});' % {'container_name': container.name(), 'widget_name': widget.name()})

class QGridLayout(Layout):
    def __init__(self, caller, name, class_name=""):
        self.type = "qx.ui.layout.Grid"
        Layout.__init__(self, caller, name, class_name)
        self.buffer.append('        this.%(self_name)s.setSpacingX(9);' % {'self_name': self.name()})
        self.buffer.append('        this.%(self_name)s.setSpacingY(9);' % {'self_name': self.name()})

        self.register_handlers()

        self.row_flex_flags = set()
        self.column_flex_flags = set()
        
    def add_widget(self, container, widget, **kwargs):
        if isinstance(widget, Dummy):
            return

        row = widget.item_properties.get("row")
        column = widget.item_properties.get("column")
        
        self.buffer.append('        this.%(container_name)s.add(this.%(widget_name)s, {row: %(row)s, column: %(col)s });' % {
             'container_name': container.name()
            ,'widget_name': widget.name()
            ,'row': row
            ,'col': column
        })
        
        if not column in self.column_flex_flags:
            self.buffer.append('        this.%(self_name)s.setColumnFlex(%(column)s, 1);' % { 'self_name': self.name(), 'column': column } )
            self.column_flex_flags.add(column)
        
        if not row in self.row_flex_flags:
            self.buffer.append('        this.%(self_name)s.setRowFlex(%(row)s, 1);' % { 'self_name': self.name(), 'row': row } )
            self.row_flex_flags.add(row)
                