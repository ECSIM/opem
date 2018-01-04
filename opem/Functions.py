# -*- coding: utf-8 -*-
import os
import datetime
from art import text2art


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
def Get_Input(InputParams):
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
        return Output
    except Exception:
        print("Bad Input")
        return False


def Output_Save(OutputParamsKeys, OutputDict,OutputParams, i, file):
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


def Output_Init(InputDict,Title):
    """
    This function initialize output file
    :param InputDict: Input Test Vector
    :type InputDict:dict
    :return: file object
    """
    Art = text2art("Opem")
    file = open(Title+"-Model-Result.opem", "w")
    file.write(Art)
    file.write("Simulation Date : " + str(datetime.datetime.now()) + "\n")
    file.write("**********\n")
    file.write(Title+" Model\n\n")
    file.write("**********\n")
    file.write("Simulation Inputs : \n\n")
    Input_Keys = list(InputDict.keys())
    Input_Keys.sort()
    for key in Input_Keys:
        file.write(key + " : " + str(InputDict[key]) + "\n")
    file.write("**********\n")
    return file


def CSV_Init(OutputParamsKeys,OutputParams,Title):
    """
    This function initialize csv file
    :param OutputParamsKeys: Output Params as dict
    :return: file object
    """
    file = open(Title+"-Model-Result.csv", "w")
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


def filter_lambda(Input_Dict):
    '''
    This function filter lambda parameter
    :param Input_Dict: Input Parameters Dictionary
    :return: Modified Dictionary
    '''
    try:
        if Input_Dict["lambda"] > 23:
            Input_Dict["lambda"] = 23
            print("[Warning] Opem Automatically Set Lambda To Maximum Value (23) ")
        elif Input_Dict["lambda"] < 14:
            Input_Dict["lambda"] = 23
            print("[Warning] Opem Automatically Set Lambda To Minimum Value (14) ")
        return Input_Dict
    except Exception:
        return Input_Dict

def filter_alpha(Input_Dict):
    '''
    This function filter alpha parameter
    :param Input_Dict: Input Parameters Dictionary
    :return: Modified Dictionary
    '''
    try:
        if Input_Dict["alpha"] > 1:
            Input_Dict["alpha"] = 1
            print("[Warning] Opem Automatically Set Alpha To Maximum Value (1) ")
        elif Output["alpha"] < 0:
            Input_Dict["alpha"] = 0
            print("[Warning] Opem Automatically Set Alpha To Maximum Value (0) ")
        return Input_Dict
    except Exception:
        return Input_Dict
