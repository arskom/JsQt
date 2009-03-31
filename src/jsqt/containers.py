# encoding: utf8

#
# This file is part of JsQT.
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

from widgets import Widget
from layouts import *

class Container(Widget):
    layout = None
    in_layout = False

    def __init__(self, caller, name, class_name):
        Widget.__init__(self, caller, name, class_name)
        
        self.in_layout = False
                        
    def set_window_title(self, text):
        self.buffer.append('        // this.%(self_name)s.setWindowTitle("%(text)s"); // TODO:' % {'self_name': self.name(), 'text': str(text)})
    
    def set_layout(self, layout):
        self.layout = layout
        self.buffer.append('        this.%(self_name)s.setLayout(this.%(layout_name)s);' % {'self_name': self.name(), 'layout_name': layout.name()})
        self.in_layout = True

    def add_widget(self, widget, **kwargs):
        if self.layout == None:
            self.set_layout(CanvasLayout(self.caller, self.name() + "_implicit_container"))
        
        self.children.append(widget)
        self.layout.add_widget(self, widget, **kwargs)
        
class QGroupBox(Container):
    def __init__(self, caller, name, class_name=""):
        self.type = "qx.ui.groupbox.GroupBox"
        Widget.__init__(self, caller, name, class_name)
        
        self.layout = None
        self.register_handlers()

        self.xmltext_handlers[("title", None, "string")] = self.set_legend
    
    def set_legend(self, text, *args):
        self.buffer.append('        this.%(self_name)s.setLegend("%(text)s");' % {'self_name': self.name(), 'text': text})

    def set_text(self, text, *args):
        self.buffer.append('        // how to set the title of a %(self_type)s?");' % {'self_type': self.__class__.__name__})
    
class QMainWindow(Container):
    def __init__(self, caller, name, class_name=""):
        Container.__init__(self, caller, name, class_name)

        self.register_handlers()

    def w_text(self, text, *args):
        pass

    def h_text(self, text, *args):
        pass

    def js_inst(self):
        self.buffer.append('        this.%(self_name)s = new qx.ui.container.Composite(); // QMainWindow' % {'self_name': self.name()})
        self.caller.members.add("%(self_name)s : null" % {'self_name' : self.name()})
        self.buffer.append('        this.setWidget(this.%(self_name)s);' % {'self_name': self.name()})
        self.set_layout(QVBoxLayout(self.caller, "__cnt_v"))
        self.buffer.append('')


class QWidget(Container):
    def __init__(self, caller, name, class_name=""):
        self.type = "qx.ui.container.Composite"
        Container.__init__(self, caller, name, class_name)

        self.layout = None
        self.register_handlers()
        
    def set_text(self, text):
        self.buffer.append('        // how to set the title of a %(self_type)s?' % {'self_type': self.__class__.__name__})

class QToolBar(Container):
    def __init__(self, caller, name, class_name=""):
        self.type = "qx.ui.toolbar.ToolBar"
        Container.__init__(self, caller, name, class_name)

        self.layout = None
        self.register_handlers()

class QDialog(Container):
    def __init__(self, caller, name, class_name=""):
        Container.__init__(self, caller, name, class_name)

        self.layout = None

        self.register_handlers()

    def js_inst(self):
        self.buffer.append('')
        self.buffer.append('        // TODO: QDialog yeni window tanimlayacak ' % {'self_name': self.name()})

class QScrollArea(Container):
    def __init__(self, caller, name, class_name=""):
        self.type = "qx.ui.container.Scroll"
        Container.__init__(self, caller, name, class_name)

        self.layout = None

        self.register_handlers()
        
    #
    # quoting qooxdoo api docs:
    #     Note that this class can only have one child widget. 
    #     This container has a fixed layout, which cannot be changed.
    # 
    # so set_layout here does nothing.
    #
    def set_layout(self, layout):
        pass

    def add_widget(self, widget, **kwargs):
        self.children.append(widget)
        self.buffer.append("        this.%(self_name)s.add(this.%(widget_name)s);" % {'self_name': self.name(), 'widget_name': widget.name()})

class QTabWidget(Container):
    def __init__(self, caller, name, class_name=""):
        self.type = "qx.ui.tabview.TabView"
        Container.__init__(self, caller, name, class_name)

        self.layout = None
        self.register_handlers()

    def add_widget(self, widget, **kwargs):
        self.children.append(widget)
        widget.type = "qx.ui.tabview.Page"
        widget.js_inst()
        self.buffer.append('        this.%(self_name)s.add(this.%(widget_name)s);' % {'self_name': self.name(), 'widget_name': widget.name()})
        

