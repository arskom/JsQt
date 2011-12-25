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

from jsqt import il
import container
import obj
from base import SimpleProp
    
class QMenuBar(container.WithoutLayout):
    type = "qx.ui.menubar.MenuBar"
    ver_stretch_pol = "Fixed"

    def add_child(self, instance):
        instance.type = "qx.ui.menubar.Button"

        container.WithoutLayout.add_child(self, instance)

class MenuSeparator(obj.Base):
    def __init__(self):
        obj.Base.__init__(self, None, "dummy_layout")
        self.real = False

    def _compile_instantiation(self, dialect, ret):
        pass

    def compile(self, dialect, ret):
        add_separator = il.primitive.FunctionCall('retval.addSeparator')
        self.parent.factory_function.add_statement(add_separator)

class MenuButton(container.WithoutLayout):
    type = "qx.ui.menu.Button"
    add_function = "setMenu"
    known_simple_props = {
        "title": SimpleProp("setLabel", il.primitive.TranslatableString, ""),
    }

    def __init__(self, elt, name=None, action=None):
        self.menu = None

        container.WithoutLayout.__init__(self, elt, name)

    def _init_before_parse(self):
        container.WithoutLayout._init_before_parse(self)
        self.tag_handlers['addaction'] = self._handle_addaction_tag

    def _handle_addaction_tag(self, elt):
        if self.menu == None:
            self.menu = QMenu(None, "%s_implicit_menu" % self.name)

        self.menu._handle_addaction_tag(elt)

    def _compile_sub_menu(self, dialect, ret):
        set_menu = il.primitive.FunctionCall('retval.setMenu',
                 [il.primitive.FunctionCall("this.create_%s" % self.menu.name)])

        self.factory_function.add_statement(set_menu)

    def compile(self, dialect, ret):
        container.WithoutLayout.compile(self, dialect, ret)

        if self.menu != None:
            self.menu.compile(dialect, ret)
            self._compile_sub_menu(dialect, ret)

    def add_child(self, instance):
        if self.menu == None:
            self.menu = QMenu(None, "%s_implicit_menu" % self.name)

        if instance.name == "separator":
            raise Exception("As there is no way to tell a non-leaf menu item "
                "named 'separator' from a real separator, you are not allowed "
                "to add a menu item named 'separator'. Sorry.")

        self.menu.add_child_action(instance)

class Bar(container.WithoutLayout):
    def __init__(self, elt, name=None):
        self.actions = []
        self.child_actions = {}

        container.WithoutLayout.__init__(self, elt, name)

    def _handle_addaction_tag(self, elt):
        self.actions.append(elt.attrib['name'])

    def add_child_action(self, inst):
        self.child_actions[inst.name] = inst

    def compile(self, dialect, ret):
        for a in self.actions:
            if a == "separator":
                self.add_child(self.Separator())

            elif a in ret.main_widget.actions:
                action = ret.main_widget.actions[a]
                button = self.Button(None, action.name + self.suffix, action)
                button.simple_prop_data['title'] = action.prop_text
                self.add_child(button)

            else:
                self.add_child(self.child_actions[a])

        container.WithoutLayout.compile(self, dialect, ret)


class QMenu(Bar):
    type = "qx.ui.menu.Menu"
    Button = MenuButton
    suffix = "_menu"
    Separator = MenuSeparator


class ToolBarSeparator(obj.Base):
    def __init__(self):
        obj.Base.__init__(self, None, "dummy_layout")
        self.real = False

    def _compile_instantiation(self, dialect, ret):
        pass

    def compile(self, dialect, ret):
        add_separator = il.primitive.FunctionCall('retval.add',
                         [il.primitive.Instantiation('qx.ui.toolbar.Separator')])
        self.parent.factory_function.add_statement(add_separator)


class ToolBarButton(obj.Base):
    type = "qx.ui.toolbar.Button"
    known_simple_props = {
        "title": SimpleProp("setLabel", il.primitive.TranslatableString, ""),
    }

    def __init__(self, elt, name=None, action=None):
        obj.Base.__init__(self, elt, name)
        if action and action.checkable:
            self.type = 'qx.ui.toolbar.CheckBox'
        self.icons.base = action.icons.base


class QToolBar(Bar):
    type = "qx.ui.toolbar.ToolBar"
    ver_stretch_pol = "Fixed"
    Button = ToolBarButton
    suffix = "_toolbar"
    Separator = ToolBarSeparator

    def _init_before_parse(self):
        container.WithoutLayout._init_before_parse(self)
        self.tag_handlers['addaction'] = self._handle_addaction_tag

    def __handle_toolbar_area(self, elt):
        self.toolbar_area = elt[0].text

    known_complex_props = {
        "toolBarArea": __handle_toolbar_area,
    }
