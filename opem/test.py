# -*- coding: utf-8 -*-
'''
>>> from telecheck import *
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
>>> T=200
>>> PH2=1
>>> PO2=1
>>> i=1.5
>>> A=30
>>> l=5
>>> lambda_param=5
>>> N=8
>>> Enernst_Calc(T,PH2,PO2)
1.3124275
>>> CH2_Calc(PH2,T)
6.242666387198051e-07
>>> CO2_Calc(PO2,T)
2.374266952843449e-06
>>> Rho_Calc(i,A,T,lambda_param)
371.3457646696301
>>> Xi2_Calc(A,PH2,T)
0.002925911881401602
>>> Eta_Conc_Calc(i,A)
4.4754740929238115e-05
>>> Eta_Ohmic_Calc(i,l,A,T,lambda_param)
92.83644116740754
>>> Eta_Act_Calc(T,PO2,PH2,i,A)
-0.6113210685498855
>>> T=240
>>> PH2=3
>>> PO2=2
>>> i=3.3
>>> A=15
>>> l=2
>>> lambda_param=20
>>> N=20
>>> Enernst_Calc(T,PH2,PO2)
1.29336956583962
>>> CH2_Calc(PH2,T)
1.996910545709694e-06
>>> CO2_Calc(PO2,T)
3.1356482122184143e-06
>>> Rho_Calc(i,A,T,lambda_param)
29.30233863355657
>>> Xi2_Calc(A,PH2,T)
0.0028372819403690084
>>> Eta_Conc_Calc(i,A)
0.0001743731218320777
>>> Eta_Ohmic_Calc(i,l,A,T,lambda_param)
12.89302899876489
>>> Eta_Act_Calc(T,PO2,PH2,i,A)
-0.5895044084663448
>>> Test_Vector_1={"T":200,"PH2":1,"PO2":1,"i":1.5,"A":30,"l":5,"lambda":5,"N":8}
>>> Static_Analysis(Test_Vector_1,TestMode=True)
Analyzing . . .
Done!
Enernst : 1.3124275
Eta Activation : -0.6113210685498855
Eta Concentration : 4.4754740929238115e-05
Eta Ohmic : 92.83644116740754
Loss : 92.22516485359859
PEM Efficiency : -58.27739573948627
Power : -136.3691060303979
VStack : -727.3018988287887
Vcell : -90.91273735359859
>>> Test_Vector_2={"T":240,"PH2":3,"PO2":2,"i":3.3,"A":15,"l":2,"lambda":20,"N":20}
>>> Static_Analysis(Test_Vector_2,TestMode=True)
Analyzing . . .
Done!
Enernst : 1.29336956583962
Eta Activation : -0.5895044084663448
Eta Concentration : 0.0001743731218320777
Eta Ohmic : 12.89302899876489
Loss : 12.303698963420377
PEM Efficiency : -7.0579034599876636
Power : -36.3340870120165
VStack : -220.20658795161512
Vcell : -11.010329397580756
>>> cov.stop()
>>> cov.save()

'''