#labels Featured
Here's how to get the sample .ui file compiled to .js code step by step:

  * Download Qooxdoo source development kit from www.qooxdoo.org and unzip it to a path to your liking. 
  * Download !JsQt from the downloads page and unzip it to another path to your liking. !JsQt comes with a sample project under `test/` directory. You should either:
    * Copy the contents of the qooxdoo package inside the `qooxdoo/` directory that you'll find inside the `test/` directory.
    * Create a symbolic link to the qooxdoo package
    * Modify the `config.json` file to point to the path of the qooxdoo installation.
   in order to make the project aware of your qooxdoo installation. See [http://qooxdoo.org/documentation/0.8/helloworld here] for more info.
  * Go to the !JsQt root directory and run:
{{{
python setup.py install
}}}
  as a privileged user. This will install !JsQt, and will create executable scripts. you can now run
{{{
jsqt test/source/xml test/source/class test
}}}
  to generate js code from .ui files. !JsQt will mirror the directory structure of the first directory (`"test/source/xml"` in this case) into the second directory. (`"test/source/class"` in this case) The third parameter is the root namespace of the application. The generated classes can be referenced by `test.draw.Add` and `test.draw.Test`.

  * Finally, run:
{{{
./generate.py source
}}}
  or, for windows,
{{{
generate.py source
}}}
  in the project directory. For details on how to do it, refer to the helloworld documentation above.
  * Point your browser to source/index.html to see the results.