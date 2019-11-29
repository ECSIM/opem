#!/bin/bash
# Dump Environment (so that we can check PATH, UT_FLAGS, etc.)
set -e
set -x
IS_IN_TRAVIS=false
PYTHON_COMMAND=python
  
if [ "$TRAVIS_OS_NAME" == "osx" ]
then
	PYTHON_COMMAND=python3
fi
 
if [ "$CI" = 'true' ] && [ "$TRAVIS" = 'true' ]
then
     IS_IN_TRAVIS=true
fi

if [ "$IS_IN_TRAVIS" = 'false' ] || [ "$TRAVIS_PYTHON_VERSION" = '3.7' ]
then
	$PYTHON_COMMAND version_check.py
	$PYTHON_COMMAND -m bandit -r opem -s B322
	$PYTHON_COMMAND -m vulture --min-confidence 65 --exclude=build,.eggs --sort-by-size opem setup.py version_check.py
	$PYTHON_COMMAND -m pydocstyle
fi

$PYTHON_COMMAND -m pytest opem/Test --cov=opem --cov-report=term
$PYTHON_COMMAND -m cProfile -s cumtime opem/Profile.py