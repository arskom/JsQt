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

import jsqt.parser
from jsqt import DuckTypedList
from jsqt import il


class QWidget(il.primitive.MultiPartCompilable):
    type = "qx.ui.container.Composite"

    def __init__(self, elt):
        self.children = DuckTypedList(['compile'])
        self.__main_widget = False
        self.__parent = None

        print "\tQWidget.__init__:",elt.tag, elt.attrib

        self.name = elt.attrib['name']

        for e in elt:
            if e.tag == 'property':
                self.set_property(e)

            elif e.tag == 'item':
                pass
            
            else:
                instance = jsqt.parser.widget_dict[e.attrib['class']](e)
                self.add_child(instance)

    def add_child(self, inst):
        self.children.append(inst)

    def compile(self, dialect, ret=None):
        instantiation = il.primitive.Assignment()
        instantiation.set_left(il.primitive.ObjectReference('this.%s' % self.name))
        instantiation.set_right(il.primitive.Instantiation(self.type))

        set_main_widget=il.primitive.FunctionCall('this.setWidget',
            [il.primitive.ObjectReference("this.%s" % self.name)])

        ret.ctor.add_statement(instantiation)

        for c in self.children:
            c.compile(dialect, ret)

        if self.__main_widget:
            ret.ctor.add_statement(set_main_widget)

        ret.set_member(self.name,il.primitive.ObjectReference('null'))

    def set_parent(self,parent):
        self.__parent = parent

    def is_primitive(self):
        return False

    def set_property(self, elt):
        print "\t\t", elt.tag, elt.attrib

        prop_name = elt.attrib['name']
        if prop_name in self.__known_props:
            QWidget.__known_props[prop_name](elt)
        else:
            pass #QWidget.set_property(self,elt)

    def set_main_widget(self, what):
        self.__main_widget = what

    __known_props = {

    }

