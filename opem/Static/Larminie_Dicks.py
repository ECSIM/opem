# -*- coding: utf-8 -*-
import math
from opem.Static.Amphlett import Power_Calc,Efficiency_Calc,VStack_Calc,PowerStack_Calc
from opem.Params import Larminiee_InputParams as InputParams
from opem.Params import Larminiee_OutputParams as OutputParams
from opem.Functions import *
from opem.Params import Larminiee_Description
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
        print("[Error] Vcell Calculation Error (E0:%s, i:%s, i_0:%s, i_n:%s, i_L:%s, R_M:%s, A:%s, B:%s)"%(str(E0),
                                                                                                           str(i),
                                                                                                           str(i_0),
                                                                                                           str(i_n),
                                                                                                           str(i_L),
                                                                                                           str(R_M),
                                                                                                           str(A),
                                                                                                           str(B)))


def Static_Analysis(InputMethod=Get_Input, TestMode=False, PrintMode=True, ReportMode=True):
    """
    This function run Larminie-Dicks static analysis with calling other functions
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
        Simulation_Title="Larminie-Dicks"
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
        Input_Dict=filter_alpha(Input_Dict)
        Name=Input_Dict["Name"]
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
                Output_Dict["Vcell"] = Vcell_Calc(E0=Input_Dict["E0"],i=i,i_0=Input_Dict["i_0"],i_n=Input_Dict["i_n"],
                                                  i_L=Input_Dict["i_L"],R_M=Input_Dict["RM"],B=Input_Dict["B"],A=Input_Dict["A"])
                [Warning1, I_Warning] = warning_check_1(Output_Dict["Vcell"], I_Warning, i, Warning1)
                Output_Dict["PEM Efficiency"] = Efficiency_Calc(Output_Dict["Vcell"])
                Output_Dict["Power"] = Power_Calc(Output_Dict["Vcell"], i)
                Output_Dict["VStack"] = VStack_Calc(Input_Dict["N"], Output_Dict["Vcell"])
                Output_Dict["Power-Stack"] = PowerStack_Calc(Output_Dict["Power"], Input_Dict["N"])
                Vstack_List.append(Output_Dict["VStack"])
                Power_List.append(Output_Dict["Power-Stack"])
                if ReportMode==True:
                    Output_Save(OutputParamsKeys, Output_Dict,OutputParams, i, OutputFile,PrintMode)
                    CSV_Save(OutputParamsKeys, Output_Dict, i, CSVFile)
                i = rounder(i + IStep, Precision)
            except Exception as e:
                print(e)
                i = rounder(i + IStep, Precision)
                if ReportMode==True:
                    Output_Save(OutputParamsKeys, Output_Dict, OutputParams, i, OutputFile,PrintMode)
                    CSV_Save(OutputParamsKeys, Output_Dict, i, CSVFile)
        if ReportMode==True:
            HTML_Desc(Simulation_Title, Larminiee_Description, HTMLFile)
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
        print("[Error] Larminiee Simulation Failed!(Check Your Inputs)")
