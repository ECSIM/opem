# -*- coding: utf-8 -*-
import math
from opem.Params import Padulles_InputParams as InputParams
from opem.Params import Padulles_Outparams as OutputParams
from opem.Params import R,F,uF,HHV,Padulles_Description
from opem.Static.Amphlett import Power_Calc
from opem.Functions import *
import os



def Enernst_Calc(E0,N0,T, PH2, PO2):
    """
    This function calculate Enernst
    :param E0: Opencell voltage [V]
    :type E0 : float
    :param N0: Number of fuel cells in the stack
    :type N0 : int
    :param T: Cell Operation Temperature [K]
    :type T : float
    :param PH2:  Partial Pressure [atm]
    :type PH2 : float
    :param PO2: Partial Pressure [atm]
    :type PO2 : float
    :return: Enernest [V] as float
    """
    try:
        result = N0*(E0+(R*T/(2*F))*math.log(PH2*((PO2)**0.5)))
        return result
    except Exception:
        print("[Error] Enernst Calculation Failed (E0:%s, N0:%s, T:%s, PH2:%s, PO2:%s)"%(str(E0),str(N0),str(T),
                                                                                         str(PH2),str(PO2)))


def PH2_Calc(KH2,tH2,Kr,I,qH2):
    """
    This function calculate PH2
    :param KH2: Hydrogen Valve Constant [kmol.s^(-1).atm^(-1)]
    :type KH2 : float
    :param tH2: Hydrogen time constant [s]
    :type tH2 : float
    :param Kr: Modeling constant [kmol.s^(-1).A^(-1)]
    :type Kr : float
    :param I: Cell load current [A]
    :type I : float
    :param qH2: Molar flow of hydrogen [kmol.s^(-1)]
    :type qH2 : float
    :return: PH2 [atm] as float
    """
    try:
        result = ((1/KH2)/(1+tH2))*(qH2-2*Kr*I)
        return result
    except Exception:
        print("[Error] PH2 Calculation Failed (KH2:%s, tH2:%s, Kr:%s, I:%s, qH2:%s)"%(str(KH2),str(tH2),str(Kr),
                                                                                      str(I),str(qH2)))


def PO2_Calc(KO2,tO2,Kr,I,qO2):
    """
    This function calculate PO2
    :param KO2: Oxygen Valve Constant [kmol.s^(-1).atm^(-1)]
    :type KO2 : float
    :param tO2: Oxygen time constant [s]
    :type tO2 : float
    :param Kr: Modeling constant [kmol.s^(-1).A^(-1)]
    :type Kr : float
    :param I: Cell load current [A]
    :type I : float
    :param qO2: Molar flow of oxygen [kmol.s^(-1)
    :type qO2 : float
    :return: PO2 [atm] as float
    """
    try:
        result = ((1/KO2)/(1+tO2))*(qO2-Kr*I)
        return result
    except Exception:
        print("[Error] PO2 Calculation Failed (KO2:%s, tO2:%s, Kr:%s, I:%s, qO2:%s)"%(str(KO2),str(tO2),str(Kr),
                                                                                      str(I),str(qO2)))


def Kr_Calc(N0):
    """
    This function calculate Kr
    :param N0: Number of fuel cells in the stack
    :type N0 : int
    :return: Kr [kmol.s^(-1).A^(-1)] as float
    """
    try:
        result = N0/(4*F)
        return result
    except Exception:
        print("[Error] Kr Calculation Failed (N0:%s)"%str(N0))




def Vcell_Calc(Enernst, B,C,I,Rint):
    """
    This function calculate Vcell
    :param Enernst: Enernst [V]
    :type Enernst : float
    :param B: Activation voltage constant [V]
    :type B: float
    :param C: Constant [A^(-1)
    :type C : float
    :param I: Cell load current [A]
    :type I: float
    :param Rint: Fuel cell internal resistance [ohm]
    :type Rint : float
    :return: Vcell [V] as float
    """
    try:
        result = Enernst-B*math.log(C*I)-Rint*I
        return result
    except Exception:
        print("[Error] Vcell Calculation Error (Enernst:%s, B:%s, C:%s, I:%s, Rint:%s)"%(str(Enernst),str(B),
                                                                                         str(C),str(I),str(Rint)))

def qO2_Calc(qH2,rho):
    """
    This function calculate qO2
    :param qH2: Molar flow of hydrogen [kmol.s^(-1)]
    :type qH2 : float
    :param rho: Hydrogen-Oxygen flow rate
    :type rho : float
    :return: qO2 [kmol.s^(-1)] as float
    """
    try:
        result = (qH2/rho)
        return result
    except Exception:
        print("[Error] qO2 Calculation Error (qH2:%s, rho:%s)"%(str(qH2),str(rho)))



def Efficiency_Calc(Vcell,N):
    """
    This function calculate PEM Cell Efficiency
    :param Vcell: Cell Voltage [V]
    :type Vcell:float
    :param N0: Number of fuel cells in the stack
    :type N0 : int
    :return: Efficiency as float
    """
    try:
        result = (uF * Vcell) / (N*HHV)
        return result
    except Exception:
        print("[Error] PEM Efficiency Calculation Failed (Vcell:%s, N:%s)"%(str(Vcell),str(N)))




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
        Simulation_Title="Padulles-I"
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
        qO2=qO2_Calc(Input_Dict["qH2"],Input_Dict["rho"])
        while i < IEnd:
            try:
                I_List.append(i)
                Output_Dict["PO2"]=PO2_Calc(Input_Dict["KO2"],Input_Dict["tO2"],Kr,i,qO2)
                Output_Dict["PH2"]=PH2_Calc(Input_Dict["KH2"],Input_Dict["tH2"],Kr,i,Input_Dict["qH2"])
                Output_Dict["E"]=Enernst_Calc(Input_Dict["E0"],Input_Dict["N0"],Input_Dict["T"],Output_Dict["PH2"],Output_Dict["PO2"])
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
            HTML_Desc(Simulation_Title, Padulles_Description, HTMLFile)
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
                print("Result In -->" + os.path.join(os.getcwd(), Simulation_Title))
        else:
            return {"P": Power_List, "I": I_List, "V": Vstack_List}
    except Exception:
        print("[Error] Dynamic Simulation Failed!(Check Your Inputs)")
