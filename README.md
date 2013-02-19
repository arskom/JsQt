Introduction
-------------

JsQt is a tool to compile QtDesigner's .ui files to javascript code,
which is targeted to work with the [qooxdoo](http://qooxdoo.org) framework.

There's still a lot of remaining work to support QtDesigner's feature
set, yet some promising results can be obtained for a number of
common use cases.


Installation
-------------

JsQt is written in Python-2.7, using lxml as the xml library of choice.

The recommended way to install JsQt is to run:

    easy_install --user JsQt

This command requires a recent version of setuptools, so it may or may
not work with your setup. It's the recommended way because it installs
JsQt in your home directory, helping to keep your file system free from
files unknown to your package manager. It installes the 'jsqt' and
'jsuic' commands in ``~/.local/bin`` so make sure to add this path to
your ``PATH`` variable.

You can of course use:

    sudo easy_install JsQt

or an equivalent command to install JsQt to the central site-packages directory
of the Python interpreter.

Usage
-----

JsQt has two entry points: 'jsqt' and 'jsuic' commands. 'jsuic' is the tool that
seeks to implement an interface similar to Qt's well-known uic tool. It takes a
single .ui file as argument and writes the resulting qooxdoo class to stdout.

'jsqt' is a convenience wrapper around 'jsuic' that compiles .ui files in source
directory to .js files in the target directory preserving directory structure
and file names.

The canonical way to work with jsqt is illustrated in the test project in
https://github.com/arskom/JsQt/tree/master/test:

Here's the explanation:

1. Have your .ui files under source/xml/<root_ns>/draw/Sample.ui
2. Compile them using:

        jsqt source/xml source/class <root_ns>

3. Have overriding classes in `source/class/<root_ns>/impl` where you customize
   JsQt-generated widgets according to the needs of your application. Never use
   draw.* classes but always use impl.* classes in your code.

4. Make sure that the impl directory has the same directory structure as the
   `source/class/<root_ns>/draw` and `source/xml/<root_ns>`

An example about how an impl.* class overrides a draw.* class can be seen in
the test project: https://github.com/arskom/JsQt/tree/master/test/source/class/test/impl/Test.js

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

The ``compile()`` functions in objects from the ``il`` package (the il objects)
are for generating objects' own javascript ``create_*()`` functions.

``_compile_children()`` calls call objects' own ``compile()`` functions and
adds calls to these functions in its own constructor.

The rest is hacks and infrastructure to make this design work.

Note: As of now, the ``dialect`` parameter passed to the ``compile()`` call does not
have any effect.
