#!/bin/bash

virtualenv --system-site-packages .
source ./bin/activate

pip install -I ipython pelican tabulate grid
pip install -U beautifulsoup4

deactivate
