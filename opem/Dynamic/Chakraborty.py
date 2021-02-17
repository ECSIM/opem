# -*- coding: utf-8 -*-
"""Chakraborty model functions."""
import os
import math
from opem.Params import Chakraborty_InputParams as InputParams
from opem.Params import Chakraborty_Outparams as OutputParams
from opem.Params import Chakraborty_Params_Default as Defaults
from opem.Params import R,F
from opem.Static.Amphlett import Power_Calc, Power_Thermal_Calc, Power_Total_Calc, Linear_Aprox_Params_Calc, Max_Params_Calc
from opem.Dynamic.Padulles1 import Efficiency_Calc
from opem.Dynamic.Padulles2 import Enernst_Calc
import opem.Functions
from opem.Params import Chakraborty_Description, Overall_Params_Max_Description, Overall_Params_Linear_Description, Report_Message

def PH2_Init_Calc(KH2, u, I):
    """
    Calculate PH2-Initial.

    :param KH2: hydrogen valve constant [kmol.s^(-1).atm^(-1)]
    :type KH2 : float
    :param u: fuel utilization  ratio
    :type u: float
    :param I: cell load current [A]
    :type I : float
    :return: PH2-Initial [atm] as float
    """
    try:
        result = ((1 / KH2) * ((1/u) - 1) * I/(2*F))
        return result
    except (TypeError, ZeroDivisionError):
        print(
            "[Error] PH2-Initial Calculation Failed (KH2:%s, u:%s, I:%s)" %
            (str(KH2), str(u), str(I)))

def PO2_Init_Calc(KO2, u, rHO, I):
    """
    Calculate PO2-Initial.

    :param KO2: oxygen valve constant [kmol.s^(-1).atm^(-1)]
    :type KO2 : float
    :param u: fuel utilization  ratio
    :type u: float
    :param rHO: ratio  of  hydrogen  to  oxygen  input  flow  rates
    :type rHO: float
    :param I: cell load current [A]
    :type I : float
    :return: PO2-Initial [atm] as float
    """
    try:
        result = ((1 / KO2) * ((1/(u*rHO)) - 0.5) * I/(2*F))
        return result
    except (TypeError, ZeroDivisionError):
        print(
            "[Error] PO2-Initial Calculation Failed (KO2:%s, u:%s, rHO:%s, I:%s)" %
            (str(KO2), str(u), str(rHO), str(I)))

def PH2O_Init_Calc(KH2O, I):
    """
    Calculate PH2O-Initial.

    :param KH2O: water valve constant [kmol.s^(-1).atm^(-1)]
    :type KH2O : float
    :param I: cell load current [A]
    :type I : float
    :return: PH2O-Initial [atm] as float
    """
    try:
        result = ((1 / KH2O) * I/(2*F))
        return result
    except (TypeError, ZeroDivisionError):
        print(
            "[Error] PH2O-Initial Calculation Failed (KH2O:%s, I:%s)" %
            (str(KH2O), str(I)))

def I_Ratio_Calc(PH2_init, PO2_init, PH2O_init, I):
    """
    Calculate I-Ratio.

    :param PH2_init: hydrogen partial pressure initial [atm]
    :type PH2_init: float
    :param PO2_init: oxygen partial pressure initial [atm]
    :type PO2_init: float
    :param PH2O_init: water partial pressure initial [atm]
    :type PH2O_init: float
    :param I: cell load current [A]
    :type I: float
    :return: I-Ratio
    """
    try:
        result = I/(PH2_init*math.sqrt(PO2_init)/PH2O_init)
        return result
    except (TypeError, ZeroDivisionError):
        print("[Error] I-Ratio Calculation Error (PH2_init:%s, PO2_init:%s, PH2O_init:%s, I:%s)" %(str(PH2_init), str(PO2_init), str(PH2O_init), str(I)))

def Vcell_Calc(Enernst, T, I, I_ratio, Rint, N):
    """
    Calculate cell voltage.

    :param Enernst:  Enernst [V}
    :type Enernst : float
    :param T: cell operation temperature [K]
    :type T : float
    :param I: cell load current [A]
    :type I : float
    :param I_ratio: cell load current ratio
    :type I_ratio: float
    :param Rint: fuel cell internal resistance [ohm]
    :type Rint : float
    :param N: number of fuel cells in the stack
    :type N : int
    :return:  cell voltage [V] as float
    """
    try:
        loss = ((R * T)/(4 * F)) * math.log(I_ratio) - Rint*I
        result = Enernst + (N * loss)
        return result
    except TypeError:
        print(
            "[Error] Vcell Calculation Error (Enernst:%s, T:%s, I:%s, I-Ratio:%s, Rint:%s, N:%s)" %
            (str(Enernst), str(T), str(I), str(I_ratio), str(Rint), str(N)))


def Dynamic_Analysis(
        InputMethod=opem.Functions.Get_Input,
        TestMode=False,
        PrintMode=True,
        ReportMode=True):
    """
    Run Chakraborty analysis.

    :param InputMethod : input function or input test vector
    :param TestMode : test mode flag
    :type InputMethod : dict or Get_Input function object
    :type TestMode:bool
    :param PrintMode : print mode control flag (True : print outputs)
    :type PrintMode:bool
    :param ReportMode : report mode control flag (True : generate report)
    :type ReportMode: bool
    :return: result as dict
    """
    OutputFile = None
    CSVFile = None
    Warning1 = False
    Warning2 = False
    I_Warning = 0
    Overall_Params_Max = {}
    Overall_Params_Linear = {}
    Simulation_Title = "Chakraborty"
    try:

        if PrintMode:
            print("###########")
            print(Simulation_Title + "-Model Simulation")
            print("###########")
        OutputParamsKeys = sorted(OutputParams.keys())
        Output_Dict = dict(
            zip(OutputParamsKeys, [None] * len(OutputParamsKeys)))
        if not TestMode:
            Input_Dict = InputMethod(InputParams, params_default=Defaults)
        else:
            Input_Dict = InputMethod
            Input_Dict = opem.Functions.filter_default(
                input_dict=Input_Dict, params_default=Defaults)
        Input_Dict = opem.Functions.filter_lambda(Input_Dict)
        if PrintMode:
            print("Analyzing . . .")
        Name = Input_Dict["Name"]
        if ReportMode:
            OutputFile = opem.Functions.Output_Init(
                Input_Dict, Simulation_Title, Name)
            CSVFile = opem.Functions.CSV_Init(
                OutputParamsKeys,
                OutputParams,
                Simulation_Title,
                Name)
            HTMLFile = opem.Functions.HTML_Init(Simulation_Title, Name)
        IEnd = Input_Dict["i-stop"]
        IStep = Input_Dict["i-step"]
        Precision = opem.Functions.get_precision(IStep)
        [i, IEnd, IStep] = opem.Functions.filter_range(Input_Dict["i-start"], IEnd, IStep)
        I_List = []
        Power_List = []
        Vstack_List = []
        Efficiency_List = []
        PH2_Init_List = []
        PO2_Init_List = []
        PH2O_Init_List = []
        I_Ratio_List = []
        Power_Thermal_List = []
        while i < IEnd:
            try:
                I_List.append(i)
                Output_Dict["PO2-Initial"] = PO2_Init_Calc(
                    Input_Dict["KO2"], Input_Dict["u"], Input_Dict["rho"], i)
                Output_Dict["PH2-Initial"] = PH2_Init_Calc(
                    Input_Dict["KH2"], Input_Dict["u"], i)
                PH2_Init_List.append(Output_Dict["PH2-Initial"])
                PO2_Init_List.append(Output_Dict["PO2-Initial"])
                Output_Dict["PH2O-Initial"] = PH2O_Init_Calc(
                    Input_Dict["KH2O"], i)
                PH2O_Init_List.append(Output_Dict["PH2O-Initial"])
                Output_Dict["E"] = Enernst_Calc(
                    Input_Dict["E0"],
                    Input_Dict["N0"],
                    Input_Dict["T"],
                    Input_Dict["PH2"],
                    Input_Dict["PO2"],
                    Input_Dict["PH2O"])
                Output_Dict["I-Ratio"] = I_Ratio_Calc(Output_Dict["PH2-Initial"], Output_Dict["PO2-Initial"], Output_Dict["PH2O-Initial"], i)
                I_Ratio_List.append(Output_Dict["I-Ratio"])
                Output_Dict["FC Voltage"] = Vcell_Calc(
                    Output_Dict["E"], Input_Dict["T"], i, Output_Dict["I-Ratio"], Input_Dict["R"], Input_Dict["N0"])
                [Warning1, I_Warning] = opem.Functions.warning_check_1(
                    Output_Dict["FC Voltage"], I_Warning, i, Warning1)
                Warning2 = opem.Functions.warning_check_2(
                    Vcell=Output_Dict["FC Voltage"],
                    warning_flag=Warning2)
                Vstack_List.append(Output_Dict["FC Voltage"])
                Output_Dict["FC Efficiency"] = Efficiency_Calc(
                    Output_Dict["FC Voltage"], Input_Dict["N0"])
                Efficiency_List.append(Output_Dict["FC Efficiency"])
                Output_Dict["FC Power"] = Power_Calc(
                    Output_Dict["FC Voltage"], i)
                Output_Dict["Power-Thermal"] = Power_Thermal_Calc(
                    VStack=Output_Dict["FC Voltage"], N=Input_Dict["N0"], i=i)
                Power_List.append(Output_Dict["FC Power"])
                Power_Thermal_List.append(Output_Dict["Power-Thermal"])
                if ReportMode:
                    opem.Functions.Output_Save(
                        OutputParamsKeys,
                        Output_Dict,
                        OutputParams,
                        i,
                        OutputFile,
                        PrintMode)
                    opem.Functions.CSV_Save(
                        OutputParamsKeys, Output_Dict, i, CSVFile)
                i = opem.Functions.rounder(i + IStep, Precision)
            except Exception as e:
                print(str(e))
                i = opem.Functions.rounder(i + IStep, Precision)
                if ReportMode:
                    opem.Functions.Output_Save(
                        OutputParamsKeys,
                        Output_Dict,
                        OutputParams,
                        i,
                        OutputFile,
                        PrintMode)
                    opem.Functions.CSV_Save(
                        OutputParamsKeys, Output_Dict, i, CSVFile)
        [Estimated_V, B0, B1] = opem.Functions.linear_plot(
            x=I_List, y=Vstack_List)
        Linear_Approx_Params = Linear_Aprox_Params_Calc(B0, B1)
        Max_Params = Max_Params_Calc(Power_List, Efficiency_List, Vstack_List)
        Power_Total = Power_Total_Calc(Vstack_List, IStep, Input_Dict["N0"])
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
            OutputFile.close()
            CSVFile.close()
            if PrintMode:
                print(Report_Message)
            opem.Functions.HTML_Desc(
                Simulation_Title,
                Chakraborty_Description,
                HTMLFile)
            opem.Functions.HTML_Input_Table(
                Input_Dict=Input_Dict,
                Input_Params=InputParams,
                file=HTMLFile)
            opem.Functions.HTML_Overall_Params_Table(
                Overall_Params_Max,
                Overall_Params_Max_Description,
                file=HTMLFile,
                header=True)
            opem.Functions.HTML_Chart(
                x=str(I_List),
                y=str(Power_List),
                color='rgba(255,99,132,1)',
                x_label="I(A)",
                y_label="P(W)",
                chart_name="FC-Power",
                size="600px",
                file=HTMLFile)
            opem.Functions.HTML_Chart(
                x=str(I_List), y=[
                    str(Vstack_List), str(Estimated_V)], color=[
                    'rgba(99,100,255,1)', 'rgb(238, 210, 141)'], x_label="I(A)", y_label="V(V)", chart_name=[
                    "FC-Voltage", "Linear-Apx"], size="600px", file=HTMLFile)
            opem.Functions.HTML_Overall_Params_Table(
                Overall_Params_Linear,
                Overall_Params_Linear_Description,
                file=HTMLFile,
                header=False)
            opem.Functions.HTML_Chart(
                x=str(I_List),
                y=str(Efficiency_List),
                color='rgb(255, 0, 255)',
                x_label="I(A)",
                y_label="EFF",
                chart_name="Efficiency",
                size="600px",
                file=HTMLFile)
            opem.Functions.HTML_Chart(
                x=str(I_List),
                y=str(PO2_Init_List),
                color='	rgb(0, 255, 128)',
                x_label="I(A)",
                y_label="PO2-Init(atm)",
                chart_name="PO2-Init",
                size="600px",
                file=HTMLFile)
            opem.Functions.HTML_Chart(
                x=str(I_List),
                y=str(PH2_Init_List),
                color='	rgb(128, 0, 255)',
                x_label="I(A)",
                y_label="PH2-Init(atm)",
                chart_name="PH2-Init",
                size="600px",
                file=HTMLFile)
            opem.Functions.HTML_Chart(
                x=str(I_List),
                y=str(PH2O_Init_List),
                color='	rgb(165, 185, 112)',
                x_label="I(A)",
                y_label="PH2O-Init(atm)",
                chart_name="PH2O-Init",
                size="600px",
                file=HTMLFile)
            opem.Functions.HTML_Chart(x=str(list(map(opem.Functions.rounder,
                                                     Power_List))),
                                      y=str(Efficiency_List),
                                      color='rgb(238, 210, 141)',
                                      x_label="P(W)",
                                      y_label="EFF",
                                      chart_name="Efficiency vs Power",
                                      size="600px",
                                      file=HTMLFile)
            opem.Functions.HTML_Chart(
                x=str(I_List),
                y=str(Power_Thermal_List),
                color='rgb(255, 0, 255)',
                x_label="I(A)",
                y_label="P(W)",
                chart_name="Power(Thermal)",
                size="600px",
                file=HTMLFile)
            opem.Functions.HTML_Chart(
                x=str(I_List),
                y=str(I_Ratio_List),
                color='	rgb(165, 185, 112)',
                x_label="I(A)",
                y_label="I-Ratio",
                chart_name="I-Ratio",
                size="600px",
                file=HTMLFile)
            opem.Functions.warning_print(
                warning_flag_1=Warning1,
                warning_flag_2=Warning2,
                I_Warning=I_Warning,
                file=HTMLFile,
                PrintMode=PrintMode)
            opem.Functions.HTML_End(HTMLFile)
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
                "PO2-Init": PO2_Init_List,
                "PH2-Init": PH2_Init_List,
                "PH2O-Init": PH2O_Init_List,
                "I-Ratio": I_Ratio_List,
                "Ph": Power_Thermal_List,
                "V0": B0,
                "K": B1,
                "VE": Estimated_V}
    except Exception:
        if TestMode:
            return {
                "Status": False,
                "Message": "[Error] " +
                Simulation_Title +
                " Simulation Failed!(Check Your Inputs)"}
        print("[Error] " +Simulation_Title +" Simulation Failed!(Check Your Inputs)")