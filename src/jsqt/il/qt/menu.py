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
from container import ContainerWithoutLayout, SimpleProp

class QMenuBar(ContainerWithoutLayout):
    type = "qx.ui.menubar.MenuBar"
  
    def add_child(self, instance):
        instance.type = "qx.ui.menubar.Button"

        ContainerWithoutLayout.add_child(self, instance)

class Button(ContainerWithoutLayout):
    type = "qx.ui.menu.Button"
    add_function = "setMenu"
    known_simple_props = {
        "title": SimpleProp("setLabel", il.primitive.TranslatableString, ""),
    }

    def __init__(self, elt, name=None):
        self.menu = None

        ContainerWithoutLayout.__init__(self, elt, name)

    def _compile_sub_menu(self, dialect, ret):
        if self.menu != None:
            set_menu = il.primitive.FunctionCall('retval.setMenu',
                   [il.primitive.FunctionCall("this.create_%s" % self.menu.name)])

            self.factory_function.add_statement(set_menu)

    def compile(self, dialect, ret):
        ContainerWithoutLayout.compile(self, dialect, ret)

        if self.menu != None:
            self.menu.compile(dialect, ret)
        self._compile_sub_menu(dialect, ret)

    def add_child(self, instance):
        if self.menu == None:
            self.menu = QMenu(None, "%s_implicit_menu" % self.name)

        self.menu.add_child(instance)

class QMenu(ContainerWithoutLayout):
    type = "qx.ui.menu.Menu"

