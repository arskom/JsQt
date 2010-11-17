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

from gui import WidgetBase
from jsqt import il
from base import SimpleProp

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
            self.__name = il.primitive.TranslatableString(name)

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

class EnumSelectionMode(il.primitive.Enum):
    value_map = {
        "QAbstractItemView::SingleSelection": il.primitive.String("single"),
        "QAbstractItemView::ContiguousSelection": il.primitive.String("multi"),
        "QAbstractItemView::ExtendedSelection": il.primitive.String("additive"),
        "QAbstractItemView::MultiSelection": il.primitive.String("additive"),
        "QAbstractItemView::NoSelection": il.primitive.String("single"),
    }

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
        
class QListWidget(QAbstractItemView, MItemView):
    type = "qx.ui.form.List"

    def __init__(self, elt, name=None):
        MItemView.__init__(self)
        QAbstractItemView.__init__(self,elt,name)

    def _init_before_parse(self):
        MItemView._init_before_parse(self)
        QAbstractItemView._init_before_parse(self)

    def compile(self, dialect, ret):
        QAbstractItemView.compile(self, dialect, ret)
        MItemView.compile(self, dialect, ret)

    known_simple_props = {
        "selectionMode": SimpleProp("setSelectionMode", EnumSelectionMode),
    }

class QTableWidget(QAbstractItemView):
    type="qx.ui.table.Table"
    
    def __init__(self, elt, name=None):
        WidgetBase.__init__(self,elt,name)
        
class QTreeWidget(QAbstractItemView):
    type="qx.ui.tree.Tree"
