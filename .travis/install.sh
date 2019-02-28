#!/bin/bash
set -e
set -x

pip install -r requirements.txt
python setup.py install
