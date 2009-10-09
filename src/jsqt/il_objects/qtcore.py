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

class QWidget(object):
    def __init__(self, elt):
        self.children = DuckTypedList(['compile'])
        self.__parent = None

        print "\t",elt.tag, elt.attrib

        for e in elt:
            if e.tag == 'property':
                self.set_property(e)
            elif e.tag == 'widget':
                instance = jsqt.parser.widget_dict[e.attrib['class']](e)
                self.add_child(instance)

    def add_child(self, inst):
        self.children.append(inst)

    def compile(self, dialect, ret=None):
        pass

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

    __known_props = {

    }

