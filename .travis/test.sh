#!/bin/bash
# Dump Environment (so that we can check PATH, UT_FLAGS, etc.)
set

python version_check.py
python -m bandit -r opem -s B322
tox -- --cov=opem --cov-report=term
python -m cProfile -s cumtime opem/Profile.py