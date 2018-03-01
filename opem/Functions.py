# -*- coding: utf-8 -*-
import datetime
from art import text2art
from opem.Script import *
from opem.Params import Version,Website,UpdateUrl
import io
import os
import requests
def check_update():
    try:
        update_obj=requests.get(UpdateUrl)
        update_data=update_obj.text
        if float(update_data)>Version:
            print("###########")
            print("New Version ("+update_data+") Is Available!")
            print("Website : "+Website)
            print("###########")
    except Exception:
        pass

def filter_default(input_dict,params_default):
    for i in params_default.keys():
        if i not in input_dict.keys():
            input_dict[i]=params_default[i]
    return input_dict
def get_precision(input_number):
    '''
    This function return precision of input number
    :param input_number: input number
    :type input_number : float
    :return: precision as int
    '''
    input_string=str(input_number)
    if "." in input_string:
        splitted_input=input_string.split(".")
        return len(splitted_input[1])
    else:
        return 0
def isfloat(value):
    '''
    This function check input for float conversion
    :param value: input value
    :type value:str
    :return: True if input_value is a number and False otherwise
    '''
    try:
        float(value)
        return True
    except ValueError:
        return False

def rounder(input_number,digit=2):
    '''
    This function round input number
    :param input_number: input number
    :type input_number : anything
    :param digit: precision
    :type digit : int
    :return: round number as float
    '''
    if isfloat(input_number)==True:
        return round(input_number,digit)
    else:
        return input_number

def input_test(a):
    '''
    This function is for test Get_Input
    :param a: input
    :return: "1"
    '''
    return "1"
def Get_Input(InputParams,input_item=input,params_default={}):
    """
    This function get inputs from users
    :param InputParams : InputParams  for each  model
    :type InputParams :dict
    :param input_item : input function (this parameter added for Get_Input doctest)
    :return: Input Dictionary
    """
    try:
        Input_Keys = list(InputParams.keys())
        Input_Keys.sort()
        Input_Values = []
        Name=""
        while(True):
            Name=input_item("Please Enter Simulation Name :")
            if len(Name)!=0:
                break
            else:
                print("[Error] Bad Name Try Again")
        for item in Input_Keys:
            Input_Flag = False
            Input_Item = None
            while not Input_Flag:
                Input_Item = input_item("Please Enter " + item + "(" + InputParams[item] + ") : ")
                if isfloat(Input_Item):
                    Input_Flag = True
                else:
                    if item in params_default.keys():
                        Input_Item=params_default[item]
                        Input_Flag=True
                    else:
                        print("[Error] Bad Input Try Again")
            Input_Values.append(Input_Item)
        Input_Values = list(map(float, Input_Values))
        Output = dict(zip(Input_Keys, Input_Values))
        Output["Name"]=Name
        return Output
    except Exception:
        print("Bad Input")
        return False


def Output_Save(OutputParamsKeys, OutputDict,OutputParams, i, file,PrintMode):
    """
    This function write analysis result in Simulation-Result.opem file
    :param OutputParamsKeys : OutputParams Key as  list
    :type OutputParamsKeys : list
    :param OutputDict: Analysis Result Dictionary
    :type OutputDict:dict
    :param OutputParams : Output Params as dict
    :type OutputParams : dict
    :param i: cell load current [A]
    :type i : float
    :param file : file object
    :return: None
    """

    file.write("I :" + str(i) + " A \n\n")
    if PrintMode==True:
        print("I : " + str(i))
    for key in OutputParamsKeys:
        file.write(key + " : " + str(OutputDict[key]) + " " + OutputParams[key] + "\n")
        if PrintMode==True:
            print(key + " : " + str(OutputDict[key]) + " " + OutputParams[key])
    file.write("###########\n")
    if PrintMode==True:
        print("###########")

def Output_Init(InputDict,Title,Name):
    """
    This function initialize output file
    :param InputDict: Input Test Vector
    :type InputDict:dict
    :param Title : Simulation Title
    :type Title :str
    :return: file object
    """
    Art = text2art("Opem")
    if Title not in os.listdir(os.getcwd()):
        os.mkdir(Title)
    file = open(os.path.join(Title,Name+".opem"), "w")
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

def CSV_Init(OutputParamsKeys,OutputParams,Title,Name):
    """
    This function initialize csv file
    :param OutputParamsKeys: OutputParams Key as list
    :type OutputParamsKeys : list
    :param OutputParams : Output Params as dict
    :type OutputParams : dict
    :return: file object
    """
    if Title not in os.listdir(os.getcwd()):
        os.mkdir(Title)
    file = open(os.path.join(Title,Name+".csv"), "w")
    file.write("I (A),")
    for index, item in enumerate(OutputParamsKeys):
        file.write(item + " (" + OutputParams[item] + ")")
        if index < len(OutputParamsKeys) - 1:
            file.write(",")
    file.write("\n")
    return file

def None_Omit(Input_Str):
    '''
    This function repleace None object with "None" string
    :param Input_Str: Input String
    :type Input_Str : str
    :return: modified string as str
    '''
    result=Input_Str
    result=result.replace("None",'\"None\"')
    return result
def HTML_Init(Title,Name):
    """
    This function initialize html file
    :param OutputParamsKeys: OutputParams Key as list
    :type OutputParamsKeys : list
    :param OutputParams : Output Params as dict
    :type OutputParams : dict
    :return: file object
    """
    if Title not in os.listdir(os.getcwd()):
        os.mkdir(Title)
    file=io.open(os.path.join(Title,Name+".html"),"w", encoding="utf-8")
    file.write("<html>\n")
    file.write("<head>\n")
    file.write("<title>"+Name+"</title>\n")
    file.write("<script>\n"+JS_SCRIPT+"\n</script>\n")
    file.write("</head>\n<body>\n")
    file.write('<h1 style="border-bottom:1px solid black;text-align:center;">OPEM Report ('+Title+" Model)"+'</h1>\n')
    return file

def HTML_Chart(x,y,color,x_label,y_label,chart_name,size,file):
    '''
    This function write chartjs chart in html file
    :param x: x data as a string list
    :type x : str
    :param y: y data as string list
    :type y : str
    :param color: color code of chart
    :type color : str
    :param x_label:x-axis label
    :type x_label : str
    :param y_label:y-axis label
    :type y_label : str
    :param chart_name: chart name
    :type chart_name : str
    :param size: chart size in pixel
    :type size : str
    :param file: html file object
    :type file : file object
    :return: None
    '''
    y_data=None_Omit(y)
    file.write(LINE_CHART.format(x,y_data,color,y_label,x_label,chart_name,size))

def HTML_Input_Table(Input_Dict,Input_Params,file):
    '''
    This function add table to html file
    :param Input_Dict: Input values dictionary
    :type Input_Dict : dict
    :param Input_Params: Input params dictionary
    :type Input_Params : dict
    :param file: html file object
    :type file : file object
    :return: None
    '''
    file.write('<table style="border:1px solid black;border-collapse: collapse;margin:auto;">\n')
    file.write('<tr align="center" style="border:1px solid black;border-collapse: collapse;">\n')
    file.write('<td style="border:1px solid black;padding:4px;border-collapse: collapse;">\n'+"Input\n</td>")
    file.write('<td style="border:1px solid black;padding:4px;border-collapse: collapse;">\n' + "Description\n</td>")
    file.write('<td style="border:1px solid black;padding:4px;border-collapse: collapse;">\n' + "Value\n</td>\n</tr>\n")
    Input_Params_Keys=list(Input_Params.keys())
    Input_Params_Keys.sort()
    for key in Input_Params_Keys:
        file.write('<tr align="center" style="border:1px solid black;border-collapse: collapse;">\n')
        file.write('<td style="border:1px solid black;padding:4px;border-collapse: collapse;">\n'+key+"\n</td>\n")
        file.write('<td style="border:1px solid black;padding:4px;border-collapse: collapse;">\n'+Input_Params[key]+"\n</td>\n")
        file.write('<td style="border:1px solid black;padding:4px;border-collapse: collapse;">\n'+str(Input_Dict[key])+"\n</td>\n")
    file.write("</table>")


def HTML_End(file):
    '''
    This function add end part of html file
    :param file: html file object
    :type file : file object
    :return: None
    '''

    file.write('<p style="text-align:center;position:absoloute;border-top:1px solid black;">Generated By ' \
    '<a href="http://opem.ecsim.ir">OPEM</a> Version ' + str(Version) + '</p>\n')
    file.write("</body>\n")
    file.write("</html>")

def CSV_Save(OutputParamsKeys, OutputDict, i, file):
    """
    This Function Save Parameters In CSV File
    :param OutputParamsKeys : OutputParams Key as  list
    :type OutputParamsKeys : list
    :param OutputDict: Analysis Result Dictionary
    :type OutputDict:dict
    :param i: cell load current [A]
    :type i : float
    :param file : file object
    :return: None
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
    :type Input_Dict : dict
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
    :type Input_Dict : dict
    :return: Modified Dictionary
    '''
    try:
        if Input_Dict["alpha"] > 1:
            Input_Dict["alpha"] = 1
            print("[Warning] Opem Automatically Set Alpha To Maximum Value (1) ")
        elif Input_Dict["alpha"] < 0:
            Input_Dict["alpha"] = 0
            print("[Warning] Opem Automatically Set Alpha To Maximum Value (0) ")
        return Input_Dict
    except Exception:
        return Input_Dict
