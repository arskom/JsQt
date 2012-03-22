# encoding: utf8

#
# This file is part of JsQt.
#
# Copyright (C) Arskom Ltd. www.arskom.com.tr
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Ssetoftware Foundation; either version 2
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

from jsqt import il,AutoExpandingList
import obj

class QLayout(obj.Base):
    def __init__(self, elt, name=None):
        obj.Base.__init__(self, elt, name)

    def add_child(self, child):
        raise Exception("layouts don't accept children")

    def _loop_children(self, elt):
        pass

    def _compile_props(self, dialect, ret):
        pass

    def get_properties(self, elt, inst):
        raise Exception("please inherit and override.")

    def meet_child(self, inst):
        pass

    def post_fill_ops(self, dialect, ret, factory_function):
        pass
    
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
        if inst.ver_stretch_pol != "Fixed":
            return il.primitive.AssociativeArrayInitialization(
	                                        {"flex": inst.ver_stretch_coef})
        else:
            return None

class QHBoxLayout(QLayout):
    type = "qx.ui.layout.HBox"

    def get_properties(self, elt, inst):
        if inst.hor_stretch_pol != "Fixed":
            return il.primitive.AssociativeArrayInitialization(
                                                {"flex": inst.hor_stretch_coef})
        else:
            return None

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

    def meet_child(self, inst):
        lp = inst.layout_properties.value
        if self.col_flex[lp['row'].value] == None:
            self.col_flex[lp['row'].value] = \
                                        FlexProp("Fixed", inst.ver_stretch_coef)

        if self.row_flex[lp['column'].value] == None:
            self.row_flex[lp['column'].value] = \
                                        FlexProp("Fixed", inst.hor_stretch_coef)

        if inst.hor_stretch_pol in ("Expanding","Preferred"):
            self.col_flex[lp['row'].value].pol = "Expanding"

        if inst.ver_stretch_pol in ("Expanding","Preferred"):
            self.row_flex[lp['column'].value].pol = "Expanding"

    def post_fill_ops(self, dialect, ret, factory_function):
        factory_function.add_statement(il.primitive.ObjectReference("var layout = retval.getLayout()")) # FIXME: hack

        for i in range(len(self.row_flex)):
            if self.row_flex[i] and self.row_flex[i].pol == "Expanding":
                fc = il.primitive.FunctionCall("layout.setRowFlex",
                    [il.primitive.DecimalInteger(i),
                     il.primitive.DecimalInteger(self.row_flex[i].coef)],
                )
                factory_function.add_statement(fc)

        for i in range(len(self.col_flex)):
            if self.col_flex[i] and self.col_flex[i].pol == "Expanding":
                fc=il.primitive.FunctionCall("layout.setColumnFlex",
                    [il.primitive.DecimalInteger(i),
                     il.primitive.DecimalInteger(self.col_flex[i].coef)],
                )
                factory_function.add_statement(fc)

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
        return None
    