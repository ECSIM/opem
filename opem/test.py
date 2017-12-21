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
>>> Test_Vector_1={"T":333,"PH2":1,"PO2":0.2095,"i":0,"A":64,"l":0.178,"lambda":23,"N":32,"R":0.0003}
>>> Static_Analysis(Test_Vector_1,TestMode=True)
Analyzing . . .
Done!
Enernst : 1.1881661561119832
Eta Activation : 0
Eta Concentration : 0
Eta Ohmic : 0
Loss : 0
PEM Efficiency : 0.7616449718666559
Power : 0.0
VStack : 38.02131699558346
Vcell : 1.1881661561119832
>>> Test_Vector_2={"T":333,"PH2":1,"PO2":0.2095,"i":5,"A":64,"l":0.178,"lambda":23,"N":32,"R":0.0003}
>>> Static_Analysis(Test_Vector_2,TestMode=True)
Analyzing . . .
Done!
Enernst : 1.1881661561119832
Eta Activation : 0.41693014676843
Eta Concentration : 0.002915439242692384
Eta Ohmic : 0.0799945457422374
Loss : 0.4998401317533598
PEM Efficiency : 0.4412346309991175
Power : 3.441630121793117
VStack : 22.026432779475947
Vcell : 0.6883260243586233
>>> Test_Vector_3={"T":333,"PH2":1,"PO2":0.2095,"i":10,"A":64,"l":0.178,"lambda":23,"N":32,"R":0.0003}
>>> Static_Analysis(Test_Vector_3,TestMode=True)
Analyzing . . .
Done!
Enernst : 1.1881661561119832
Eta Activation : 0.46147802291583717
Eta Concentration : 0.006483177905588141
Eta Ohmic : 0.16213453668729905
Loss : 0.6300957375087244
PEM Efficiency : 0.35773744782260175
Power : 5.580704186032587
VStack : 17.85825339530428
Vcell : 0.5580704186032588
>>> Test_Vector_4={"T":333,"PH2":1,"PO2":0.2095,"i":15,"A":64,"l":0.178,"lambda":23,"N":32,"R":0.0003}
>>> Static_Analysis(Test_Vector_4,TestMode=True)
Analyzing . . .
Done!
Enernst : 1.1881661561119832
Eta Activation : 0.4875368599488408
Eta Concentration : 0.011081828376633707
Eta Ohmic : 0.24665132658417524
Loss : 0.7452700149096497
PEM Efficiency : 0.2839077828220086
Power : 6.643442118035002
VStack : 14.17267651847467
Vcell : 0.44289614120233345
>>> Test_Vector_5={"T":333,"PH2":1,"PO2":0.2095,"i":20,"A":64,"l":0.178,"lambda":23,"N":32,"R":0.0003}
>>> Static_Analysis(Test_Vector_5,TestMode=True)
Analyzing . . .
Done!
Enernst : 1.1881661561119832
Eta Activation : 0.5060258990632442
Eta Concentration : 0.017560748135457147
Eta Ohmic : 0.33383619615521415
Loss : 0.8574228433539155
PEM Efficiency : 0.2120149440756844
Power : 6.6148662551613535
VStack : 10.583786008258166
Vcell : 0.3307433127580677
>>> Test_Vector_6={"T":333,"PH2":1,"PO2":0.2095,"i":25,"A":64,"l":0.178,"lambda":23,"N":32,"R":0.0003}
>>> Static_Analysis(Test_Vector_6,TestMode=True)
Analyzing . . .
Done!
Enernst : 1.1881661561119832
Eta Activation : 0.5203671119626572
Eta Concentration : 0.028625564311891123
Eta Ohmic : 0.42403348346231934
Loss : 0.9730261597368677
PEM Efficiency : 0.1379102540866125
Power : 5.378499909377887
VStack : 6.884479884003696
Vcell : 0.2151399963751155
>>> Test_Vector_7={"T":333,"PH2":1,"PO2":0.2095,"i":30,"A":64,"l":0.178,"lambda":23,"N":32,"R":0.0003}
>>> Static_Analysis(Test_Vector_7,TestMode=True)
Analyzing . . .
Done!
Enernst : 1.1881661561119832
Eta Activation : 0.532084736096248
Eta Concentration : 0.12059035407306083
Eta Ohmic : 0.5176378690828786
Loss : 1.1703129592521873
PEM Efficiency : 0.011444356961407639
Power : 0.5355959057938775
VStack : 0.5713022995134693
Vcell : 0.017853196859795917
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