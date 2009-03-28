
import string
from xml import sax

from jsqt.containers import *
from jsqt.widgets import *
from jsqt.layouts import *
from jsqt import Class

class_name = ""

class QtUiFileHandler(object):
    members = set()
    buffers = []
    
    tag_entry_handlers = {}
    tag_exit_handlers = {}
    
    stack = []
    class_handlers = {}
    layout_handlers = {}
    item_attrs = None
    
    main_container = None

    def __init__(self, js_file_name):
        self.buffer = []
        self.buffers.append(self.buffer)
        self.xmltext_handler = None
        self.js_file = open(js_file_name, 'w')
       
        self.tag_entry_handlers["resources"] = self.resources_entry
        self.tag_exit_handlers["resources"] = self.resources_exit
        
        self.tag_entry_handlers["connections"] = self.connections_entry
        self.tag_exit_handlers["connections"] = self.connections_exit
        
        self.tag_entry_handlers["property"] = self.property_entry
        self.tag_exit_handlers["property"] = self.property_exit
        self.tag_entry_handlers["attribute"] = self.property_entry
        self.tag_exit_handlers["attribute"] = self.property_exit

        self.tag_entry_handlers["spacer"] = self.spacer_entry
        self.tag_exit_handlers["spacer"] = self.spacer_exit

        self.tag_entry_handlers["widget"] = self.widget_entry
        self.tag_exit_handlers["widget"] = self.widget_exit
        
        self.tag_entry_handlers["layout"] = self.layout_entry
        self.tag_exit_handlers["layout"] = self.layout_exit

        self.tag_entry_handlers["tabstops"] = self.tabstops_entry
        self.tag_exit_handlers["tabstops"] = self.tabstops_exit
        self.tag_entry_handlers["tabstop"] = self.tabstop_entry
        self.tag_exit_handlers["tabstop"] = self.tabstop_exit

        self.tag_entry_handlers["item"] = self.item_entry
        self.tag_exit_handlers["item"] = self.item_exit

        self.tag_entry_handlers["class"] = self.class_entry
        self.tag_exit_handlers["class"] = self.class_exit

        self.tag_entry_handlers["ui"] = self.ui_entry
        self.tag_exit_handlers["ui"] = self.ui_exit

        self.tag_entry_handlers["zorder"] = self.zorder_entry
        self.tag_exit_handlers["zorder"] = self.zorder_exit
        
        # widget definitions
        self.layout_handlers["QVBoxLayout"] = QVBoxLayout
        self.layout_handlers["QHBoxLayout"] = QHBoxLayout
        self.layout_handlers["QGridLayout"] = QGridLayout
        
        self.class_handlers["QScrollArea"] = QScrollArea
        self.class_handlers["QTabWidget"] = QTabWidget
        self.class_handlers["QToolBar"] = QToolBar

        self.class_handlers["QMainWindow"] = QMainWindow
        self.class_handlers["QDialog"] = QDialog
        self.class_handlers["QWidget"] = QWidget
        
        self.class_handlers["QDateTimeEdit"] = QLineEdit
        self.class_handlers["QDateEdit"] = QLineEdit
        
        self.class_handlers["QGraphicsView"] = QWidget
        
        self.class_handlers["QTableWidget"] = QTableWidget
        self.class_handlers["QListWidget"] = QListWidget
        
        self.class_handlers["QPushButton"] = QPushButton
        self.class_handlers["QLineEdit"] = QLineEdit
        self.class_handlers["QTextEdit"] = QTextEdit
        self.class_handlers["QComboBox"] = QComboBox
        self.class_handlers["QCheckBox"] = QCheckBox
        self.class_handlers["QGroupBox"] = QGroupBox
        self.class_handlers["QLabel"] = QLabel

        self.class_handlers["Spacer"] = Spacer
        self.class_handlers["Class"] = Class

    def ui_entry(self, attrs):
        self.buffer.append("")
        self.buffer.append("/*")
        self.buffer.append(" * This file is auto generated. If you'd like to \n * alter how things work, please extend it.")
        self.buffer.append(" */")
        self.buffer.append("")

    def class_entry(self, attrs):
        self.stack.append(Class(self, class_name))

    def property_entry(self, attrs):
        self.stack[-1].set_current_property(attrs.get("name"))

    def widget_entry(self, attrs):
        self.__widget_entry(attrs.get("class"), attrs.get("name"))

    def item_entry(self, attrs):
        self.item_attrs = attrs

    def item_exit(self):
        self.item_attrs = None

    def spacer_entry(self, attrs):
        self.__widget_entry("Spacer", attrs.get("name"))

    def __widget_entry(self, class_name, name):
        if not self.class_handlers.has_key(class_name):
            raise Exception("class '%s' is not handled yet." % class_name)

        tmp = self.class_handlers[class_name](self, name)
        
        if self.main_container == None:
            self.main_container = tmp

        tmp.item_properties = self.item_attrs
        self.stack.append(tmp)

    def layout_entry(self, attrs):
        layout_name = attrs.get("class")
        if not self.layout_handlers.has_key(layout_name):
            raise Exception("layout '%s' is not handled yet." % class_name)

        layout = self.layout_handlers[layout_name](self, attrs.get("name"))
        if (self.stack[ - 1].layout != None):
            self.stack.append(QWidget(self, attrs.get("name") + "_implicit_container"))
            self.stack[ - 1].implicit = True
            self.stack[ - 1].item_properties = self.item_attrs

        else:
            self.stack[ - 1].implicit = False
        
        self.stack[ - 1].set_layout(layout)        
        
    def layout_exit(self):
        self.stack[-1].in_layout = False
        self.stack[-1].close()
        
        if self.stack[-1].implicit:
            self.stack[-1].layout.close()
            self.stack[-1].parent.add_widget(self.stack[-1])
            self.stack.pop()

    def property_exit(self):
        self.stack[-1].set_current_property(None)

    def widget_exit(self):
        if len(self.stack) == 0:
            return
        elif self.stack[ - 1].parent != None:
            self.stack[ - 1].parent.add_widget(self.stack[ - 1])

        self.stack[ - 1].close()
        self.stack.pop()

    def spacer_exit(self):
        self.widget_exit()

    def class_exit(self):
        self.stack.pop()

    def ui_exit(self):
        pass
    
    def zorder_entry(self, attrs, *args):
        self.xmltext_handler = self.zorder_text    
    def zorder_exit(self):
        self.xmltext_handler = None
    def zorder_text(self, text, *args):
        self.buffer.append("        // WARNING: zorder tag is ignored")

    def tabstops_entry(self, attrs, *args):
        pass    
    def tabstops_exit(self):
        pass
    def tabstop_entry(self, attrs, *args):
        self.xmltext_handler = self.tabstop_text    
    def tabstop_exit(self):
        self.xmltext_handler = None
    def tabstop_text(self, text, *args):
        self.buffer.append("        // WARNING: tabstop tag is ignored")

    def resources_entry(self, attrs):
        self.buffer = []
        self.buffers.append(self.buffer)
        self.buffer.append("        // resources entry is not handled yet.")
    def resources_exit(self):
        self.buffer.append("        // resources exit is not handled yet.")

    def connections_entry(self, attrs):
        self.buffer = []
        self.buffers.append(self.buffer)
        self.buffer.append("        // connections entry is not handled yet.")
    def connections_exit(self):
        self.buffer.append("        // connections exit is not handled yet.")

class QtUiFileParser(sax.ContentHandler, QtUiFileHandler):
    def __init__(self, js_file_name):
        QtUiFileHandler.__init__(self, js_file_name)

    def startDocument(self):
        pass

    def startElement(self, name, attributes):
        if not self.tag_entry_handlers.has_key(name):
            self.stack[-1].tag_entry_handlers[name](attributes, name)

        else:
            self.tag_entry_handlers[name](attributes)

    def endElement(self, name):
        if not self.tag_exit_handlers.has_key(name):
            self.stack[ - 1].tag_exit_handlers[name]()
        else:
            self.tag_exit_handlers[name]()

    def characters(self, text):
        if text.isspace():
            return
        if self.xmltext_handler == None:        
            if self.stack[-1].xmltext_handler == None:
                if self.stack[-1].in_layout:
                    self.stack[-1].layout.xmltext_handler(text, tuple(self.stack[-1].current))
                else:
                    print " *",self.stack[-1].name(), type(self.stack[-1])
                    raise Exception("No property text handler found for %s" % str(tuple(self.stack[-1].current)))
            else:
                self.stack[-1].xmltext_handler(text, tuple(self.stack[-1].current))
        else:
            self.xmltext_handler(text)

    def endDocument(self):
        self.flush_buffers()
        
    def flush_buffers(self):
        self.buffer = []
        self.buffers.append(self.buffer)
        if not isinstance(self.main_container, QMainWindow): 
            self.buffer.append("        this.setWidget(%(self_parent)s);" % {'self_parent': self.main_container.name})
        self.buffer.append("    }")
        self.buffer.append("    ,members : {")
        self.buffer.append(''.join(["        ", "\n        ,".join(self.members)]))
        self.buffer.append("    }")
        self.buffer.append("});")
        
        for b in self.buffers:
            self.js_file.write('\n'.join([bb.encode('utf8') for bb in b]))
            self.js_file.write('\n')

        self.js_file.close()
        del self.buffer[:]
        del self.buffers[:]

def qx_08(ui_file_name, js_file_name, root_namespace):
    global class_name
    
    f = open(js_file_name, 'w')
    class_name = js_file_name[js_file_name.rfind(root_namespace):].replace("//", "/").replace("/", ".")[0:-3]
    print js_file_name

    # Create a new parser instance, using the default XML engine SAX provides
    parser = sax.make_parser()

    # Create an instance of our handler class, which will be registered
    # to receive SAX events
    handler = QtUiFileParser(js_file_name)

    # Pass a file to be parsed, and pass the handler to be registered
    # to receive SAX events.
    sax.parse(ui_file_name, handler)
    
