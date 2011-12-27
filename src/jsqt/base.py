# encoding: utf8

#
# This file is part of JsQt.
#
# Copyright (C) Arskom Ltd. www.arskom.com.tr
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
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.
#

class DuckTypedList(list):
    """
    Not exactly duck typing, but it comes close.
    """
    def __init__(self,attr_list, data=[]):
        for a in attr_list:
            if not isinstance(a,str):
                raise Exception("DuckTypedList accepts only an iterable of str "
                                                                    "instances")

        self.__attr_list = attr_list

        for i in range(len(data)):
            try:
                self.append(data[i])
            except TypeError,e:
                raise TypeError("%s\nIn the element no %d of the incoming data"%
                                                                  (e.args[0],i))

    def append(self, v):
        for a in self.__attr_list:
            if not hasattr(v, a):
                raise TypeError("TypedList should have objects with a '%s' "
                                                                      "member\n"
                                 "The '%s' type doesn't conform to this."
                                                                  % (a,type(v)))

        list.append(self,v)

    def __setitem__(self, k, v):
        for a in self.__attr_list:
            if not hasattr(v, a):
                raise TypeError('This DuckTypedList instance requires objects '
                            'to have a "%s" member' % a)

        list.__setitem__(self,k,v)

class DuckTypedDict(dict):
    """
    Not exactly duck typing, but it comes close.
    """
    def __init__(self,attr_list):
        for a in attr_list:
            if not isinstance(a,str):
                raise Exception("""DuckTypedDict accepts only an iterable of str instances""")

        self.__attr_list = attr_list

    def __setitem__(self, k, v):
        for a in self.__attr_list:
            if not hasattr(v, a):
                raise TypeError('This DuckTypedDict instance requires objects '
                                'to have a "%s" member\n'
                         "The '%s' type doesn't conform to this." % (a,type(v)))

        dict.__setitem__(self,k,v)

class NoTrailingSpace(object):
    def __init__(self,os):
        self.__os = os;
        self.__seen_space = 0
        self.__seen_newline = 0
        self.__depth = 0
        self.__prev_char = None

    def write(self,what):
        os=self.__os

        for c in what:
            if c == " ":
                self.__seen_space += 1
            
            elif c == "\n":
                self.__seen_space = 0
                self.__seen_newline += 1
                if self.__seen_newline < 2 or self.__prev_char in ('{','}'):
                    os.write(c)

            else:
                if c == "{":
                    self.__depth += 1

                elif c == "}":
                    self.__depth -= 1

                os.write(" " * self.__seen_space)
                self.__seen_space = 0
                self.__seen_newline = 0
                self.__prev_char = c
                os.write(c)

class JsPp(object):
    """
    A simple pretty printer for javascript.
    """
    def __init__(self,os):
        self.__os = os;
        self.__indent = 0
        self.__comma_causes_new_line=[]
        self.__brace_causes_new_line=[True]
        self.__in_comment = False
        self.__pc = None
        self.__in_string_literal = None

    def write(self,what):
        os = self.__os

        if not self.__in_comment:
            if not self.__brace_causes_new_line[-1]:
                if what == ";":
                    self.__brace_causes_new_line=[True]

            if what.endswith(".add"):
                self.__brace_causes_new_line=[False]

        for c in what:
            c = c.replace(u"−","-").encode("utf8");

            if self.__pc == '/' and c=='*':
                self.__in_comment = True

            elif self.__pc == '*' and c=='/':
                self.__in_comment = False

            if self.__in_comment:
                os.write(c)

            elif c == '{' and self.__in_string_literal is None:
                os.write(" ")
                os.write(c)
                if self.__brace_causes_new_line[-1]:
                    self.__indent+=1
                    self.newline()
                    self.__comma_causes_new_line.append(True)

            elif c == "}" and self.__in_string_literal is None:
                if self.__brace_causes_new_line[-1]:
                    self.__indent-=1
                    self.newline()
                os.write(c)
                if self.__brace_causes_new_line[-1]:
                    self.newline()
                    self.__comma_causes_new_line.pop()

            elif c == "(" and self.__in_string_literal is None:
                self.__comma_causes_new_line.append(False)
                os.write(c)

            elif c == ")" and self.__in_string_literal is None:
                self.__comma_causes_new_line.pop()
                os.write(c)

            elif self.__pc == '*' and c=='/'  and self.__in_string_literal is None:
                os.write(c)
                self.newline()

            elif c == ',' and self.__in_string_literal is None:
                if self.__comma_causes_new_line[-1]:
                    self.newline()
                os.write(c)

            elif c == ";" and self.__in_string_literal is None:
                os.write(c)
                self.newline()

            elif c == ":" and self.__in_string_literal is None:
                os.write(c)
                os.write(" ")

            elif c == "=" and self.__in_string_literal is None:
                os.write(" ")
                os.write(c)
                os.write(" ")

            elif c in ('"', "'") and self.__pc != '\\':
                if self.__in_string_literal is None:
                    self.__in_string_literal = c

                elif self.__in_string_literal == c:
                    self.__in_string_literal = None

                os.write(c)

            elif c =="\n" and self.__in_string_literal is None:
                self.newline()

            else:
                os.write(c)
            self.__pc = c

    def newline(self):
        self.__os.write("\n")
        for i in range(self.__indent):
            self.__os.write("    ")

class AutoExpandingList(list):
    def __getitem__(self, key):
        retval = None

        try:
            retval = list.__getitem__(self,key)

        except IndexError:
            self.extend( [None] * (key-len(self)+1))

        return retval
