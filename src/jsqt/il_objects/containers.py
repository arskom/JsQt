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

from qtcore import QWidget
from lang import MultiPartCompilable
import sys
from jsqt.dialects import javascript
from jsqt.il_objects import lang

class QMainWindow(QWidget, MultiPartCompilable):
    def __init__(self, elt):
        QWidget.__init__(self,elt)
        self.name = elt.attrib['name']

    def compile(self, dialect, ret=None):
        st = lang.Assignment()
        st.set_left(javascript.ObjectReference('this.%s' % self.name))
        st.set_right(javascript.Instantiation('qx.ui.container.Composite'))

        ret.ctor.add_statement(st)



