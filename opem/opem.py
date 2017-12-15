# -*- coding: utf-8 -*-
import math
def Enerst_Calc(T,PH2,PO2):
    try:
        result=1.229-(8.5*(10**-4))*(T-298.15)+(4.308*(10**-5))*T*(math.log(PH2)+0.5*math.log(PO2))
        return result
    except Exception:
        print("[Error] Enerst Calculation Faild")






