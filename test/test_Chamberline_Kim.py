# -*- coding: utf-8 -*-
'''
>>> import os
>>> from math import isclose
>>> from opem.Static.Chamberline_Kim import *
>>> import shutil
>>> E0=0.982
>>> b=0.0689
>>> R=0.328
>>> m=0.000125
>>> n=9.45
>>> i=1
>>> A=50.0
>>> ABS_TOL = 1e-12
>>> REL_TOL = 0
>>> assert isclose(Vcell_Calc(E0,b,R,m,n,i,A), 1.244827379954939, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> Vcell_Calc(None,b,R,m,n,i,A)
[Error] Vcell Calculation Error (E0:None, b:0.0689, R:0.328, m:0.000125, n:9.45, i:1, A:50.0)
>>> Chamberline_Data=Static_Analysis(InputMethod={}, TestMode=True,PrintMode=False)
>>> Chamberline_Data["Status"]
False
>>> Test_Vector={"A":50.0,"E0":0.982,"b":0.0689,"R":0.328,"m":0.000125,"n":9.45,"N":1,"i-start":1,"i-stop":4,"i-step":0.1,"Name":"test1"}
>>> Chamberline_Kim_Data=Static_Analysis(InputMethod=Test_Vector, TestMode=True)
###########
Chamberline-Kim-Model Simulation
###########
Analyzing . . .
I : 1
PEM Efficiency : 0.797966269201884
Power : 1.244827379954939 W
Power-Stack : 1.244827379954939 W
Power-Thermal : -0.01482737995493899 W
VStack : 1.244827379954939 V
Vcell : 1.244827379954939 V
###########
I : 1.1
PEM Efficiency : 0.7933343765568479
Power : 1.3613617901715511 W
Power-Stack : 1.3613617901715511 W
Power-Thermal : -0.008361790171551031 W
VStack : 1.2376016274286827 V
Vcell : 1.2376016274286827 V
###########
I : 1.2
PEM Efficiency : 0.7890689791314186
Power : 1.4771371289340156 W
Power-Stack : 1.4771371289340156 W
Power-Thermal : -0.0011371289340155854 W
VStack : 1.230947607445013 V
Vcell : 1.230947607445013 V
###########
I : 1.3
PEM Efficiency : 0.7851113286904084
Power : 1.5922057745841485 W
Power-Stack : 1.5922057745841485 W
Power-Thermal : 0.006794225415851485 W
VStack : 1.2247736727570373 V
Vcell : 1.2247736727570373 V
###########
I : 1.4
PEM Efficiency : 0.7814157591393215
Power : 1.706612017960278 W
Power-Stack : 1.706612017960278 W
Power-Thermal : 0.015387982039721892 W
VStack : 1.2190085842573415 V
Vcell : 1.2190085842573415 V
###########
I : 1.5
PEM Efficiency : 0.7779460692405816
Power : 1.820393802022961 W
Power-Stack : 1.820393802022961 W
Power-Thermal : 0.02460619797703889 W
VStack : 1.2135958680153074 V
Vcell : 1.2135958680153074 V
###########
I : 1.6
PEM Efficiency : 0.7746730751436158
Power : 1.933583995558465 W
Power-Stack : 1.933583995558465 W
Power-Thermal : 0.03441600444153501 W
VStack : 1.2084899972240406 V
Vcell : 1.2084899972240406 V
###########
I : 1.7
PEM Efficiency : 0.771572906202878
Power : 2.0462113472500323 W
Power-Stack : 2.0462113472500323 W
Power-Thermal : 0.04478865274996757 W
VStack : 1.2036537336764896 V
Vcell : 1.2036537336764896 V
###########
I : 1.8
PEM Efficiency : 0.7686257886450131
Power : 2.158301214515197 W
Power-Stack : 2.158301214515197 W
Power-Thermal : 0.055698785484803184 W
VStack : 1.1990562302862204 V
Vcell : 1.1990562302862204 V
###########
I : 1.9
PEM Efficiency : 0.7658151585364871
Power : 2.2698761299021477 W
Power-Stack : 2.2698761299021477 W
Power-Thermal : 0.06712387009785219 W
VStack : 1.1946716473169199 V
Vcell : 1.1946716473169199 V
###########
I : 2.0
PEM Efficiency : 0.7631270025420254
Power : 2.380956247931119 W
Power-Stack : 2.380956247931119 W
Power-Thermal : 0.07904375206888092 W
VStack : 1.1904781239655595 V
Vcell : 1.1904781239655595 V
###########
I : 2.1
PEM Efficiency : 0.7605493596935309
Power : 2.491559702356007 W
Power-Stack : 2.491559702356007 W
Power-Thermal : 0.09144029764399271 W
VStack : 1.1864570011219082 V
Vcell : 1.1864570011219082 V
###########
I : 2.2
PEM Efficiency : 0.7580719391696471
Power : 2.601702895230229 W
Power-Stack : 2.601702895230229 W
Power-Thermal : 0.10429710476977118 W
VStack : 1.1825922251046495 V
Vcell : 1.1825922251046495 V
###########
I : 2.3
PEM Efficiency : 0.7556858231082223
Power : 2.7114007333123014 W
Power-Stack : 2.7114007333123014 W
Power-Thermal : 0.11759926668769842 W
VStack : 1.1788698840488268 V
Vcell : 1.1788698840488268 V
###########
I : 2.4
PEM Efficiency : 0.753383232714607
Power : 2.820666823283489 W
Power-Stack : 2.820666823283489 W
Power-Thermal : 0.13133317671651062 W
VStack : 1.1752778430347872 V
Vcell : 1.1752778430347872 V
###########
I : 2.5
PEM Efficiency : 0.7511573421474446
Power : 2.929513634375034 W
Power-Stack : 2.929513634375034 W
Power-Thermal : 0.14548636562496609 W
VStack : 1.1718054537500135 V
Vcell : 1.1718054537500135 V
###########
I : 2.6
PEM Efficiency : 0.7490021289286691
Power : 3.0379526349346824 W
Power-Stack : 3.0379526349346824 W
Power-Thermal : 0.16004736506531766 W
VStack : 1.168443321128724 V
Vcell : 1.168443321128724 V
###########
I : 2.7
PEM Efficiency : 0.7469122526002784
Power : 3.145994407952373 W
Power-Stack : 3.145994407952373 W
Power-Thermal : 0.17500559204762714 W
VStack : 1.1651831140564344 V
Vcell : 1.1651831140564344 V
###########
I : 2.8
PEM Efficiency : 0.7448829554595718
Power : 3.2536487494474096 W
Power-Stack : 3.2536487494474096 W
Power-Thermal : 0.1903512505525901 W
VStack : 1.162017410516932 V
Vcell : 1.162017410516932 V
###########
I : 2.9
PEM Efficiency : 0.7429099807210011
Power : 3.360924752781809 W
Power-Stack : 3.360924752781809 W
Power-Thermal : 0.20607524721819082 W
VStack : 1.1589395699247618 V
Vcell : 1.1589395699247618 V
###########
I : 3.0
PEM Efficiency : 0.7409895045575802
Power : 3.4678308813294754 W
Power-Stack : 3.4678308813294754 W
Power-Thermal : 0.22216911867052458 W
VStack : 1.1559436271098251 V
Vcell : 1.1559436271098251 V
###########
I : 3.1
PEM Efficiency : 0.7391180792895339
Power : 3.5743750314441862 W
Power-Stack : 3.5743750314441862 W
Power-Thermal : 0.23862496855581392 W
VStack : 1.153024203691673 V
Vcell : 1.153024203691673 V
###########
I : 3.2
PEM Efficiency : 0.7372925855955158
Power : 3.6805645872928157 W
Power-Stack : 3.6805645872928157 W
Power-Thermal : 0.2554354127071847 W
VStack : 1.1501764335290048 V
Vcell : 1.1501764335290048 V
###########
I : 3.3
PEM Efficiency : 0.7355101920796727
Power : 3.786406468826155 W
Power-Stack : 3.786406468826155 W
Power-Thermal : 0.2725935311738447 W
VStack : 1.1473958996442895 V
Vcell : 1.1473958996442895 V
###########
I : 3.4
PEM Efficiency : 0.7337683208763324
Power : 3.891907173928067 W
Power-Stack : 3.891907173928067 W
Power-Thermal : 0.29009282607193304 W
VStack : 1.1446785805670785 V
Vcell : 1.1446785805670785 V
###########
I : 3.5
PEM Efficiency : 0.7320646182417239
Power : 3.9970728155998123 W
Power-Stack : 3.9970728155998123 W
Power-Thermal : 0.30792718440018774 W
VStack : 1.1420208044570892 V
Vcell : 1.1420208044570892 V
###########
I : 3.6
PEM Efficiency : 0.7303969292894269
Power : 4.101909154889422 W
Power-Stack : 4.101909154889422 W
Power-Thermal : 0.3260908451105779 W
VStack : 1.1394192096915061 V
Vcell : 1.1394192096915061 V
###########
I : 3.7
PEM Efficiency : 0.7287632761880597
Power : 4.206421630157481 W
Power-Stack : 4.206421630157481 W
Power-Thermal : 0.3445783698425195 W
VStack : 1.136870710853373 V
Vcell : 1.136870710853373 V
###########
I : 3.8
PEM Efficiency : 0.7271618392669932
Power : 4.310615383174736 W
Power-Stack : 4.310615383174736 W
Power-Thermal : 0.36338461682526346 W
VStack : 1.1343724692565096 V
Vcell : 1.1343724692565096 V
###########
I : 3.9
PEM Efficiency : 0.7255909405767029
Power : 4.414495282468661 W
Power-Stack : 4.414495282468661 W
Power-Thermal : 0.38250471753133874 W
VStack : 1.1319218672996567 V
Vcell : 1.1319218672996567 V
###########
Report is generating ...
Done!
>>> assert isclose(Chamberline_Kim_Data["P"][5], 1.820393802022961, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> Chamberline_Kim_Data["Status"]
True
>>> assert isclose(Chamberline_Kim_Data["I"][5], 1.5, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(Chamberline_Kim_Data["V"][5], 1.2135958680153074, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(Chamberline_Kim_Data["EFF"][5], 0.7779460692405816, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(Chamberline_Kim_Data["Ph"][5], 0.02460619797703889, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(Chamberline_Kim_Data["V0"], 1.2696835857181188, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(Chamberline_Kim_Data["K"], -0.0372516118425709, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(Chamberline_Kim_Data["VE"][5], 1.2138061679542624, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> Test_Vector={"A":50.0,"E0":-5,"b":0.0689,"R":0.328,"m":0.000125,"n":9.45,"N":1,"i-start":5,"i-stop":1,"i-step":-1,"Name":"test1"}
>>> Chamberline_Kim_Data=Static_Analysis(InputMethod=Test_Vector, TestMode=True)
###########
Chamberline-Kim-Model Simulation
###########
Analyzing . . .
I : 1
PEM Efficiency : -3.036649115413501
Power : -4.737172620045062 W
Power-Stack : -4.737172620045062 W
Power-Thermal : 5.967172620045062 W
VStack : -4.737172620045062 V
Vcell : -4.737172620045062 V
###########
I : 2
PEM Efficiency : -3.0714883820733587
Power : -9.58304375206888 W
Power-Stack : -9.58304375206888 W
Power-Thermal : 12.04304375206888 W
VStack : -4.79152187603444 V
Vcell : -4.79152187603444 V
###########
I : 3
PEM Efficiency : -3.0936258800578047
Power : -14.478169118670525 W
Power-Stack : -14.478169118670525 W
Power-Thermal : 18.168169118670527 W
VStack : -4.826056372890175 V
Vcell : -4.826056372890175 V
###########
I : 4
PEM Efficiency : -3.110566355084641
Power : -19.40993405572816 W
Power-Stack : -19.40993405572816 W
Power-Thermal : 24.32993405572816 W
VStack : -4.85248351393204 V
Vcell : -4.85248351393204 V
###########
Report is generating ...
Warning : The value of I(>1) leads to minus amount of V, please check your inputs
Done!
>>> sorted(os.listdir("Chamberline-Kim")) == ['test1.csv', 'test1.html', 'test1.opem']
True
>>> Test_Vector={"A":50.0,"E0":-5,"b":0.0689,"R":0.328,"m":0.000125,"n":9.45,"N":1,"i-start":5,"i-stop":1,"i-step":-1,"Name":"test2"}
>>> Chamberline_Kim_Data=Static_Analysis(InputMethod=Test_Vector, TestMode=True, PrintMode=False, Folder=os.path.join(os.getcwd(), "Folder_Test"))
>>> sorted(os.listdir(os.path.join("Folder_Test", "Chamberline-Kim"))) == ['test2.csv', 'test2.html', 'test2.opem']
True
>>> shutil.rmtree("Chamberline-Kim")
>>> shutil.rmtree("Folder_Test")

'''
