#!/usr/bin/python -tt

import os
import sys
import stat

from gen import qx_08

header_string="""
JsQT v0.1-alpha
(c) Arskom Ltd, 2009.
"""

def walktree (top = ".", depthfirst = False):
    names = os.listdir(top)
    if not depthfirst:
        yield top, names
    
    for name in names:
        try:
            st = os.lstat(os.path.join(top, name))
        except os.error:
            continue

        if stat.S_ISDIR(st.st_mode):
            for (newtop, children) in walktree (os.path.join(top, name), depthfirst):
                yield newtop, children
    
    if depthfirst:
        yield top, names

def usage():
    print "Usage:", sys.argv[0], "xml_input_path js_output_path root_namespace"

def main(argv):
    print header_string

    if len(argv) == 4:
        if os.path.isdir(argv[1]) and os.path.isdir(argv[2]):
            for (basepath, children) in walktree(argv[1]):
                for c in children:
                    if c[-3:] == '.ui':
                        ui_file_name=os.path.join(basepath, c)
                        js_file_name=ui_file_name.replace(argv[1],argv[2],1)[0:-3]+".js"
                        root_namespace = argv[3]

                        try:
                            os.makedirs(os.path.dirname(js_file_name))
                        except OSError,e:
                            pass
                    
                        qx_08(ui_file_name, js_file_name, root_namespace)
        else:
            usage()
            print '       First two arguments must be directories!'
            print

    else:
        usage()
        print

if __name__ == "__main__":
    main(sys.argv)


