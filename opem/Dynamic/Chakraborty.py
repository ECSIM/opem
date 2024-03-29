# -*- coding: utf-8 -*-
"""Chakraborty model functions."""
import os
import math
from opem.Params import Chakraborty_InputParams as InputParams
from opem.Params import Chakraborty_Outparams as OutputParams
from opem.Params import Chakraborty_Params_Default as Defaults
from opem.Params import R, F, HHV
from opem.Static.Amphlett import Power_Calc, Power_Thermal_Calc, Power_Total_Calc, Linear_Aprox_Params_Calc, Max_Params_Calc
import opem.Functions
from opem.Params import Chakraborty_Description, Overall_Params_Max_Description, Overall_Params_Linear_Description, Report_Message


def Enernst_Calc(E0, N0, T, PH2, PO2, PH2O):
    """
    Calculate Enernst.

    :param E0: open cell voltage [V]
    :type E0: float
    :param N0: number of fuel cells in the stack
    :type N0: int
    :param T: cell operation temperature [K]
    :type T: float
    :param PH2: partial pressure [atm]
    :type PH2: float
    :param PO2: partial pressure [atm]
    :type PO2: float
    :param PH2O:  partial pressure [atm]
    :type PH2O: float
    :return: Enernest [V] as float
    """
    try:
        result = N0 * (E0 - (R * T / (2 * F)) *
                       math.log((PH2 * math.sqrt(PO2)) / PH2O))
        return result
    except (TypeError, ZeroDivisionError, OverflowError, ValueError):
        print(
            "[Error] Enernst Calculation Failed (E0:%s, N0:%s, T:%s, PH2:%s, PO2:%s, PH2O:%s)" %
            (str(E0), str(N0), str(T), str(PH2), str(PO2), str(PH2O)))


def PH2_Calc(KH2, u, I):
    """
    Calculate PH2.

    :param KH2: hydrogen valve constant [kmol.s^(-1).atm^(-1)]
    :type KH2: float
    :param u: fuel utilization  ratio
    :type u: float
    :param I: cell load current [A]
    :type I: float
    :return: PH2 [atm] as float
    """
    try:
        result = ((1 / KH2) * ((1 / u) - 1) * I / (2 * F))
        return result
    except (TypeError, ZeroDivisionError):
        print(
            "[Error] PH2 Calculation Failed (KH2:%s, u:%s, I:%s)" %
            (str(KH2), str(u), str(I)))


def PO2_Calc(KO2, u, rHO, I):
    """
    Calculate PO2.

    :param KO2: oxygen valve constant [kmol.s^(-1).atm^(-1)]
    :type KO2: float
    :param u: fuel utilization  ratio
    :type u: float
    :param rHO: ratio of hydrogen to oxygen input flow rates
    :type rHO: float
    :param I: cell load current [A]
    :type I: float
    :return: PO2 [atm] as float
    """
    try:
        result = ((1 / KO2) * ((1 / (u * rHO)) - 0.5) * I / (2 * F))
        return result
    except (TypeError, ZeroDivisionError):
        print(
            "[Error] PO2 Calculation Failed (KO2:%s, u:%s, rHO:%s, I:%s)" %
            (str(KO2), str(u), str(rHO), str(I)))


def PH2O_Calc(KH2O, I):
    """
    Calculate PH2O.

    :param KH2O: water valve constant [kmol.s^(-1).atm^(-1)]
    :type KH2O: float
    :param I: cell load current [A]
    :type I: float
    :return: PH2O [atm] as float
    """
    try:
        result = ((1 / KH2O) * I / (2 * F))
        return result
    except (TypeError, ZeroDivisionError):
        print(
            "[Error] PH2O Calculation Failed (KH2O:%s, I:%s)" %
            (str(KH2O), str(I)))


def Nernst_Gain_Calc(T, I):
    """
    Calculate Nernst gain.

    :param T: cell operation temperature [K]
    :type T: float
    :param I: cell load current [A]
    :type I: float
    :return: Nernst gain [V] as float
    """
    try:
        return ((R * T) / (4 * F)) * math.log(I)
    except TypeError:
        print(
            "[Error] Nernst Gain Calculation Error (T:%s, I:%s)" %
            (str(T), str(I)))


def Ohmic_Loss_Calc(Rint, I):
    """
    Calculate ohmic loss.

    :param Rint: fuel cell internal resistance [ohm]
    :type Rint: float
    :param I: cell load current [A]
    :type I: float
    :return: ohmic loss [V] as float
    """
    try:
        return Rint * I
    except TypeError:
        print(
            "[Error] Ohmic Loss Calculation Error (Rint:%s, I:%s)" %
            (str(Rint), str(I)))


def Vcell_Calc(Enernst, Nernst_Gain, Ohmic_Loss, N):
    """
    Calculate cell voltage.

    :param Enernst: Enernst [V}
    :type Enernst: float
    :param Nernst_Gain: Nernst Gain [V]
    :type Nernst_Gain: float
    :param Ohmic_Loss: ohmic loss [V]
    :type Ohmic_Loss: float
    :param N: number of fuel cells in the stack
    :type N: int
    :return: cell voltage [V] as float
    """
    try:
        loss = Nernst_Gain - Ohmic_Loss
        result = Enernst + (N * loss)
        return result
    except TypeError:
        print(
            "[Error] Vcell Calculation Error (Enernst:%s, Nernst_Gain:%s, Ohmic_Loss:%s, N:%s)" %
            (str(Enernst), str(Nernst_Gain), str(Ohmic_Loss), str(N)))


def Efficiency_Calc(Vcell, u, N):
    """
    Calculate PEM cell efficiency.

    :param Vcell: cell voltage [V]
    :type Vcell: float
    :param u: fuel utilization ratio
    :type u: float
    :param N: number of fuel cells in the stack
    :type N: int
    :return: efficiency as float
    """
    try:
        result = (u * Vcell) / (N * HHV)
        return result
    except (TypeError, ZeroDivisionError):
        print(
            "[Error] PEM Efficiency Calculation Failed (Vcell:%s, u:%s, N:%s)" %
            (str(Vcell), str(u), str(N)))


def Dynamic_Analysis(
        InputMethod=opem.Functions.Get_Input,
        TestMode=False,
        PrintMode=True,
        ReportMode=True,
        Folder=os.getcwd()):
    """
    Run Chakraborty analysis.

    :param InputMethod: input function or input test vector
    :type InputMethod: dict or Get_Input function object
    :param TestMode: test mode flag
    :type TestMode: bool
    :param PrintMode: print mode control flag (True : print outputs)
    :type PrintMode: bool
    :param ReportMode: report mode control flag (True : generate report)
    :type ReportMode: bool
    :param Folder: output folder address
    :type Folder: str
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
        OutputParamsKeys = sorted(OutputParams)
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
                Input_Dict, Simulation_Title, Name, Folder)
            CSVFile = opem.Functions.CSV_Init(
                OutputParamsKeys,
                OutputParams,
                Simulation_Title,
                Name,
                Folder)
            HTMLFile = opem.Functions.HTML_Init(Simulation_Title, Name, Folder)
        IEnd = Input_Dict["i-stop"]
        IStep = Input_Dict["i-step"]
        Precision = opem.Functions.get_precision(IStep)
        [i, IEnd, IStep] = opem.Functions.filter_range(
            Input_Dict["i-start"], IEnd, IStep)
        I_List = []
        Power_List = []
        Vstack_List = []
        Efficiency_List = []
        PH2_List = []
        PO2_List = []
        PH2O_List = []
        Power_Thermal_List = []
        Ohmic_Loss_List = []
        Nernst_Gain_List = []
        while i < IEnd:
            try:
                I_List.append(i)
                Output_Dict["PO2"] = PO2_Calc(
                    Input_Dict["KO2"], Input_Dict["u"], Input_Dict["rho"], i)
                Output_Dict["PH2"] = PH2_Calc(
                    Input_Dict["KH2"], Input_Dict["u"], i)
                PH2_List.append(Output_Dict["PH2"])
                PO2_List.append(Output_Dict["PO2"])
                Output_Dict["PH2O"] = PH2O_Calc(
                    Input_Dict["KH2O"], i)
                PH2O_List.append(Output_Dict["PH2O"])
                Output_Dict["E"] = Enernst_Calc(
                    Input_Dict["E0"],
                    Input_Dict["N0"],
                    Input_Dict["T"],
                    Output_Dict["PH2"],
                    Output_Dict["PO2"],
                    Output_Dict["PH2O"])
                Output_Dict["Nernst Gain"] = Nernst_Gain_Calc(
                    Input_Dict["T"], i)
                Output_Dict["Ohmic Loss"] = Ohmic_Loss_Calc(Input_Dict["R"], i)
                Nernst_Gain_List.append(Output_Dict["Nernst Gain"])
                Ohmic_Loss_List.append(Output_Dict["Ohmic Loss"])
                Output_Dict["FC Voltage"] = Vcell_Calc(
                    Output_Dict["E"],
                    Output_Dict["Nernst Gain"],
                    Output_Dict["Ohmic Loss"],
                    Input_Dict["N0"])
                [Warning1, I_Warning] = opem.Functions.warning_check_1(
                    Output_Dict["FC Voltage"], I_Warning, i, Warning1)
                Warning2 = opem.Functions.warning_check_2(
                    Vcell=Output_Dict["FC Voltage"],
                    warning_flag=Warning2)
                Vstack_List.append(Output_Dict["FC Voltage"])
                Output_Dict["FC Efficiency"] = Efficiency_Calc(
                    Output_Dict["FC Voltage"], Input_Dict["u"], Input_Dict["N0"])
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
                x=str(I_List), y=[
                    str(Nernst_Gain_List), str(Ohmic_Loss_List)], color=[
                    'rgba(99,100,255,1)', 'rgb(128, 0, 255)'], x_label="I(A)", y_label="V(V)", chart_name=[
                    "Nernst Gain", "Ohmic Loss"], size="600px", file=HTMLFile)
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
                y=str(PO2_List),
                color='	rgb(0, 255, 128)',
                x_label="I(A)",
                y_label="PO2(atm)",
                chart_name="PO2",
                size="600px",
                file=HTMLFile)
            opem.Functions.HTML_Chart(
                x=str(I_List),
                y=str(PH2_List),
                color='	rgb(128, 0, 255)',
                x_label="I(A)",
                y_label="PH2(atm)",
                chart_name="PH2",
                size="600px",
                file=HTMLFile)
            opem.Functions.HTML_Chart(
                x=str(I_List),
                y=str(PH2O_List),
                color='	rgb(165, 185, 112)',
                x_label="I(A)",
                y_label="PH2O(atm)",
                chart_name="PH2O",
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
                "Nernst Gain": Nernst_Gain_List,
                "Ohmic Loss": Ohmic_Loss_List,
                "EFF": Efficiency_List,
                "PO2": PO2_List,
                "PH2": PH2_List,
                "PH2O": PH2O_List,
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
        print(
            "[Error] " +
            Simulation_Title +
            " Simulation Failed!(Check Your Inputs)")
