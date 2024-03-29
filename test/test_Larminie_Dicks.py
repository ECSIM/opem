# -*- coding: utf-8 -*-
'''
>>> import os
>>> from math import isclose
>>> from opem.Static.Larminie_Dicks import *
>>> import shutil
>>> ABS_TOL = 1e-12
>>> REL_TOL = 0
>>> E0=1.178
>>> A=0.0587
>>> B=0.0517
>>> RM=0.0018
>>> i_0=0.00654
>>> i_L=100
>>> i_n=0.23
>>> N=23
>>> assert isclose(Vcell_Calc(E0=E0, i=1,i_0=i_0,i_n=i_n,i_L=i_L,R_M=RM,A=A,B=B), 0.8677440917797067, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> Vcell_Calc(E0=None, i=1,i_0=i_0,i_n=i_n,i_L=i_L,R_M=RM,A=A,B=B)
[Error] Vcell Calculation Error (E0:None, i:1, i_0:0.00654, i_n:0.23, i_L:100, R_M:0.0018, A:0.0587, B:0.0517)
>>> Larminie_Dicks_Data=Static_Analysis(InputMethod={}, TestMode=True,PrintMode=False)
>>> Larminie_Dicks_Data["Status"]
False
>>> Test_Vector={"A":0.06,"T":328.15,"E0":1.178,"RM":0.0018,"i_0":0.00654,"i_L":100.0,"i_n":0.23,"N":23,"i-start":0.1,"i-stop":4,"i-step":0.1,"Name":"test1"}
>>> Larminie_Dicks_Data=Static_Analysis(InputMethod=Test_Vector, TestMode=True)
###########
Larminie-Dicks-Model Simulation
###########
Analyzing . . .
I : 0.1
PEM Efficiency : 0.6039038043415609
Power : 0.09420899347728351 W
Power-Stack : 2.1668068499775206 W
Power-Thermal : 0.6621931500224794 W
VStack : 21.668068499775206 V
Vcell : 0.9420899347728351 V
###########
I : 0.2
PEM Efficiency : 0.5935988388304153
Power : 0.1852028377150896 W
Power-Stack : 4.259665267447061 W
Power-Thermal : 1.3983347325529394 W
VStack : 21.298326337235302 V
Vcell : 0.9260141885754479 V
###########
I : 0.3
PEM Efficiency : 0.5854323548069047
Power : 0.2739823420496314 W
Power-Stack : 6.301593867141523 W
Power-Thermal : 2.185406132858478 W
VStack : 21.00531289047174 V
Vcell : 0.9132744734987713 V
###########
I : 0.4
PEM Efficiency : 0.5786600533545858
Power : 0.3610838732932615 W
Power-Stack : 8.304929085745016 W
Power-Thermal : 3.011070914254985 W
VStack : 20.762322714362536 V
Vcell : 0.9027096832331538 V
###########
I : 0.5
PEM Efficiency : 0.5728692080343738
Power : 0.4468379822668116 W
Power-Stack : 10.277273592136666 W
Power-Thermal : 3.8677264078633335 W
VStack : 20.554547184273332 V
Vcell : 0.8936759645336232 V
###########
I : 0.6
PEM Efficiency : 0.5678069515210789
Power : 0.5314673066237299 W
Power-Stack : 12.223748052345787 W
Power-Thermal : 4.750251947654213 W
VStack : 20.37291342057631 V
Vcell : 0.8857788443728831 V
###########
I : 0.7
PEM Efficiency : 0.5633070812262543
Power : 0.6151313326990697 W
Power-Stack : 14.148020652078603 W
Power-Thermal : 5.654979347921395 W
VStack : 20.211458074398006 V
Vcell : 0.8787590467129568 V
###########
I : 0.8
PEM Efficiency : 0.559254485938545
Power : 0.6979495984513041 W
Power-Stack : 16.052840764379994 W
Power-Thermal : 6.579159235620006 W
VStack : 20.066050955474992 V
Vcell : 0.8724369980641301 V
###########
I : 0.9
PEM Efficiency : 0.555566137728257
Power : 0.7800148573704729 W
Power-Stack : 17.940341719520877 W
Power-Thermal : 7.520658280479121 W
VStack : 19.933713021689865 V
Vcell : 0.866683174856081 V
###########
I : 1.0
PEM Efficiency : 0.5521801761623923
Power : 0.8614010748133321 W
Power-Stack : 19.812224720706638 W
Power-Thermal : 8.477775279293361 W
VStack : 19.812224720706638 V
Vcell : 0.8614010748133321 V
###########
I : 1.1
PEM Efficiency : 0.5490492731447867
Power : 0.9421685527164539 W
Power-Stack : 21.66987671247844 W
Power-Thermal : 9.449123287521559 W
VStack : 19.699887920434946 V
Vcell : 0.8565168661058672 V
###########
I : 1.2
PEM Efficiency : 0.546136409695077
Power : 1.0223673589491842 W
Power-Stack : 23.514449255831238 W
Power-Thermal : 10.43355074416876 W
VStack : 19.595374379859365 V
Vcell : 0.8519727991243202 V
###########
I : 1.3
PEM Efficiency : 0.5434120834903051
Power : 1.1020397053183388 W
Power-Stack : 25.346913222321792 W
Power-Thermal : 11.430086777678207 W
VStack : 19.497625555632148 V
Vcell : 0.8477228502448759 V
###########
I : 1.4
PEM Efficiency : 0.5408524022350751
Power : 1.1812216464814043 W
Power-Stack : 27.168097869072298 W
Power-Thermal : 12.4379021309277 W
VStack : 19.4057841921945 V
Vcell : 0.8437297474867174 V
###########
I : 1.5
PEM Efficiency : 0.5384377456798006
Power : 1.2599443248907334 W
Power-Stack : 28.97871947248687 W
Power-Thermal : 13.456280527513128 W
VStack : 19.319146314991247 V
Vcell : 0.839962883260489 V
###########
I : 1.6
PEM Efficiency : 0.5361518041755653
Power : 1.338234903222211 W
Power-Stack : 30.779402774110853 W
Power-Thermal : 14.48459722588915 W
VStack : 19.23712673381928 V
Vcell : 0.8363968145138818 V
###########
I : 1.7
PEM Efficiency : 0.5339808733545007
Power : 1.4161172761361358 W
Power-Stack : 32.57069735113112 W
Power-Thermal : 15.522302648868873 W
VStack : 19.159233735959486 V
Vcell : 0.8330101624330211 V
###########
I : 1.8
PEM Efficiency : 0.5319133271838169
Power : 1.493612622732158 W
Power-Stack : 34.353090322839634 W
Power-Thermal : 16.568909677160363 W
VStack : 19.085050179355353 V
Vcell : 0.8297847904067545 V
###########
I : 1.9
PEM Efficiency : 0.5299392178574475
Power : 1.5707398417294742 W
Power-Stack : 36.127016359777905 W
Power-Thermal : 17.623983640222086 W
VStack : 19.014219136725217 V
Vcell : 0.826705179857618 V
###########
I : 2.0
PEM Efficiency : 0.5280499675656114
Power : 1.6475158988047076 W
Power-Stack : 37.89286567250827 W
Power-Thermal : 18.687134327491727 W
VStack : 18.946432836254136 V
Vcell : 0.8237579494023538 V
###########
I : 2.1
PEM Efficiency : 0.5262381279323336
Power : 1.7239561071063247 W
Power-Stack : 39.65099046344547 W
Power-Thermal : 19.758009536554532 W
VStack : 18.881424030212127 V
Vcell : 0.8209314795744403 V
###########
I : 2.2
PEM Efficiency : 0.5244971900414818
Power : 1.8000743562223656 W
Power-Stack : 41.40171019311441 W
Power-Thermal : 20.836289806885592 W
VStack : 18.818959178688367 V
Vcell : 0.8182156164647115 V
###########
I : 2.3
PEM Efficiency : 0.5228214327988451
Power : 1.8758833008822562 W
Power-Stack : 43.14531592029189 W
Power-Thermal : 21.9216840797081 W
VStack : 18.758833008822563 V
Vcell : 0.8156014351661984 V
###########
I : 2.4
PEM Efficiency : 0.521205800705988
Power : 1.9513945178432193 W
Power-Stack : 44.88207391039404 W
Power-Thermal : 23.01392608960595 W
VStack : 18.700864129330853 V
Vcell : 0.8130810491013414 V
###########
I : 2.5
PEM Efficiency : 0.5196458044550865
Power : 2.0266186373748374 W
Power-Stack : 46.61222865962126 W
Power-Thermal : 24.112771340378742 W
VStack : 18.644891463848502 V
Vcell : 0.810647454949935 V
###########
I : 2.6
PEM Efficiency : 0.5181374394151615
Power : 2.1015654542678956 W
Power-Stack : 48.3360054481616 W
Power-Thermal : 25.21799455183841 W
VStack : 18.590771326215997 V
Vcell : 0.8082944054876521 V
###########
I : 2.7
PEM Efficiency : 0.5166771182793914
Power : 2.176244022192797 W
Power-Stack : 50.053612510434334 W
Power-Thermal : 26.329387489565672 W
VStack : 18.538375003864566 V
Vcell : 0.8060163045158507 V
###########
I : 2.8
PEM Efficiency : 0.5152616150201836
Power : 2.250662734408162 W
Power-Stack : 51.76524289138773 W
Power-Thermal : 27.446757108612264 W
VStack : 18.48758674692419 V
Vcell : 0.8038081194314866 V
###########
I : 2.9
PEM Efficiency : 0.5138880179476886
Power : 2.324829393195343 W
Power-Stack : 53.47107604349289 W
Power-Thermal : 28.569923956507104 W
VStack : 18.438302083963066 V
Vcell : 0.8016653079983942 V
###########
I : 3.0
PEM Efficiency : 0.5125536901530251
Power : 2.3987512699161577 W
Power-Stack : 55.171279208071624 W
Power-Thermal : 29.698720791928377 W
VStack : 18.39042640269054 V
Vcell : 0.7995837566387192 V
###########
I : 3.1
PEM Efficiency : 0.5112562359845451
Power : 2.47243515722126 W
Power-Stack : 56.866008616088976 W
Power-Thermal : 30.832991383911025 W
VStack : 18.343873747125475 V
Vcell : 0.7975597281358903 V
###########
I : 3.2
PEM Efficiency : 0.5099934724855826
Power : 2.5458874146480284 W
Power-Stack : 58.55541053690465 W
Power-Thermal : 31.97258946309536 W
VStack : 18.2985657927827 V
Vcell : 0.7955898170775088 V
###########
I : 3.3
PEM Efficiency : 0.5087634049378041
Power : 2.6191140086198157 W
Power-Stack : 60.23962219825576 W
Power-Thermal : 33.11737780174424 W
VStack : 18.25443096916841 V
Vcell : 0.7936709117029744 V
###########
I : 3.4
PEM Efficiency : 0.5075642058217301
Power : 2.6921205476784564 W
Power-Stack : 61.9187725966045 W
Power-Thermal : 34.2672274033955 W
VStack : 18.211403704883676 V
Vcell : 0.791800161081899 V
###########
I : 3.5
PEM Efficiency : 0.5063941966370149
Power : 2.7649123136381015 W
Power-Stack : 63.592983213676334 W
Power-Thermal : 35.42201678632366 W
VStack : 18.169423775336096 V
Vcell : 0.7899749467537432 V
###########
I : 3.6
PEM Efficiency : 0.5052518321283558
Power : 2.8374942892328465 W
Power-Stack : 65.26236865235548 W
Power-Thermal : 36.58163134764453 W
VStack : 18.128435736765407 V
Vcell : 0.7881928581202351 V
###########
I : 3.7
PEM Efficiency : 0.5041356865448693
Power : 2.909871182736986 W
Power-Stack : 66.92703720295067 W
Power-Thermal : 37.74596279704932 W
VStack : 18.088388433229913 V
Vcell : 0.7864516710099961 V
###########
I : 3.8
PEM Efficiency : 0.503044441626258
Power : 2.982047449960458 W
Power-Stack : 68.58709134909053 W
Power-Thermal : 38.91490865090946 W
VStack : 18.04923456555014 V
Vcell : 0.7847493289369626 V
###########
I : 3.9
PEM Efficiency : 0.5019768760617338
Power : 3.054027313959588 W
Power-Stack : 70.24262822107053 W
Power-Thermal : 40.08837177892947 W
VStack : 18.010930313095006 V
Vcell : 0.7830839266563047 V
###########
Report is generating ...
Done!
>>> Larminie_Dicks_Data["Status"]
True
>>> assert isclose(Larminie_Dicks_Data["P"][5], 12.223748052345787, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(Larminie_Dicks_Data["I"][5], 0.6, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(Larminie_Dicks_Data["V"][5], 20.37291342057631, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(Larminie_Dicks_Data["EFF"][5], 0.5678069515210789, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(Larminie_Dicks_Data["Ph"][5], 4.750251947654213, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(Larminie_Dicks_Data["V0"], 20.823811410978124, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(Larminie_Dicks_Data["K"], -0.8163936642494803, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(Larminie_Dicks_Data["VE"][5], 20.333975212428435, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> Test_Vector={"A":0.06,"E0":-1.178,"T":328.15,"RM":0.0018,"i_0":0.00654,"i_L":100.0,"i_n":0.23,"N":23,"i-start":5,"i-stop":0.1,"i-step":-2,"Name":"test1"}
>>> Larminie_Dicks_Data=Static_Analysis(InputMethod=Test_Vector, TestMode=True)
###########
Larminie-Dicks-Model Simulation
###########
Analyzing . . .
I : 0.1
PEM Efficiency : -0.9063526059148493
Power : -0.1413910065227165 W
Power-Stack : -3.2519931500224795 W
Power-Thermal : 6.080993150022479 W
VStack : -32.51993150022479 V
Vcell : -1.413910065227165 V
###########
I : 2.0
PEM Efficiency : -0.9822064426907987
Power : -3.0644841011952924 W
Power-Stack : -70.48313432749173 W
Power-Thermal : 127.06313432749172 W
VStack : -35.24156716374586 V
Vcell : -1.5322420505976462 V
###########
I : 4.0
PEM Efficiency : -1.0093245540461908
Power : -6.29818521724823 W
Power-Stack : -144.8582599967093 W
Power-Thermal : 258.0182599967093 W
VStack : -36.21456499917733 V
Vcell : -1.5745463043120576 V
###########
Report is generating ...
Warning : The value of I(>0.1) leads to minus amount of V, please check your inputs
Done!
>>> sorted(os.listdir("Larminie-Dicks")) == ['test1.csv', 'test1.html', 'test1.opem']
True
>>> Test_Vector={"A":0.06,"E0":-1.178,"T":328.15,"RM":0.0018,"i_0":0.00654,"i_L":100.0,"i_n":0.23,"N":23,"i-start":5,"i-stop":0.1,"i-step":-2,"Name":"test2"}
>>> Larminie_Dicks_Data=Static_Analysis(InputMethod=Test_Vector, TestMode=True, PrintMode=False, Folder=os.path.join(os.getcwd(), "Folder_Test"))
>>> sorted(os.listdir(os.path.join("Folder_Test", "Larminie-Dicks"))) == ['test2.csv', 'test2.html', 'test2.opem']
True
>>> shutil.rmtree("Larminie-Dicks")
>>> shutil.rmtree("Folder_Test")

'''
