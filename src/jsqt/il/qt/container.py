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

from jsqt import il
from jsqt.xml import etree
from jsqt.il.qt import gui
from jsqt.il.qt import obj

from base import SimpleProp

class Base(gui.WidgetBase):
    add_method_name = "add"
    layout_in_ctor = True

    def _init_before_parse(self):
        gui.WidgetBase._init_before_parse(self)

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
        for c in self.children:
            self.layout.meet_child(c)

        self.layout.compile(dialect, ret)
        
        if not self.layout_in_ctor:
            set_layout = il.primitive.FunctionCall('retval.setLayout',
                   [il.primitive.FunctionCall("this.create_%s" % self.layout.name)])

            self.factory_function.add_statement(set_layout)

    def _compile_instantiation(self, dialect, ret):
        gui.WidgetBase._compile_instantiation(self, dialect, ret)

        if self.layout_in_ctor:
            layout_call = il.primitive.FunctionCall("this.create_%s" %
                                                               self.layout.name)

            self.instantiation.right.args.append(layout_call)

    def _compile_child(self, dialect, ret, c):
        c.compile(dialect, ret)

        if c.real:
            args = [il.primitive.FunctionCall("this.create_%s" % c.name)]

            if c._elt != None:
                c.layout_properties = self.layout.get_properties(
                                                      c._elt.getparent(), c)
                if c.layout_properties != None:
                    args.append(c.layout_properties)

            add_child = il.primitive.FunctionCall('retval.%s' %
                                                     self.add_method_name, args)
            self.factory_function.add_statement(add_child)

    def _compile_children(self, dialect, ret):
        for c in self.children:
            self._compile_child(dialect, ret, c)

    def compile(self, dialect, ret):
        gui.WidgetBase.compile(self, dialect, ret)
        self._compile_layout(dialect, ret)
        self._compile_children(dialect, ret)
        self.layout.post_fill_ops(dialect, ret, self.factory_function)

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

class WithoutLayout(Base):
    layout_in_ctor = False
    
    def __init__(self, elt, name=None):
        Base.__init__(self, elt, name)

        self.layout = il.qt.layout.DummyLayout(None, "dummy_layout")

    def _compile_layout(self, dialect, ret):
        pass

class QWidget(Base):
    type = "qx.ui.container.Composite"

class QDialog(Base):
    type = "qx.ui.container.Composite"

    def __init__(self, elt, name=None):
        self.actions = {}

        Base.__init__(self, elt, name)

    def _init_before_parse(self):
        Base._init_before_parse(self)

        self.tag_handlers['action'] = self._handle_actions_tag

    def _handle_actions_tag(self, elt):
        self.actions[elt.attrib['name']] = obj.Action(elt)

    def _compile_children(self, dialect, ret):
        for i in range(len(self.children)):
            if self.children[i]._elt.attrib['class'] == 'QMenuBar':
                self._compile_child(dialect, ret, self.children[i])
                del self.children[i]
                break

        i = 0
        while i < len(self.children):
            if (self.children[i]._elt.attrib['class'] == 'QToolBar' and
                             self.children[i].toolbar_area == "TopToolBarArea"):
                self._compile_child(dialect, ret, self.children[i])
                del self.children[i]

            else:
                i+=1

        for i in range(len(self.children)):
            self._compile_child(dialect, ret, self.children[i])

class _FakeAttrib(object):
    def __init__(self, value):
        self.value = value

class QMainWindow(QDialog):
    def __init__(self, elt, name=None):
        QDialog.__init__(self, elt, name)
        self.set_layout(il.qt.layout.QVBoxLayout(None,"__lv"))

class QTabWidget(WithoutLayout):
    type = "qx.ui.tabview.TabView"
    
    def _handle_widget_tag(self, elt):
        elt.set("class", "TabPage")
        Base._handle_widget_tag(self, elt)

class TabPage(Base):
    type = "qx.ui.tabview.Page"
    layout_in_ctor = False
    known_simple_props = {
        "title": SimpleProp("setLabel", il.primitive.TranslatableString),
    }
    
    def __init__(self, elt, name=None):
        self.layout_properties = None
        Base.__init__(self, elt, name)

class EnumOrientation(il.primitive.Enum):
    value_map = {
        "Qt::Vertical": "vertical",
        "Qt::Horizontal": "horizontal",
    }


class QSplitter(Base):
    type = "qx.ui.splitpane.Pane"

    def __init__(self, elt, name=None):
        self.layout_properties = None
        self.__orientation = "horizontal" # FIXME

        Base.__init__(self, elt, name)

    def get_orientation(self):
        return self.__orientation
    orientation = property(get_orientation)

    def add_child(self, instance):
        if len(self.children)>1:
            raise Exception("QSplitter can have two child widgets")
        Base.add_child(self, instance)

    def _init_before_parse(self):
        Base._init_before_parse(self)
        self.layout = il.qt.layout.SplitPaneLayout(None,"x")

    def _compile_layout(self, dialect, ret):
        pass

    def _compile_instantiation(self, dialect, ret):
        jsqt.debug_print("\t\tinstantiation")

        instantiation = il.primitive.Assignment()
        instantiation.left = il.primitive.ObjectReference('this.%s' % self.name)
        instantiation.right = il.primitive.Instantiation(self.type,[
            il.primitive.String(self.__orientation.get_value())])

        self.factory_function.add_statement(instantiation)
        self.factory_function.add_statement(il.primitive.VariableDeclaration(
            "retval", il.primitive.ObjectReference("this.%s" % self.name)
        ))

        ret.set_member(self.factory_function.name, self.factory_function)

        self.factory_function.set_return_statement(
                            il.primitive.ObjectReference('retval'))

        ret.set_member(self.name, il.primitive.ObjectReference('null'))

    def _handle_prop_orientation(self, elt):
        self.__orientation = EnumOrientation(elt.find('enum').text)

    known_complex_props = {
        "orientation": _handle_prop_orientation,
    }

class QGroupBox(Base):
    type = "qx.ui.groupbox.GroupBox"
    known_simple_props = {
        "title": SimpleProp("setLegend", il.primitive.TranslatableString),
    }
    layout_in_ctor = False

    def __init__(self, elt, name=None):
        self.layout_properties = None
        Base.__init__(self, elt, name)

class QScrollArea(Base):
    type = "qx.ui.container.Scroll"
    layout_in_ctor = False
    
    def _compile_layout(self, dialect, ret):
        pass

    def add_child(self, instance):
        if len(self.children)>0:
            raise Exception("QScrollArea can have only one child widget")
        Base.add_child(self, instance)
