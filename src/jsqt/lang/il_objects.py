
import sys
from jsqt import TypedList

class Comment(object):
    def __init__(self, comment):
        if type(comment) != str:
            raise Exception("Comments only accept strings")
        self.__comment = comment

    def compile(self, dialect):
        for l in dialect.comment(self.__comment):
            yield l

class Function(object):
    def __init__(self):
        self.source =[]

    def add_statement(self, what):
        self.source.append(what)

    def compile(self, dialect):
        for s in self.source:
            for l in s.compile(dialect):
                yield l

class Object(object):
    def __init__(self,name):
        if len(name) == 0:
            raise Exception("Empty name not allowed")
        self.members = {}
        self.statics = {}
        self.ctor = Function()
        self.dtor = Function()
        self.name = name
        self.lang = TypedList(['to_stream'])

    def set_member(self, key, val):
        self.members[key]=val

    def get_member(self, key, val, default=None):
        return self.__elts['members'].get(key, default)

    def compile(self, dialect):
        for l in dialect.class_definition(self.name, members=self.members, ctor=self.ctor, dtor=self.dtor):
            self.lang.append(l)

    def to_stream(self, os=sys.stdout):
        for l in self.lang:
            l.to_stream(os)
        