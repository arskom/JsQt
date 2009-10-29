# encoding: utf8

#
# This file is part of JsQt.
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
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.
#

version   = "trunk"
copyright = "(c) 2009 Arskom Ltd."
header_string = """JsQt %s
%s
""" % (version, copyright)

loglevel = 0

import sys

def debug_print(*args):
    if loglevel > 0:
        for i in range(len(args)):
            sys.stderr.write(str(args[i]))
            if i != len(args)-1:
                sys.stderr.write(" ")
        sys.stderr.write("\n")

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
                raise TypeError, 'This DuckTypedList instance requires objects to have a "%s" member' % a

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

    def write(self,what):
        os=self.__os
        i=0

        if not self.__in_comment:
            if not self.__brace_causes_new_line[-1]:
                if what == ";":
                    self.__brace_causes_new_line=[True]

            if what.endswith(".add"):
                self.__brace_causes_new_line=[False]

        for c in what:
            if what[i-1] == '/' and c=='*':
                self.__in_comment = True

            elif what[i-1] == '*' and c=='/':
                self.__in_comment = False

            if self.__in_comment:
                os.write(c)

            elif c == '{':
                os.write(" ")
                os.write(c)
                if self.__brace_causes_new_line[-1]:
                    self.__indent+=1
                    self.newline()
                    self.__comma_causes_new_line.append(True)

            elif c == "}":
                if self.__brace_causes_new_line[-1]:
                    self.__indent-=1
                    self.newline()
                os.write(c)
                if self.__brace_causes_new_line[-1]:
                    self.newline()
                    self.__comma_causes_new_line.pop()

            elif c == "(":
                self.__comma_causes_new_line.append(False)
                os.write(c)

            elif c == ")":
                self.__comma_causes_new_line.pop()
                os.write(c)
            
            elif what[i-1] == '*' and c=='/':
                os.write(c)
                self.newline()

            elif c == ',':
                if self.__comma_causes_new_line[-1]:
                    self.newline()
                os.write(c)

            elif c == ";":
                os.write(c)
                self.newline()

            elif c == ":":
                os.write(c)
                os.write(" ")
            
            elif c == "=":
                os.write(" ")
                os.write(c)
                os.write(" ")
            
            elif c =="\n":
                self.newline()

            else:
                os.write(c)
            i+=1

    def newline(self):
        self.__os.write("\n")
        for i in range(self.__indent):
            self.__os.write("    ")
