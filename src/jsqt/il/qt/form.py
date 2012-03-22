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

from gui import WidgetBase
from base import SimpleProp
from itemview import MItemView
from jsqt import il

class QLabel(WidgetBase):
    type = "qx.ui.basic.Label"
    known_simple_props = {
        "text": SimpleProp("setValue", il.primitive.TranslatableString, ""),
    }

    def __init__(self, *args, **kwargs):
        WidgetBase.__init__(self, *args, **kwargs)

        self.ver_stretch_pol='Fixed'
        self.hor_stretch_pol='Fixed'

class QPushButton(WidgetBase):
    type = "qx.ui.form.Button"
    known_simple_props = {
        "text": SimpleProp("setLabel", il.primitive.TranslatableString, ""),
        "checked": SimpleProp("setValue", il.primitive.Boolean, ""),
    }

    def __init__(self, *args, **kwargs):
        WidgetBase.__init__(self, *args, **kwargs)

        self.ver_stretch_pol='Fixed'
        self.hor_stretch_pol='Fixed'

    def _handle_checkable(self, elt):
        if elt.find('bool').text == 'true':
            self.type = 'qx.ui.form.ToggleButton'

    known_complex_props = {
        "checkable": _handle_checkable
    }

class QLineEdit(WidgetBase):
    type="qx.ui.form.TextField"
    likes_to_flex = False

    def __init__(self, *args, **kwargs):
        WidgetBase.__init__(self, *args, **kwargs)

        self.ver_stretch_pol='Fixed'

class QTextEdit(WidgetBase):
    type="qx.ui.form.TextArea"

class QTextBrowser(WidgetBase):
    type="qx.ui.embed.Html"

class QSpinBox(WidgetBase):
    type="qx.ui.form.Spinner"
    ver_stretch_pol = "Fixed"

    known_simple_props = {
        "value": SimpleProp("setValue", il.primitive.DecimalInteger),
        "maximum": SimpleProp("setMaximum", il.primitive.DecimalInteger),
        "minimum": SimpleProp("setMinimum", il.primitive.DecimalInteger),
        "singleStep": SimpleProp("setSingleStep", il.primitive.DecimalInteger),
    }

    def __init__(self, *args, **kwargs):
        WidgetBase.__init__(self, *args, **kwargs)

        self.ver_stretch_pol='Fixed'

class QDateEdit(WidgetBase):
    type="qx.ui.form.DateField"

    def __init__(self, *args, **kwargs):
        WidgetBase.__init__(self, *args, **kwargs)

        self.ver_stretch_pol='Fixed'

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
