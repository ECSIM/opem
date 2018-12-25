#!/bin/bash
if [[ $TRAVIS_OS_NAME == 'osx' ]]; then
	pip3 install tox
	exit 0
fi

# Make sure tox is installed and up to date
pip install -U tox