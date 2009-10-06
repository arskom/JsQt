
from lang_objects import Base

class Assignment(Base):
    def __init__(self, assign_to, assignee):
        self.__to = assign_to
        self.__eq = assignee

    def compile(self,dialect,os=sys.stdout):
        pass
    