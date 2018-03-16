# -*- coding: utf-8 -*-
import math
from opem.Params import Chamberline_InputParams as InputParams
from opem.Params import Chamberline_OutputParams as OutputParams
from opem.Static.Amphlett import Efficiency_Calc,Power_Calc,VStack_Calc,PowerStack_Calc
from opem.Functions import *
from opem.Params import Chamberline_Description
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
    except Exception:
        print("[Error] Vcell Calculation Error (E0:%s, b:%s, R:%s, m:%s, n:%s, i:%s, A:%s)"%(str(E0),str(b),str(R),
                                                                                             str(m),str(n),str(i),
                                                                                             str(A)))


def Static_Analysis(InputMethod=Get_Input, TestMode=False, PrintMode=True, ReportMode=True):
    """
    This function run Chamberline-Kim static analysis with calling other functions
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
        Simulation_Title="Chamberline-Kim"
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
        while i < IEnd:
            try:
                I_List.append(i)
                Output_Dict["Vcell"] = Vcell_Calc(Input_Dict["E0"],Input_Dict["b"],Input_Dict["R"],Input_Dict["m"],Input_Dict["n"],i,Input_Dict["A"])
                [Warning1, I_Warning] = warning_check_1(Output_Dict["Vcell"], I_Warning, i, Warning1)
                Warning2 = warning_check_2(Vcell=Output_Dict["Vcell"], warning_flag=Warning2)
                Output_Dict["PEM Efficiency"] = Efficiency_Calc(Output_Dict["Vcell"])
                Output_Dict["Power"] = Power_Calc(Output_Dict["Vcell"], i)
                Output_Dict["VStack"] = VStack_Calc(Input_Dict["N"], Output_Dict["Vcell"])
                Vstack_List.append(Output_Dict["VStack"])
                Output_Dict["Power-Stack"]=PowerStack_Calc(Output_Dict["Power"],Input_Dict["N"])
                Power_List.append(Output_Dict["Power-Stack"])
                if ReportMode==True:
                    Output_Save(OutputParamsKeys, Output_Dict,OutputParams,i, OutputFile,PrintMode)
                    CSV_Save(OutputParamsKeys, Output_Dict, i, CSVFile)
                i = rounder(i + IStep, Precision)
            except Exception as e:
                print(e)
                i = rounder(i + IStep, Precision)
                if ReportMode==True:
                    Output_Save(OutputParamsKeys, Output_Dict, OutputParams, i, OutputFile,PrintMode)
                    CSV_Save(OutputParamsKeys, Output_Dict, i, CSVFile)
        if ReportMode==True:
            HTML_Desc(Simulation_Title, Chamberline_Description, HTMLFile)
            HTML_Input_Table(Input_Dict=Input_Dict, Input_Params=InputParams, file=HTMLFile)
            HTML_Chart(x=str(I_List), y=str(Power_List), color='rgba(255,99,132,1)', x_label="I(A)", y_label="P(W)",
                    chart_name="Power-Stack", size="600px", file=HTMLFile)
            HTML_Chart(x=str(I_List), y=str(Vstack_List), color='rgba(99,100,255,1)', x_label="I(A)", y_label="V(V)",
                    chart_name="Voltage-Stack", size="600px", file=HTMLFile)
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
                print("Result In -->" + os.path.join(os.getcwd(), Simulation_Title))
        else:
            return {"P": Power_List, "I": I_List, "V": Vstack_List}
    except Exception:
        print("[Error] Chamberline-Kim Simulation Failed!(Check Your Inputs)")
