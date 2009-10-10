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

import sys

from jsqt import il
from jsqt.il.qtcore import QWidget
from jsqt.il.primitives import MultiPartCompilable

class QMainWindow(QWidget, MultiPartCompilable):
    def __init__(self, elt):
        QWidget.__init__(self,elt)
        self.name = elt.attrib['name']

    def compile(self, dialect, ret=None):
        st = il.primitives.Assignment()
        st.set_left(il.primitives.ObjectReference('this.%s' % self.name))
        st.set_right(il.primitives.Instantiation('qx.ui.container.Composite'))

        ret.ctor.add_statement(st)
        ret.members[self.name] = il.primitives.ObjectReference('null')

        ret.set_member(self.name,il.primitives.ObjectReference('null'))




