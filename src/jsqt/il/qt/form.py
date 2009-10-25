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

class QLabel(QWidget):
    def __init__(self, elt, name=None):
        QWidget.__init__(self,elt,name)

        self.type="qx.ui.basic.Label"

class QPushButton(QWidget):
    def __init__(self, elt, name=None):
        QWidget.__init__(self,elt,name)

        self.type = "qx.ui.form.Button"

class QLabel(QWidget):
    def __init__(self, elt, name=None):
        QWidget.__init__(self,elt,name)

        self.type="qx.ui.basic.Label"

class QLineEdit(QWidget):
    def __init__(self, elt, name=None):
        QWidget.__init__(self,elt,name)

        self.type="qx.ui.form.TextField"

class QTextEdit(QWidget):
    def __init__(self, elt, name=None):
        QWidget.__init__(self,elt,name)

        self.type="qx.ui.form.TextArea"

class QSpinBox(QWidget):
    def __init__(self, elt, name=None):
        QWidget.__init__(self,elt,name)

        self.type="qx.ui.form.Spinner"

class QDateEdit(QWidget):
    def __init__(self, elt, name=None):
        QWidget.__init__(self,elt,name)

        self.type="qx.ui.form.DateField"

class QCheckBox(QWidget):
    def __init__(self, elt, name=None):
        QWidget.__init__(self,elt,name)

        self.type="qx.ui.form.CheckBox"

class QRadioButton(QWidget):
    def __init__(self, elt, name=None):
        QWidget.__init__(self,elt,name)

        self.type="qx.ui.form.RadioButton"

class QComboBox(QWidget):
    def __init__(self, elt, name=None):
        self.items = []
        QWidget.__init__(self,elt,name)

        self.type = "qx.ui.form.SelectBox"

    def _handle_item_tag(self, elt):
        print "\t\t",elt[0].tag,elt[0].attrib, "%s: '%s'" %(elt[0][0].tag,
                                                                 elt[0][0].text)
        self.items.append(elt[0][0].text)

class QSpacer(QWidget):
    def __init__(self, elt, name=None):
        QWidget.__init__(self,elt,name)

        self.type = "qx.ui.core.Spacer"


