# -*- coding: utf-8 -*-

from .Amphlett import *
from .Amphlett_Params import *
from art import tprint
import doctest
import sys
if __name__=="__main__":
    args=sys.argv
    argsup=list(map(str.upper,args))
    if "TEST" in argsup:
        doctest.testfile("test.py", optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)
    else:
        ExitFlag=False
        while(ExitFlag==False):
            tprint("OPEM")
            tprint("v"+str(Version))
            Static_Analysis()
            InputIndex = input("Press [R] to restart OPEM or any other key to exit.")
            if InputIndex.upper() != "R":
                ExitFlag = True







