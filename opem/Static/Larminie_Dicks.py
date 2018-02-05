# -*- coding: utf-8 -*-
import math
from opem.Static.Amphlett import Power_Calc,Efficiency_Calc,VStack_Calc,PowerStack_Calc
from opem.Params import Larminiee_InputParams as InputParams
from opem.Params import Larminiee_OutputParams as OutputParams
from opem.Functions import *
import os

def Vcell_Calc(E0, i,i_0,i_n,i_L,R_M,A,B):
    """
    This function calculate cell voltage
    :param E0:  Fuel Cell reversible no loss voltage [V]
    :type E0 : float
    :param i : Cell operating current [A]
    :type i : float
    :param i_0: Exchange current at which the overvoltage begins to move from zero [A]
    :type i_0 : float
    :param i_n : Internal current [A]
    :type i_n : float
    :param i_L : Limiting current [A]
    :type i_L : float
    :param R_M : The membrane and contact resistances [ohm]
    :type R_M : float
    :param A : The slope of the Tafel line [V]
    :type A : float
    :param B : Constant in the mass transfer term [V}
    :type B : float
    :return:  Cell voltage [V]
    """
    try:
        result=E0-A*(math.log((i+i_n)/i_0))-R_M*(i+i_n)+B*(math.log(1-((i+i_n)/i_L)))
        return result
    except Exception:
        print("[Error] Vcell Calculation Error")


def Static_Analysis(InputMethod=Get_Input, TestMode=False):
    """
    This function run Larminie-Dicks static analysis with calling other functions
    :param InputMethod : Input Function Or Input Test Vector
    :param TestMode : Test Mode Flag
    :type InputMethod : dict or Get_Input function object
    :type TestMode:bool
    :return: None
    """
    OutputFile = None
    CSVFile = None
    try:
        Simulation_Title="Larminie-Dicks"
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
        Input_Dict=filter_alpha(Input_Dict)
        OutputFile = Output_Init(Input_Dict,Simulation_Title)
        CSVFile = CSV_Init(OutputParamsKeys,OutputParams,Simulation_Title)
        print("Analyzing . . .")
        IEnd = Input_Dict["i-stop"]
        IStep = Input_Dict["i-step"]
        i = Input_Dict["i-start"]
        while i < IEnd:
            try:
                Output_Dict["Vcell"] = Vcell_Calc(E0=Input_Dict["E0"],i=i,i_0=Input_Dict["i_0"],i_n=Input_Dict["i_n"],
                                                  i_L=Input_Dict["i_L"],R_M=Input_Dict["RM"],B=Input_Dict["B"],A=Input_Dict["A"])
                Output_Dict["PEM Efficiency"] = Efficiency_Calc(Output_Dict["Vcell"])
                Output_Dict["Power"] = Power_Calc(Output_Dict["Vcell"], i)
                Output_Dict["VStack"] = VStack_Calc(Input_Dict["N"], Output_Dict["Vcell"])
                Output_Dict["Power-Stack"] = PowerStack_Calc(Output_Dict["Power"], Input_Dict["N"])
                Output_Save(OutputParamsKeys, Output_Dict,OutputParams, i, OutputFile)
                CSV_Save(OutputParamsKeys, Output_Dict, i, CSVFile)
                i = i + IStep
            except Exception as e:
                print(e)
                i = i + IStep
                Output_Save(OutputParamsKeys, Output_Dict, OutputParams, i, OutputFile)
                CSV_Save(OutputParamsKeys, Output_Dict, i, CSVFile)
        OutputFile.close()
        CSVFile.close()
        print("Done!")
        if not TestMode:
            print("Result In "+Simulation_Title+"-Model-Result.opem -->" + os.getcwd())
            print("Output-Table In "+Simulation_Title+"-Model-Result.csv --> " + os.getcwd())
    except Exception:
        if not OutputFile.closed:
            OutputFile.close()
        if not CSVFile.closed:
            CSVFile.close()
        print("[Error] Larminiee Simulation Failed!(Check Your Inputs)")
