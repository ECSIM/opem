# -*- coding: utf-8 -*-
import math
def Enerst_Calc(T,PH2,PO2):
    '''
    This function calculate Enerst
    :param T: Cell Operation Temperature [K]
    :param PH2: Partial Pressure [atm]
    :param PO2: partial Pressure [atm]
    :return: Enerst [V}
    '''
    try:
        result=1.229-(8.5*(10**-4))*(T-298.15)+(4.308*(10**-5))*T*(math.log(PH2)+0.5*math.log(PO2))
        return result
    except Exception:
        print("[Error] Enerst Calculation Faild")

def CH2_Calc(PH2,T):
    '''
    This function calculate CH2
    :param PH2: Partial Pressure [atm]
    :param T: Cell Operation Temperature [K]
    :return: CH2 [mol/cm^3]
    '''
    try:
        result=PH2/(1.09*(10**6)*math.exp(77/T))
        return result
    except Exception:
        print("[Error] CH2 Calculation Faild")






