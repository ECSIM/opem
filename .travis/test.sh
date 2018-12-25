#!/bin/bash
# Dump Environment (so that we can check PATH, UT_FLAGS, etc.)
set

tox -- --cov=opem --cov-report=term