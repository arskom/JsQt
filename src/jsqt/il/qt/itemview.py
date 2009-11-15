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

from gui import WidgetBase
from jsqt import il

class QAbstractItemView(WidgetBase):
    def __init__(self, elt, name=None):
        WidgetBase.__init__(self,elt,name)

class Item(object):
    def __init__(self, name, icon, value):
        object.__init__(self)
        
        self.name = name
        self.icon = icon
        self.value = value
    
    def set_name(self,name):
        if name == None:
            self.__name = il.primitive.ObjectReference("null")
        else:
            self.__name = il.primitive.String(name)

    def set_icon(self,icon):
        if icon == None:
            self.__icon = il.primitive.ObjectReference("null")
        else:
            self.__icon = il.primitive.String(icon)

    def set_value(self, value):
        if value == None:
            self.__value = il.primitive.ObjectReference("null")
        else:
            self.__value = il.primitive.String(value)

    def get_name(self):
        return self.__name

    def get_icon(self):
        return self.__icon

    def get_value(self):
        return self.__value

    name = property(get_name, set_name)
    icon = property(get_icon, set_icon)
    value = property(get_value, set_value)

class MItemView(object):
    def __init__(self):
        self.__items = []

    def compile(self, dialect, elt, function_name = "setLabel"):
        for a in self.__items:
            fc = il.primitive.FunctionCall("retval.add",
                [il.primitive.Instantiation("qx.ui.form.ListItem",
                                                       [a.name,a.icon,a.value])]
            )
            self.factory_function.add_statement(fc)
            

    def add_child(self, elt):
        name = elt[0][0].text
        icon = None
        value = None
        if 'extracomment' in elt[0][0].attrib:
            value = elt[0][0].attrib['extracomment']
        self.__items.append(Item(name,icon,value))

    def _init_before_parse(self):
        self.tag_handlers['item'] = self._handle_item_tag

    def _handle_item_tag(self, elt):
        self.add_child(elt)
        
class QListWidget(QAbstractItemView):
    type = "qx.ui.form.List"

    def __init__(self, elt, name=None):
        WidgetBase.__init__(self,elt,name)

class QTableWidget(QAbstractItemView):
    type="qx.ui.table.Table"
    
    def __init__(self, elt, name=None):
        WidgetBase.__init__(self,elt,name)
        
    def _compile_instantiation(self, dialect, ret):
        factory_function_retval = il.primitive.ObjectReference('retval')
        assignment = il.primitive.Assignment()
        assignment.set_left(factory_function_retval)

        args = [il.primitive.ObjectReference("null")]

        return_tcm = il.primitive.FunctionDefinition("",["obj"])
        return_tcm.set_return_statement(il.primitive.Instantiation(
            "qx.ui.table.columnmodel.Resize",
            [il.primitive.ObjectReference("obj")]
        ))

        args.append(il.primitive.AssociativeArrayInitialization({
            "tableColumnModel": return_tcm
        }))

        #this.tbl_vehicle = new atr.comp.SmallVehicleTable(null,{
        #    tableColumnModel : function(obj) {
        #        return new qx.ui.table.columnmodel.Resize(obj);
        #    }
        #}); // QTableWidget

        instantiation = il.primitive.Instantiation(self.type, args)

        assignment.set_right(instantiation)

        self.factory_function.add_statement(assignment)

        ret.set_member(self.factory_function.name, self.factory_function)
        self.factory_function.set_return_statement(
                            il.primitive.ObjectReference('retval'))

        ret.set_member(self.name, il.primitive.ObjectReference('null'))

class QTreeWidget(QAbstractItemView):
    type="qx.ui.tree.Tree"

