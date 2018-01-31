# -*- coding: utf-8 -*-
import math
from opem.Params import Padulles_InputParams as InputParams
from opem.Params import Padulles_Outparams as OutputParams
from opem.Params import R,F,uF,HHV
from opem.Static.Amphlett import Power_Calc
from opem.Functions import *
import os



def Enernst_Calc(E0,N0,T, PH2, PO2):
    """
    This function calculate Enernst
    :param E0: Opencell voltage [V]
    :type E0 : float
    :param N0: Number of fuel cells in the stack
    :type N0 : int
    :param T: Cell Operation Temperature [K]
    :type T : float
    :param PH2:  Partial Pressure [atm]
    :type PH2 : float
    :param PO2: Partial Pressure [atm]
    :type PO2 : float
    :return: Enernest [V] as float
    """
    try:
        result = N0*(E0+(R*T/(2*F))*math.log(PH2*((PO2)**0.5)))
        return result
    except Exception:
        print("[Error] Enernst Calculation Failed")


def PH2_Calc(KH2,tH2,Kr,I,qH2):
    """
    This function calculate PH2
    :param KH2: Hydrogen Valve Constant [kmol.s^(-1).atm^(-1)]
    :type KH2 : float
    :param tH2: Hydrogen time constant [s]
    :type tH2 : float
    :param Kr: Modeling constant [kmol.s^(-1).A^(-1)]
    :type Kr : float
    :param I: Cell load current [A]
    :type I : float
    :param qH2: Molar flow of hydrogen [kmol.s^(-1)]
    :type qH2 : float
    :return: PH2 [atm] as float
    """
    try:
        result = ((1/KH2)/(1+tH2))*(qH2-2*Kr*I)
        return result
    except Exception:
        print("[Error] PH2 Calculation Failed")


def PO2_Calc(KO2,tO2,Kr,I,qO2):
    """
    This function calculate PO2
    :param KO2: Oxygen Valve Constant [kmol.s^(-1).atm^(-1)]
    :type KO2 : float
    :param tO2: Oxygen time constant [s]
    :type tO2 : float
    :param Kr: Modeling constant [kmol.s^(-1).A^(-1)]
    :type Kr : float
    :param I: Cell load current [A]
    :type I : float
    :param qO2: Molar flow of oxygen [kmol.s^(-1)
    :type qO2 : float
    :return: PO2 [atm] as float
    """
    try:
        result = ((1/KO2)/(1+tO2))*(qO2-Kr*I)
        return result
    except Exception:
        print("[Error] PO2 Calculation Failed")


def Kr_Calc(N0):
    """
    This function calculate Kr
    :param N0: Number of fuel cells in the stack
    :type N0 : int
    :return: Kr [kmol.s^(-1).A^(-1)] as float
    """
    try:
        result = N0/(4*F)
        return result
    except Exception:
        print("[Error] Kr Calculation Failed")




def Vcell_Calc(Enernst, B,C,I,Rint):
    """
    This function calculate Vcell
    :param Enernst: Enernst [V]
    :type Enernst : float
    :param B: Activation voltage constant [V]
    :type B: float
    :param C: Constant [A^(-1)
    :type C : float
    :param I: Cell load current [A]
    :type I: float
    :param Rint: Fuel cell internal resistance [ohm]
    :type Rint : float
    :return: Vcell [V] as float
    """
    try:
        result = Enernst-B*math.log(C*I)-Rint*I
        return result
    except Exception:
        print("[Error] Vcell Calculation Error")

def qO2_Calc(qH2,rho):
    """
    This function calculate qO2
    :param qH2: Molar flow of hydrogen [kmol.s^(-1)]
    :type qH2 : float
    :param rho: Hydrogen-Oxygen flow rate
    :type rho : float
    :return: qO2 [kmol.s^(-1)] as float
    """
    try:
        result = (qH2/rho)
        return result
    except Exception:
        print("[Error] qO2 Calculation Error")



def Efficiency_Calc(Vcell,N):
    """
    This function calculate PEM Cell Efficiency
    :param Vcell: Cell Voltage [V]
    :type Vcell:float
    :param N0: Number of fuel cells in the stack
    :type N0 : int
    :return: Efficiency as float
    """
    try:
        result = (uF * Vcell) / (N*HHV)
        return result
    except Exception:
        print("[Error] PEM Efficiency Calculation Failed")




def Dynamic_Analysis(InputMethod=Get_Input, TestMode=False):
    """
    This function run Padulles I analysis  with calling other functions
    :param InputMethod : Input Function Or Input Test Vector
    :param TestMode : Test Mode Flag
    :type InputMethod : dict or Get_Input function object
    :type TestMode:bool
    :return: None
    """
    OutputFile = None
    CSVFile = None
    try:
        Simulation_Title="Padulles I"
        print("###########")
        print(Simulation_Title+"-Model Simulation")
        print("###########")
        OutputParamsKeys = list(OutputParams.keys())
        OutputParamsKeys.sort()
        Output_Dict = dict(zip(OutputParamsKeys, [None] * len(OutputParamsKeys)))
        if not TestMode:
            Input_Dict = InputMethod(InputParams)
        else:
            Input_Dict = InputMethod
        OutputFile = Output_Init(Input_Dict,Simulation_Title)
        CSVFile = CSV_Init(OutputParamsKeys,OutputParams,Simulation_Title)
        print("Analyzing . . .")
        IEnd = Input_Dict["i-stop"]
        IStep = Input_Dict["i-step"]
        i = Input_Dict["i-start"]
        Kr=Kr_Calc(Input_Dict["N0"])
        qO2=qO2_Calc(Input_Dict["qH2"],Input_Dict["rho"])
        while i < IEnd:
            try:
                Output_Dict["PO2"]=PO2_Calc(Input_Dict["KO2"],Input_Dict["tO2"],Kr,i,qO2)
                Output_Dict["PH2"]=PH2_Calc(Input_Dict["KH2"],Input_Dict["tH2"],Kr,i,Input_Dict["qH2"])
                Output_Dict["E"]=Enernst_Calc(Input_Dict["E0"],Input_Dict["N0"],Input_Dict["T"],Output_Dict["PH2"],Output_Dict["PO2"])
                Output_Dict["FC Voltage"]=Vcell_Calc(Output_Dict["E"],Input_Dict["B"],Input_Dict["C"],i,Input_Dict["Rint"])
                Output_Dict["FC Efficiency"] = Efficiency_Calc(Output_Dict["FC Voltage"],Input_Dict["N0"])
                Output_Dict["FC Power"] = Power_Calc(Output_Dict["FC Voltage"], i)
                Output_Save(OutputParamsKeys, Output_Dict,OutputParams, i, OutputFile)
                CSV_Save(OutputParamsKeys, Output_Dict, i, CSVFile)
                i = i + IStep
            except Exception as e:
                print(str(e))
                i = i + IStep
                Output_Save(OutputParamsKeys, Output_Dict, OutputParams, i, OutputFile)
                CSV_Save(OutputParamsKeys, Output_Dict, i, CSVFile)
        OutputFile.close()
        CSVFile.close()
        print("Done!")
        if not TestMode:
            print("Result In "+Simulation_Title+"-Model-Result.opem -->" + os.getcwd())
            print("Output-Table In"+Simulation_Title+"-Model-Result.csv --> " + os.getcwd())
    except Exception:
        if not OutputFile.closed:
            OutputFile.close()
        if not CSVFile.closed:
            CSVFile.close()
        print("[Error] Dynamic Simulation Failed!(Check Your Inputs)")
