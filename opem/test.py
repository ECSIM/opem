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
>>> Eta_Conc_Calc(i,A)
0
>>> Eta_Ohmic_Calc(i,l,A,T,lambda_param)
0
>>> Eta_Act_Calc(T,PO2,PH2,i,A)
0
>>> Test_Vector_1={"T":343.15,"PH2":1,"PO2":1,"i":0,"A":50.6,"l":0.178,"lambda":23,"N":1}
>>> Static_Analysis(Test_Vector_1,TestMode=True)
Analyzing . . .
Done!
Enernst : 1.19075
Eta Activation : 0
Eta Concentration : 0
Eta Ohmic : 0
Loss : 0
PEM Efficiency : 0.763301282051282
Power : 0.0
VStack : 1.19075
Vcell : 1.19075
>>> Test_Vector_2={"T":343.15,"PH2":1,"PO2":1,"i":25.3,"A":50.6,"l":0.178,"lambda":23,"N":1}
>>> Static_Analysis(Test_Vector_2,TestMode=True)
Analyzing . . .
Done!
Enernst : 1.19075
Eta Activation : -0.5205357898108074
Eta Concentration : 0.0016379445009943273
Eta Ohmic : 0.48876763670032947
Loss : -0.030130208609483598
PEM Efficiency : 0.7826155183394127
Power : 30.888269277819937
VStack : 1.2208802086094837
Vcell : 1.2208802086094837
>>> Test_Vector_3={"T":343.15,"PH2":1,"PO2":1,"i":50.6,"A":50.6,"l":0.178,"lambda":23,"N":1}
>>> Static_Analysis(Test_Vector_3,TestMode=True)
Analyzing . . .
Done!
Enernst : 1.19075
Eta Activation : -0.5664415066275723
Eta Concentration : 0.08942873961125186
Eta Ohmic : 1.1356047108209584
Loss : 0.6585919438046379
PEM Efficiency : 0.34112695909959106
Power : 26.92719764348532
VStack : 0.532158056195362
Vcell : 0.532158056195362
>>> Test_Vector_4={"T":343.15,"PH2":1,"PO2":1,"i":75.9,"A":50.6,"l":0.178,"lambda":23,"N":1}
>>> Static_Analysis(Test_Vector_4,TestMode=True)
Analyzing . . .
Done!
Enernst : 1.19075
Eta Activation : -0.5932946295341045
Eta Concentration : 4.882643742570118
Eta Ohmic : 2.103719891323974
Loss : 6.393069004359988
PEM Efficiency : -3.3348198745897353
Power : -394.85601243092304
VStack : -5.202319004359987
Vcell : -5.202319004359987
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
>>> Eta_Conc_Calc(i,A)
[Error] Eta Concentration Calculation Faild
>>> Eta_Ohmic_Calc(i,l,A,T,lambda_param)
[Error] Rho Calculation Faild
[Error] Eta Ohmic Calculation Faild
>>> Eta_Act_Calc(T,PO2,PH2,i,A)
[Error] CO2 Calculation Faild
[Error] CH2 Calculation Faild
[Error] Xi2 Calculation Faild
[Error] Eta Activation Calculation Faild
>>> cov.stop()
>>> cov.save()

'''