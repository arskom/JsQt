
import sys

import javascript

class v0_8_3(object):
    def __init__(self, version="0.8.3"):
        self.__version = version

    def comment(self, string):
        yield javascript.Comment(string)

    def class_definition(self, name, base_class=javascript.ObjectReference('qx.core.Object'), members={}, ctor=None, dtor=None):
        if len(name) == 0:
            raise Exception("Empty class name not allowed")
        retval = javascript.FunctionCall("qx.Class.Define")
        retval.add_argument(javascript.String(name))

        class_dict = javascript.Object()
        class_dict.set_member("extends", base_class)

        class_members = javascript.Object()
        for k in members:
            class_members.set_member(k,members[k])
            
        class_dict.set_member("members", class_members)
        
        retval.add_argument(class_dict)

        yield retval
