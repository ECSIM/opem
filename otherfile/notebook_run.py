# -*- coding: utf-8 -*-
"""Notebook-run script."""
import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from art import tprint

NOTEBOOKS_LIST = [
    "Amphlett",
    "Chakraborty",
    "Chamberline_Kim",
    "Larminie_Dicks",
    "Padulles_Amphlett",
    "Padulles_Hauer",
    "Padulles1",
    "Padulles2"]

EXTENSION = ".ipynb"

if __name__ == "__main__":
    tprint("OPEM", "bulbhead")
    tprint("Document Run", "bulbhead")
    print("Processing ...")
    for index, notebook in enumerate(NOTEBOOKS_LIST):
        ep = ExecutePreprocessor(timeout=6000, kernel_name='python3')
        path = os.path.join("Documents", notebook)
        with open(path + EXTENSION, "r", encoding="utf-8") as f:
            nb = nbformat.read(f, as_version=4)
            ep.preprocess(nb, {'metadata': {'path': 'Documents/'}})
        with open(path + EXTENSION, 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)
        print("{0}.{1} [OK]".format(str(index + 1), notebook))
