# -*- coding: utf-8 -*-
"""Notebook-run script."""
import os
import shutil
import opem
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

COPY_DICT = {os.path.join("Documents", "Amphlett", "Amphlett_Test.csv"): os.path.join("otherfile", "test.csv"),
             os.path.join("Documents", "Amphlett", "Amphlett_Test.html"): os.path.join("otherfile", "test.html"),
             os.path.join("Documents", "Amphlett", "Amphlett_Test.opem"): os.path.join("otherfile", "test.opem")}

NOTEBOOK_EXTENSION = ".ipynb"

if __name__ == "__main__":
    tprint("OPEM", "bulbhead")
    tprint("v{0}".format(opem.__version__), "bulbhead")
    tprint("Notebook Run", "amc3line")
    print("Processing ...\n")
    for index, notebook in enumerate(NOTEBOOKS_LIST):
        ep = ExecutePreprocessor(timeout=6000, kernel_name='python3')
        path = os.path.join("Documents", notebook)
        with open(path + NOTEBOOK_EXTENSION, "r", encoding="utf-8") as f:
            nb = nbformat.read(f, as_version=4)
            ep.preprocess(nb, {'metadata': {'path': 'Documents/'}})
        with open(path + NOTEBOOK_EXTENSION, 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)
        print("\t{0}.{1} [OK]".format(index + 1, notebook))
    print("\nCopying ...")
    for index, item in enumerate(sorted(COPY_DICT)):
        shutil.copy(item, COPY_DICT[item])
        print("\t{0}.{1} --> {2} [OK]".format(index + 1, item, COPY_DICT[item]))
