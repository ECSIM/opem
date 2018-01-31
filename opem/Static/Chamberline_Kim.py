# -*- coding: utf-8 -*-
import math
from opem.Params import Chamberline_InputParams as InputParams
from opem.Params import Chamberline_OutputParams as OutputParams
from opem.Static.Amphlett import Efficiency_Calc,Power_Calc,VStack_Calc,PowerStack_Calc
from opem.Functions import *
import os
import datetime
from art import text2art


def Vcell_Calc(E0,b,R,m,n,i,A):
    """
    This function calculate cell voltage
    :param E0: Open circuit voltage [V]
    :type E0 : float
    :param b: Tafel's parameter for the oxygen reduction [V]
    :type b : float
    :param R: Resistance [ohm.cm2]
    :type R : float
    :param m: Diffusion's parameters [V]
    :type m : float
    :param n: Diffusion's parameters [V]
    :type n : float
    :param i: Cell operating current [A]
    :type i : float
    :param A: Active area [cm2]
    :type A : float
    :return:  Cell voltage [V]
    """
    try:
        J=i/A
        result=E0-b*math.log(J)-R*J-m*math.exp(n*J)
        return result
    except Exception as e:
        print("[Error] Vcell Calculation Error")


def Static_Analysis(InputMethod=Get_Input, TestMode=False):
    """
    This function run Chamberline-Kim static analysis with calling other functions
    :param InputMethod : Input Function Or Input Test Vector
    :param TestMode : Test Mode Flag
    :type InputMethod : dict or Get_Input function object
    :type TestMode:bool
    :return: None
    """
    OutputFile = None
    CSVFile = None
    try:
        Simualtion_Title="Chamberline-Kim"
        print("###########")
        print(Simualtion_Title+"-Model Simulation")
        print("###########")
        OutputParamsKeys = list(OutputParams.keys())
        OutputParamsKeys.sort()
        Output_Dict = dict(zip(OutputParamsKeys, [None] * len(OutputParamsKeys)))
        if not TestMode:
            Input_Dict = InputMethod(InputParams)
        else:
            Input_Dict = InputMethod
        OutputFile = Output_Init(Input_Dict,Simualtion_Title)
        CSVFile = CSV_Init(OutputParamsKeys,OutputParams,Simualtion_Title)
        print("Analyzing . . .")
        IEnd = Input_Dict["i-stop"]
        IStep = Input_Dict["i-step"]
        i = Input_Dict["i-start"]
        while i < IEnd:
            try:
                Output_Dict["Vcell"] = Vcell_Calc(Input_Dict["E0"],Input_Dict["b"],Input_Dict["R"],Input_Dict["m"],Input_Dict["n"],i,Input_Dict["A"])
                Output_Dict["PEM Efficiency"] = Efficiency_Calc(Output_Dict["Vcell"])
                Output_Dict["Power"] = Power_Calc(Output_Dict["Vcell"], i)
                Output_Dict["VStack"] = VStack_Calc(Input_Dict["N"], Output_Dict["Vcell"])
                Output_Dict["Power-Stack"]=PowerStack_Calc(Output_Dict["Power"],Input_Dict["N"])
                Output_Save(OutputParamsKeys, Output_Dict,OutputParams,i, OutputFile)
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
            print("Result In "+Simualtion_Title+"-Model-Result.opem -->" + os.getcwd())
            print("Output-Table In "+Simualtion_Title+"-Model-Result.csv --> " + os.getcwd())
    except Exception:
        if not OutputFile.closed:
            OutputFile.close()
        if not CSVFile.closed:
            CSVFile.close()
        print("[Error] Chamberline-Kim Simulation Failed!(Check Your Inputs)")
