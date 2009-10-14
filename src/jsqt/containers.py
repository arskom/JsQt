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

from widgets import Widget
from layouts import *

class QToolBar(Container):
    def __init__(self, caller, name, class_name=""):
        self.type = "qx.ui.toolbar.ToolBar"
        Container.__init__(self, caller, name, class_name)

        self.layout = None
        self.register_handlers()

class QScrollArea(Container):
    def __init__(self, caller, name, class_name=""):
        self.type = "qx.ui.container.Scroll"
        Container.__init__(self, caller, name, class_name)

        self.layout = None

        self.register_handlers()

    #
    # quoting qooxdoo api docs:
    #     Note that this class can only have one child widget.
    #     This container has a fixed layout, which cannot be changed.
    #
    # so set_layout here does nothing.
    #
    def set_layout(self, layout):
        pass

    def add_widget(self, widget, **kwargs):
        if len(self.children)>0:
            raise Exception("QScrollArea can have one child widget")
        self.children.append(widget)
        self.buffer.append("        this.%(self_name)s.add(this.%(widget_name)s);" % {'self_name': self.name(), 'widget_name': widget.name()})

    def close(self):
        self.children[0].vsize_type = 'Expanding'
        self.children[0].hsize_type = 'Expanding'
        self.children[0].set_vsizepolicy()
        self.children[0].set_hsizepolicy()
        Container.close(self)

class QxTabPage(Container):
    def __init__(self, caller, name, class_name=""):
        self.type = "qx.ui.tabview.Page"
        Container.__init__(self, caller, name, class_name)

        self.layout = None
        self.register_handlers()

    def add_widget(self, widget, **kwargs):
        if len(self.children) > 0:
            print self.children
            raise Exception("qx.ui.tabview.Page should have only one child!")

        self.buffer.append('        this.%(self_name)s.setLayout(new qx.ui.layout.Canvas());' % {'self_name': self.name(), 'widget_name': widget.name()})
        self.buffer.append('        this.%(self_name)s.add(this.%(widget_name)s,{edge:0});' % {'self_name': self.name(), 'widget_name': widget.name()})
        self.buffer.append('        this.%(self_name)s.setLabel("%(widget_text)s");' % {'self_name': self.name(), 'widget_text': widget.title_text})


