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

from jsqt import il
from gui import ContainerBase, SimpleProp

class ContainerWithoutLayout(ContainerBase):
    def __init__(self, elt, name=None):
        ContainerBase.__init__(self, elt, name)

        self.layout = il.qt.layout.DummyLayout(None, "")

    def _compile_layout(self, dialect, ret):
        pass

class QMainWindow(ContainerBase):
    type = "qx.ui.container.Composite"

class QTabWidget(ContainerWithoutLayout):
    type = "qx.ui.tabview.TabView"
    
    def _handle_widget_tag(self, elt):
        elt.set("class", "TabPage")
        ContainerBase._handle_widget_tag(self, elt)

class TabPage(ContainerBase):
    type = "qx.ui.tabview.Page"
    known_simple_props = {
        "title": SimpleProp("setLabel", il.primitive.TranslatableString),
    }
    
    def __init__(self, elt, name=None):
        self.layout_properties = None
        ContainerBase.__init__(self, elt, name)

class QSplitter(ContainerBase):
    type = "qx.ui.splitpane.Pane"

    def __init__(self, elt, name=None):
        self.layout_properties = None
        self.__orientation = "horizontal" # FIXME

        ContainerBase.__init__(self, elt, name)

    def get_orientation(self):
        return self.__orientation
    orientation = property(get_orientation)

    def add_child(self, instance):
        if len(self.children)>1:
            raise Exception("QSplitter can have two child widgets")
        ContainerBase.add_child(self, instance)

    def _init_before_parse(self):
        ContainerBase._init_before_parse(self)
        self.layout = il.qt.layout.SplitPaneLayout(None,"x")

    def _compile_layout(self, dialect, ret):
        pass

    def _compile_instantiation(self, dialect, ret):
        instantiation = il.primitive.Assignment()
        instantiation.set_left(il.primitive.ObjectReference('this.%s' % self.name))
        instantiation.set_right(il.primitive.Instantiation(self.type,[
            il.primitive.String(self.__orientation)]))

        self.factory_function.add_statement(instantiation)
        self.factory_function.add_statement(il.primitive.ObjectReference("var retval = this.%s" % self.name)) # FIXME: hack

        ret.set_member(self.factory_function.name, self.factory_function)

        self.factory_function.set_return_statement(
                            il.primitive.ObjectReference('retval'))

        ret.set_member(self.name, il.primitive.ObjectReference('null'))

class QGroupBox(ContainerBase):
    type = "qx.ui.groupbox.GroupBox"
    known_simple_props = {
        "title": SimpleProp("setLegend", il.primitive.TranslatableString),
    }

    def __init__(self, elt, name=None):
        self.layout_properties = None
        ContainerBase.__init__(self, elt, name)

class QScrollArea(ContainerBase):
    type = "qx.ui.container.Scroll"
    
    def _compile_layout(self, dialect, ret):
        pass

    def add_child(self, instance):
        if len(self.children)>0:
            raise Exception("QScrollArea can have only one child widget")
        ContainerBase.add_child(self, instance)
