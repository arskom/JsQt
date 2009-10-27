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

import sys

from jsqt import il
import il.qt
from jsqt import DuckTypedList, JsPp

il.qt.gui.layout_dict = {
    "QVBoxLayout": il.qt.layout.QVBoxLayout,
    "QHBoxLayout": il.qt.layout.QHBoxLayout,
    "QGridLayout": il.qt.layout.QGridLayout,
    "QFormLayout": il.qt.layout.QGridLayout,
}

il.qt.gui.widget_dict = {
    "QMainWindow": il.qt.container.QMainWindow,
    "QTabWidget": il.qt.container.QTabWidget,
    "TabPage": il.qt.container.TabPage,
    "QScrollArea": il.qt.container.QScrollArea,

    "QWidget": il.qt.gui.QWidget,
    "QFrame": il.qt.gui.QWidget,

    "QRadioButton": il.qt.form.QRadioButton,
    "QPushButton": il.qt.form.QPushButton,
    "QDateEdit": il.qt.form.QDateEdit,
    "QLineEdit": il.qt.form.QLineEdit,
    "QTextEdit": il.qt.form.QTextEdit,
    "QComboBox": il.qt.form.QComboBox,
    "QCheckBox": il.qt.form.QCheckBox,
    "QSpinBox": il.qt.form.QSpinBox,
    "QGroupBox": il.qt.container.QGroupBox,
    "QLabel": il.qt.form.QLabel,
    "Spacer": il.qt.gui.QSpacer,

    #"QDateTimeEdit": NoQooxdooEquivalent,
    #"QTimeEdit": NoQooxdooEquivalent,

    "QTableWidget": il.qt.itemview.QTableWidget,
    "QListWidget": il.qt.itemview.QListWidget,
}

# http://codespeak.net/lxml/tutorial.html

from jsqt.xml import etree

class_name = ""

class CodeBlocks(DuckTypedList):
    def __init__(self):
        DuckTypedList.__init__(self,['to_stream'])
    def to_stream(self, os=sys.stdout):
        for l in self:
            l.to_stream(os)

class UiParser(object):
    def __init__(self,object_name):
        if len(object_name) == 0:
            raise Exception("Empty object_name not allowed")
        self.custom_widgets = {}
        self.clazz = il.primitive.ClassDefinition(object_name)
        self.lang = CodeBlocks()

        self.handlers = {
            'ui': self.parse_ui,
            'class': self.parse_class,
            'widget': self.parse_widget,
            'customwidgets': self.parse_custom_widgets,
        }


    def compile(self, dialect):
        for l in self.clazz.compile(dialect):
            self.lang.append(l)
        
    def parse(self, file_handle):
        tree = etree.parse(file_handle)
        root = tree.getroot()
        self.handlers[root.tag](root)

    def parse_custom_widget(self,element):
        for tag in elt:
            print "\t\t",tag

    def parse_class(self, elt):
        print "\tclass:", elt.text
        
    def parse_ui(self,elements):
        # <customwidgets> tag needs to be parsed first
        for i in range(len(elements)):
            if elements[i].tag == 'customwidgets':
                self.parse_custom_widgets(elements[i])
                del elements[i]
                break

        for elt in elements:
            if elt.tag in self.handlers:
                self.handlers[elt.tag](elt)
            else:
                self.parse_unknown_tag(elt)

    def __get_instance(self, elt):
        return 

    def parse_widget(self, elt):
        instance = il.qt.gui.widget_dict[elt.attrib['class']](elt)
        set_main_widget=il.primitive.FunctionCall('this.setWidget',
                  [il.primitive.FunctionCall("this.create_%s" % instance.name)])
        self.clazz.ctor.add_statement(set_main_widget)

        self.clazz.set_member(elt.attrib['name'], instance)

    def parse_custom_widgets(self,elt):
        self.clazz.preamble.append(il.primitive.Comment("WARNING: '%s' tag is not supported" % elt.tag))

    def parse_unknown_tag(self,elt):
        self.clazz.preamble.append(il.primitive.Comment("WARNING: '%s' tag is not supported" % elt.tag))

def compile(ui_file_name, js_file_name, root_namespace, dialect):
    print ui_file_name

    if js_file_name.rfind(root_namespace) == -1:
        raise Exception("root_namespace '%s' not found in class name '%s'" % (
                root_namespace, js_file_name))

    object_name = js_file_name[js_file_name.rfind(root_namespace):].replace("//", "/").replace("/", ".")[0:-3]
    parser=UiParser(object_name)
    parser.parse(ui_file_name)
    compiled_object = parser.clazz.compile(dialect)

    f=open(js_file_name, 'w')
    compiled_object.to_stream(JsPp(f))
    f.close()

