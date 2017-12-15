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

def CO2_Calc(PO2,T):
    '''
    This function calculate CO2
    :param PO2: Partial Pressure [atm]
    :param T: Cell Operation Temperature [K]
    :return: CO2 [mol/cm^3]
    '''
    try:
        result=PO2/(5.08*(10**6)*math.exp(-498/T))
    except Exception:
        print("[Error] CO2 Calculation Faild")

def Rho_Calc(i,A,T,lambda_param):
    '''
    This function calculate Rho
    :param i: Cell load current [A]
    :param A: active area [cm^2]
    :param T: Cell Operation Temperature [K]
    :param lambda_param: is an adjustable parameter with a possible maximum value of 23
    :return: Rho -- > Membrane Specific Resistivity [ohm.cm]
    '''
    try:
        result=(181.6*(1+0.03*(i/A)+0.062*((T/303)**2)*((i/A)**2.5)))/((lambda_param-0.634-3*(i/A))*math.exp(4.18*((T-303)/T)))
        return result
    except Exception:
        print("[Error] Rho Calculation Faild")






