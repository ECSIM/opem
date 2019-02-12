#!/bin/bash
# Dump Environment (so that we can check PATH, UT_FLAGS, etc.)
set -e
set -x

python -m opem test
pip install -r dev-requirements.txt
python version_check.py
python -m bandit -r opem -s B322
python -m vulture --min-confidence 80 --exclude=opem,build,.eggs --sort-by-size .
python -m pytest Test --cov=opem --cov-report=term
python -m cProfile -s cumtime opem/Profile.py