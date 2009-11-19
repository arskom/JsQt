#!/bin/bash

version=$(python setup.py --version)
pack=JsQt-$version

rm -rf dist

python setup.py sdist
cd dist
tar xf $pack.tar.gz
rm $pack.tar.gz
rm -rf $pack/test/build

tar czf $pack.tar.gz $pack
rm -rf $pack