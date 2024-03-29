# -*- coding: utf-8 -*-
'''
>>> import os
>>> from math import isclose
>>> from opem.Dynamic.Padulles1 import *
>>> import shutil
>>> ABS_TOL = 1e-12
>>> REL_TOL = 0
>>> Test_Vector={"T":343,"E0":0.6,"N0":88,"KO2":0.0000211,"KH2":0.0000422,"tH2":3.37,"tO2":6.74,"B":0.04777,"C":0.0136,"Rint":0.00303,"rho":1.168,"qH2":0.0004,"i-start":0,"i-stop":4,"i-step":0.1,"Name":"test1"}
>>> Padulles_I_Data=Dynamic_Analysis(InputMethod=Test_Vector, TestMode=True)
###########
Padulles-I-Model Simulation
###########
Analyzing . . .
[Error] Vcell Calculation Error (Enernst:54.28850557413407, B:0.04777, C:0.0136, I:0, Rint:0.00303)
[Error] PEM Efficiency Calculation Failed (Vcell:None, N:88)
[Error] Power Calculation Error (Vcell:None, i:0)
I : 0
E : 54.28850557413407 V
FC Efficiency : None
FC Power : None W
FC Voltage : None V
PH2 : 2.169032719858579 atm
PO2 : 2.0969773162414582 atm
Power-Thermal : None W
###########
I : 0.1
E : 54.288313997298886 V
FC Efficiency : 0.3977513543332525
FC Power : 5.4603305922868905 W
FC Voltage : 54.6033059228689 V
PH2 : 2.168785433142166 atm
PO2 : 2.096837698289168 atm
Power-Thermal : 5.36366940771311 W
###########
I : 0.2
E : 54.28812240067271 V
FC Efficiency : 0.39750655365258875
FC Power : 10.913939937085477 W
FC Voltage : 54.56969968542738 V
PH2 : 2.1685381464257527 atm
PO2 : 2.096698080336878 atm
Power-Thermal : 10.734060062914523 W
###########
I : 0.3
E : 54.287930784251316 V
FC Efficiency : 0.39736185898012566
FC Power : 16.364950800237498 W
FC Voltage : 54.54983600079166 V
PH2 : 2.168290859709339 atm
PO2 : 2.096558462384588 atm
Power-Thermal : 16.1070491997625 W
###########
I : 0.4
E : 54.28773914803044 V
FC Efficiency : 0.3972581497084044
FC Power : 21.814239516787904 W
FC Voltage : 54.535598791969754 V
PH2 : 2.1680435729929264 atm
PO2 : 2.0964188444322978 atm
Power-Thermal : 21.4817604832121 W
###########
I : 0.5
E : 54.28754749200584 V
FC Efficiency : 0.3971768980805572
FC Power : 27.262222284249443 W
FC Voltage : 54.524444568498886 V
PH2 : 2.1677962862765128 atm
PO2 : 2.0962792264800076 atm
Power-Thermal : 26.857777715750554 W
###########
I : 0.6
E : 54.28735581617328 V
FC Efficiency : 0.3971098513395853
FC Power : 32.709144235138965 W
FC Voltage : 54.515240391898274 V
PH2 : 2.1675489995600996 atm
PO2 : 2.0961396085277175 atm
Power-Thermal : 32.23485576486103 W
###########
I : 0.7
E : 54.287164120528516 V
FC Efficiency : 0.3970526072135646
FC Power : 38.155167342794705 W
FC Voltage : 54.507381918278156 V
PH2 : 2.1673017128436864 atm
PO2 : 2.0959999905754274 atm
Power-Thermal : 37.61283265720528 W
###########
I : 0.8
E : 54.28697240506729 V
FC Efficiency : 0.39700253793845613
FC Power : 43.60040672655301 W
FC Voltage : 54.50050840819126 V
PH2 : 2.1670544261272733 atm
PO2 : 2.0958603726231373 atm
Power-Thermal : 42.991593273446995 W
###########
I : 0.9
E : 54.286780669785365 V
FC Efficiency : 0.39695794855256433
FC Power : 49.044948459566434 W
FC Voltage : 54.49438717729603 V
PH2 : 2.16680713941086 atm
PO2 : 2.0957207546708467 atm
Power-Thermal : 48.37105154043357 W
###########
I : 1.0
E : 54.28658891467849 V
FC Efficiency : 0.39691768174793257
FC Power : 54.48885935035618 W
FC Voltage : 54.48885935035618 V
PH2 : 2.166559852694447 atm
PO2 : 2.0955811367185566 atm
Power-Thermal : 53.751140649643816 W
###########
I : 1.1
E : 54.2863971397424 V
FC Efficiency : 0.39688091206389015
FC Power : 59.93219276894392 W
FC Voltage : 54.483811608130836 V
PH2 : 2.1663125659780333 atm
PO2 : 2.095441518766267 atm
Power-Thermal : 59.13180723105608 W
###########
I : 1.2
E : 54.286205344972856 V
FC Efficiency : 0.3968470300107991
FC Power : 65.37499233585899 W
FC Voltage : 54.4791602798825 V
PH2 : 2.16606527926162 atm
PO2 : 2.0953019008139764 atm
Power-Thermal : 64.51300766414099 W
###########
I : 1.3
E : 54.286013530365594 V
FC Efficiency : 0.3968155727355017
FC Power : 70.81729437266857 W
FC Voltage : 54.47484182512967 V
PH2 : 2.165817992545207 atm
PO2 : 2.0951622828616863 atm
Power-Thermal : 69.89470562733142 W
###########
I : 1.4
E : 54.28582169591637 V
FC Efficiency : 0.3967861804549145
FC Power : 76.25912959399092 W
FC Voltage : 54.470806852850664 V
PH2 : 2.165570705828794 atm
PO2 : 2.095022664909396 atm
Power-Thermal : 75.27687040600905 W
###########
I : 1.5
E : 54.28562984162091 V
FC Efficiency : 0.3967585679566162
FC Power : 81.7005243136264 W
FC Voltage : 54.46701620908427 V
PH2 : 2.1653234191123807 atm
PO2 : 2.094883046957106 atm
Power-Thermal : 80.65947568637358 W
###########
I : 1.6
E : 54.28543796747497 V
FC Efficiency : 0.39673250531602267
FC Power : 87.14150132765376 W
FC Voltage : 54.46343832978359 V
PH2 : 2.1650761323959675 atm
PO2 : 2.094743429004816 atm
Power-Thermal : 86.04249867234626 W
###########
I : 1.7
E : 54.28524607347429 V
FC Efficiency : 0.3967078044696878
FC Power : 92.58208057591786 W
FC Voltage : 54.46004739759874 V
PH2 : 2.164828845679554 atm
PO2 : 2.094603811052526 atm
Power-Thermal : 91.42591942408212 W
###########
I : 1.8
E : 54.285054159614596 V
FC Efficiency : 0.3966843096322109
FC Power : 98.02227964735785 W
FC Voltage : 54.456822026309915 V
PH2 : 2.164581558963141 atm
PO2 : 2.0944641931002357 atm
Power-Thermal : 96.80972035264215 W
###########
I : 1.9
E : 54.284862225891644 V
FC Efficiency : 0.3966618903075967
FC Power : 103.46211417271105 W
FC Voltage : 54.45374430142687 V
PH2 : 2.1643342722467276 atm
PO2 : 2.094324575147945 atm
Power-Thermal : 102.19388582728892 W
###########
I : 2.0
E : 54.28467027230115 V
FC Efficiency : 0.39664043609530514
FC Power : 108.90159813432699 W
FC Voltage : 54.450799067163494 V
PH2 : 2.1640869855303144 atm
PO2 : 2.0941849571956554 atm
Power-Thermal : 107.578401865673 W
###########
I : 2.1
E : 54.28447829883886 V
FC Efficiency : 0.3966198527648516
FC Power : 114.34074411387355 W
FC Voltage : 54.44797338755883 V
PH2 : 2.1638396988139013 atm
PO2 : 2.094045339243365 atm
Power-Thermal : 112.96325588612645 W
###########
I : 2.2
E : 54.2842863055005 V
FC Efficiency : 0.3966000592444172
FC Power : 119.77956349276191 W
FC Voltage : 54.44525613307359 V
PH2 : 2.1635924120974876 atm
PO2 : 2.0939057212910748 atm
Power-Thermal : 118.34843650723809 W
###########
I : 2.3
E : 54.284094292281814 V
FC Efficiency : 0.39658098527940633
FC Power : 125.21806661606087 W
FC Voltage : 54.4426376591569 V
PH2 : 2.163345125381075 atm
PO2 : 2.0937661033387847 atm
Power-Thermal : 123.7339333839391 W
###########
I : 2.4
E : 54.28390225917852 V
FC Efficiency : 0.3965625695896912
FC Power : 130.65626292785475 W
FC Voltage : 54.44010955327281 V
PH2 : 2.1630978386646613 atm
PO2 : 2.0936264853864945 atm
Power-Thermal : 129.11973707214523 W
###########
I : 2.5
E : 54.28371020618635 V
FC Efficiency : 0.3965447584032809
FC Power : 136.09416108400603 W
FC Voltage : 54.43766443360241 V
PH2 : 2.162850551948248 atm
PO2 : 2.0934868674342044 atm
Power-Thermal : 134.50583891599396 W
###########
I : 2.6
E : 54.28351813330103 V
FC Efficiency : 0.3965275042777518
FC Power : 141.5317690468494 W
FC Voltage : 54.435295787249764 V
PH2 : 2.162603265231835 atm
PO2 : 2.0933472494819143 atm
Power-Thermal : 139.8922309531506 W
###########
I : 2.7
E : 54.2833260405183 V
FC Efficiency : 0.39651076514422556
FC Power : 146.9690941652981 W
FC Voltage : 54.432997838999285 V
PH2 : 2.162355978515422 atm
PO2 : 2.093207631529624 atm
Power-Thermal : 145.27890583470193 W
###########
I : 2.8
E : 54.28313392783386 V
FC Efficiency : 0.3964945035252972
FC Power : 152.40614324306785 W
FC Voltage : 54.4307654439528 V
PH2 : 2.1621086917990087 atm
PO2 : 2.093068013577334 atm
Power-Thermal : 150.66585675693213 W
###########
I : 2.9
E : 54.28294179524345 V
FC Efficiency : 0.39647868589026086
FC Power : 157.84292259714354 W
FC Voltage : 54.428593999015014 V
PH2 : 2.1618614050825955 atm
PO2 : 2.092928395625044 atm
Power-Thermal : 156.05307740285645 W
###########
I : 3.0
E : 54.282749642742786 V
FC Efficiency : 0.39646328211968823
FC Power : 163.2794381081724 W
FC Voltage : 54.4264793693908 V
PH2 : 2.161614118366182 atm
PO2 : 2.0927887776727534 atm
Power-Thermal : 161.4405618918276 W
###########
I : 3.1
E : 54.282557470327596 V
FC Efficiency : 0.3964482650578333
FC Power : 168.71569526413202 W
FC Voltage : 54.42441782713936 V
PH2 : 2.1613668316497687 atm
PO2 : 2.0926491597204633 atm
Power-Thermal : 166.828304735868 W
###########
I : 3.2
E : 54.282365277993584 V
FC Efficiency : 0.39643361013612227
FC Power : 174.15169919835796 W
FC Voltage : 54.42240599948686 V
PH2 : 2.1611195449333556 atm
PO2 : 2.0925095417681736 atm
Power-Thermal : 172.21630080164203 W
###########
I : 3.3
E : 54.282173065736494 V
FC Efficiency : 0.39641929505459833
FC Power : 179.58745472281433 W
FC Voltage : 54.420440825095255 V
PH2 : 2.1608722582169424 atm
PO2 : 2.092369923815883 atm
Power-Thermal : 177.60454527718562 W
###########
I : 3.4
E : 54.28198083355201 V
FC Efficiency : 0.3964052995109346
FC Power : 185.02296635732776 W
FC Voltage : 54.41851951686111 V
PH2 : 2.1606249715005292 atm
PO2 : 2.092230305863593 atm
Power-Thermal : 182.9930336426722 W
###########
I : 3.5
E : 54.28178858143586 V
FC Efficiency : 0.3963916049687393
FC Power : 190.45823835537988 W
FC Voltage : 54.41663953010853 V
PH2 : 2.160377684784116 atm
PO2 : 2.092090687911303 atm
Power-Thermal : 188.38176164462013 W
###########
I : 3.6
E : 54.281596309383765 V
FC Efficiency : 0.39637819445850625
FC Power : 195.89327472694944 W
FC Voltage : 54.414798535263735 V
PH2 : 2.1601303980677025 atm
PO2 : 2.0919510699590127 atm
Power-Thermal : 193.77072527305054 W
###########
I : 3.7
E : 54.281404017391424 V
FC Efficiency : 0.39636505240584513
FC Power : 201.32807925881536 W
FC Voltage : 54.41299439427442 V
PH2 : 2.1598831113512893 atm
PO2 : 2.0918114520067226 atm
Power-Thermal : 199.15992074118464 W
###########
I : 3.8
E : 54.28121170545457 V
FC Efficiency : 0.3963521644826228
FC Power : 206.76265553266293 W
FC Voltage : 54.41122514017446 V
PH2 : 2.159635824634876 atm
PO2 : 2.0916718340544325 atm
Power-Thermal : 204.54934446733702 W
###########
I : 3.9
E : 54.28101937356888 V
FC Efficiency : 0.39633951747744234
FC Power : 212.1970069412828 W
FC Voltage : 54.40948895930328 V
PH2 : 2.159388537918463 atm
PO2 : 2.0915322161021423 atm
Power-Thermal : 209.9389930587172 W
###########
Report is generating ...
Warning : There are errors in the simulations in some of I amounts; please refer to the .opem file for review. If you are confident about this parameters, ignore this warning.
Done!
>>> Padulles_I_Data["Status"]
True
>>> assert isclose(Padulles_I_Data["P"][5], 27.262222284249443, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(Padulles_I_Data["I"][5], 0.5, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(Padulles_I_Data["V"][5], 54.524444568498886, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(Padulles_I_Data["EFF"][5], 0.3971768980805572, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(Padulles_I_Data["PO2"][5], 2.0962792264800076, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(Padulles_I_Data["PH2"][5], 2.1677962862765128, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(Padulles_I_Data["Ph"][5], 26.857777715750554, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(Padulles_I_Data["V0"], 54.539964013494824, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(Padulles_I_Data["K"], -0.03833515487668971, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(Padulles_I_Data["VE"][5], 54.52079643605648, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> Padulles_I_Data=Dynamic_Analysis(InputMethod={}, TestMode=True,PrintMode=False)
>>> Padulles_I_Data["Status"]
False
>>> Enernst_Calc(E0=None,N0=0,T=1, PH2=2.1, PO2=2.1)
[Error] Enernst Calculation Failed (E0:None, N0:0, T:1, PH2:2.1, PO2:2.1)
>>> PH2_Calc(KH2=None,tH2=1,Kr=0.3,I=3,qH2=0.3)
[Error] PH2 Calculation Failed (KH2:None, tH2:1, Kr:0.3, I:3, qH2:0.3)
>>> PO2_Calc(KO2=None,tO2=1.2,Kr=0.3,I=5,qO2=0.3)
[Error] PO2 Calculation Failed (KO2:None, tO2:1.2, Kr:0.3, I:5, qO2:0.3)
>>> Kr_Calc(N0=None)
[Error] Kr Calculation Failed (N0:None)
>>> qO2_Calc(qH2=2,rho=0)
[Error] qO2 Calculation Error (qH2:2, rho:0)
>>> Test_Vector={"T":343,"E0":-0.6,"N0":88,"KO2":0.0000211,"KH2":0.0000422,"tH2":3.37,"tO2":6.74,"B":0.04777,"C":0.0136,"Rint":0.00303,"rho":1.168,"qH2":0.0004,"i-start":4,"i-stop":0,"i-step":-2,"Name":"test1"}
>>> Padulles_I_Data=Dynamic_Analysis(InputMethod=Test_Vector, TestMode=True)
###########
Padulles-I-Model Simulation
###########
Analyzing . . .
[Error] Vcell Calculation Error (Enernst:-51.31149442586593, B:0.04777, C:0.0136, I:0, Rint:0.00303)
[Error] PEM Efficiency Calculation Failed (Vcell:None, N:88)
[Error] Power Calculation Error (Vcell:None, i:0)
I : 0
E : -51.31149442586593 V
FC Efficiency : None
FC Power : None W
FC Voltage : None V
PH2 : 2.169032719858579 atm
PO2 : 2.0969773162414582 atm
Power-Thermal : None W
###########
I : 2
E : -51.31532972769885 V
FC Efficiency : -0.372590333135464
FC Power : -102.29840186567301 W
FC Voltage : -51.14920093283651 V
PH2 : 2.1640869855303144 atm
PO2 : 2.0941849571956554 atm
Power-Thermal : 318.778401865673 W
###########
Report is generating ...
Warning : The value of I(>2) leads to minus amount of V, please check your inputs
Warning : There are errors in the simulations in some of I amounts; please refer to the .opem file for review. If you are confident about this parameters, ignore this warning.
Done!
>>> sorted(os.listdir("Padulles-I")) == ['test1.csv', 'test1.html', 'test1.opem']
True
>>> Test_Vector={"T":343,"E0":-0.6,"N0":88,"KO2":0.0000211,"KH2":0.0000422,"tH2":3.37,"tO2":6.74,"B":0.04777,"C":0.0136,"Rint":0.00303,"rho":1.168,"qH2":0.0004,"i-start":4,"i-stop":0,"i-step":-2,"Name":"test2"}
>>> Padulles_I_Data=Dynamic_Analysis(InputMethod=Test_Vector, TestMode=True, PrintMode=False, Folder=os.path.join(os.getcwd(), "Folder_Test"))
[Error] Vcell Calculation Error (Enernst:-51.31149442586593, B:0.04777, C:0.0136, I:0, Rint:0.00303)
[Error] PEM Efficiency Calculation Failed (Vcell:None, N:88)
[Error] Power Calculation Error (Vcell:None, i:0)
>>> sorted(os.listdir(os.path.join("Folder_Test", "Padulles-I"))) == ['test2.csv', 'test2.html', 'test2.opem']
True
>>> shutil.rmtree("Padulles-I")
>>> shutil.rmtree("Folder_Test")

'''
