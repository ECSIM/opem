# -*- coding: utf-8 -*-
import math
from .params import *
def Enernst_Calc(T,PH2,PO2):
    '''
    This function calculate Enernst
    :param T: Cell Operation Temperature [K]
    :param PH2: Partial Pressure [atm]
    :param PO2: partial Pressure [atm]
    :return: Enernst [V}
    '''
    try:
        result=1.229-(8.5*(10**-4))*(T-298.15)+(4.308*(10**-5))*T*(math.log(PH2)+0.5*math.log(PO2))
        return result
    except Exception:
        print("[Error] Enernst Calculation Faild")

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

def Xi2_Calc(A,PH2,T):
    '''
    This function calculate Xi2
    :param A: active area [cm^2]
    :param PH2: Partial Pressure [atm]
    :param T: Cell Operation Temperature [K]
    :return: Xi2
    '''
    try:
        CH2=CH2_Calc(PH2,T)
        result=0.00286+0.0002*math.log(A)+(4.3*(10**-5))*math.log(CH2)
        return result
    except Exception:
        print("[Error] Xi2 Calculation Faild")

def Eta_Conc_Calc(i,A):
    '''
    This function calculate Eta Concentration
    :param i: Cell load current [A]
    :param A: active area [cm^2]
    :return: Eta Concentration
    '''
    try:
        i_star=(i*1000)/A
        result=m*math.exp(n*i_star)
        return result
    except Exception:
        print("[Error] Eta Concentration Calculation Faild")

def Eta_Ohmic_Calc(i,l,A,T,lambda_param):
    '''
    This function calculate Eta Ohmic
    :param i: cell load current [A]
    :param l: Membrane Thickness [cm]
    :param A: active area [cm^2]
    :param T: Cell Operation Temperature [K]
    :param lambda_param: is an adjustable parameter with a possible maximum value of 23
    :return: Eta Ohmic
    '''
    try:
        Rho=Rho_Calc(i,A,T,lambda_param)
        R_prot=(Rho*l)/A
        result=i*R_prot
        return result
    except Exception:
        print("[Error] Eta Ohmic Calculation Faild")

def Eta_Act_Calc(T,PO2,PH2,i,A):
    '''
    This function calculate Eta Activation
    :param T: Cell Operation Temperature [K]
    :param PO2: Partial Pressure [atm]
    :param i: cell load current [A]
    :return:  Eta Activation
    '''
    try:
        CO2=CO2_Calc(PO2,T)
        xi2=Xi2_Calc(A,PH2,T)
        result=xi1+xi2*T+xi3*T*math.log(CO2)+xi4*T*math.log(i)
        return result
    except Exception:
        print("[Error] Eta Activation Calculation Faild")

def Efficiency_Calc(Vcell):
    '''
    This function calculate PEM Cell Efficiency
    :param Vcell: Cell Voltage [V]
    :return: Efficiency
    '''
    try:
        result=(uF*Vcell)/HHV
        return result
    except Exception:
        print("[Error] PEM Efficiency Calculation Faild")

def Static_Analysis






