#!/usr/bin/python

import os
import sys
import stat

from gen import qx_08

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

def main(argv):
    if len(argv) == 4:
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
        print "Usage:", argv[0], "xml_input_path js_output_path root_namespace"

if __name__ == "__main__":
    main(sys.argv)


