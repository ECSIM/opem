# -*- coding: utf-8 -*-
'''
OPEM Main File
'''
import doctest
import sys
import coverage
import os
from opem.Static.Amphlett import Static_Analysis as Amphlett_Analysis
from opem.Static.Larminie_Dicks import Static_Analysis as Larminiee_Analysis
from opem.Static.Chamberline_Kim import Static_Analysis as Chamberline_Kim_Analysis
from opem.Dynamic.Padulles1 import Dynamic_Analysis as Padulles1_Analysis
from opem.Dynamic.Padulles2 import Dynamic_Analysis as Padulles2_Analysis
from opem.Dynamic.Padulles_Hauer import Dynamic_Analysis as Padulles_Hauer_Analysis
from opem.Dynamic.Padulles_Amphlett import Dynamic_Analysis as Padulles_Amphlett_Analysis
from art import tprint
from opem.Params import Version, Description_Menu, Description_Links, Vectors
from opem.Functions import check_update, description_print, description_control


def run_test(test_path):
    '''
    This function run test cases
    :param test_path: test files path
    :type test_path : str
    :return: None
    '''
    cov = coverage.Coverage()
    cov.start()
    doctest.testfile(os.path.join(test_path, "Amphlett_test.py"),
                     optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS,
                     verbose=False)
    doctest.testfile(os.path.join(test_path, "Chamberline_Kim_test.py"),
                     optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS,
                     verbose=False)
    doctest.testfile(os.path.join(test_path, "Functions_test.py"),
                     optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS,
                     verbose=False)
    doctest.testfile(os.path.join(test_path, "Larminie_Dicks_test.py"),
                     optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS,
                     verbose=False)
    doctest.testfile(os.path.join(test_path, "Padulles_Amphlett_test.py"),
                     optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS,
                     verbose=False)
    doctest.testfile(os.path.join(test_path, "Padulles_Hauer_test.py"),
                     optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS,
                     verbose=False)
    doctest.testfile(os.path.join(test_path, "Padulles1_test.py"),
                     optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS,
                     verbose=False)
    doctest.testfile(os.path.join(test_path, "Padulles2_test.py"),
                     optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS,
                     verbose=False)
    cov.stop()
    cov.report()
    cov.save()


if __name__ == "__main__":
    TESTPATH = "Test"
    ARGS = sys.argv
    ARGSUP = list(map(str.upper, ARGS))
    Menu = {
        "Amphlett_Analysis (Static)": Amphlett_Analysis,
        "Larminiee_Analysis (Static)": Larminiee_Analysis,
        "Chamberline_Kim_Analysis (Static)": Chamberline_Kim_Analysis,
        "Padulles_Analysis I (Dynamic)": Padulles1_Analysis,
        "Padulles_Analysis II (Dynamic)": Padulles2_Analysis,
        "Padulles_Hauer Analysis (Dynamic)": Padulles_Hauer_Analysis,
        "Padulles_Amphlett Analysis (Dynamic)": Padulles_Amphlett_Analysis}
    MENUKEYS = sorted(Menu.keys())
    if "TEST" in ARGSUP:
        run_test(TESTPATH)
    else:
        EXITFLAG = False
        check_update()
        while not EXITFLAG:
            tprint("OPEM")
            tprint("v" + str(Version))
            description_print("Overview", Description_Menu)
            for i, item in enumerate(MENUKEYS):
                print(str(i + 1) + "-" + item)
            try:
                ANALYSISINDEX = int(input(("Please Choose Analysis : ")))
            except Exception:
                ANALYSISINDEX = -1
            if ANALYSISINDEX - 1 in range(len(MENUKEYS)):
                ANALYSISNAME = MENUKEYS[ANALYSISINDEX - 1]
                description_print(ANALYSISNAME, Description_Menu)
                USERINPUT = input(
                    "\nEnter [M]: More Information,[T]: Run Standard Test Vector or any other key to "
                    "continue \n")
                description_control(
                    Analysis_Name=ANALYSISNAME,
                    Analysis_List=Menu,
                    User_Input=USERINPUT,
                    Links_Dict=Description_Links,
                    Vectors_Dict=Vectors)
                INPUTINDEX = input(
                    "Press [R] to restart OPEM or any other key to exit.")
                if INPUTINDEX.upper() != "R":
                    EXITFLAG = True
