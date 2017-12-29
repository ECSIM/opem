# -*- coding: utf-8 -*-
import math
from .Larminiee_Params import *
from .Amphlett import Enernst_Calc,Power_Calc,Efficiency_Calc,Rho_Calc,VStack_Calc
from .Amphlett_Params import uF,HHV
import os
import datetime
from art import text2art


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
def Get_Input():
    """
    This function get inputs from users
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




def Vcell_Calc(Enernst, i,i_0,i_n,i_lim,T,alpha,R_M):
    """
    This function calculate cell voltage
    :param Enernst:  Enernst [V}
    :param Loss:  Loss [V]
    :return:  Cell voltage [V]
    """
    try:
        A1=(R1*T)/(2*alpha*F)
        B1=(R1*T)/(2*F)
        result=Enernst-A1*(math.log((i+i_n)/i_0))-R_M*(i-i_n)-B1*(math.log(1-((i-i_n)/i_lim)))
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
        Output_Dict["Enernst"]= Enernst_Calc(Input_Dict["T"], Input_Dict["PH2"], Input_Dict["PO2"])
        i = Input_Dict["i-start"]
        while i < IEnd:
            try:
                Output_Dict["Vcell"] = Vcell_Calc(Output_Dict["Enernst"],i,Input_Dict["I_0"],Input_Dict["I_N"],Input_Dict["I_Lim"],Input_Dict["T"],
                                                  Input_Dict["alpha"],Input_Dict["R"])
                Output_Dict["PEM Efficiency"] = Efficiency_Calc(Output_Dict["Vcell"])
                Output_Dict["Power"] = Power_Calc(Output_Dict["Vcell"], i)
                Output_Dict["VStack"] = VStack_Calc(Input_Dict["N"], Output_Dict["Vcell"])

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
