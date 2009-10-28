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

from gui import ContainerBase

class QMainWindow(ContainerBase):
    def __init__(self, elt, name=None):
        ContainerBase.__init__(self, elt, name)

        self.type = "qx.ui.container.Composite"

class QTabWidget(ContainerBase):
    def __init__(self, elt, name=None):
        ContainerBase.__init__(self, elt, name)

        self.type = "qx.ui.tabview.TabView"

    def _handle_widget_tag(self, elt):
        elt.set("class", "TabPage")
        ContainerBase._handle_widget_tag(self, elt)
    
    def _compile_layout(self, dialect, ret):
        pass

class TabPage(ContainerBase):
    def __init__(self, elt, name=None):
        self.layout_properties = None
        ContainerBase.__init__(self, elt, name)

        self.type = "qx.ui.tabview.Page"
                
class QGroupBox(ContainerBase):
    def __init__(self, elt, name=None):
        ContainerBase.__init__(self, elt, name)

        self.type = "qx.ui.groupbox.GroupBox"

class QScrollArea(ContainerBase):
    def __init__(self, elt, name=None):
        ContainerBase.__init__(self, elt, name)

        self.type = "qx.ui.container.Scroll"

    def _compile_layout(self, dialect, ret):
        pass

    def add_child(self, instance):
        if len(self.children)>0:
            raise Exception("QScrollArea can have one child widget")
        ContainerBase.add_child(self, instance)

    def close(self):
        self.children[0].vsize_type = 'Expanding'
        self.children[0].hsize_type = 'Expanding'
        self.children[0].set_vsizepolicy()
        self.children[0].set_hsizepolicy()
        Container.close(self)
