# -*- coding: utf-8 -*-

from .opem import *
from .params import *
from art import tprint
import doctest
import sys
if __name__=="__main__":
    args=sys.argv
    argsup=list(map(str.upper,args))
    if "TEST" in argsup:
        doctest.testfile("test.py", optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)
    else:
        tprint("OPEM")
        tprint("v"+str(Version))
        Static_Analysis()







