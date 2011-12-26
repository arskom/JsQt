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

import re

from base import SimpleProp
from gui import WidgetBase
from jsqt import il
from obj import Base


class EnumSelectionMode(il.primitive.Enum):
    value_map = {
        "QAbstractItemView::SingleSelection": il.primitive.String("single"),
        "QAbstractItemView::ExtendedSelection": il.primitive.String("additive"),
        "QAbstractItemView::ContiguousSelection": il.primitive.String("multi"),
        "QAbstractItemView::MultiSelection": il.primitive.String("additive"),
        "QAbstractItemView::NoSelection": il.primitive.String("single"),
    }


class Item(Base):
    counter = 0

    def __init__(self, elt, name=None):
        if name is None:
            Item.counter += 1
            elt.attrib['name'] = 'item_%d' % self.counter

        self.value = None
        self.text = None

        Base.__init__(self, elt, name)

    def _handle_text(self, elt):
        string = elt.find('string')

        self.text = unicode(string.text)
        self.name = "item_%s" % re.sub(r'[^\w]', '_', self.text).lower()
        if 'extracomment' in string.attrib:
            self.value = unicode(string.attrib['extracomment'])
            self.name = "item_%s" % re.sub(r'[^\w]', '_', self.value).lower()


    def _compile_instantiation(self, dialect, ret):
        Base._compile_instantiation(self, dialect, ret)
        if self.text is None:
            text = il.primitive.ObjectReference("null")
        else:
            text = il.primitive.TranslatableString(self.text)

        if self.value == None:
            value = il.primitive.ObjectReference("null")
        else:
            value = il.primitive.String(self.value)

        self.instantiation.right.args.append(text)
        self.instantiation.right.args.append(il.primitive.ObjectReference("null"))
        self.instantiation.right.args.append(value)

    known_complex_props = {
        "text": _handle_text
    }


class QAbstractItemView(WidgetBase):
    add_function_name = 'add'
    known_simple_props = {
        "selectionMode": SimpleProp("setSelectionMode", EnumSelectionMode),
    }

    def _handle_item(self, elt):
        item = self.Item(elt)
        item.set_parent(self)
        self.children.append(item)

    def _compile_children(self, dialect, ret):
        for c in self.children:
            c.compile(dialect, ret)
            args = [il.primitive.FunctionCall("this.create_%s" % c.name)]
            add_child = il.primitive.FunctionCall('retval.%s' %
                                                self.add_function_name, args)
            self.factory_function.add_statement(add_child)

    def compile(self, dialect, ret):
        WidgetBase.compile(self, dialect, ret)
        self._compile_children(dialect, ret)

    def _init_before_parse(self):
        self.tag_handlers['item'] = self._handle_item


class ListItem(Item):
    type = "qx.ui.form.ListItem"

class QListWidget(QAbstractItemView):
    type = "qx.ui.form.List"
    Item = ListItem


class TreeItem(Item):
    type = "qx.ui.tree.TreeFolder"

    def _handle_item(self, elt):
        item = TreeItem(elt)
        item.set_parent(self)
        self.children.append(item)

    def _compile_children(self, dialect, ret):
        for c in self.children:
            c.compile(dialect, ret)
            args = [il.primitive.FunctionCall("this.create_%s" % c.name)]
            add_child = il.primitive.FunctionCall('retval.add', args)
            self.factory_function.add_statement(add_child)

    def compile(self, dialect, ret):
        if len(self.children) == 0:
            self.type = "qx.ui.tree.TreeFile"

        Item.compile(self, dialect, ret)
        self._compile_children(dialect, ret)

    def _init_before_parse(self):
        self.tag_handlers['item'] = self._handle_item

class QTreeWidget(QAbstractItemView):
    type = "qx.ui.tree.Tree"
    Item = TreeItem
    add_function_name = 'setRoot'

    def _compile_children(self, dialect, ret):
        assert len(self.children) == 1, "Qooxdoo only supports one child in a " \
                                        "tree widget."
        QAbstractItemView._compile_children(self, dialect, ret)

class QTableWidget(WidgetBase):
    type = "qx.ui.table.Table"


# DEPRECATED
class _Item(object):
    def __init__(self, name, icon, value):
        object.__init__(self)

        self.name = name
        self.icon = icon
        self.value = value

    def set_name(self, name):
        if name == None:
            self.__name = il.primitive.ObjectReference("null")
        else:
            self.__name = il.primitive.TranslatableString(name)

    def set_icon(self, icon):
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

    def compile(self, dialect, elt, function_name="setLabel"):
        for a in self.__items:
            fc = il.primitive.FunctionCall("retval.add",
                    [il.primitive.Instantiation("qx.ui.form.ListItem",
                                                    [a.name, a.icon, a.value])])
            self.factory_function.add_statement(fc)

    def add_child(self, elt):
        name = elt[0][0].text
        icon = None
        value = None
        if 'extracomment' in elt[0][0].attrib:
            value = elt[0][0].attrib['extracomment']
        self.__items.append(_Item(name, icon, value))

    def _init_before_parse(self):
        self.tag_handlers['item'] = self._handle_item_tag

    def _handle_item_tag(self, elt):
        self.add_child(elt)
