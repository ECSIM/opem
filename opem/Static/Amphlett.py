# -*- coding: utf-8 -*-
import math
from opem.Params import Amphlett_InputParams as InputParams
from opem.Params import Amphlett_OutputParams as OutputParams
from opem.Params import Amphlett_Params_Default as Defaults
from opem.Params import xi1,xi3,xi4,HHV,uF,Amphlett_Description
from opem.Functions import *
import os



def Enernst_Calc(T, PH2, PO2):
    """
    This function calculate Enernst
    :param T: Cell Operation Temperature [K]
    :type T : float
    :param PH2: Partial Pressure [atm]
    :type PH2 : float
    :param PO2: partial Pressure [atm]
    :type PO2: float
    :return: Enernst [V} as float
    """
    try:
        result = 1.229 - (8.5 * (10 ** -4)) * (T - 298.15) + (4.308 * (10 ** -5)) * T * (
            math.log(PH2) + 0.5 * math.log(PO2))
        return result
    except Exception:
        print("[Error] Enernst Calculation Failed (T:%s , PH2:%s, PO2:%s)"%(str(T),str(PH2),str(PO2)))


def CH2_Calc(PH2, T):
    """
    This function calculate CH2
    :param PH2: Partial Pressure [atm]
    :type PH2 : float
    :param T: Cell Operation Temperature [K]
    :type T:float
    :return: CH2 [mol/cm^3] as float
    """
    try:
        result = PH2 / (1.09 * (10 ** 6) * math.exp(77 / T))
        return result
    except Exception:
        print("[Error] CH2 Calculation Failed (PH2:%s, T:%s)"%(str(PH2),str(T)))


def CO2_Calc(PO2, T):
    """
    This function calculate CO2
    :param PO2: Partial Pressure [atm]
    :type PO2 : float
    :param T: Cell Operation Temperature [K]
    :type T : float
    :return: CO2 [mol/cm^3] as float
    """
    try:
        result = PO2 / (5.08 * (10 ** 6) * math.exp(-498 / T))
        return result
    except Exception:
        print("[Error] CO2 Calculation Failed (PO2:%s, T:%s)"%(str(PO2),str(T)))


def Rho_Calc(i, A, T, lambda_param):
    """
    This function calculate Rho
    :param i: Cell load current [A]
    :type i : float
    :param A: active area [cm^2]
    :type A:float
    :param T: Cell Operation Temperature [K]
    :type T:float
    :param lambda_param: is an adjustable parameter with a possible maximum value of 23
    :type lambda_param : float
    :return: Rho -- > Membrane Specific Resistivity [ohm.cm] as float
    """
    try:
        result = (181.6 * (1 + 0.03 * (i / A) + 0.062 * ((T / 303) ** 2) * ((i / A) ** 2.5))) / (
            (lambda_param - 0.634 - 3 * (i / A)) * math.exp(4.18 * ((T - 303) / T)))
        return result
    except Exception:
        print("[Error] Rho Calculation Failed (i:%s, A:%s, T:%s, lambda:%s)"%(str(i),str(A),str(T),str(lambda_param)))


def Xi2_Calc(A, PH2, T):
    """
    This function calculate Xi2
    :param A: active area [cm^2]
    :type A : float
    :param PH2: Partial Pressure [atm]
    :type PH2:float
    :param T: Cell Operation Temperature [K]
    :type T:float
    :return: Xi2 as float
    """
    try:
        CH2 = CH2_Calc(PH2, T)
        result = 0.00286 + 0.0002 * math.log(A) + (4.3 * (10 ** -5)) * math.log(CH2)
        return result
    except Exception:
        print("[Error] Xi2 Calculation Failed (A:%s, PH2:%s, T:%s)"%(str(A),str(PH2),str(T)))


def Eta_Conc_Calc(i, A, B, JMax):
    """
    This function calculate Eta Concentration
    :param i: Cell load current [A]
    :type i :float
    :param A: active area [cm^2]
    :type A : float
    :return: Eta Concentration [V] as float
    """
    try:
        if i != 0:
            J = (i / A)
            result = -B * math.log(1 - (J / JMax))
            return result
        else:
            return 0
    except Exception:
        print("[Error] Eta Concentration Calculation Failed (i:%s, A:%s, B:%s, JMax:%s)"%(str(i),str(A),
                                                                                          str(B),str(JMax)))


def Eta_Ohmic_Calc(i, l, A, T, lambda_param, R_elec=None):
    """
    This function calculate Eta Ohmic
    :param R_elec: R-Electronic [ohm]
    :type R_elec:float
    :param i: cell load current [A]
    :type i:float
    :param l: Membrane Thickness [cm]
    :type l:float
    :param A: active area [cm^2]
    :type A:float
    :param T: Cell Operation Temperature [K]
    :type T:float
    :param lambda_param: is an adjustable parameter with a possible maximum value of 23
    :type lambda_param:float
    :return: Eta Ohmic [V] as float
    """
    try:
        if i != 0:
            Rho = Rho_Calc(i, A, T, lambda_param)
            R_prot = (Rho * l) / A
            R_total = R_prot
            if isfloat(R_elec):
                R_total += R_elec
            result = i * R_total
            return result
        else:
            return 0
    except Exception:
        print("[Error] Eta Ohmic Calculation Failed (i:%s, l:%s, A:%s, T:%s, lambda:%s, R_elec:%s)"%(str(i),str(l),
                                                                                                     str(A),str(T),
                                                                                                     str(lambda_param),
                                                                                                     str(R_elec)))


def Eta_Act_Calc(T, PO2, PH2, i, A):
    """
    This function calculate Eta Activation
    :param T: Cell Operation Temperature [K]
    :type T:float
    :param PO2: Partial Pressure [atm]
    :type PO2:float
    :param i: cell load current [A]
    :type i:float
    :return:  Eta Activation [V] as float
    """
    try:
        if i != 0:
            CO2 = CO2_Calc(PO2, T)
            xi2 = Xi2_Calc(A, PH2, T)
            result = -(xi1 + xi2 * T + xi3 * T * math.log(CO2) + xi4 * T * math.log(i))
            return result
        else:
            return 0
    except Exception:
        print("[Error] Eta Activation Calculation Failed (T:%s, PO2:%s, PH2:%s, i:%s, A:%s)"%(str(T),str(PO2),str(PH2),
                                                                                              str(i),str(A)))


def Efficiency_Calc(Vcell):
    """
    This function calculate PEM Cell Efficiency
    :param Vcell: Cell Voltage [V]
    :type Vcell:float
    :return: Efficiency as float
    """
    try:
        result = (uF * Vcell) / HHV
        return result
    except Exception:
        print("[Error] PEM Efficiency Calculation Failed (Vcell:%s)"%str(Vcell))


def VStack_Calc(N, Vcell):
    """
    This function calculate VStack
    :param N: number of single cells
    :type N  :int
    :param Vcell: Cell Voltage [V}
    :type Vcell:float
    :return: VStack [V] as float
    """
    try:
        result = N * (Vcell)
        return result
    except Exception:
        print("[Error] VStack Calculation Error (N:%s, Vcell:%s)"%(str(N),str(Vcell)))

def Loss_Calc(Eta_Act, Eta_Ohmic, Eta_Conc):
    """
    This function calculate loss
    :param Eta_Act: Eta Activation [V]
    :type Eta_Act : float
    :param Eta_Ohmic: Eta Ohmic [V]
    :type Eta_Ohmic : float
    :param Eta_Conc: Eta Concentration [V]
    :type Eta_Conc : float
    :return: Loss [V] as float
    """
    try:
        result = Eta_Act + Eta_Ohmic + Eta_Conc
        return result
    except Exception:
        print("[Error] Loss Calculation Error (Eta_Act:%s, Eta_Ohmic:%s, Eta_Conc:%s)"%(str(Eta_Act),str(Eta_Ohmic),
                                                                                        str(Eta_Conc)))


def Vcell_Calc(Enernst, Loss):
    """
    This function calculate cell voltage
    :param Enernst:  Enernst [V}
    :type Enernst : float
    :param Loss:  Loss [V]
    :type Loss : float
    :return:  Cell voltage [V] as float
    """
    try:
        result = Enernst - Loss
        return result
    except Exception:
        print("[Error] Vcell Calculation Error (Enernst:%s, Loss:%s)"%(str(Enernst),str(Loss)))


def Power_Calc(Vcell, i):
    """
    This function calculate power
    :param Vcell: Vell Voltage [V]
    :type Vcell : float
    :param i: cell load current [A]
    :type i : float
    :return: Cell power [W] as float
    """
    try:
        result = Vcell * i
        return result
    except Exception:
        print("[Error] Power Calculation Error (Vcell:%s, i:%s)"%(str(Vcell),str(i)))


def PowerStack_Calc(Power,N):
    '''
    This function calculate power_stack
    :param Power: Single Cell power [W]
    :type Power : float
    :param N: number of single cells
    :type N : int
    :return: Power Stack [W] as float
    '''
    try:
        result=N*Power
        return result
    except Exception:
        print("[Error] Power Stack Calculation Error (Power:%s, N:%s)"%(str(Power),str(N)))


def Static_Analysis(InputMethod=Get_Input, TestMode=False, PrintMode=True, ReportMode=True):
    """
    This function run Amphlett static analysis with calling other functions
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
    Warning1=False
    Warning2=False
    I_Warning=0
    try:
        Simulation_Title="Amphlett"
        if PrintMode==True:
            print("###########")
            print(Simulation_Title+"-Model Simulation")
            print("###########")
        OutputParamsKeys = list(OutputParams.keys())
        OutputParamsKeys.sort()
        Output_Dict = dict(zip(OutputParamsKeys, [None] * len(OutputParamsKeys)))
        if not TestMode:
            Input_Dict = InputMethod(InputParams,params_default=Defaults)
        else:
            Input_Dict = InputMethod
            Input_Dict = filter_default(input_dict=Input_Dict,params_default=Defaults)
        Input_Dict=filter_lambda(Input_Dict)
        if PrintMode==True:
            print("Analyzing . . .")
        Name = Input_Dict["Name"]
        if ReportMode==True:
            OutputFile = Output_Init(Input_Dict,Simulation_Title,Name)
            CSVFile = CSV_Init(OutputParamsKeys,OutputParams,Simulation_Title,Name)
            HTMLFile=HTML_Init(Simulation_Title,Name)
        IEndMax = Input_Dict["JMax"] * Input_Dict["A"]
        IEnd = min(IEndMax, Input_Dict["i-stop"])
        IStep = Input_Dict["i-step"]
        Precision = get_precision(IStep)
        Output_Dict["Enernst"] = Enernst_Calc(Input_Dict["T"], Input_Dict["PH2"], Input_Dict["PO2"])
        i = Input_Dict["i-start"]
        I_List=[]
        Power_List=[]
        Vstack_List=[]
        while i < IEnd:
            try:
                I_List.append(i)
                Output_Dict["Eta Activation"] = Eta_Act_Calc(Input_Dict["T"], Input_Dict["PO2"], Input_Dict["PH2"], i,
                                                             Input_Dict["A"])
                Output_Dict["Eta Ohmic"] = Eta_Ohmic_Calc(i, Input_Dict["l"], Input_Dict["A"], Input_Dict["T"],
                                                          Input_Dict["lambda"], R_elec=Input_Dict["R"])
                Output_Dict["Eta Concentration"] = Eta_Conc_Calc(i, Input_Dict["A"], Input_Dict["B"],
                                                                 Input_Dict["JMax"])
                Output_Dict["Loss"] = Loss_Calc(Output_Dict["Eta Activation"], Output_Dict["Eta Ohmic"],
                                                Output_Dict["Eta Concentration"])
                Output_Dict["Vcell"] = Vcell_Calc(Output_Dict["Enernst"], Output_Dict["Loss"])
                [Warning1,I_Warning] = warning_check_1(Output_Dict["Vcell"],I_Warning,i,Warning1)
                Warning2 = warning_check_2(Vcell=Output_Dict["Vcell"], warning_flag=Warning2)
                Output_Dict["PEM Efficiency"] = Efficiency_Calc(Output_Dict["Vcell"])
                Output_Dict["Power"] = Power_Calc(Output_Dict["Vcell"], i)
                Output_Dict["VStack"] = VStack_Calc(Input_Dict["N"], Output_Dict["Vcell"])
                Vstack_List.append(Output_Dict["VStack"])
                Output_Dict["Power-Stack"]=PowerStack_Calc(Output_Dict["Power"],Input_Dict["N"])
                Power_List.append(Output_Dict["Power-Stack"])
                if ReportMode==True:
                    Output_Save(OutputParamsKeys, Output_Dict,OutputParams, i, OutputFile,PrintMode)
                    CSV_Save(OutputParamsKeys, Output_Dict, i, CSVFile)
                i = rounder(i + IStep,Precision)
            except Exception as e:
                print(str(e))
                i = rounder(i + IStep,Precision)
                if ReporttMode==True:
                    Output_Save(OutputParamsKeys, Output_Dict, OutputParams, i, OutputFile,PrintMode)
                    CSV_Save(OutputParamsKeys, Output_Dict, i, CSVFile)
        if ReportMode==True:
            HTML_Desc(Simulation_Title, Amphlett_Description, HTMLFile)
            HTML_Input_Table(Input_Dict=Input_Dict, Input_Params=InputParams, file=HTMLFile)
            HTML_Chart(x=str(I_List), y=str(Power_List), color='rgba(255,99,132,1)', x_label="I(A)", y_label="P(W)",
                    chart_name="Power-Stack",size="600px",file=HTMLFile)
            HTML_Chart(x=str(I_List), y=str(Vstack_List), color='rgba(99,100,255,1)', x_label="I(A)", y_label="V(V)",
                    chart_name="Voltage-Stack",size="600px",file=HTMLFile)
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
            return {"P":Power_List,"I":I_List,"V":Vstack_List}
    except Exception as e:
        print("[Error] Amphlett Simulation Failed!(Check Your Inputs)")
