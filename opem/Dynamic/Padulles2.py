# -*- coding: utf-8 -*-
import math
from opem.Params import Padulles2_InputParams as InputParams
from opem.Params import Padulles2_Outparams as OutputParams
from opem.Params import R,F
from opem.Static.Amphlett import Power_Calc
from opem.Dynamic.Padulles1 import PH2_Calc,PO2_Calc,Kr_Calc,Vcell_Calc,qO2_Calc,Efficiency_Calc
from opem.Functions import *
import os



def Enernst_Calc(E0,N0,T, PH2, PO2,PH2O):
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
    :param PH2O:  Partial Pressure [atm]
    :type PH2O : float
    :return: Enernest [V] as float
    """
    try:
        result = N0*(E0+(R*T/(2*F))*math.log((PH2*math.sqrt(PO2))/PH2O))
        return result
    except Exception:
        print("[Error] Enernst Calculation Failed")

def PH2O_Calc(KH2O,tH2O,Kr,I,qH2O):
    """
    This function calculate PH2O
    :param KH2O: Water Valve Constant [kmol.s^(-1).atm^(-1)]
    :type KH2O : float
    :param tH2O: Water time constant [s]
    :type tH2O : float
    :param Kr: Modeling constant [kmol.s^(-1).A^(-1)]
    :type Kr : float
    :param I: Cell load current [A]
    :type I : float
    :param qH2O: Molar flow of water [kmol.s^(-1)]
    :type qH2O : float
    :return: PH2O [atm] as float
    """
    try:
        result = ((1/KH2O)/(1+tH2O))*(qH2O-2*Kr*I)
        return result
    except Exception:
        print("[Error] PH2O Calculation Failed")




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
        Simulation_Title="Padulles II"
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
                Output_Dict["PH2O"]=PH2O_Calc(Input_Dict["KH2O"],Input_Dict["tH2O"],Kr,i,Input_Dict["qH2O"])
                Output_Dict["E"]=Enernst_Calc(Input_Dict["E0"],Input_Dict["N0"],Input_Dict["T"],Output_Dict["PH2"],Output_Dict["PO2"],Output_Dict["PH2O"])
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
