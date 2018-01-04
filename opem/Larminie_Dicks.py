# -*- coding: utf-8 -*-
import math
from .Amphlett import Enernst_Calc,Power_Calc,Efficiency_Calc,Rho_Calc,VStack_Calc,PowerStack_Calc
from .Params import Larminiee_InputParams as InputParams
from .Params import Larminiee_OutputParams as OutputParams
from .Params import F,R1
from .Functions import *
import os

def Vcell_Calc(E0, i,i_0,i_n,i_L,T,alpha,R_M,A):
    """
    This function calculate cell voltage
    :param Enernst:  Enernst [V}
    :param Loss:  Loss [V]
    :return:  Cell voltage [V]
    """
    try:
        J=i/A
        J_n=(i_n/A)
        J_0=(i_0/A)
        J_L=(i_L/A)
        A1=(R1*T)/(2*alpha*F)
        B1=(R1*T)/(2*F)
        result=E0-A1*(math.log10((J+J_n)/J_0))-R_M*(J+J_n)-B1*(math.log10(1-((J+J_n)/J_L)))
        return result
    except Exception:
        print("[Error] Vcell Calculation Error")


def Static_Analysis(InputMethod=Get_Input, TestMode=False):
    """
    This function run static analysis with calling other functions
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
                Output_Dict["Vcell"] = Vcell_Calc(E0=Input_Dict["E0"],i=i,i_0=Input_Dict["i_0"],i_n=Input_Dict["i_n"],i_L=Input_Dict["i_L"],T=Input_Dict["T"],
                                                  alpha=Input_Dict["alpha"],R_M=Input_Dict["R"],A=Input_Dict["A"])
                Output_Dict["PEM Efficiency"] = Efficiency_Calc(Output_Dict["Vcell"])
                Output_Dict["Power"] = Power_Calc(Output_Dict["Vcell"], i)
                Output_Dict["VStack"] = VStack_Calc(Input_Dict["N"], Output_Dict["Vcell"])
                Output_Dict["Power-Stack"]=PowerStack_Calc(Output_Dict["Power"],Input_Dict["N"])
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
