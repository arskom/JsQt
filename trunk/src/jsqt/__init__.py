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

version   = "0.1-alpha"
copyright = "(c) Arskom Ltd."
header_string = """
JsQT %s
%s
""" % (version, copyright)

class Base(object):
    __name = ""
    parent = None
    children = []
    buffer = None
    caller = None
    implicit = False
    
    inst_line = None
    
    tag_entry_handlers = {}
    tag_exit_handlers = {}
    xmltext_handlers = {}
            #  prop  comp  prim    
    current = [None, None, None]
        
    text_handler = None

    item_properties = None

    type = None

    def __init__(self, caller, name):
        print "\t"+name
        self.__name = name
        if len(caller.stack) > 0:
            self.parent = caller.stack[ - 1]

        self.caller = caller
        self.buffer = caller.buffer
                
        self.implicit = False
        self.inst_line = None
        self.js_inst()

    def close(self):
        pass
    
    def js_inst(self):
        if self.type == None:
            return
        
        js_inst_str = '        this.%(self_name)s = new %(self_type)s(); // %(internal_type)s' % {'self_name': self.name(), 'self_type': self.type, 'internal_type': self.__class__.__name__}

        if self.inst_line == None:
            self.caller.members.add("%(self_name)s : null" % {'self_name' : self.name()})
            self.buffer.append('')
            self.buffer.append(js_inst_str)
            self.inst_line = len(self.buffer) - 1

        else:
            self.buffer[self.inst_line] = js_inst_str 

    def register_handlers(self):
        self.tag_entry_handlers["rect"] = self.rect_entry
        self.tag_exit_handlers["rect"] = self.rect_exit

        self.tag_entry_handlers["size"] = self.size_entry
        self.tag_exit_handlers["size"] = self.size_exit

        self.tag_entry_handlers["string"] = self.prim_entry
        self.tag_exit_handlers["string"] = self.prim_exit

        self.tag_entry_handlers["x"] = self.prim_entry
        self.tag_exit_handlers["x"] = self.prim_exit
        
        self.tag_entry_handlers["y"] = self.prim_entry
        self.tag_exit_handlers["y"] = self.prim_exit

        self.tag_entry_handlers["width"] = self.prim_entry
        self.tag_exit_handlers["width"] = self.prim_exit

        self.tag_entry_handlers["height"] = self.prim_entry
        self.tag_exit_handlers["height"] = self.prim_exit

        self.tag_entry_handlers["horstretch"] = self.prim_entry
        self.tag_exit_handlers["horstretch"] = self.prim_exit

        self.tag_entry_handlers["verstretch"] = self.prim_entry
        self.tag_exit_handlers["verstretch"] = self.prim_exit
        
        self.tag_entry_handlers["enum"] = self.prim_entry
        self.tag_exit_handlers["enum"] = self.prim_exit

        self.tag_entry_handlers["set"] = self.prim_entry
        self.tag_exit_handlers["set"] = self.prim_exit

        self.tag_entry_handlers["font"] = self.font_entry
        self.tag_exit_handlers["font"] = self.font_exit

        self.tag_entry_handlers["pointsize"] = self.prim_entry
        self.tag_exit_handlers["pointsize"] = self.prim_exit

        self.tag_entry_handlers["family"] = self.prim_entry
        self.tag_exit_handlers["family"] = self.prim_exit

        self.tag_entry_handlers["weight"] = self.prim_entry
        self.tag_exit_handlers["weight"] = self.prim_exit

        self.tag_entry_handlers["bold"] = self.prim_entry
        self.tag_exit_handlers["bold"] = self.prim_exit

        self.tag_entry_handlers["bool"] = self.prim_entry
        self.tag_exit_handlers["bool"] = self.prim_exit

        self.tag_entry_handlers["number"] = self.prim_entry
        self.tag_exit_handlers["number"] = self.prim_exit

        self.tag_entry_handlers["sizepolicy"] = self.sizepolicy_entry
        self.tag_exit_handlers["sizepolicy"] = self.sizepolicy_exit

        # property tanimlari
        self.xmltext_handlers[("geometry", "rect", "x")] = self.x_text
        self.xmltext_handlers[("geometry", "rect", "y")] = self.y_text
        self.xmltext_handlers[("geometry", "rect", "width")] = self.w_text
        self.xmltext_handlers[("geometry", "rect", "height")] = self.h_text

        self.xmltext_handlers[("windowTitle", None, "string")] = self.set_windowTitle
        self.xmltext_handlers[("title", None, "string")] = self.set_title
        self.xmltext_handlers[("text", None, "string")] = self.set_text

        self.xmltext_handlers[("inputMask", None, "string")] = self.set_inputMask
        self.xmltext_handlers[("echoMode", None, "enum")] = self.set_echoMode
        self.xmltext_handlers[("orientation", None, "enum")] = self.set_orientation

        self.xmltext_handlers[("sizeHint", "size", "width")] = self.w_text
        self.xmltext_handlers[("sizeHint", "size", "height")] = self.h_text

        self.xmltext_handlers[("minimumSize", "size", "width")] = self.set_dummy
        self.xmltext_handlers[("minimumSize", "size", "height")] = self.set_dummy

        self.xmltext_handlers[("sizeConstraint", None, "enum")] = self.set_dummy
        
        self.xmltext_handlers[("font", None, "pointsize")] = self.set_dummy
        self.xmltext_handlers[("font", None, "family")] = self.set_dummy
        self.xmltext_handlers[("font", None, "weight")] = self.set_dummy
        self.xmltext_handlers[("font", None, "bold")] = self.set_dummy

        self.xmltext_handlers[("margin", None, "number")] = self.set_dummy
        self.xmltext_handlers[("spacing", None, "number")] = self.set_dummy
        self.xmltext_handlers[("readOnly", None, "bool")] = self.set_readOnly

        self.xmltext_handlers[("sizePolicy", None, "horstretch")] = self.set_dummy
        self.xmltext_handlers[("sizePolicy", None, "verstretch")] = self.set_dummy

        self.xmltext_handlers[("maximumSize", "size", "width")] = self.set_dummy
        self.xmltext_handlers[("maximumSize", "size", "height")] = self.set_dummy
        
        self.xmltext_handlers[(u'maxLength', None, u'number')] = self.set_dummy
    
        self.xmltext_handlers[("textFormat", None, "enum")] = self.set_dummy
        self.xmltext_handlers[("alignment", None, "set")] = self.set_dummy
        self.xmltext_handlers[(u'autoFillBackground', None, u'bool')] = self.set_dummy

    def set_dummy(self, attrs, *args):
        self.buffer.append("        // TODO: %s is to be supported" % str(self.current))

    def set_readOnly(self, text, *args):
        self.buffer.append("        this.%(self_name)s.setReadOnly(%(text)s)" % { 'self_name' : self.name(), 'text': text })
        
    def set_inputMask(self, attrs, *args):
        self.buffer.append("        // TODO: inputmask property ignored")

    def set_echoMode(self, attrs, *args):
        self.buffer.append("        // TODO: echoMode property ignored")

    def set_orientation(self, attrs, *args):
        self.buffer.append("        // TODO: orientation property ignored")

    def get_type(self):
        return self.__class__.__name__
    
    def set_current_property(self, name):
        self.current[0] = name
        
    def name(self):
        return self.__name
    
    def rect_entry(self, attrs, *args):
        self.current[1] = "rect"
    def rect_exit(self):
        self.current[1] = None

    def font_entry(self, attrs, *args):
        self.buffer.append("        // font entry is not handled yet.")
    def font_exit(self):
        self.buffer.append("        // font exit is not handled yet.")
                
    def size_entry(self, attrs, *args):
        self.current[1] = "size"
    def size_exit(self):
        self.current[1] = None
    
    def sizepolicy_entry(self, attrs, *args):
        self.buffer.append("        // sizepolicy entry is not handled yet.")
    def sizepolicy_exit(self):
        self.buffer.append("        // sizepolicy exit is not handled yet.")

    def prim_entry(self, attrs, what):
        self.current[2] = what
        self.xmltext_handler = self.xmltext_handlers[tuple(self.current)]
    def prim_exit(self):
        self.xmltext_handler = None
        self.current[2] = None

    def number_text(self, text, *args):
        pass
    def bool_text(self, text, *args):
        pass
    def x_text(self, text, *args):
        self.x = text
    def y_text(self, text, *args):
        self.y = text
    def w_text(self, text, *args):
        self.buffer.append("        this.%s.setWidth(%s);" % (self.name(), text))
    def h_text(self, text, *args):
        self.buffer.append("        this.%s.setHeight(%s);" % (self.name(), text))
    def enum_text(self, text, *args):
        self.buffer.append("        // enum text is not handled yet.")
    def pointsize_text(self, text, *args):
        self.buffer.append("        // pointsize text is not handled yet.")
    def weight_text(self, text, *args):
        self.buffer.append("        // weight entry is not handled yet.")
    def bold_text(self, text, *args):
        self.buffer.append("        // bold entry is not handled yet.")
    def horstretch_text(self, text, *args):
        self.buffer.append("        // horstretch entry is not handled yet.")
    def verstretch_text(self, text, *args):
        self.buffer.append("        // verstretch entry is not handled yet.")

    def set_windowTitle(self, attrs, *args):
        self.buffer.append("        // windowTitle property is not handled yet.")
    def set_title(self, attrs, *args):
        self.buffer.append("        // title property is not handled yet.")
    def set_text(self, attrs, *args):
        self.buffer.append("        // text property is not handled yet.")
        
class Class(Base):
    def __init__(self, caller, name):
        Base.__init__(self, caller, name)
        
    def js_type(self):
        pass
        
    def xmltext_handler(self, text, *args):
        self.buffer.append('qx.Class.define("%(class_name)s", { extend : qx.core.Object ' % { "class_name": self.name() })
        self.buffer.append('    ,properties : {');
        self.buffer.append('        widget : { check : "Object" }');
        self.buffer.append('    }');
        self.buffer.append('    ,construct : function () {');
    
    def add_widget(self, *args, **kwargs):
        pass
    
    
    