#!/bin/bash

virtualenv --system-site-packages .
source ./bin/activate

pip install -I ipython pelican tabulate grid

deactivate
