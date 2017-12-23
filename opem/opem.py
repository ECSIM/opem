# -*- coding: utf-8 -*-
import math
from .params import *
import os
import datetime

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
    :return: Eta Concentration
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
    :return: Eta Ohmic
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
    :return:  Eta Activation
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
        return Output
    except Exception:
        print("Bad Input")
        return False

def Output_Save(OutputDict,InputDict):
    '''
    This function write analysis result in Simulation-Result.opem file
    :param OutputDict: Analysis Result Dictionary
    :return: None
    '''
    file=open("Simulation-Result.opem","w")
    file.write("Simulation Date : "+str(datetime.datetime.now())+"\n")
    file.write("**********\n")
    Input_Keys=list(InputDict.keys())
    Output_Keys=list(OutputDict.keys())
    Input_Keys.sort()
    Output_Keys.sort()
    file.write("Simulation Inputs : \n\n")
    for key in Input_Keys:
        file.write(key + " : " + str(InputDict[key]) + "\n")
    file.write("**********\n")
    file.write("Simulation Outputs : \n\n")
    for key in Output_Keys:
        file.write(key+" : "+str(OutputDict[key])+"\n")
        print(key+" : "+str(OutputDict[key]))
    file.close()


def Static_Analysis(InputMethod=Get_Input,TestMode=False):
    '''
    This function run static analysis with calling other functions
    :return: None
    '''
    try:
        if TestMode==False:
            Input_Dict=InputMethod()
        else:
            Input_Dict=InputMethod
        print("Analyzing . . .")
        Enernst=Enernst_Calc(Input_Dict["T"],Input_Dict["PH2"],Input_Dict["PO2"])
        Eta_Act=Eta_Act_Calc(Input_Dict["T"],Input_Dict["PO2"],Input_Dict["PH2"],Input_Dict["i"],Input_Dict["A"])
        Eta_Ohmic=Eta_Ohmic_Calc(Input_Dict["i"],Input_Dict["l"],Input_Dict["A"],Input_Dict["T"],Input_Dict["lambda"],R_elec=Input_Dict["R"])
        Eta_Conc=Eta_Conc_Calc(Input_Dict["i"],Input_Dict["A"],Input_Dict["B"],Input_Dict["JMax"])
        Loss=Eta_Act+Eta_Ohmic+Eta_Conc
        Vcell=Enernst-Loss
        Efficiency=Efficiency_Calc(Vcell)
        Power=Vcell*Input_Dict["i"]
        VStack=VStack_Calc(Input_Dict["N"],Enernst,Loss)
        Output_Dict={"Enernst":Enernst,"Eta Activation":Eta_Act,"Eta Ohmic":Eta_Ohmic,"Eta Concentration":Eta_Conc,"Loss":Loss,
                    "Vcell":Vcell,"PEM Efficiency":Efficiency,"Power":Power,"VStack":VStack}
        print("Done!")
        Output_Save(Output_Dict, Input_Dict)
        if TestMode==False:
            print("Result In Simulation-Result.opem -->"+os.getcwd())
    except Exception:
        print("[Error] Simulation Faild!(Check Your Inputs)")










