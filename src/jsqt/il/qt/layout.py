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

from gui import ObjectBase

class QLayout(ObjectBase):
    def __init__(self, elt, name=None):
        ObjectBase .__init__(self, elt, name)

    def add_child(self, child):
        raise Exception("layouts don't accept children")

    def _loop_children(self, elt):
        pass

    def _compile_props(self, dialect, ret):
        pass

class CanvasLayout(QLayout):
    type = "qx.ui.layout.Canvas"

class QVBoxLayout(QLayout):
    type = "qx.ui.layout.VBox"

class QHBoxLayout(QLayout):
    type = "qx.ui.layout.HBox"

class QGridLayout(QLayout):
    type = "qx.ui.layout.Grid"

class SplitPaneLayout(QLayout):
    type = None

    def _compile_instantiation(self, dialect, ret):
        pass

class TabViewLayout(QLayout):
    type = None

    def _compile_instantiation(self, dialect, ret):
        pass
