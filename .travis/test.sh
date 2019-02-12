#!/bin/bash
# Dump Environment (so that we can check PATH, UT_FLAGS, etc.)
set

python version_check.py
tox -- --cov=opem --cov-report=term
python -m cProfile -s cumtime opem/Profile.py