# -*- coding: utf-8 -*-
import math
from .Amphlett_Params import *
import os
import datetime
from art import text2art

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

def Enernst_Calc(T,PH2,PO2):
    '''
    This function calculate Enernst
    :param T: Cell Operation Temperature [K]
    :param PH2: Partial Pressure [atm]
    :param PO2: partial Pressure [atm]
    :return: Enernst [V}
    '''
    try:
        result=1.229-(8.5*(10**-4))*(T-298.15)+(4.308*(10**-5))*T*(math.log(PH2)+0.5*math.log(PO2))
        return result
    except Exception:
        print("[Error] Enernst Calculation Faild")

def CH2_Calc(PH2,T):
    '''
    This function calculate CH2
    :param PH2: Partial Pressure [atm]
    :param T: Cell Operation Temperature [K]
    :return: CH2 [mol/cm^3]
    '''
    try:
        result=PH2/(1.09*(10**6)*math.exp(77/T))
        return result
    except Exception:
        print("[Error] CH2 Calculation Faild")

def CO2_Calc(PO2,T):
    '''
    This function calculate CO2
    :param PO2: Partial Pressure [atm]
    :param T: Cell Operation Temperature [K]
    :return: CO2 [mol/cm^3]
    '''
    try:
        result=PO2/(5.08*(10**6)*math.exp(-498/T))
        return result
    except Exception:
        print("[Error] CO2 Calculation Faild")

def Rho_Calc(i,A,T,lambda_param):
    '''
    This function calculate Rho
    :param i: Cell load current [A]
    :param A: active area [cm^2]
    :param T: Cell Operation Temperature [K]
    :param lambda_param: is an adjustable parameter with a possible maximum value of 23
    :return: Rho -- > Membrane Specific Resistivity [ohm.cm]
    '''
    try:
        result=(181.6*(1+0.03*(i/A)+0.062*((T/303)**2)*((i/A)**2.5)))/((lambda_param-0.634-3*(i/A))*math.exp(4.18*((T-303)/T)))
        return result
    except Exception:
        print("[Error] Rho Calculation Faild")

def Xi2_Calc(A,PH2,T):
    '''
    This function calculate Xi2
    :param A: active area [cm^2]
    :param PH2: Partial Pressure [atm]
    :param T: Cell Operation Temperature [K]
    :return: Xi2
    '''
    try:
        CH2=CH2_Calc(PH2,T)
        result=0.00286+0.0002*math.log(A)+(4.3*(10**-5))*math.log(CH2)
        return result
    except Exception:
        print("[Error] Xi2 Calculation Faild")

def Eta_Conc_Calc(i,A,B,JMax):
    '''
    This function calculate Eta Concentration
    :param i: Cell load current [A]
    :param A: active area [cm^2]
    :return: Eta Concentration [V]
    '''
    try:
        if i!=0:
            J=(i/A)
            result=-B*math.log(1-(J/JMax))
            return result
        else:
            return 0
    except Exception:
        print("[Error] Eta Concentration Calculation Faild")

def Eta_Ohmic_Calc(i,l,A,T,lambda_param,R_elec=None):
    '''
    This function calculate Eta Ohmic
    :param i: cell load current [A]
    :param l: Membrane Thickness [cm]
    :param A: active area [cm^2]
    :param T: Cell Operation Temperature [K]
    :param lambda_param: is an adjustable parameter with a possible maximum value of 23
    :return: Eta Ohmic [V]
    '''
    try:
        if i!=0:
            Rho=Rho_Calc(i,A,T,lambda_param)
            R_prot=(Rho*l)/A
            R_total=R_prot
            if isfloat(R_elec)==True:
                R_total+=R_elec
            result=i*R_total
            return result
        else:
            return 0
    except Exception:
        print("[Error] Eta Ohmic Calculation Faild")

def Eta_Act_Calc(T,PO2,PH2,i,A):
    '''
    This function calculate Eta Activation
    :param T: Cell Operation Temperature [K]
    :param PO2: Partial Pressure [atm]
    :param i: cell load current [A]
    :return:  Eta Activation [V]
    '''
    try:
        if i!=0:
            CO2=CO2_Calc(PO2,T)
            xi2=Xi2_Calc(A,PH2,T)
            result=-(xi1+xi2*T+xi3*T*math.log(CO2)+xi4*T*math.log(i))
            return result
        else:
            return 0
    except Exception:
        print("[Error] Eta Activation Calculation Faild")

def Efficiency_Calc(Vcell):
    '''
    This function calculate PEM Cell Efficiency
    :param Vcell: Cell Voltage [V]
    :return: Efficiency
    '''
    try:
        result=(uF*Vcell)/HHV
        return result
    except Exception:
        print("[Error] PEM Efficiency Calculation Faild")

def VStack_Calc(N,Enernst,Loss):
    '''
    This function calculate VStack
    :param N: number of single cells
    :param Enernst: Enernst Voltage [V}
    :param Loss: Loss [V]
    :return: VStack [V]
    '''
    try:
        reuslt=N*(Enernst-Loss)
        return reuslt
    except Exception:
        print("[Error] VStack Calculation Error")

def Get_Input():
    '''
    This function get inputs from users
    :return: Input Dictionary
    '''
    try:
        Input_Keys=list(InputParams.keys())
        Input_Keys.sort()
        Input_Values=[]
        for item in Input_Keys:
            Input_Flag=False
            while(Input_Flag==False):
                Input_Item=input("Please Enter "+item+"("+InputParams[item]+") : ")
                if isfloat(Input_Item)==True:
                    Input_Flag=True
                else:
                    print("[Error] Bad Input Try Again")
            Input_Values.append(Input_Item)
        Input_Values=list(map(float,Input_Values))
        Output=dict(zip(Input_Keys,Input_Values))
        if Output["lambda"]>23:
            Output["lambda"]=23
            print("[Warning] Opem Automatically Set Lambda To Maximum Value (23) ")
        elif Output["lambda"]<14:
            Output["lambda"] = 23
            print("[Warning] Opem Automatically Set Lambda To Minimum Value (14) ")
        return Output
    except Exception:
        print("Bad Input")
        return False

def Output_Save(OutputParamsKeys,OutputDict,i,file):
    '''
    This function write analysis result in Simulation-Result.opem file
    :param OutputParamsKeys : Output Params as dict
    :param OutputDict: Analysis Result Dictionary
    :param i: cell load current [A]
    :param file : file object
    :return: None
    '''

    file.write("I :"+str(i)+" A \n\n")
    print("I : "+str(i))
    for key in OutputParamsKeys:
        file.write(key+" : "+str(OutputDict[key])+" "+OutputParams[key]+"\n")
        print(key+" : "+str(OutputDict[key])+" "+OutputParams[key])
    file.write("###########\n")
    print("###########")
def Output_Init(InputDict):
    '''
    This function initialize output file
    :param InputDict: Input Test Vector
    :type InputDict:dict
    :return: file object
    '''
    Art = text2art("Opem")
    file = open("Amphlett-Model-Result.opem", "w")
    file.write(Art)
    file.write("Simulation Date : " + str(datetime.datetime.now()) + "\n")
    file.write("**********\n")
    file.write("Amphlett Static Model\n\n")
    file.write("**********\n")
    file.write("Simulation Inputs : \n\n")
    Input_Keys = list(InputDict.keys())
    Input_Keys.sort()
    for key in Input_Keys:
        file.write(key + " : " + str(InputDict[key]) + "\n")
    file.write("**********\n")
    return file

def CSV_Init(OutputParamsKeys):
    '''
    This function initialize csv file
    :param OutputParamsKeys: Output Params as dict
    :return: file object
    '''
    file=open("Amphlett-Model-Result.csv","w")
    file.write("I (A),")
    for index,item in enumerate(OutputParamsKeys):
        file.write(item+" ("+OutputParams[item]+")")
        if index<len(OutputParamsKeys)-1:
            file.write(",")
    file.write("\n")
    return file

def CSV_Save(OutputParamsKeys,OutputDict,i,file):
    '''
    This Function Save Parameters In CSV File
    :param OutputParamsKeys: Output Params
    :param OutputDict: Output Values Dictionary
    :param i: cell load current [A]
    :param file: CSV_File object
    :return: None
    '''
    file.write(str(i)+",")
    for key in OutputParamsKeys:
        file.write(str(OutputDict[key]))
        if key!=OutputParamsKeys[-1]:
            file.write(",")
    file.write("\n")
def Loss_Calc(Eta_Act,Eta_Ohmic,Eta_Conc):
    '''
    This function calculate loss
    :param Eta_Act: Eta Activation [V]
    :param Eta_Ohmic: Eta Ohmic [V]
    :param Eta_Conc: Eta Concentration [V]
    :return: Loss [V]
    '''
    try:
        result=Eta_Act+Eta_Ohmic+Eta_Conc
        return result
    except Exception:
        print("[Error] Loss Calculation Error")
def Vcell_Calc(Enernst,Loss):
    '''
    This function calculate cell voltage
    :param Enernst:  Enernst [V}
    :param Loss:  Loss [V]
    :return:  Cell voltage [V]
    '''
    try:
        result=Enernst-Loss
        return result
    except Exception:
        print("[Error] Vcell Calculation Error")
def Power_Calc(Vcell,i):
    '''
    This function calculate power
    :param Vcell: Vell Voltage [V]
    :param i: cell load current [A]
    :return: Cell power [W]
    '''
    try:
        result=Vcell*i
        return result
    except Exception:
        print("[Error] Power Calculation Error")
def Static_Analysis(InputMethod=Get_Input,TestMode=False):
    '''
    This function run static analysis with calling other functions
    :return: None
    '''
    try:
        print("###########")
        print("Amphlett-Model Simulation")
        print("###########")
        OutputParamsKeys = list(OutputParams.keys())
        OutputParamsKeys.sort()
        Output_Dict = dict(zip(OutputParamsKeys, [None] * len(OutputParamsKeys)))
        if TestMode==False:
            Input_Dict=InputMethod()
        else:
            Input_Dict=InputMethod
        OutputFile=Output_Init(Input_Dict)
        CSVFile=CSV_Init(OutputParamsKeys)
        print("Analyzing . . .")
        IEndMax=Input_Dict["JMax"]*Input_Dict["A"]
        IEnd=min(IEndMax,Input_Dict["i-stop"])
        IStep=Input_Dict["i-step"]
        Output_Dict["Enernst"]=Enernst_Calc(Input_Dict["T"],Input_Dict["PH2"],Input_Dict["PO2"])
        i=Input_Dict["i-start"]
        while(i<IEnd):
            try:

                Output_Dict["Eta Activation"]=Eta_Act_Calc(Input_Dict["T"],Input_Dict["PO2"],Input_Dict["PH2"],i,Input_Dict["A"])
                Output_Dict["Eta Ohmic"]=Eta_Ohmic_Calc(i,Input_Dict["l"],Input_Dict["A"],Input_Dict["T"],Input_Dict["lambda"],R_elec=Input_Dict["R"])
                Output_Dict["Eta Concentration"]=Eta_Conc_Calc(i,Input_Dict["A"],Input_Dict["B"],Input_Dict["JMax"])
                Output_Dict["Loss"]=Loss_Calc(Output_Dict["Eta Activation"],Output_Dict["Eta Ohmic"],Output_Dict["Eta Concentration"])
                Output_Dict["Vcell"]=Vcell_Calc(Output_Dict["Enernst"],Output_Dict["Loss"])
                Output_Dict["PEM Efficiency"]=Efficiency_Calc(Output_Dict["Vcell"])
                Output_Dict["Power"]=Power_Calc(Output_Dict["Vcell"],i)
                Output_Dict["VStack"]=VStack_Calc(Input_Dict["N"],Output_Dict["Enernst"],Output_Dict["Loss"])

                Output_Save(OutputParamsKeys,Output_Dict, i, OutputFile)
                CSV_Save(OutputParamsKeys,Output_Dict,i,CSVFile)
                i=i+IStep
            except Exception:
                i = i + IStep
                OutputFile.write("[Simulation Error]\n")
                CSV_Save(OutputParamsKeys, Output_Dict, i, CSVFile)
        OutputFile.close()
        CSVFile.close()
        print("Done!")
        if TestMode==False:
            print("Result In Amphlett-Model-Result.opem -->"+os.getcwd())
            print("Output-Table In Amphlett-Model-Result.csv --> "+os.getcwd())
    except Exception:
        if OutputFile.closed==False:
            OutputFile.close()
        if CSVFile.closed==False:
            CSVFile.close()
        print("[Error] Amphlett Simulation Faild!(Check Your Inputs)")










