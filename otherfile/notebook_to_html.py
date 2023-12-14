# -*- coding: utf-8 -*-
"""Notebook-to-HTML script."""
import os
import time
import shutil
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert import HTMLExporter
from art import tprint

NOTEBOOKS_DICT = {
    "Static": [
        "Amphlett",
        "Chamberline_Kim",
        "Larminie_Dicks"],
    "Dynamic": [
        "Chakraborty",
        "Padulles_Amphlett",
        "Padulles_Hauer",
        "Padulles1",
        "Padulles2"]}

NOTEBOOK_EXTENSION = ".ipynb"

HTML_EXTENSION = ".html"

OUTPUT_FOLDER = "doc"

IMAGES_FOLDER_PATH = os.path.join("Documents", "images")

IMAGES_COPY_PATH = os.path.join(OUTPUT_FOLDER, "images")

if __name__ == "__main__":
    tprint("OPEM", "bulbhead")
    tprint("Notebook Convert", "amc3line")
    print("Processing ...")
    if OUTPUT_FOLDER in os.listdir():
        shutil.rmtree(OUTPUT_FOLDER)
    time.sleep(5)
    os.mkdir(OUTPUT_FOLDER)
    shutil.copytree(IMAGES_FOLDER_PATH, IMAGES_COPY_PATH)
    for folder in sorted(NOTEBOOKS_DICT):
        print("{0}:".format(folder))
        folder_path = os.path.join("doc", folder)
        os.mkdir(folder_path)
        for index, notebook in enumerate(NOTEBOOKS_DICT[folder]):
            notebook_path = os.path.join(
                "Documents", notebook + NOTEBOOK_EXTENSION)
            notebook_copy_path = os.path.join(
                folder_path, notebook + NOTEBOOK_EXTENSION)
            html_file_path = os.path.join(
                folder_path, notebook + HTML_EXTENSION)
            shutil.copy(notebook_path, notebook_copy_path)
            ep = ExecutePreprocessor(timeout=6000, kernel_name='python3')
            with open(notebook_copy_path, "r", encoding="utf-8") as f:
                nb = nbformat.read(f, as_version=4)
                ep.preprocess(
                    nb, {
                        'metadata': {
                            'path': folder_path, 'title': notebook}})
            with open(notebook_copy_path, 'w', encoding='utf-8') as f:
                nbformat.write(nb, f)
            exporter = HTMLExporter()
            output_notebook = nbformat.read(notebook_copy_path, as_version=4)
            output, resources = exporter.from_notebook_node(
                output_notebook, {'metadata': {'name': notebook}})
            with open(html_file_path, "w", encoding="utf-8") as html_file:
                html_file.write(output)
            os.remove(notebook_copy_path)
            print("{0}.{1} [OK]".format(str(index + 1), notebook))
