# -*- coding: utf-8 -*-
import math
from opem.Static.Amphlett import Power_Calc,Efficiency_Calc,VStack_Calc,PowerStack_Calc,Power_Thermal_Calc,Power_Total_Calc,Linear_Aprox_Params_Calc,Max_Params_Calc
from opem.Params import Larminiee_InputParams as InputParams
from opem.Params import Larminiee_OutputParams as OutputParams
from opem.Functions import *
from opem.Params import Larminiee_Description,Overall_Params_Max_Description,Overall_Params_Linear_Description
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
    Overall_Params_Max = {}
    Overall_Params_Linear = {}
    Simulation_Title = "Larminie-Dicks"
    try:

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
        Efficiency_List = []
        Power_List = []
        Vstack_List = []
        Power_Thermal_List = []
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
                Output_Dict["Power-Thermal"] = Power_Thermal_Calc(VStack=Output_Dict["VStack"], N=Input_Dict["N"], i=i)
                Vstack_List.append(Output_Dict["VStack"])
                Efficiency_List.append(Output_Dict["PEM Efficiency"])
                Power_List.append(Output_Dict["Power-Stack"])
                Power_Thermal_List.append(Output_Dict["Power-Thermal"])
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
        [Estimated_V, B0, B1] = linear_plot(x=I_List, y=Vstack_List)
        Linear_Approx_Params = Linear_Aprox_Params_Calc(B0, B1)
        Max_Params = Max_Params_Calc(Power_List, Efficiency_List, Vstack_List)
        Power_Total = Power_Total_Calc(Vstack_List, IStep, Input_Dict["N"])
        Overall_Params_Linear["Pmax(L-Approx)"] = Linear_Approx_Params[0]
        Overall_Params_Linear["V0"] = B0
        Overall_Params_Linear["K"] = B1
        Overall_Params_Linear["VFC|Pmax(L-Approx)"] = Linear_Approx_Params[1]

        Overall_Params_Max["Pmax"] = Max_Params["Max_Power"]
        Overall_Params_Max["VFC|Pmax"] = Max_Params["Max_VStack"]
        Overall_Params_Max["Efficiency|Pmax"] = Max_Params["Max_EFF"]
        Overall_Params_Max["Ptotal(Elec)"] = Power_Total[0]
        Overall_Params_Max["Ptotal(Thermal)"] = Power_Total[1]
        if ReportMode==True:
            HTML_Desc(Simulation_Title, Larminiee_Description, HTMLFile)
            HTML_Input_Table(Input_Dict=Input_Dict, Input_Params=InputParams, file=HTMLFile)
            HTML_Overall_Params_Table(Overall_Params_Max, Overall_Params_Max_Description, file=HTMLFile, header=True)
            HTML_Chart(x=str(I_List), y=str(Power_List), color='rgba(255,99,132,1)', x_label="I(A)", y_label="P(W)",
                    chart_name="Power-Stack", size="600px", file=HTMLFile)
            HTML_Chart(x=str(I_List), y=[str(Vstack_List), str(Estimated_V)],
                       color=['rgba(99,100,255,1)', 'rgb(238, 210, 141)'], x_label="I(A)", y_label="V(V)",
                       chart_name=["Voltage-Stack", "Linear-Apx"], size="600px", file=HTMLFile)
            HTML_Overall_Params_Table(Overall_Params_Linear, Overall_Params_Linear_Description, file=HTMLFile,
                                      header=False)
            HTML_Chart(x=str(I_List), y=str(Efficiency_List), color='rgb(255, 0, 255)', x_label="I(A)", y_label="EFF",
                       chart_name="Efficiency", size="600px", file=HTMLFile)
            HTML_Chart(x=str(list(map(rounder, Power_List))), y=str(Efficiency_List), color='rgb(238, 210, 141)',
                       x_label="P(W)", y_label="EFF",
                       chart_name="Efficiency vs Power", size="600px", file=HTMLFile)
            HTML_Chart(x=str(I_List), y=str(Power_Thermal_List), color='rgb(255, 0, 255)', x_label="I(A)",
                       y_label="P(W)",
                       chart_name="Power(Thermal)", size="600px", file=HTMLFile)
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
            return {"Status":True,"P": Power_List, "I": I_List, "V": Vstack_List,"EFF":Efficiency_List,"Ph":Power_Thermal_List,"V0":B0,"K":B1}
    except Exception:
        if TestMode==True:
            return {"Status":False,"Message":"[Error] "+Simulation_Title+" Simulation Failed!(Check Your Inputs)"}
        else:
            print("[Error] "+Simulation_Title+" Simulation Failed!(Check Your Inputs)")
