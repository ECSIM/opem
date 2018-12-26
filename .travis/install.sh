#!/bin/bash
if [[ $TRAVIS_OS_NAME == 'osx' ]]; then
	pip3 install tox
	exit 0
fi
pip install -r requirements.txt
python setup.py install
# Make sure tox is installed and up to date
pip install -U tox