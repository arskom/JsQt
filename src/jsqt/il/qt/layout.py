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

from jsqt import il
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
            return il.primitive.AssociativeArrayInitialization({
                "edge": 0
            })
        else:
            return il.primitive.AssociativeArrayInitialization({
                "top": inst.geometry_top,
                "left": inst.geometry_left,
            })

class QVBoxLayout(QLayout):
    type = "qx.ui.layout.VBox"

    def get_properties(self, elt, inst):
        return il.primitive.AssociativeArrayInitialization(
	                                        {"flex": inst.ver_stretch_coef})

class QHBoxLayout(QLayout):
    type = "qx.ui.layout.HBox"

    def get_properties(self, elt, inst):
        return il.primitive.AssociativeArrayInitialization(
                                                {"flex": inst.hor_stretch_coef})

class AutoExpandingList(list):
    def __getitem__(self, key):
        retval = None

        try:
            retval = list.__getitem__(self,key)

        except IndexError,e:
            self.extend( [None] * (key-len(self)+1))

        return retval

class FlexProp(object):
    def __init__(self, pol, coef):
        self.pol = pol
        self.coef = coef
    def __repr__(self):
        return "FlexProp(pol=%s, coef=%d)" % (self.pol,self.coef)

class QGridLayout(QLayout):
    type = "qx.ui.layout.Grid"

    def __init__(self, *args):
        QLayout.__init__(self, *args)
        self.row_flex=AutoExpandingList()
        self.col_flex=AutoExpandingList()

    def compile(self, dialect, ret):
        QLayout.compile(self, dialect, ret)

        for i in range(len(self.row_flex)):
            if self.row_flex[i] and self.row_flex[i].pol == "Expanding":
                fc = il.primitive.FunctionCall("retval.setRowFlex",
                    [il.primitive.DecimalInteger(i),
                     il.primitive.DecimalInteger(self.row_flex[i].coef)],
                )
                self.factory_function.add_statement(fc)

        for i in range(len(self.col_flex)):
            if self.col_flex[i] and self.col_flex[i].pol == "Expanding":
                fc=il.primitive.FunctionCall("retval.setColumnFlex",
                    [il.primitive.DecimalInteger(i),
                     il.primitive.DecimalInteger(self.col_flex[i].coef)],
                )
                self.factory_function.add_statement(fc)


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
        
        if self.row_flex[retval['row']] == None:
            self.row_flex[retval['row']] = \
                                    FlexProp("Expanding", inst.ver_stretch_coef)

        if self.col_flex[retval['column']] == None:
            self.col_flex[retval['column']] = \
                                    FlexProp("Expanding", inst.hor_stretch_coef)

        if inst.hor_stretch_pol == "Fixed":
            self.row_flex[retval['row']].pol = "Fixed"

        if inst.ver_stretch_pol == "Fixed":
            self.col_flex[retval['column']].pol = "Fixed"

        return il.primitive.AssociativeArrayInitialization(retval)

class SplitPaneLayout(QLayout):
    type = None

    def _compile_instantiation(self, dialect, ret):
        pass

    def get_properties(self, elt, inst):
        if self.parent.orientation == "horizontal":
            return il.primitive.DecimalInteger(inst.hor_stretch_coef)
        elif self.parent.orientation == "vertical":
            return il.primitive.DecimalInteger(inst.ver_stretch_coef)

class DummyLayout(QLayout):
    type = None

    def _compile_instantiation(self, dialect, ret):
        pass
    
    def get_properties(self, elt, inst):
        return il.primitive.AssociativeArrayInitialization({})

    