# -*- coding: utf-8 -*-
import math
from opem.Params import Chamberline_InputParams as InputParams
from opem.Params import Chamberline_OutputParams as OutputParams
from opem.Static.Amphlett import Efficiency_Calc, Power_Calc, VStack_Calc, PowerStack_Calc, Power_Thermal_Calc, Power_Total_Calc, Linear_Aprox_Params_Calc, Max_Params_Calc
from opem.Functions import *
from opem.Params import Chamberline_Description, Overall_Params_Max_Description, Overall_Params_Linear_Description
import os
import datetime
from art import text2art


def Vcell_Calc(E0, b, R, m, n, i, A):
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
        J = i / A
        result = E0 - b * math.log(J) - R * J - m * math.exp(n * J)
        return result
    except Exception:
        print(
            "[Error] Vcell Calculation Error (E0:%s, b:%s, R:%s, m:%s, n:%s, i:%s, A:%s)" %
            (str(E0), str(b), str(R), str(m), str(n), str(i), str(A)))


def Static_Analysis(
        InputMethod=Get_Input,
        TestMode=False,
        PrintMode=True,
        ReportMode=True):
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
    Overall_Params_Max = {}
    Overall_Params_Linear = {}
    Simulation_Title = "Chamberline-Kim"
    try:

        if PrintMode:
            print("###########")
            print(Simulation_Title + "-Model Simulation")
            print("###########")
        OutputParamsKeys = sorted(OutputParams.keys())
        Output_Dict = dict(
            zip(OutputParamsKeys, [None] * len(OutputParamsKeys)))
        if not TestMode:
            Input_Dict = InputMethod(InputParams)
        else:
            Input_Dict = InputMethod
        if PrintMode:
            print("Analyzing . . .")
        Name = Input_Dict["Name"]
        if ReportMode:
            OutputFile = Output_Init(Input_Dict, Simulation_Title, Name)
            CSVFile = CSV_Init(
                OutputParamsKeys,
                OutputParams,
                Simulation_Title,
                Name)
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
                Output_Dict["Vcell"] = Vcell_Calc(
                    Input_Dict["E0"],
                    Input_Dict["b"],
                    Input_Dict["R"],
                    Input_Dict["m"],
                    Input_Dict["n"],
                    i,
                    Input_Dict["A"])
                [Warning1, I_Warning] = warning_check_1(
                    Output_Dict["Vcell"], I_Warning, i, Warning1)
                Warning2 = warning_check_2(
                    Vcell=Output_Dict["Vcell"], warning_flag=Warning2)
                Output_Dict["PEM Efficiency"] = Efficiency_Calc(
                    Output_Dict["Vcell"])
                Output_Dict["Power"] = Power_Calc(Output_Dict["Vcell"], i)
                Output_Dict["VStack"] = VStack_Calc(
                    Input_Dict["N"], Output_Dict["Vcell"])
                Vstack_List.append(Output_Dict["VStack"])
                Efficiency_List.append(Output_Dict["PEM Efficiency"])
                Output_Dict["Power-Stack"] = PowerStack_Calc(
                    Output_Dict["Power"], Input_Dict["N"])
                Output_Dict["Power-Thermal"] = Power_Thermal_Calc(
                    VStack=Output_Dict["VStack"], N=Input_Dict["N"], i=i)
                Power_List.append(Output_Dict["Power-Stack"])
                Power_Thermal_List.append(Output_Dict["Power-Thermal"])
                if ReportMode:
                    Output_Save(
                        OutputParamsKeys,
                        Output_Dict,
                        OutputParams,
                        i,
                        OutputFile,
                        PrintMode)
                    CSV_Save(OutputParamsKeys, Output_Dict, i, CSVFile)
                i = rounder(i + IStep, Precision)
            except Exception as e:
                print(e)
                i = rounder(i + IStep, Precision)
                if ReportMode:
                    Output_Save(
                        OutputParamsKeys,
                        Output_Dict,
                        OutputParams,
                        i,
                        OutputFile,
                        PrintMode)
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
        if ReportMode:
            HTML_Desc(Simulation_Title, Chamberline_Description, HTMLFile)
            HTML_Input_Table(
                Input_Dict=Input_Dict,
                Input_Params=InputParams,
                file=HTMLFile)
            HTML_Overall_Params_Table(
                Overall_Params_Max,
                Overall_Params_Max_Description,
                file=HTMLFile,
                header=True)
            HTML_Chart(
                x=str(I_List),
                y=str(Power_List),
                color='rgba(255,99,132,1)',
                x_label="I(A)",
                y_label="P(W)",
                chart_name="Power-Stack",
                size="600px",
                file=HTMLFile)
            HTML_Chart(
                x=str(I_List), y=[
                    str(Vstack_List), str(Estimated_V)], color=[
                    'rgba(99,100,255,1)', 'rgb(238, 210, 141)'], x_label="I(A)", y_label="V(V)", chart_name=[
                    "Voltage-Stack", "Linear-Apx"], size="600px", file=HTMLFile)
            HTML_Overall_Params_Table(
                Overall_Params_Linear,
                Overall_Params_Linear_Description,
                file=HTMLFile,
                header=False)
            HTML_Chart(
                x=str(I_List),
                y=str(Efficiency_List),
                color='rgb(255, 0, 255)',
                x_label="I(A)",
                y_label="EFF",
                chart_name="Efficiency",
                size="600px",
                file=HTMLFile)
            HTML_Chart(x=str(list(map(rounder,
                                      Power_List))),
                       y=str(Efficiency_List),
                       color='rgb(238, 210, 141)',
                       x_label="P(W)",
                       y_label="EFF",
                       chart_name="Efficiency vs Power",
                       size="600px",
                       file=HTMLFile)
            HTML_Chart(
                x=str(I_List),
                y=str(Power_Thermal_List),
                color='rgb(255, 0, 255)',
                x_label="I(A)",
                y_label="P(W)",
                chart_name="Power(Thermal)",
                size="600px",
                file=HTMLFile)
            warning_print(
                warning_flag_1=Warning1,
                warning_flag_2=Warning2,
                I_Warning=I_Warning,
                file=HTMLFile,
                PrintMode=PrintMode)
            HTML_End(HTMLFile)
            OutputFile.close()
            CSVFile.close()
            HTMLFile.close()
        if PrintMode:
            print("Done!")
        if not TestMode:
            if PrintMode:
                print(
                    "Result In -->" +
                    os.path.join(
                        os.getcwd(),
                        Simulation_Title))
        else:
            return {
                "Status": True,
                "P": Power_List,
                "I": I_List,
                "V": Vstack_List,
                "EFF": Efficiency_List,
                "Ph": Power_Thermal_List,
                "V0": B0,
                "K": B1}
    except Exception:
        if TestMode:
            return {
                "Status": False,
                "Message": "[Error] " +
                Simulation_Title +
                " Simulation Failed!(Check Your Inputs)"}
        else:
            print(
                "[Error] " +
                Simulation_Title +
                " Simulation Failed!(Check Your Inputs)")
