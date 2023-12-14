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

OUTPUT_FOLDER_PATH = "doc"

DOCUMENTS_FOLDER_PATH = "Documents"

IMAGES_FOLDER_PATH = os.path.join(DOCUMENTS_FOLDER_PATH, "images")

IMAGES_COPY_PATH = os.path.join(OUTPUT_FOLDER_PATH, "images")

if __name__ == "__main__":
    tprint("OPEM", "bulbhead")
    tprint("Notebook Convert", "amc3line")
    print("Processing ...")
    if OUTPUT_FOLDER_PATH in os.listdir():
        shutil.rmtree(OUTPUT_FOLDER_PATH)
    time.sleep(5)
    os.mkdir(OUTPUT_FOLDER_PATH)
    shutil.copytree(IMAGES_FOLDER_PATH, IMAGES_COPY_PATH)
    for index1, folder in enumerate(sorted(NOTEBOOKS_DICT)):
        print("\n{0}.{1} Models:\n".format(index1+1, folder))
        folder_path = os.path.join(OUTPUT_FOLDER_PATH, folder)
        os.mkdir(folder_path)
        for index2, notebook in enumerate(sorted(NOTEBOOKS_DICT[folder])):
            notebook_path = os.path.join(
                DOCUMENTS_FOLDER_PATH, notebook + NOTEBOOK_EXTENSION)
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
                            'path': folder_path}})
            with open(notebook_copy_path, 'w', encoding='utf-8') as f:
                nbformat.write(nb, f)
            notebook_title = notebook.replace("_", "-")
            exporter = HTMLExporter()
            output_notebook = nbformat.read(notebook_copy_path, as_version=4)
            output, resources = exporter.from_notebook_node(
                output_notebook, {'metadata': {'name': notebook_title}})
            with open(html_file_path, "w", encoding="utf-8") as html_file:
                html_file.write(output)
            os.remove(notebook_copy_path)
            print("\t{0}.{1} [OK]".format(index2 + 1, notebook_title))
