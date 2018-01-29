# -*- coding: utf-8 -*-
import math
from .Params import Dynamic_InputParams as InputParams
from .Params import Dynamic_Outparams as OutputParams
from .Params import R,F,uF,HHV
from .Functions import *
import os



def Enernst_Calc(E0,N0,T, PH2, PO2):
    """
    This function calculate Enernst
    :param T: Cell Operation Temperature [K]
    :type T : float
    :param PH2: Partial Pressure [atm]
    :type PH2 : float
    :param PO2: partial Pressure [atm]
    :type PO2: float
    :return: Enernst [V} as float
    """
    try:
        result = N0*(E0+(R*T/(2*F))*math.log(PH2*((PO2)**0.5)))
        return result
    except Exception:
        print("[Error] Enernst Calculation Failed")


def PH2_Calc(KH2,tH2,Kr,I,qH2):
    """
    This function calculate CH2
    :param PH2: Partial Pressure [atm]
    :type PH2 : float
    :param T: Cell Operation Temperature [K]
    :type T:float
    :return: CH2 [mol/cm^3] as float
    """
    try:
        result = ((1/KH2)/(1+tH2))*(qH2-2*Kr*I)
        return result
    except Exception:
        print("[Error] PH2 Calculation Failed")


def PO2_Calc(KO2,tO2,Kr,I,qO2):
    """
    This function calculate CO2
    :param PO2: Partial Pressure [atm]
    :type PO2 : float
    :param T: Cell Operation Temperature [K]
    :type T : float
    :return: CO2 [mol/cm^3] as float
    """
    try:
        result = ((1/KO2)/(1+tO2))*(qO2-Kr*I)
        return result
    except Exception:
        print("[Error] PO2 Calculation Failed")


def Kr_Calc(N0):
    """
    This function calculate Rho
    :param i: Cell load current [A]
    :type i : float
    :param A: active area [cm^2]
    :type A:float
    :param T: Cell Operation Temperature [K]
    :type T:float
    :param lambda_param: is an adjustable parameter with a possible maximum value of 23
    :type lambda_param : float
    :return: Rho -- > Membrane Specific Resistivity [ohm.cm] as float
    """
    try:
        result = N0/(4*F)
        return result
    except Exception:
        print("[Error] Kr Calculation Failed")

def Efficiency_Calc(Vcell):
    """
    This function calculate PEM Cell Efficiency
    :param Vcell: Cell Voltage [V]
    :type Vcell:float
    :return: Efficiency as float
    """
    try:
        result = (uF * Vcell) / HHV
        return result
    except Exception:
        print("[Error] PEM Efficiency Calculation Failed")


def VStack_Calc(N, Vcell):
    """
    This function calculate VStack
    :param N: number of single cells
    :type N  :int
    :param Vcell: Cell Voltage [V}
    :type Vcell:float
    :return: VStack [V] as float
    """
    try:
        result = N * (Vcell)
        return result
    except Exception:
        print("[Error] VStack Calculation Error")




def Vcell_Calc(Enernst, B,C,I,Rint):
    """
    This function calculate cell voltage
    :param Enernst:  Enernst [V}
    :type Enernst : float
    :param Loss:  Loss [V]
    :type Loss : float
    :return:  Cell voltage [V] as float
    """
    try:
        result = Enernst-B*math.log(C*I)-Rint*I
        return result
    except Exception:
        print("[Error] Vcell Calculation Error")

def qO2_Calc(qH2,rho):
    """
    This function calculate cell voltage
    :param Enernst:  Enernst [V}
    :type Enernst : float
    :param Loss:  Loss [V]
    :type Loss : float
    :return:  Cell voltage [V] as float
    """
    try:
        result = (qH2/rho)
        return result
    except Exception:
        print("[Error] Vcell Calculation Error")


def Power_Calc(Vcell, i):
    """
    This function calculate power
    :param Vcell: Vell Voltage [V]
    :type Vcell : float
    :param i: cell load current [A]
    :type i : float
    :return: Cell power [W] as float
    """
    try:
        result = Vcell * i
        return result
    except Exception:
        print("[Error] Power Calculation Error")




def Static_Analysis(InputMethod=Get_Input, TestMode=False):
    """
    This function run Amphlett static analysis with calling other functions
    :param InputMethod : Input Function Or Input Test Vector
    :param TestMode : Test Mode Flag
    :type InputMethod : dict or Get_Input function object
    :type TestMode:bool
    :return: None
    """
    OutputFile = None
    CSVFile = None
    try:
        Simulation_Title="Dynamic"
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
                Output_Dict["Vcell"]=Vcell_Calc(Output_Dict["E"],Input_Dict["B"],Input_Dict["C"],i,Input_Dict["Rint"])
                Output_Dict["PEM Efficiency"] = Efficiency_Calc(Output_Dict["Vcell"])
                Output_Dict["Power"] = Power_Calc(Output_Dict["Vcell"], i)
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
