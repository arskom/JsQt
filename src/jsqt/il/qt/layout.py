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

    def get_properties(self, elt, inst):
        raise Exception("please inherit and override.")

class CanvasLayout(QLayout):
    type = "qx.ui.layout.Canvas"

    def get_properties(self, elt, inst):
        if self.parent == None:
            return {"edge": 0}
        else:
            return {
                "top": inst.geometry_top,
                "left": inst.geometry_left,
            }

class QVBoxLayout(QLayout):
    type = "qx.ui.layout.VBox"

    def get_properties(self, elt, inst):
        return {"flex": inst.ver_stretch_coef}

class QHBoxLayout(QLayout):
    type = "qx.ui.layout.HBox"

    def get_properties(self, elt, inst):
        return {"flex": inst.hor_stretch_coef}

class QGridLayout(QLayout):
    type = "qx.ui.layout.Grid"

    def get_properties(self, elt, inst):
        attr = dict(elt.attrib)

        if not "row" in attr: # FIXME: Hack!
            attr = dict(elt.getparent().attrib)

        map_ = {
            "row": "row",
            "column": "column",
            "colspan": "colSpan",
            "rowspan": "rowSpan",
        }

        retval={}
        for k in attr:
            retval[map_[k]]=int(attr[k])
        
        return retval

class SplitPaneLayout(QLayout):
    type = None

    def _compile_instantiation(self, dialect, ret):
        pass

    def get_properties(self, elt, inst):
        return 1 # FIXME

class TabViewLayout(QLayout):
    type = None

    def _compile_instantiation(self, dialect, ret):
        pass
    
    def get_properties(self, elt, inst):
        return None

    