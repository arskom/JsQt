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
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#


import sys

# http://codespeak.net/lxml/tutorial.html

# the ultra-portable etree import
try:
    from lxml import etree
    print("running with lxml.etree")
except ImportError:
    try: # Python 2.5
        import xml.etree.cElementTree as etree
        print("running with cElementTree on Python 2.5+")
    except ImportError:
        try: # Python 2.5
            import xml.etree.ElementTree as etree
            print("running with ElementTree on Python 2.5+")
        except ImportError:
            try: # normal cElementTree install
                import cElementTree as etree
                print("running with cElementTree")
            except ImportError:
                try: # normal ElementTree install
                    import elementtree.ElementTree as etree
                    print("running with ElementTree")
                except ImportError:
                    print("Failed to import ElementTree from any known place")

import string

import jsqt
import lang
import lang.il_objects
import lang.lang_objects
import lang.dialects
import lang.dialects.qooxdoo

from jsqt.containers import *
from jsqt.widgets import *
from jsqt.layouts import *
from jsqt import Class, Dummy, NoQooxdooEquivalent

try:
    from orderedset import OrderedSet
    JsQtSet=OrderedSet
except: # < python-2.6
    JsQtSet=set
    pass

class_name = ""
layout_dict = {
    "QVBoxLayout": QVBoxLayout,
    "QHBoxLayout": QHBoxLayout,
    "QGridLayout": QGridLayout,
    "QFormLayout": QFormLayout,
}

widget_dict = {
    "QScrollArea": QScrollArea,
    "QTabWidget": QTabWidget,
    "QToolBar": QToolBar,

    "QMainWindow": QMainWindow,
    "QWidget": QWidget,
    "QFrame": QWidget,

    "QDateTimeEdit": NoQooxdooEquivalent,
    "QTimeEdit": NoQooxdooEquivalent,

    "QGraphicsView": QWidget,

    "QTableWidget": QTableWidget,
    "QListWidget": QListWidget,

    "QRadioButton": QRadioButton,
    "QPushButton": QPushButton,
    "QDateEdit": QDateEdit,
    "QLineEdit": QLineEdit,
    "QTextEdit": QTextEdit,
    "QComboBox": QComboBox,
    "QCheckBox": QCheckBox,
    "QGroupBox": QGroupBox,
    "QSpinBox": QSpinBox,
    "QLabel": QLabel,

    "Spacer": Spacer,
    "Class": Class,
}

class UiParser(object):
    def __init__(self,object_name):
        if len(object_name) == 0:
            raise Exception("Empty object_name not allowed")
        self.custom_widgets = {}
        self.source = lang.il_objects.Object(object_name)
        self.lang = []

    def compile(self, dialect):
        self.source.compile(dialect)
        
    def parse(self, file_handle):
        tree = etree.parse(file_handle)
        root = tree.getroot()
        self.handlers[root.tag](self,root)

    def parse_custom_widget(self,element):
        for tag in elt:
            print "\t\t",tag

    def parse_class(self, elt):
        print "\tclass name:", elt.text
        
    def parse_ui(self,elements):
        for i in range(len(elements)):
            if elements[i].tag == 'customwidgets':
                self.parse_custom_widgets(elements[i])
                del elements[i]
                break

        for elt in elements:
            if elt.tag in self.handlers:
                self.handlers[elt.tag](self,elt)
            else:
                self.parse_unknown_tag(elt)

    def parse_widget(self, elements):
        for elt in elements:
            print elt.tag

    def parse_custom_widgets(self,element):
        for elt in element:
            pass

    def parse_unknown_tag(self,elt):
        self.source.ctor.add_statement(lang.il_objects.Comment("WARNING: '%s' tag is not supported" % elt.tag))

    def to_stream(self,os=sys.stdout):
        self.source.to_stream(os)
        
    handlers = {
        'ui': parse_ui,
        'class': parse_class,
        'customwidgets': parse_custom_widgets,
    }

def qx_08(ui_file_name, js_file_name, root_namespace):
    print ui_file_name

    if js_file_name.rfind(root_namespace) == -1:
        raise Exception("root_namespace '%s' not found in class name '%s'" % (
                root_namespace, js_file_name))

    object_name = js_file_name[js_file_name.rfind(root_namespace):].replace("//", "/").replace("/", ".")[0:-3]
    parser=UiParser(object_name)
    parser.parse(ui_file_name)
    parser.compile(lang.dialects.qooxdoo.v0_8_3())


    f=open(js_file_name, 'w')
    parser.to_stream(f)
    f.close()
