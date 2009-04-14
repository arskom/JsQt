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

version   = "trunk"
copyright = "(c) 2009 Arskom Ltd."
header_string = """
JsQT %s
%s
""" % (version, copyright)

class Base(object):
    type = None
    
    def __init__(self, caller, name, class_name):
        # TODO: name validation
        self.children = []
        self.__name = name
        if len(caller.stack) > 0:
            self.parent = caller.stack[-1]
        else:
            self.parent = None

        self.inst_line = None    

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
        self.current = [None, None, None]
        
        self.text_handler = None
        self.item_properties = None

        self.vsize_type = None
        self.hsize_type = None
    
        self.tag_entry_handlers = {}
        self.tag_exit_handlers = {}
        self.xmltext_handlers = {}
        self.xmltext_handler = None

        self.caller = caller
        self.buffer = caller.buffer
                
        self.implicit = False
        self.inst_line = None

        self.in_layout = False

        self.class_name = class_name
        
        self.display()
        self.js_inst()

    def display(self):
        """
        This is the function that is called when showing the progresss report.
        """
        print "\t","  ok ",self.__name, self.class_name

    def close(self):
        pass
    
    def js_inst(self):
        """
            When called the first time, this function writes the instantiation line.
            When called more than once, it overwrites the previous instantiation. It
            is useful when a property value in Qt is represented with a different 
            widget in Qooxdoo.
        """
        if self.type == None:
            return
        
        js_inst_str = '        this.%(self_name)s = new %(self_type)s(); // %(internal_type)s' % \
            {'self_name': self.name(), 'self_type': self.type, 'internal_type': self.__class__.__name__}

        if self.inst_line == None:
            self.caller.add_member("%(self_name)s : null" % {'self_name' : self.name()})
            self.buffer.append('')
            self.buffer.append(js_inst_str)
            self.inst_line = len(self.buffer) - 1

        else:
            self.buffer[self.inst_line] = js_inst_str 

    def register_handlers(self):
        self.tag_entry_handlers["rect"] = self.rect_entry
        self.tag_exit_handlers["rect"] = self.rect_exit

        self.tag_entry_handlers["datetime"] = self.datetime_entry
        self.tag_exit_handlers["datetime"] = self.datetime_exit

        self.tag_entry_handlers["size"] = self.size_entry
        self.tag_exit_handlers["size"] = self.size_exit

        self.tag_entry_handlers["hour"] = self.prim_entry
        self.tag_exit_handlers["hour"] = self.prim_exit

        self.tag_entry_handlers["minute"] = self.prim_entry
        self.tag_exit_handlers["minute"] = self.prim_exit

        self.tag_entry_handlers["second"] = self.prim_entry
        self.tag_exit_handlers["second"] = self.prim_exit

        self.tag_entry_handlers["year"] = self.prim_entry
        self.tag_exit_handlers["year"] = self.prim_exit

        self.tag_entry_handlers["month"] = self.prim_entry
        self.tag_exit_handlers["month"] = self.prim_exit

        self.tag_entry_handlers["day"] = self.prim_entry
        self.tag_exit_handlers["day"] = self.prim_exit

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

        self.xmltext_handlers[("minimumSize", "size", "width")] = self.set_minimum_width
        self.xmltext_handlers[("minimumSize", "size", "height")] = self.set_minimum_height        
        self.xmltext_handlers[("maximumSize", "size", "width")] = self.set_maximum_width
        self.xmltext_handlers[("maximumSize", "size", "height")] = self.set_maximum_height

        self.xmltext_handlers[("bottomMargin", None, "number")] = self.set_margin_bottom
        self.xmltext_handlers[("leftMargin", None, "number")] = self.set_margin_left
        self.xmltext_handlers[("rightMargin", None, "number")] = self.set_margin_right
        self.xmltext_handlers[("topMargin", None, "number")] = self.set_margin_top
        self.xmltext_handlers[("margin", None, "number")] = self.set_margin
        
    def get_type(self):
        return self.__class__.__name__

    def name(self):
        return self.__name    
    
    def set_current_property(self, name):
        self.current[0] = name
        
    def set_current_vsize(self, vsize):     
        self.vsize_type = vsize
        
    def set_current_hsize(self, hsize):     
        self.hsize_type = hsize

    def rect_entry(self, attrs, *args):
        self.current[1] = "rect"

    def rect_exit(self):
        self.current[1] = None


    def datetime_entry(self, attrs, *args):
        self.current[1] = "datetime"

    def datetime_exit(self):
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
            self.buffer.append("        // WARNING: %s: property is ignored" % str(t))

    def prim_exit(self):
        """ Exit tag handler for the primitive data types """
        self.xmltext_handler = None
        self.current[2] = None


    def x_text(self, text, *args):
        self.x = text

    def y_text(self, text, *args):
        self.y = text

    def w_text(self, text, *args):
        self.buffer.append("        this.%(self_name)s.setWidth(%(text)s);" % {'self_name': self.name(), 'text': text})

    def h_text(self, text, *args):
        self.buffer.append("        this.%(self_name)s.setHeight(%(text)s);" % {'self_name': self.name(), 'text': text})
        
    def set_minimum_width(self, minWidth, *args):
        self.buffer.append('        this.%(self_name)s.set({minWidth: %(minWidth)s});' % {'self_name': self.name(), 'minWidth': minWidth})
    def set_minimum_height(self, minHeight, *args):       
        self.buffer.append('        this.%(self_name)s.set({minHeight: %(minHeight)s});' % {'self_name': self.name(), 'minHeight': minHeight})        
    def set_maximum_width(self, maxWidth, *args):       
        self.buffer.append('        this.%(self_name)s.set({maxWidth: %(maxWidth)s});' % {'self_name': self.name(), 'maxWidth': maxWidth})
    def set_maximum_height(self, maxHeight, *args):       
        self.buffer.append('        this.%(self_name)s.set({maxHeight: %(maxHeight)s});' % {'self_name': self.name(), 'maxHeight': maxHeight})        

    def set_margin_bottom(self, marginBottom, *args):       
        self.buffer.append('        this.%(self_name)s.set({marginBottom: %(marginBottom)s});' % {'self_name': self.name(), 'marginBottom': marginBottom})
    def set_margin_left(self, marginLeft, *args):       
        self.buffer.append('        this.%(self_name)s.set({marginLeft: %(marginLeft)s});' % {'self_name': self.name(), 'marginLeft': marginLeft})
    def set_margin_right(self, marginRight, *args):       
        self.buffer.append('        this.%(self_name)s.set({marginRight: %(marginRight)s});' % {'self_name': self.name(), 'marginRight': marginRight})
    def set_margin_top(self, marginTop, *args):       
        self.buffer.append('        this.%(self_name)s.set({marginTop: %(marginTop)s});' % {'self_name': self.name(), 'marginTop': marginTop})        
    def set_margin(self, margin, *args):
        self.buffer.append('        this.%(self_name)s.set({margin: %(margin)s});' % {'self_name': self.name(), 'margin': margin})
    
class Class(Base):
    def __init__(self, caller, name, class_name):
        Base.__init__(self, caller, name, class_name)
        self.xmltext_handler = self.__xmltext_handler
        
    def js_type(self):
        pass
        
    def __xmltext_handler(self, text, *args):
        self.buffer.append('qx.Class.define("%(class_name)s", { extend : qx.core.Object ' % { "class_name": self.name() })
        self.buffer.append('    ,properties : {');
        self.buffer.append('        widget : { check : "Object" }');
        self.buffer.append('    }');
        self.buffer.append('    ,construct : function () {');
    
    def add_widget(self, *args, **kwargs):
        pass

class Dummy(Base):

    def js_inst(self):
        self.buffer.append('        // WARNING: %(class_name)s widget is not supported (yet?).' % {'class_name':self.class_name})

    def display(self):
        print "\t WARN", self.class_name, "is not supported (yet?)."

    def do_nothing(self,*args,**kwargs):
        pass

    set_layout = do_nothing
    add_widget = do_nothing

class NoQooxdooEquivalent(Dummy):
    def register_handlers(self):
        pass

    def js_inst(self):
        self.buffer.append('        // WARNING: %(class_name)s widget is not supported by Qooxdoo.' % {'class_name':self.class_name})

    def display(self):
        print "\t WARN", self.class_name, "is not supported by Qooxdoo."

