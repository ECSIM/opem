#!/bin/bash
# Dump Environment (so that we can check PATH, UT_FLAGS, etc.)
set

python version_check.py
python -m bandit -r opem -s B322
python -m vulture --min-confidence 80 --exclude=opem,build,.eggs --sort-by-size .
tox -- --cov=opem --cov-report=term
python -m cProfile -s cumtime opem/Profile.py