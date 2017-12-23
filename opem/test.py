# -*- coding: utf-8 -*-
'''
>>> import coverage
>>> from opem import *
>>> import random
>>> cov=coverage.Coverage()
>>> cov.start()
>>> isfloat("2")
True
>>> isfloat("2.02")
True
>>> isfloat('ss')
False
>>> T=343.15
>>> PH2=1
>>> PO2=1
>>> i=0
>>> A=50.6
>>> l=0.178
>>> lambda_param=23
>>> N=1
>>> Jn=0.003
>>> JMax=0.469
>>> Enernst_Calc(T,PH2,PO2)
1.19075
>>> CH2_Calc(PH2,T)
7.330294784824117e-07
>>> CO2_Calc(PO2,T)
8.402541445801334e-07
>>> Rho_Calc(i,A,T,lambda_param)
4.978789826264977
>>> Xi2_Calc(A,PH2,T)
0.0030373688787134006
>>> Eta_Conc_Calc(i,A,Jn,JMax)
0
>>> Eta_Ohmic_Calc(i,l,A,T,lambda_param)
0
>>> Eta_Act_Calc(T,PO2,PH2,i,A)
0
>>> T='20000000000'
>>> PH2='10000000'
>>> PO2='1000000000'
>>> i='160000000'
>>> A='30000000000'
>>> l='50000000000'
>>> lambda_param='50000000000'
>>> N='80000000000'
>>> Enernst_Calc(T,PH2,PO2)
[Error] Enernst Calculation Faild
>>> CH2_Calc(PH2,T)
[Error] CH2 Calculation Faild
>>> CO2_Calc(PO2,T)
[Error] CO2 Calculation Faild
>>> Rho_Calc(i,A,T,lambda_param)
[Error] Rho Calculation Faild
>>> Xi2_Calc(A,PH2,T)
[Error] CH2 Calculation Faild
[Error] Xi2 Calculation Faild
>>> Eta_Conc_Calc(i,A,Jn,JMax)
[Error] Eta Concentration Calculation Faild
>>> Eta_Ohmic_Calc(i,l,A,T,lambda_param)
[Error] Rho Calculation Faild
[Error] Eta Ohmic Calculation Faild
>>> Eta_Act_Calc(T,PO2,PH2,i,A)
[Error] CO2 Calculation Faild
[Error] CH2 Calculation Faild
[Error] Xi2 Calculation Faild
[Error] Eta Activation Calculation Faild
>>> i=0
>>> while(i<30):
...    Test_Vector={"T":333,"PH2":1,"PO2":0.2095,"i":i,"A":64,"l":0.178,"lambda":23,"N":32,"R":0.0003,"Jn":0.003,"JMax":0.469}
...    Static_Analysis(Test_Vector,TestMode=True)
...    i=i+0.1
>>> cov.stop()
>>> cov.save()

'''