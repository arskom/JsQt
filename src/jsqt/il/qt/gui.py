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
        self.parent = None
        self.layout = None
        self.type = "qx.ui.container.Composite"

        if name != None:
            if elt != None:
                raise Exception("You should provide either name or elt"
                    "arguments, but not both.")

            self.name = name

        else:
            self.name = elt.attrib['name']
            print "\tQWidget.__init__:",elt.tag, elt.attrib

            self._loop_children(elt)

        self.factory_function = il.primitive.FunctionDefinition(
                                                        "create_%s" % self.name)

    def __setattr__(self,key,val):
        if key == 'main_widget':
            raise Exception("olmaz")
        else:
            object.__setattr__(self,key,val)

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

    def get_instance(self,elt):
        if elt.tag == 'spacer':
            return widget_dict['Spacer'](elt)
        
        else:
            class_name = elt.attrib['class']
            if class_name in widget_dict:
                return widget_dict[class_name](elt)
            else:
                return QWidgetStub(elt)

    def add_child(self, inst):
        self.children.append(inst)
        inst.set_parent(self)

    def set_layout(self, layout):
        self.layout = layout
        layout.set_parent(self)

    def compile(self, dialect, ret):
        factory_function_retval=il.primitive.ObjectReference('this.%s'
                                                                    % self.name)
        instantiation = il.primitive.Assignment()
        instantiation.set_left(factory_function_retval)
        instantiation.set_right(il.primitive.Instantiation(self.type))

        self.factory_function.add_statement(instantiation)

        # layout
        if self.layout != None:
            self.layout.compile(dialect,ret)
            set_layout=il.primitive.FunctionCall('this.%s.setLayout'% self.name,
                   [il.primitive.ObjectReference("this.%s" % self.layout.name)])

            self.factory_function.add_statement(set_layout)

        # children
        for c in self.children:
            c.compile(dialect, ret)
            from jsqt.il.qt.layout import QLayout

            add_children=il.primitive.FunctionCall('this.%s.add' % self.name,
                    [il.primitive.FunctionCall("this.create_%s" % c.name)])

            self.factory_function.add_statement(add_children)

        ret.set_member(self.factory_function.name, self.factory_function)
        self.factory_function.add_statement(il.primitive.Return(
                                                       factory_function_retval))

        ret.set_member(self.name,il.primitive.ObjectReference('null'))

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

