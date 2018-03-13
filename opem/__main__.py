# -*- coding: utf-8 -*-

from opem.Static.Amphlett import Static_Analysis as Amphlett_Analysis
from opem.Static.Larminie_Dicks import Static_Analysis as Larminiee_Analysis
from opem.Static.Chamberline_Kim import Static_Analysis as Chamberline_Kim_Analysis
from opem.Dynamic.Padulles1 import Dynamic_Analysis as Padulles1_Analysis
from opem.Dynamic.Padulles2 import Dynamic_Analysis as Padulles2_Analysis
from opem.Dynamic.Padulles_Hauer import Dynamic_Analysis as Padulles_Hauer_Analysis
from opem.Dynamic.Padulles_Amphlett import Dynamic_Analysis as Padulles_Amphlett_Analysis
from art import tprint
from opem.Params import Version,Description_Menu,Description_Links,Vectors
from opem.Functions import check_update,description_print,description_control
import doctest
import sys


if __name__ == "__main__":
    args = sys.argv
    argsup = list(map(str.upper, args))
    Menu={"Amphlett_Analysis (Static)":Amphlett_Analysis,"Larminiee_Analysis (Static)":Larminiee_Analysis,
          "Chamberline_Kim_Analysis (Static)":Chamberline_Kim_Analysis,
          "Padulles_Analysis I (Dynamic)":Padulles1_Analysis,"Padulles_Analysis II (Dynamic)":Padulles2_Analysis,
          "Padulles_Hauer Analysis (Dynamic)":Padulles_Hauer_Analysis,
          "Padulles_Amphlett Analysis (Dynamic)":Padulles_Amphlett_Analysis}
    MenuKeys=list(Menu.keys())
    MenuKeys.sort()
    if "TEST" in argsup:
        doctest.testfile("test.py", optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)
    else:
        ExitFlag = False
        check_update()
        while not ExitFlag:
            tprint("OPEM")
            tprint("v" + str(Version))
            description_print("Overview",Description_Menu)
            for i,item in enumerate(MenuKeys):
                print(str(i+1)+"-"+item)
            try:
                AnalysisIndex=int(input(("Please Choose Analysis : ")))
            except Exception:
                AnalysisIndex=-1
            if AnalysisIndex-1 in range(len(MenuKeys)):
                AnalysisName=MenuKeys[AnalysisIndex-1]
                description_print(AnalysisName, Description_Menu)
                UserInput=input("\nEnter [M]: More Information,[T]: Run Standard Test Vector or any other key to "
                                "continue \n")
                description_control(Analysis_Name=AnalysisName, Analysis_List=Menu, User_Input=UserInput,
                                    Links_Dict=Description_Links, Vectors_Dict=Vectors)
                InputIndex = input("Press [R] to restart OPEM or any other key to exit.")
                if InputIndex.upper() != "R":
                    ExitFlag = True
