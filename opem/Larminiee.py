# -*- coding: utf-8 -*-
import math
from .Amphlett import Enernst_Calc,Power_Calc,Efficiency_Calc,Rho_Calc,VStack_Calc,PowerStack_Calc,isfloat
from .Params import Larminiee_InputParams as InputParams
from .Params import Larminiee_OutputParams as OutputParams
from .Params import F,R1
import os
import datetime
from art import text2art

def Get_Input():
    """
    This function get inputs from users
    :param InputMethod : Input Function Or Input Test Vector
    :param TestMode : Test Mode Flag
    :return: Input Dictionary
    """
    try:
        Input_Keys = list(InputParams.keys())
        Input_Keys.sort()
        Input_Values = []
        for item in Input_Keys:
            Input_Flag = False
            Input_Item = None
            while not Input_Flag:
                Input_Item = input("Please Enter " + item + "(" + InputParams[item] + ") : ")
                if isfloat(Input_Item):
                    Input_Flag = True
                else:
                    print("[Error] Bad Input Try Again")
            Input_Values.append(Input_Item)
        Input_Values = list(map(float, Input_Values))
        Output = dict(zip(Input_Keys, Input_Values))
        if Output["alpha"]>1:
            Output["alpha"] = 1
            print("[Warning] Opem Automatically Set Alpha To Maximum Value (1) ")
        elif Output["alpha"]<0:
            Output["alpha"] = 0
            print("[Warning] Opem Automatically Set Alpha To Maximum Value (0) ")
        return Output
    except Exception:
        print("Bad Input")
        return False


def Output_Save(OutputParamsKeys, OutputDict, i, file):
    """
    This function write analysis result in Simulation-Result.opem file
    :param OutputParamsKeys : Output Params as dict
    :param OutputDict: Analysis Result Dictionary
    :param i: cell load current [A]
    :param file : file object
    :return: None
    """

    file.write("I :" + str(i) + " A \n\n")
    print("I : " + str(i))
    for key in OutputParamsKeys:
        file.write(key + " : " + str(OutputDict[key]) + " " + OutputParams[key] + "\n")
        print(key + " : " + str(OutputDict[key]) + " " + OutputParams[key])
    file.write("###########\n")
    print("###########")


def Output_Init(InputDict):
    """
    This function initialize output file
    :param InputDict: Input Test Vector
    :type InputDict:dict
    :return: file object
    """
    Art = text2art("Opem")
    file = open("Larminiee-Model-Result.opem", "w")
    file.write(Art)
    file.write("Simulation Date : " + str(datetime.datetime.now()) + "\n")
    file.write("**********\n")
    file.write("Larminiee Static Model\n\n")
    file.write("**********\n")
    file.write("Simulation Inputs : \n\n")
    Input_Keys = list(InputDict.keys())
    Input_Keys.sort()
    for key in Input_Keys:
        file.write(key + " : " + str(InputDict[key]) + "\n")
    file.write("**********\n")
    return file


def CSV_Init(OutputParamsKeys):
    """
    This function initialize csv file
    :param OutputParamsKeys: Output Params as dict
    :return: file object
    """
    file = open("Larminiee-Model-Result.csv", "w")
    file.write("I (A),")
    for index, item in enumerate(OutputParamsKeys):
        file.write(item + " (" + OutputParams[item] + ")")
        if index < len(OutputParamsKeys) - 1:
            file.write(",")
    file.write("\n")
    return file


def CSV_Save(OutputParamsKeys, OutputDict, i, file):
    """
    This Function Save Parameters In CSV File
    :param OutputParamsKeys: Output Params
    :param OutputDict: Output Values Dictionary
    :param i: cell load current [A]
    :param file: CSV_File object
    :return: None
    """
    file.write(str(i) + ",")
    for key in OutputParamsKeys:
        file.write(str(OutputDict[key]))
        if key != OutputParamsKeys[-1]:
            file.write(",")
    file.write("\n")




def Vcell_Calc(E0, i,J_0,J_n,J_L,T,alpha,R_M,A):
    """
    This function calculate cell voltage
    :param Enernst:  Enernst [V}
    :param Loss:  Loss [V]
    :return:  Cell voltage [V]
    """
    try:
        J=i/A
        A1=(R1*T)/(2*alpha*F)
        B1=(R1*T)/(2*F)
        result=E0-A1*(math.log((J+J_n)/J_0))-R_M*(J+J_n)+B1*(math.log(1-((J+J_n)/J_L)))
        return result
    except Exception as e:
        print("[Error] Vcell Calculation Error")


def Static_Analysis(InputMethod=Get_Input, TestMode=False):
    """
    This function run static analysis with calling other functions
    :return: None
    """
    OutputFile = None
    CSVFile = None
    try:
        print("###########")
        print("Larminiee-Model Simulation")
        print("###########")
        OutputParamsKeys = list(OutputParams.keys())
        OutputParamsKeys.sort()
        Output_Dict = dict(zip(OutputParamsKeys, [None] * len(OutputParamsKeys)))
        if not TestMode:
            Input_Dict = InputMethod()
        else:
            Input_Dict = InputMethod
        print(Input_Dict)
        OutputFile = Output_Init(Input_Dict)
        CSVFile = CSV_Init(OutputParamsKeys)
        print("Analyzing . . .")
        IEnd = Input_Dict["i-stop"]
        IStep = Input_Dict["i-step"]
        i = Input_Dict["i-start"]
        while i < IEnd:
            try:
                Output_Dict["Vcell"] = Vcell_Calc(E0=Input_Dict["E0"],i=i,J_0=Input_Dict["J_0"],J_n=Input_Dict["J_n"],J_L=Input_Dict["J_L"],T=Input_Dict["T"],
                                                  alpha=Input_Dict["alpha"],R_M=Input_Dict["R"],A=Input_Dict["A"])
                Output_Dict["PEM Efficiency"] = Efficiency_Calc(Output_Dict["Vcell"])
                Output_Dict["Power"] = Power_Calc(Output_Dict["Vcell"], i)
                Output_Dict["VStack"] = VStack_Calc(Input_Dict["N"], Output_Dict["Vcell"])
                Output_Dict["Power-Stack"]=PowerStack_Calc(Output_Dict["Power"],Input_Dict["N"])
                Output_Save(OutputParamsKeys, Output_Dict, i, OutputFile)
                CSV_Save(OutputParamsKeys, Output_Dict, i, CSVFile)
                i = i + IStep
            except Exception as e:
                print(e)
                i = i + IStep
                OutputFile.write("[Simulation Error]\n")
                CSV_Save(OutputParamsKeys, Output_Dict, i, CSVFile)
        OutputFile.close()
        CSVFile.close()
        print("Done!")
        if not TestMode:
            print("Result In Larminiee-Model-Result.opem -->" + os.getcwd())
            print("Output-Table In Larminiee-Model-Result.csv --> " + os.getcwd())
    except Exception:
        if not OutputFile.closed:
            OutputFile.close()
        if not CSVFile.closed:
            CSVFile.close()
        print("[Error] Larminiee Simulation Failed!(Check Your Inputs)")
