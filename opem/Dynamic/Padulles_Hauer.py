# -*- coding: utf-8 -*-
from opem.Params import Padulles_Hauer_InputParams as InputParams
from opem.Params import Padulles_Hauer_Outparams as OutputParams
from opem.Static.Amphlett import Power_Calc
from opem.Dynamic.Padulles1 import PH2_Calc,PO2_Calc,Kr_Calc,Vcell_Calc,qO2_Calc,Efficiency_Calc
from opem.Dynamic.Padulles2 import Enernst_Calc,PH2O_Calc
from opem.Functions import *
from opem.Params import Padulles_Hauer_Description
import os




def qH2_Calc(qMethanol,CV,t1,t2):
    '''
    This function calculate qH2
    :param qMethanol: Molar flow of Methanol [kmol.s^(-1)
    :type qMethanol : float
    :param CV: Conversion factor
    :type CV : float
    :param t1: Reformer time constant
    :type t1 : float
    :param t2 : Reformer time constant
    :type t2 : float
    :return: qH2 as float
    '''
    try:
        result=(qMethanol*CV)/(t1+((t2)**2)+(t1+t2)+1)
        return result
    except Exception:
        print("[Error] qH2 Calculation Failed (qMethanol:%s, CV:%s, t1:%s, t2:%s)"%(str(qMethanol),str(CV),str(t1),
                                                                                    str(t2)))

def Dynamic_Analysis(InputMethod=Get_Input, TestMode=False, PrintMode=True, ReportMode=True):
    """
    This function run Padulles I analysis  with calling other functions
    :param InputMethod : Input Function Or Input Test Vector
    :param TestMode : Test Mode Flag
    :type InputMethod : dict or Get_Input function object
    :type TestMode:bool
    :param PrintMode : Print Mode Control Flag (True : Print Outputs)
    :type PrintMode:bool
    :param ReportMode : Report Mode Control Flag (True : Generate Report)
    :type ReportMode: bool
    :return: Result as dict
    """
    OutputFile = None
    CSVFile = None
    Warning1 = False
    Warning2 = False
    I_Warning = 0
    try:
        Simulation_Title="Padulles-Hauer"
        if PrintMode==True:
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
        if PrintMode==True:
            print("Analyzing . . .")
        Name = Input_Dict["Name"]
        if ReportMode==True:
            OutputFile = Output_Init(Input_Dict,Simulation_Title,Name)
            CSVFile = CSV_Init(OutputParamsKeys,OutputParams,Simulation_Title,Name)
            HTMLFile = HTML_Init(Simulation_Title, Name)
        IEnd = Input_Dict["i-stop"]
        IStep = Input_Dict["i-step"]
        Precision = get_precision(IStep)
        i = Input_Dict["i-start"]
        I_List = []
        Power_List = []
        Vstack_List = []
        Kr=Kr_Calc(Input_Dict["N0"])
        qH2=qH2_Calc(Input_Dict["qMethanol"],Input_Dict["CV"],Input_Dict["t1"],Input_Dict["t2"])
        qO2=qO2_Calc(qH2,Input_Dict["rho"])
        while i < IEnd:
            try:
                I_List.append(i)
                Output_Dict["PO2"]=PO2_Calc(Input_Dict["KO2"],Input_Dict["tO2"],Kr,i,qO2)
                Output_Dict["PH2"]=PH2_Calc(Input_Dict["KH2"],Input_Dict["tH2"],Kr,i,qH2)
                Output_Dict["PH2O"]=PH2O_Calc(Input_Dict["KH2O"],Input_Dict["tH2O"],Kr,i,qH2)
                Output_Dict["E"]=Enernst_Calc(Input_Dict["E0"],Input_Dict["N0"],Input_Dict["T"],Output_Dict["PH2"],Output_Dict["PO2"],Output_Dict["PH2O"])
                Output_Dict["FC Voltage"]=Vcell_Calc(Output_Dict["E"],Input_Dict["B"],Input_Dict["C"],i,Input_Dict["Rint"])
                [Warning1, I_Warning] = warning_check_1(Output_Dict["FC Voltage"], I_Warning, i, Warning1)
                Warning2 = warning_check_2(Vcell=Output_Dict["FC Voltage"], warning_flag=Warning2)
                Vstack_List.append(Output_Dict["FC Voltage"])
                Output_Dict["FC Efficiency"] = Efficiency_Calc(Output_Dict["FC Voltage"],Input_Dict["N0"])
                Output_Dict["FC Power"] = Power_Calc(Output_Dict["FC Voltage"], i)
                Power_List.append(Output_Dict["FC Power"])
                if ReportMode==True:
                    Output_Save(OutputParamsKeys, Output_Dict,OutputParams, i, OutputFile,PrintMode)
                    CSV_Save(OutputParamsKeys, Output_Dict, i, CSVFile)
                i = rounder(i + IStep, Precision)
            except Exception as e:
                print(str(e))
                i = rounder(i + IStep, Precision)
                if ReportMode==True:
                    Output_Save(OutputParamsKeys, Output_Dict, OutputParams, i, OutputFile,PrintMode)
                    CSV_Save(OutputParamsKeys, Output_Dict, i, CSVFile)
        if ReportMode==True:
            HTML_Desc(Simulation_Title, Padulles_Hauer_Description, HTMLFile)
            HTML_Input_Table(Input_Dict=Input_Dict, Input_Params=InputParams, file=HTMLFile)
            HTML_Chart(x=str(I_List), y=str(Power_List), color='rgba(255,99,132,1)', x_label="I(A)", y_label="P(W)",
                    chart_name="FC-Power", size="600px", file=HTMLFile)
            HTML_Chart(x=str(I_List), y=str(Vstack_List), color='rgba(99,100,255,1)', x_label="I(A)", y_label="V(V)",
                    chart_name="FC-Voltage", size="600px", file=HTMLFile)
            warning_print(warning_flag_1=Warning1, warning_flag_2=Warning2, I_Warning=I_Warning, file=HTMLFile,
                          PrintMode=PrintMode)
            HTML_End(HTMLFile)
            OutputFile.close()
            CSVFile.close()
            HTMLFile.close()
        if PrintMode==True:
            print("Done!")
        if not TestMode:
            if PrintMode==True:
                print("Result In -->" + os.path.join(os.getcwd(),Simulation_Title))
        else:
            return {"P": Power_List, "I": I_List, "V": Vstack_List}
    except Exception:
        print("[Error] Padulles-Hauer Dynamic Simulation Failed!(Check Your Inputs)")
