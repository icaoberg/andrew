#!/bin/bash

virtualenv --system-site-packages .
source ./bin/activate

pip install -I ipython pelican tabulate grid
pip install -U beautifulsoup4
pip install pelican-youtube
pip install pelican-gist

git submodule init
git submodule update

cd pelican-plugins
git submodule init
git submodule update
cd ..

deactivate
