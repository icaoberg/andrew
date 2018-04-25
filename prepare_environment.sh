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

if [ -d pelican_javascript ]; then
	ln -s $(pwd)/pelican_javascript $(pwd)/pelican-plugins/pelican_javascript
fi

if [ ! -d content/js ]; then
	mkdir content/js
fi 

if [ ! -f github-cards/src/widget.js ]; then
	ln -s $(pwd)/github-cards/src/widget.js $(pwd)/content/js/widget.js
fi

deactivate
