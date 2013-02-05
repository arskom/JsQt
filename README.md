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

in a shell with root privileges, (this means you may need to prefix the 
above command with sudo) inside the package root directory. The setup 
script will generate two executables, namely "jsqt" and "jsuic".

'jsqt' is the main executable whose functionality is described in the below 
website. 'jsuic' is the tool that seeks to implement an interface similar 
to Qt's well-known uic tool. It takes a single .ui file as argument and writes
the resulting qooxdoo class to stdout.

Usage
-----

Head over to

    http://code.google.com/p/jsqt/wiki/Tutorial

to see how to create javascript code from the sample xml files that can
be found inside test/xml/draw directory.

Code
----

At a very high level, Here's how JsQt works:

1. Convert the incoming xml tree into a higher level object tree composed of
   objects from from the Interlingua (``jsqt.il``) package.
2. Compile the interlingua to a tree of Javascript primitives from ``jsqt.js``.
3. Convert the javascript primitives to a ``.js`` file, applying miscellanous
   code beautification operators.

It's a non-optimizing (:)) declarative-to-imperative compiler.

The call to ``parser.clazz.compile()`` in ``jsqt.parser.compile`` is probably
made to a ``jsqt.il.container.QMainWindow``.

The ``compile()`` functions in object from the ``il`` package (the il objects)
are for generating objects' own ``create_*()`` functions.

``_compile_children()`` calls call objects' own ``compile()`` functions and
adds calls to these functions in its own constructor.

The rest is hacks and infrastructure to make this design work.

Note: As of now, the ``dialect`` parameter passed to the ``compile()`` call does not
have any effect.
