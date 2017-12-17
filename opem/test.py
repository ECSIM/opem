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
>>> Test_Vector_1={"T":343.15,"PH2":1,"PO2":1,"i":0,"A":50.6,"l":0.178,"lambda":23,"N":1,"R":0}
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
>>> Test_Vector_2={"T":343.15,"PH2":1,"PO2":1,"i":25.3,"A":50.6,"l":0.178,"lambda":23,"N":1,"R":0}
>>> Static_Analysis(Test_Vector_2,TestMode=True)
Analyzing . . .
Done!
Enernst : 1.19075
Eta Activation : 0.5205357898108074
Eta Concentration : 0.006487441729730628
Eta Ohmic : 0.48876763670032947
Loss : 1.0157908682408676
PEM Efficiency : 0.1121532895891874
Power : 4.426466033506049
VStack : 0.17495913175913236
Vcell : 0.17495913175913236
>>> Test_Vector_3={"T":343.15,"PH2":1,"PO2":1,"i":50.6,"A":50.6,"l":0.178,"lambda":23,"N":1,"R":0}
>>> Static_Analysis(Test_Vector_3,TestMode=True)
Analyzing . . .
Done!
Enernst : 1.19075
Eta Activation : 0.5664415066275723
Eta Concentration : 0.017577796618689752
Eta Ohmic : 1.1356047108209584
Loss : 1.7196240140672205
PEM Efficiency : -0.3390218038892439
Power : -26.761025111801363
VStack : -0.5288740140672206
Vcell : -0.5288740140672206
>>> Test_Vector_4={"T":343.15,"PH2":1,"PO2":1,"i":75.9,"A":50.6,"l":0.178,"lambda":23,"N":1,"R":0}
>>> Static_Analysis(Test_Vector_4,TestMode=True)
Analyzing . . .
[Error] Eta Concentration Calculation Faild
[Error] Simulation Faild!(Check Your Inputs)
>>> Test_Vector_R={"T":343.15,"PH2":1,"PO2":1,"i":25.3,"A":50.6,"l":0.178,"lambda":23,"N":1,"R":22}
>>> Static_Analysis(Test_Vector_R,TestMode=True)
Analyzing . . .
Done!
Enernst : 1.19075
Eta Activation : -0.5205357898108074
Eta Concentration : 0.006487441729730628
Eta Ohmic : 557.0887676367004
Loss : 556.5747192886193
PEM Efficiency : -356.01536492860214
Power : -14051.214423002071
VStack : -555.3839692886194
Vcell : -555.3839692886194
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