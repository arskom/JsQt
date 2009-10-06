
import sys

class Comment(object):
    def __init__(self, comment):
        self.__comment=comment.replace("*/", "*_/")
            
    def to_stream(self, os=sys.stdout):
        os.write(" /* %s */ " % self.__comment)

class String(object):
    def __init__(self, string):
        self.__string = string
        
    def to_stream(self, os=sys.stdout):
        os.write('"')
        os.write(self.__string)
        os.write('"')

class ObjectReference(object):
    def __init__(self, object_name):
        if len(object_name) ==0:
            raise Exception("Empty object name not allowed")
        self.__object_name = object_name

    def to_stream(self, os=sys.stdout):
        os.write(self.__object_name)

class Object(object):
    def __init__(self,**kwargs):
        self.__members = kwargs

    def set_member(self,key,value):
        if hasattr(value,'to_stream'):
            self.__members[key]=value
        else:
            raise Exception("olmaz")

    def del_member(self,key):
        del self.__members[key]
        
    def to_stream(self, os=sys.stdout):
        os.write("{")
        i=0
        for k in self.__members.keys():
            os.write(k)
            os.write(":")
            self.__members[k].to_stream(os)
            if i != len(self.__members) -1:
                os.write(",")
            i+=1

        os.write("}")


class FunctionCall(object):
    def __init__(self, function_name):
        self.__function_name = function_name
        self.__arguments = []

    def add_argument(self, argument):
        if hasattr(argument, 'to_stream'):
            self.__arguments.append(argument)
        else:
            raise Exception("olmaz")

    def to_stream(self, os=sys.stdout):
        os.write(self.__function_name)
        os.write("(")
        for i in range(len(self.__arguments)):
            self.__arguments[i].to_stream(os)
            if i != len(self.__arguments) -1:
                os.write(",")

        os.write(");")
        