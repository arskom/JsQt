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

from jsqt import il

class MWithCaption(object):
    def __init__(self, attr_name="text"):
        self.__caption = None
        self.__known_props = {
            attr_name: self.__handle_text
        }

    def __handle_text(self, elt):
        self.__caption = elt[0].text

    def _set_function_name(self, function_name):
        self.__function_name = function_name

    def compile(self, dialect, elt, function_name = "setLabel"):
        if self.__caption != None:
            fc = il.primitive.FunctionCall("this.%s.%s" %
                (self.name, function_name),
                [il.primitive.String(self.__caption)],
            )
            self.factory_function.add_statement(fc)

    def set_property(self, elt):
        prop_name = elt.attrib['name']
        if prop_name in self.__known_props:
            self.__known_props[prop_name](elt)

class QLabel(WidgetBase, MWithCaption):
    def __init__(self, elt, name=None):
        MWithCaption.__init__(self)
        WidgetBase.__init__(self,elt,name)

        self.type = "qx.ui.basic.Label"

    def compile(self, dialect, ret):
        WidgetBase.compile(self, dialect, ret)
        MWithCaption.compile(self, dialect, ret, "setValue")

    def set_property(self, elt):
        WidgetBase.set_property(self, elt)
        MWithCaption.set_property(self, elt)

class QPushButton(WidgetBase, MWithCaption):
    def __init__(self, elt, name=None):
        MWithCaption.__init__(self)
        WidgetBase.__init__(self,elt,name)

        self.type = "qx.ui.form.Button"

    def compile(self, dialect, ret):
        WidgetBase.compile(self, dialect, ret)
        MWithCaption.compile(self, dialect, ret)

    def set_property(self, elt):
        WidgetBase.set_property(self, elt)
        MWithCaption.set_property(self, elt)

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

class QCheckBox(WidgetBase,MWithCaption):
    def __init__(self, elt, name=None):
        MWithCaption.__init__(self)
        WidgetBase.__init__(self,elt,name)

        self.type="qx.ui.form.CheckBox"

    def compile(self, dialect, ret):
        WidgetBase.compile(self, dialect, ret)
        MWithCaption.compile(self, dialect, ret)

    def set_property(self, elt):
        WidgetBase.set_property(self, elt)
        MWithCaption.set_property(self, elt)

class QRadioButton(WidgetBase,MWithCaption):
    def __init__(self, elt, name=None):
        MWithCaption.__init__(self)
        WidgetBase.__init__(self,elt,name)

        self.type="qx.ui.form.RadioButton"

    def compile(self, dialect, ret):
        WidgetBase.compile(self, dialect, ret)
        MWithCaption.compile(self, dialect, ret)

    def set_property(self, elt):
        WidgetBase.set_property(self, elt)
        MWithCaption.set_property(self, elt)

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


