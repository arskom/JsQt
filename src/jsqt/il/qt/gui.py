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

from jsqt import DuckTypedList

widget_dict = {

}

class QWidget(il.primitive.MultiPartCompilable):
    def __init__(self, elt, name=None):
        self.children = DuckTypedList(['compile'])
        self.main_widget = False
        self.parent = None
        self.layout = None
        self.type = "qx.ui.container.Composite"

        if name != None:
            self.name = name

            if elt != None:
                raise Exception("logic_error: You should provide either name or elt arguments, but not both.")

        else:
            self.name = elt.attrib['name']
            print "\tQWidget.__init__:",elt.tag, elt.attrib

            self._loop_children(elt)

    def _loop_children(self, elt):
        for e in elt:
            if e.tag == 'item':
                self._loop_children(e)

            elif e.tag in ('property', 'attribute'):
                self.set_property(e)

            elif e.tag == 'layout':
                instance = self.get_instance(e)
                self.set_layout(instance)
                self._loop_children(e)

            else:
                instance = self.get_instance(e)
                self.add_child(instance)

    def get_instance(self,e):
        if e.tag == 'spacer':
            return widget_dict['Spacer'](e)
        
        else:
            class_name = e.attrib['class']
            if class_name in widget_dict:
                return widget_dict[class_name](e)
            else:
                return QWidgetStub(e)

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
            set_main_widget=il.primitive.FunctionCall('this.setWidget',
                [il.primitive.ObjectReference("this.%s" % self.name)])
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

        ret.ctor.add_statement(instantiation)

    def __compile_layout(self, dialect, ret):
        if self.layout != None:
            self.layout.compile(dialect,ret)
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

class QSpacer(QWidget):
    def __init__(self, elt, name=None):
        QWidget.__init__(self, elt,name)

        self.type = "qx.ui.core.Spacer"

class QWidgetStub(QWidget):
    def __init__(self, elt, name=None):
        QWidget.__init__(self,elt,name)

        self.class_name = elt.attrib['class']

    def compile(self, dialect, ret=None):
        ret.ctor.add_statement(
            il.primitive.Comment("'%s' widget is not supported in instance type '%s'" %
                (self.class_name, self.name)))

