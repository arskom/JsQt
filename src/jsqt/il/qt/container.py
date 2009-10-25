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

from gui import QWidget
from jsqt import il

class QMainWindow(QWidget):
    def __init__(self, elt, name=None):
        QWidget.__init__(self,elt,name)

class QTabWidget(QWidget):
    def __init__(self, elt, name=None):
        QWidget.__init__(self,elt,name)

        self.type = "qx.ui.tabview.TabView"

    def _handle_widget_tag(self, elt):
        elt.set("class", "TabPage")
        QWidget._handle_widget_tag(self,elt)

class TabPage(QWidget):
    def __init__(self, elt, name=None):
        QWidget.__init__(self,elt,name)

        self.type = "qx.ui.tabview.Page"

    def _compile_layout(self, dialect, ret):
        if self.layout == None:
            self.layout = il.qt.layout.CanvasLayout(None, "%s_implicit_layout"
                                                                    % self.name)
        QWidget._compile_layout(self,dialect,ret)

class QGroupBox(QWidget):
    def __init__(self, elt, name=None):
        QWidget.__init__(self,elt,name)

        self.type = "qx.ui.groupbox.GroupBox"


