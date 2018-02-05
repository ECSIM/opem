# -*- coding: utf-8 -*-

from .Static.Amphlett import Static_Analysis as Amphlett_Analysis
from .Static.Larminie_Dicks import Static_Analysis as Larminiee_Analysis
from .Static.Chamberline_Kim import Static_Analysis as Chamberline_Kim_Analysis
from .Dynamic.Padulles1 import Dynamic_Analysis as Padulles1_Analysis
from .Dynamic.Padulles2 import Dynamic_Analysis as Padulles2_Analysis
from art import tprint
import doctest
import sys
Version=0.4

if __name__ == "__main__":
    args = sys.argv
    argsup = list(map(str.upper, args))
    Menu={"Amphlett_Analysis (Static)":Amphlett_Analysis,"Larminiee_Analysis (Static)":Larminiee_Analysis,
          "Chamberline_Kim_Analysis (Static)":Chamberline_Kim_Analysis,
          "Padulles_Analysis I (Dynamic)":Padulles1_Analysis,"Padulles_Analysis II (Dynamic)":Padulles2_Analysis}
    MenuKeys=list(Menu.keys())
    MenuKeys.sort()
    if "TEST" in argsup:
        doctest.testfile("test.py", optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)
    else:
        ExitFlag = False
        while not ExitFlag:
            tprint("OPEM")
            tprint("v" + str(Version))
            for i,item in enumerate(MenuKeys):
                print(str(i+1)+"-"+item)
            try:
                AnalysisIndex=int(input(("Please Choose Analysis : ")))
            except:
                AnalysisIndex=-1
            if AnalysisIndex-1 in range(len(MenuKeys)):
                Menu[MenuKeys[AnalysisIndex-1]]()
                InputIndex = input("Press [R] to restart OPEM or any other key to exit.")
                if InputIndex.upper() != "R":
                    ExitFlag = True
