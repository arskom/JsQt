
from jsqt import Base

class Layout(Base):
    def __init__(self, caller, name=""):
        if len(caller.stack) > 0:
            self.parent = caller.stack[ - 1]
        if name == "":
            name = self.parent.name() + "_" + self.__class__.__name__.lower()
        Base.__init__(self, caller, name)
               
class CanvasLayout(Layout):
    implicit = False

    def __init__(self, caller, parent, name=""):
        self.type = "qx.ui.layout.Canvas"
        Layout.__init__(self, caller, name)        

        self.register_handlers()

    def add_widget(self, container, widget, **kwargs):
        props = []
        if hasattr(widget, 'x'):
            props.append('left: %s' % widget.x)
        if hasattr(widget, 'y'):
            props.append('top: %s' % widget.y)

        container.children.append(widget)

        self.buffer.append('        this.%(container_name)s.add(this.%(widget_name)s,{%(props)s});' % {'container_name': container.name(), 'widget_name': widget.name(), 'props': ', '.join(props)})

class QVBoxLayout(Layout):
    def __init__(self, caller, name=""):
        self.type = "qx.ui.layout.VBox"        
        Layout.__init__(self, caller, name)
        
        self.register_handlers()
        self.buffer.append('        this.%(self_name)s.setSpacing(9);' % {'self_name': self.name()})

    def add_widget(self, container, widget, **kwargs):
        self.buffer.append('        this.%(container_name)s.add(this.%(widget_name)s,{flex:1});' % {'container_name': container.name(), 'widget_name': widget.name()})

class QHBoxLayout(Layout):
    def __init__(self, caller, name=""):
        self.type = "qx.ui.layout.HBox"
        Layout.__init__(self, caller, name)
        self.buffer.append('        this.%(self_name)s.setSpacing(9);' % {'self_name': self.name()})

        self.register_handlers()

    def add_widget(self, container, widget, **kwargs):
        self.buffer.append('        this.%(container_name)s.add(this.%(widget_name)s,{flex:1});' % {'container_name': container.name(), 'widget_name': widget.name()})

class QGridLayout(Layout):
    def __init__(self, caller, name=""):
        self.type = "qx.ui.layout.Grid"
        Layout.__init__(self, caller, name)
        self.buffer.append('        this.%(self_name)s.setSpacingX(9);' % {'self_name': self.name()})
        self.buffer.append('        this.%(self_name)s.setSpacingY(9);' % {'self_name': self.name()})

        self.register_handlers()
        
    def add_widget(self, container, widget, **kwargs):
        self.buffer.append('        this.%(container_name)s.add(this.%(widget_name)s, {row: %(row)s, column: %(col)s });' % {
             'container_name': container.name()
            ,'widget_name': widget.name()
            ,'row': widget.item_properties.get("row")
            ,'col': widget.item_properties.get("column")
        })

