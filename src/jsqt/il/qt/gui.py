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

    def __init__(self, elt, name=None):
        self.children = DuckTypedList(['compile'])
        self.main_widget = False
        self.parent = None
        self.layout = None

        if name != None:
            self.name = name

            if elt != None:
                raise Exception("logic_error: You should provide either name or elt arguments, but not both.")

        else:
            self.name = elt.attrib['name']
            print "\tQWidget.__init__:",elt.tag, elt.attrib

            for e in elt:
                if e.tag == 'property':
                    self.set_property(e)

                elif e.tag == 'item':
                    pass

                else:
                    instance = jsqt.parser.widget_dict[e.attrib['class']](e)
                    if e.tag == 'layout':
                        self.set_layout(instance)
                    else:
                        self.add_child(instance)

    def add_child(self, inst):
        self.children.append(inst)
        inst.set_parent(self)

    def set_layout(self, layout):
        self.layout = layout
        layout.set_parent(self)

    def compile(self, dialect, ret):
        self.__compile_instantiation(dialect,ret)
        self.__compile_layout(dialect,ret)
        self.__compile_children(dialect,ret)

        if self.main_widget:
            ret.ctor.add_statement(set_main_widget)

        ret.set_member(self.name,il.primitive.ObjectReference('null'))

    def __compile_children(self, dialect, ret):
        for c in self.children:
            c.compile(dialect, ret)
            from jsqt.il.qt.layout import QLayout

            add_children=il.primitive.FunctionCall('this.%s.add' % self.name,
                    [il.primitive.ObjectReference("this.%s" % c.name)])

            ret.ctor.add_statement(add_children)

    def __compile_instantiation(self, dialect, ret):
        instantiation = il.primitive.Assignment()
        instantiation.set_left(il.primitive.ObjectReference('this.%s' % self.name))
        instantiation.set_right(il.primitive.Instantiation(self.type))

        set_main_widget=il.primitive.FunctionCall('this.setWidget',
            [il.primitive.ObjectReference("this.%s" % self.name)])

        ret.ctor.add_statement(instantiation)

    def __compile_layout(self, dialect, ret):
        if self.layout == None:
            self.layout = il.qt.layout.CanvasLayout(None,'%s_default_container' % self.name)

        ret.ctor.add_statement(self.layout.compile(dialect))
        set_layout=il.primitive.FunctionCall('this.%s.setLayout' % self.name,
                   [il.primitive.ObjectReference("this.%s" % self.layout.name)])

        ret.ctor.add_statement(set_layout)

    def set_parent(self,parent):
        self.parent = parent

    def is_primitive(self):
        return False

    def set_property(self, elt):
        print "\t\t", elt.tag, elt.attrib

        prop_name = elt.attrib['name']
        if prop_name in self.known_props:
            QWidget.known_props[prop_name](elt)
        else:
            pass #QWidget.set_property(self,elt)

    def set_main_widget(self, what):
        self.main_widget = what

    known_props = {

    }

