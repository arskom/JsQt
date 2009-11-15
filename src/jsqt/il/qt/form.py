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

from gui import WidgetBase, SimpleProp
from itemview import MItemView
from jsqt import il

class QLabel(WidgetBase):
    type = "qx.ui.basic.Label"
    known_simple_props = {
        "text": SimpleProp("setValue", il.primitive.TranslatableString),
    }

class QPushButton(WidgetBase):
    type = "qx.ui.form.Button"
    known_simple_props = {
        "text": SimpleProp("setLabel", il.primitive.TranslatableString),
    }

class QLineEdit(WidgetBase):
    type="qx.ui.form.TextField"
    likes_to_flex = False

class QTextEdit(WidgetBase):
    type="qx.ui.form.TextArea"

class QSpinBox(WidgetBase):
    type="qx.ui.form.Spinner"
    ver_stretch_pol = "Fixed"

    known_simple_props = {
        "value": SimpleProp("setValue", il.primitive.DecimalInteger),
        "maximum": SimpleProp("setMaximum", il.primitive.DecimalInteger),
        "minimum": SimpleProp("setMinimum", il.primitive.DecimalInteger),
        "singleStep": SimpleProp("setSingleStep", il.primitive.DecimalInteger),
    }

class QDateEdit(WidgetBase):
    type="qx.ui.form.DateField"

class QCheckBox(WidgetBase):
    type="qx.ui.form.CheckBox"
    known_simple_props = {
        "text": SimpleProp("setLabel", il.primitive.TranslatableString),
        "checked": SimpleProp("setValue", il.primitive.Boolean),
    }

class QRadioButton(WidgetBase):
    type="qx.ui.form.RadioButton"
    known_simple_props = {
        "text": SimpleProp("setLabel", il.primitive.TranslatableString),
        "checked": SimpleProp("setValue", il.primitive.Boolean),
    }
    
class QComboBox(WidgetBase, MItemView):
    type = "qx.ui.form.SelectBox"
    ver_stretch_pol = "Fixed"

    def __init__(self, elt, name=None):
        MItemView.__init__(self)
        WidgetBase.__init__(self,elt,name)

    def _init_before_parse(self):
        MItemView._init_before_parse(self)
        WidgetBase._init_before_parse(self)

    def compile(self, dialect, ret):
        WidgetBase.compile(self, dialect, ret)
        MItemView.compile(self, dialect, ret)

