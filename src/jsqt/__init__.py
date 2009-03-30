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
    xmltext_handler = None
    
    #
    # The three fields here represent:
    # [0]: the property name
    # [1]: a complex data type, None if the data type is simple
    # [2]: a primitive data type.
    #
    # A complex data type is one that contains more than one primitive
    # entries. for example <rect> tag has four primitive entries under
    # a property.
    #
    current = [None, None, None]
        
    text_handler = None
    item_properties = None

    type = None

    def __init__(self, caller, name):
        print "\t"+name
        self.__name = name
        if len(caller.stack) > 0:
            self.parent = caller.stack[-1]

        self.caller = caller
        self.buffer = caller.buffer
                
        self.implicit = False
        self.inst_line = None

        self.in_layout = False

        self.js_inst()

    def close(self):
        pass
    

    def js_inst(self):
        """
            When called the first time, this function writes the instantiation line.
            When called more than once, it overwrites the previous instantiation. It
            is useful when a property value in Qt is represented with a different 
            widget in Qx.
        """
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

        # property handlers
        self.xmltext_handlers[("geometry", "rect", "x")] = self.x_text
        self.xmltext_handlers[("geometry", "rect", "y")] = self.y_text
        self.xmltext_handlers[("geometry", "rect", "width")] = self.w_text
        self.xmltext_handlers[("geometry", "rect", "height")] = self.h_text

        self.xmltext_handlers[("sizeHint", "size", "width")] = self.w_text
        self.xmltext_handlers[("sizeHint", "size", "height")] = self.h_text

        self.xmltext_handlers[("readOnly", None, "bool")] = self.set_readOnly

    def get_type(self):
        return self.__class__.__name__

    def name(self):
        return self.__name    
    
    def set_readOnly(self, text, *args):
        self.buffer.append("        this.%(self_name)s.setReadOnly(%(text)s)" % { 'self_name' : self.name(), 'text': text })
        
    def set_current_property(self, name):
        self.current[0] = name
        
    def rect_entry(self, attrs, *args):
        self.current[1] = "rect"
    def rect_exit(self):
        self.current[1] = None

    def size_entry(self, attrs, *args):
        self.current[1] = "size"
    def size_exit(self):
        self.current[1] = None
    
    def prim_entry(self, attrs, what):
        """ Entry tag handler for the primitive data types """
        self.current[2] = what
        t = tuple(self.current)

        if self.xmltext_handlers.has_key(t):
            self.xmltext_handler = self.xmltext_handlers[t]
        else:
            self.buffer.append("        // WARNING: %s property is ignored" % str(t))

    def prim_exit(self):
        """ Exit tag handler for the primitive data types """
        self.xmltext_handler = None
        self.current[2] = None

    def x_text(self, text, *args):
        self.x = text
    def y_text(self, text, *args):
        self.y = text
    def w_text(self, text, *args):
        self.buffer.append("        this.%s.setWidth(%s);" % (self.name(), text))
    def h_text(self, text, *args):
        self.buffer.append("        this.%s.setHeight(%s);" % (self.name(), text))

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

