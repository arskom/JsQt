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

import sys
import os.path

import jsqt

from jsqt import il
import il.qt

from jsqt import DuckTypedList

il.qt.gui.layout_dict = {
    "QVBoxLayout": il.qt.layout.QVBoxLayout,
    "QHBoxLayout": il.qt.layout.QHBoxLayout,
    "QGridLayout": il.qt.layout.QGridLayout,
    "QFormLayout": il.qt.layout.QGridLayout,
}

il.qt.gui.widget_dict = {
    "QDialog": il.qt.container.QDialog,
    "QMainWindow": il.qt.container.QMainWindow,
    "QTabWidget": il.qt.container.QTabWidget,
    "TabPage": il.qt.container.TabPage,
    "QScrollArea": il.qt.container.QScrollArea,
    "QSplitter": il.qt.container.QSplitter,

    "QWidget": il.qt.container.QWidget,
    "QFrame": il.qt.container.QWidget,

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
    "QMenuBar": il.qt.bar.QMenuBar,
    "QMenu": il.qt.bar.MenuButton,
    "QToolBar": il.qt.bar.QToolBar,
    "QTextBrowser": il.qt.form.QTextBrowser,
    "QPlainTextEdit": il.qt.form.QTextEdit,


    #"QDateTimeEdit": NoQooxdooEquivalent,
    #"QTimeEdit": NoQooxdooEquivalent,

    "QTableWidget": il.qt.itemview.QTableWidget,
    "QTableView": il.qt.itemview.QTableWidget,
    "QTreeWidget": il.qt.itemview.QTreeWidget,
    "QTreeView": il.qt.itemview.QTreeWidget,
    "QListWidget": il.qt.itemview.QListWidget,
    "QListView": il.qt.itemview.QListWidget,
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
    def __init__(self,object_name=""):
        self.clazz = il.primitive.ClassDefinition(object_name)
        self.clazz.set_parent(self)
        self.lang = CodeBlocks()
        il.qt.gui.custom_dict = {}

        self.handlers = {
            'ui': self.parse_ui,
            'class': self.parse_class,
            'widget': self.parse_widget,
            'resources': self.parse_resources,
        }
        self.resources = {}
        self.file_name = None

    def parse(self, file_handle, file_name):
        self.file_name = file_name
        tree = etree.parse(file_handle)
        root = tree.getroot()
        self.handlers[root.tag](root)

    def parse_class(self, elt):
        jsqt.debug_print("\tclass:", elt.text)
        if self.clazz.name == "":
            self.clazz.name = elt.text

    def parse_resources(self, elt):
        project_path = os.path.dirname(self.file_name)
        while not (os.path.isfile(os.path.join(project_path,'config.json')) and
                   os.path.isfile(os.path.join(project_path,'Manifest.json'))):
            assert len(project_path) > 0, "Qooxdoo project not found!"
            project_path = os.path.dirname(project_path)

        resource_path = os.path.join(project_path,'source','resource')

        for e in elt.findall("include"):
            location = e.attrib['location']
            resource_file_id = str(e.attrib['location'])
            if location == '-':
                pass

            elif location[0] != '/':
                location = os.path.abspath(os.path.join(
                                     os.path.dirname(self.file_name), location))

            rcc = etree.fromstring(open(location,'r').read())
            if self.resources.get(resource_file_id, None) is None:
                self.resources[resource_file_id] = {}

            assert rcc.tag == "RCC", "%r is not a valid resource file" % location

            for qresource in rcc.findall('qresource'):
                if qresource.attrib['prefix'].startswith('/'):
                    slash = ''
                else:
                    slash = '/'
                resource_id = ":" + slash + str(qresource.attrib['prefix']) + "/"

                for file in qresource.findall('file'):
                    file_id = resource_id + str(file.text)

                    self.resources[resource_file_id][file_id] = os.path.relpath(
                            os.path.join(os.path.dirname(location), file.text),
                            resource_path)

    def parse_ui(self,elt):
        # <customwidgets> tag needs to be parsed first
        for i in range(len(elt)):
            if elt[i].tag == 'customwidgets':
                self.parse_custom_widgets(elt[i])
                del elt[i]
                break

        for e in elt:
            if e.tag in self.handlers:
                self.handlers[e.tag](e)
            else:
                self.parse_unknown_tag(e)

    def parse_widget(self, elt):
        instance = il.qt.gui.widget_dict[elt.attrib['class']](elt)

        set_main_widget = il.primitive.FunctionCall('this.setWidget',
                  [il.primitive.FunctionCall("this.create_%s" % instance.name)])

        self.clazz.ctor.add_statement(set_main_widget)

        self.clazz.set_member(elt.attrib['name'], instance)
        self.clazz.main_widget = instance

    def parse_custom_widgets(self,elt):
        for e in elt:
            base_class = None
            class_name = None
            for f in e:
                if f.tag == "extends":
                    base_class = f.text
                elif f.tag == "class":
                    class_name = f.text

            il.qt.gui.custom_dict[class_name] = type(
                class_name.split('.')[-1],
                il.qt.gui.widget_dict[base_class].__bases__,
                dict(il.qt.gui.widget_dict[base_class].__dict__),
            )

            il.qt.gui.custom_dict[class_name].type= class_name.replace("::",".")

        self.clazz.preamble.append(il.primitive.Comment(
                                "WARNING: '%s' tag is not supported" % elt.tag))

    def parse_unknown_tag(self,elt):
        self.clazz.preamble.append(il.primitive.Comment(
                                "WARNING: '%s' tag is not supported" % elt.tag))
