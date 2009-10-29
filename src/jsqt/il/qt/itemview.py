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

import jsqt
from jsqt import il

class QAbstractItemView(WidgetBase):
    def __init__(self, elt, name=None):
        WidgetBase.__init__(self,elt,name)

class MItemView(object):
    def __init__(self):
        self.__items = []

    def compile(self, dialect, elt, function_name = "setLabel"):
        for a in self.__items:
            fc = il.primitive.FunctionCall("this.%s.add" % (self.name),
                [
                    il.primitive.Instantiation("qx.ui.form.ListItem",
                        [il.primitive.String(a)])
                ],
            )
            self.factory_function.add_statement(fc)
            

    def add_child(self, elt):
        self.__items.append(elt[0][0].text)

    def _init_before_parse(self):
        self.tag_handlers['item'] = self._handle_item_tag

    def _handle_item_tag(self, elt):
        jsqt.debug_print("\t\t",elt[0].tag,elt[0].attrib, "%s: '%s'"
                                              % (elt[0][0].tag, elt[0][0].text))
        self.__items.append(elt[0][0].text)

class QListWidget(QAbstractItemView):
    type = "qx.ui.form.List"

    def __init__(self, elt, name=None):
        WidgetBase.__init__(self,elt,name)


class QTableWidget(QAbstractItemView):
    type="qx.ui.table.Table"
    
    def __init__(self, elt, name=None):
        WidgetBase.__init__(self,elt,name)
        
    def _compile_instantiation(self, dialect, ret):
        factory_function_retval = il.primitive.ObjectReference('this.%s'
                                                                    % self.name)
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
                            il.primitive.ObjectReference('this.%s' % self.name))

        ret.set_member(self.name, il.primitive.ObjectReference('null'))

