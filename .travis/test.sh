#!/bin/bash
# Dump Environment (so that we can check PATH, UT_FLAGS, etc.)
set -e
set -x

python -m opem test
pip install -r dev-requirements.txt
python version_check.py
if [ "$TRAVIS_PYTHON_VERSION" = '3.6' ]
then
	python -m bandit -r opem -s B322
	python -m vulture --min-confidence 80 --exclude=opem,build,.eggs --sort-by-size .
	python -m pydocstyle --match-dir=opem
fi
python -m pytest opem/Test --cov=opem --cov-report=term
python -m cProfile -s cumtime opem/Profile.py