Introduction
-------------

JsQt is a tool to compile QtDesigner's .ui files to javascript code,
which is targeted to work with the [qooxdoo](http://qooxdoo.org) framework.

There's still a lot of remaining work to support QtDesigner's feature
set, yet some promising results can be obtained for a number of
common use cases.


Installation
-------------

Just run:

    python setup.py install

in a shell with root privileges, (this means you may need to prepend sudo
to the above command) inside the package root directory. The setup script 
will generate two executables, namely "jsqt" and "jsuic".

'jsqt' is the main executable whose functionality is described in the below 
website. 'jsuic' is the tool that seeks to implement an interface similar 
to Qt's well-known uic tool. It takes a single .ui file as argument and writes
the resulting qooxdoo class to stdout.

Usage
------

Head over to

    http://code.google.com/p/jsqt/wiki/Tutorial

to see how to create javascript code from the sample xml files that can
be found inside test/xml/draw directory.
