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

from gui import WidgetBase

class QLabel(WidgetBase):
    def __init__(self, elt, name=None):
        WidgetBase.__init__(self,elt,name)

        self.type="qx.ui.basic.Label"

class QPushButton(WidgetBase):
    def __init__(self, elt, name=None):
        WidgetBase.__init__(self,elt,name)

        self.type = "qx.ui.form.Button"

class QLabel(WidgetBase):
    def __init__(self, elt, name=None):
        WidgetBase.__init__(self,elt,name)

        self.type="qx.ui.basic.Label"

class QLineEdit(WidgetBase):
    def __init__(self, elt, name=None):
        WidgetBase.__init__(self,elt,name)

        self.type="qx.ui.form.TextField"

class QTextEdit(WidgetBase):
    def __init__(self, elt, name=None):
        WidgetBase.__init__(self,elt,name)

        self.type="qx.ui.form.TextArea"

class QSpinBox(WidgetBase):
    def __init__(self, elt, name=None):
        WidgetBase.__init__(self,elt,name)

        self.type="qx.ui.form.Spinner"

class QDateEdit(WidgetBase):
    def __init__(self, elt, name=None):
        WidgetBase.__init__(self,elt,name)

        self.type="qx.ui.form.DateField"

class QCheckBox(WidgetBase):
    def __init__(self, elt, name=None):
        WidgetBase.__init__(self,elt,name)

        self.type="qx.ui.form.CheckBox"

class QRadioButton(WidgetBase):
    def __init__(self, elt, name=None):
        WidgetBase.__init__(self,elt,name)

        self.type="qx.ui.form.RadioButton"

class QComboBox(WidgetBase):
    def __init__(self, elt, name=None):
        self.items = []
        try:
            self.tag_handlers
        except:
            self.tag_handlers = {}

        self.tag_handlers['item'] = self._handle_item_tag

        self.type = "qx.ui.form.SelectBox"

        WidgetBase.__init__(self,elt,name)


    def _handle_item_tag(self, elt):
        print "\t\t",elt[0].tag,elt[0].attrib, "%s: '%s'" %(elt[0][0].tag,
                                                                 elt[0][0].text)
        self.items.append(elt[0][0].text)

class QSpacer(WidgetBase):
    def __init__(self, elt, name=None):
        WidgetBase.__init__(self,elt,name)

        self.type = "qx.ui.core.Spacer"


