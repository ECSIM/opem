# -*- coding: utf-8 -*-
'''
>>> import os
>>> from math import isclose
>>> from opem.Static.Amphlett import *
>>> import random
>>> import shutil
>>> ABS_TOL = 1e-12
>>> REL_TOL = 0
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
>>> assert isclose(Enernst_Calc(T,PH2,PO2), 1.19075, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(CH2_Calc(PH2,T), 7.330294784824117e-07, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(CO2_Calc(PO2,T), 8.402541445801334e-07, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(Rho_Calc(i,A,T,lambda_param), 4.978789826264977, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(Xi2_Calc(A,PH2,T), 0.0030373688787134006, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> Eta_Conc_Calc(i,A,Jn,JMax)
0
>>> Eta_Ohmic_Calc(i,l,A,T,lambda_param)
0
>>> Eta_Act_Calc(T,PO2,PH2,i,A)
0
>>> PowerStack_Calc(2,2)
4
>>> B_Calc(230,None)
>>> PowerStack_Calc(None,2)
[Error] Power Stack Calculation Error (Power:None, N:2)
>>> Power_Total_Calc([None,None,None,None],2,20)
[None, None]
>>> Linear_Aprox_Params_Calc(22, 0)
[None, 11.0]
>>> Linear_Aprox_Params_Calc(None, 22)
[None, None]
>>> T='20000000000'
>>> PH2='10000000'
>>> PO2='1000000000'
>>> i='160000000'
>>> A='30000000000'
>>> l='50000000000'
>>> lambda_param='50000000000'
>>> N='80000000000'
>>> Enernst_Calc(T,PH2,PO2)
[Error] Enernst Calculation Failed (T:20000000000 , PH2:10000000, PO2:1000000000)
>>> CH2_Calc(PH2,T)
[Error] CH2 Calculation Failed (PH2:10000000, T:20000000000)
>>> CO2_Calc(PO2,T)
[Error] CO2 Calculation Failed (PO2:1000000000, T:20000000000)
>>> Rho_Calc(i,A,T,lambda_param)
[Error] Rho Calculation Failed (i:160000000, A:30000000000, T:20000000000, lambda:50000000000)
>>> Xi2_Calc(A,PH2,T)
[Error] CH2 Calculation Failed (PH2:10000000, T:20000000000)
[Error] Xi2 Calculation Failed (A:30000000000, PH2:10000000, T:20000000000)
>>> Eta_Conc_Calc(i,A,None,None)
[Error] Eta Concentration Calculation Failed (i:160000000, A:30000000000, B:None, JMax:None)
>>> Eta_Ohmic_Calc(i,l,A,T,lambda_param)
[Error] Rho Calculation Failed (i:160000000, A:30000000000, T:20000000000, lambda:50000000000)
[Error] Eta Ohmic Calculation Failed (i:160000000, l:50000000000, A:30000000000, T:20000000000, lambda:50000000000, R_elec:None)
>>> Eta_Act_Calc(T,PO2,PH2,i,A)
[Error] CO2 Calculation Failed (PO2:1000000000, T:20000000000)
[Error] CH2 Calculation Failed (PH2:10000000, T:20000000000)
[Error] Xi2 Calculation Failed (A:30000000000, PH2:10000000, T:20000000000)
[Error] Eta Activation Calculation Failed (T:20000000000, PO2:1000000000, PH2:10000000, i:160000000, A:30000000000)
>>> Efficiency_Calc(None)
[Error] PEM Efficiency Calculation Failed (Vcell:None)
>>> VStack_Calc(12,None)
[Error] VStack Calculation Error (N:12, Vcell:None)
>>> Amphlett_Data=Static_Analysis(InputMethod={},TestMode=True,PrintMode=False)
>>> Amphlett_Data["Status"]
False
>>> Loss_Calc(122,22,None)
[Error] Loss Calculation Error (Eta_Act:122, Eta_Ohmic:22, Eta_Conc:None)
>>> Vcell_Calc(122,None)
[Error] Vcell Calculation Error (Enernst:122, Loss:None)
>>> Vcell_Calc(122,None)
[Error] Vcell Calculation Error (Enernst:122, Loss:None)
>>> Test_Vector={"T":343.15,"PH2":1,"PO2":1,"i-start":0,"i-stop":4,"i-step":0.1,"A":50.6,"l":0.0178,"lambda":23,"N":1,"R":0,"JMax":1.5,"Name":"test1"}
>>> Amphlett_Data=Static_Analysis(InputMethod=Test_Vector,TestMode=True)
###########
Amphlett-Model Simulation
###########
Analyzing . . .
I : 0
Enernst : 1.19075 V
Eta Activation : 0 V
Eta Concentration : 0 V
Eta Ohmic : 0 V
Loss : 0 V
PEM Efficiency : 0.763301282051282
Power : 0.0 W
Power-Stack : 0.0 W
Power-Thermal : 0.0 W
VStack : 1.19075 V
Vcell : 1.19075 V
###########
I : 0.1
Enernst : 1.19075 V
Eta Activation : 0.11807074742083559 V
Eta Concentration : 1.9492837182237548e-05 V
Eta Ohmic : 0.00017520002843124318 V
Loss : 0.11826544028644907 V
PEM Efficiency : 0.6874901023804812
Power : 0.10724845597135509 W
Power-Stack : 0.10724845597135509 W
Power-Thermal : 0.015751544028644916 W
VStack : 1.0724845597135508 V
Vcell : 1.0724845597135508 V
###########
I : 0.2
Enernst : 1.19075 V
Eta Activation : 0.1639764642376006 V
Eta Concentration : 3.90114074903386e-05 V
Eta Ohmic : 0.0003505137928660484 V
Loss : 0.164365989437957 V
PEM Efficiency : 0.6579384683090018
Power : 0.20527680211240862 W
Power-Stack : 0.20527680211240862 W
Power-Thermal : 0.040723197887591406 W
VStack : 1.026384010562043 V
Vcell : 1.026384010562043 V
###########
I : 0.3
Enernst : 1.19075 V
Eta Activation : 0.1908295871441327 V
Eta Concentration : 5.8555778956387346e-05 V
Eta Ohmic : 0.0005259414221215358 V
Loss : 0.19141408434521062 V
PEM Efficiency : 0.6405999459325573
Power : 0.2998007746964368 W
Power-Stack : 0.2998007746964368 W
Power-Thermal : 0.06919922530356316 W
VStack : 0.9993359156547894 V
Vcell : 0.9993359156547894 V
###########
I : 0.4
Enernst : 1.19075 V
Eta Activation : 0.20988218105436562 V
Eta Concentration : 7.812601988262199e-05 V
Eta Ohmic : 0.0007014830568214833 V
Loss : 0.21066179013106975 V
PEM Efficiency : 0.628261672992904
Power : 0.3920352839475721 W
Power-Stack : 0.3920352839475721 W
Power-Thermal : 0.09996471605242792 W
VStack : 0.9800882098689302 V
Vcell : 0.9800882098689302 V
###########
I : 0.5
Enernst : 1.19075 V
Eta Activation : 0.22466052101362555 V
Eta Concentration : 9.772219884285375e-05 V
Eta Ohmic : 0.0008771388470514419 V
Loss : 0.22563538205951983 V
PEM Efficiency : 0.6186632166285129
Power : 0.4825573089702401 W
Power-Stack : 0.4825573089702401 W
Power-Thermal : 0.13244269102975992 W
VStack : 0.9651146179404801 V
Vcell : 0.9651146179404801 V
###########
I : 0.6
Enernst : 1.19075 V
Eta Activation : 0.23673530396089773 V
Eta Concentration : 0.00011734438468392014 V
Eta Ohmic : 0.0010529089510685316 V
Loss : 0.23790555729665017 V
PEM Efficiency : 0.6107977196816344
Power : 0.5717066656220099 W
Power-Stack : 0.5717066656220099 W
Power-Thermal : 0.16629333437799013 W
VStack : 0.9528444427033498 V
Vcell : 0.9528444427033498 V
###########
I : 0.7
Enernst : 1.19075 V
Eta Activation : 0.2469443874769634 V
Eta Concentration : 0.00013699264652713124 V
Eta Ohmic : 0.001228793534444728 V
Loss : 0.24831017365793526 V
PEM Efficiency : 0.6041280938090158
Power : 0.6597078784394452 W
Power-Stack : 0.6597078784394452 W
Power-Thermal : 0.2012921215605547 W
VStack : 0.9424398263420647 V
Vcell : 0.9424398263420647 V
###########
I : 0.8
Enernst : 1.19075 V
Eta Activation : 0.25578789787113065 V
Eta Concentration : 0.0001566670537697257 V
Eta Ohmic : 0.0014047927694433354 V
Loss : 0.2573493576943437 V
PEM Efficiency : 0.5983337450677283
Power : 0.746720513844525 W
Power-Stack : 0.746720513844525 W
Power-Thermal : 0.237279486155475 W
VStack : 0.9334006423056562 V
Vcell : 0.9334006423056562 V
###########
I : 0.9
Enernst : 1.19075 V
Eta Activation : 0.26358842686742984 V
Eta Concentration : 0.000176367676086353 V
Eta Ohmic : 0.0015809068345387157 V
Loss : 0.2653457013780549 V
PEM Efficiency : 0.593207883732016
Power : 0.8328638687597506 W
Power-Stack : 0.8328638687597506 W
Power-Thermal : 0.27413613124024944 W
VStack : 0.9254042986219451 V
Vcell : 0.9254042986219451 V
###########
I : 1.0
Enernst : 1.19075 V
Eta Activation : 0.2705662378303906 V
Eta Concentration : 0.00019609458343054068 V
Eta Ohmic : 0.0017571359140316743 V
Loss : 0.2725194683278528 V
PEM Efficiency : 0.5886093151744533
Power : 0.9182305316721472 W
Power-Stack : 0.9182305316721472 W
Power-Thermal : 0.3117694683278528 W
VStack : 0.9182305316721472 V
Vcell : 0.9182305316721472 V
###########
I : 1.1
Enernst : 1.19075 V
Eta Activation : 0.27687843565296244 V
Eta Concentration : 0.0002158478460361963 V
Eta Ohmic : 0.001933480197732536 V
Loss : 0.27902776369673116 V
PEM Efficiency : 0.5844373309636339
Power : 1.0028944599335958 W
Power-Stack : 1.0028944599335958 W
Power-Thermal : 0.35010554006640426 W
VStack : 0.9117222363032689 V
Vcell : 0.9117222363032689 V
###########
I : 1.2
Enernst : 1.19075 V
Eta Activation : 0.28264102077766273 V
Eta Concentration : 0.00023562753441910272 V
Eta Ohmic : 0.002109939880694226 V
Loss : 0.28498658819277606 V
PEM Efficiency : 0.5806175716712974
Power : 1.0869160941686686 W
Power-Stack : 1.0869160941686686 W
Power-Thermal : 0.3890839058313312 W
VStack : 0.905763411807224 V
Vcell : 0.905763411807224 V
###########
I : 1.3
Enernst : 1.19075 V
Eta Activation : 0.28794208521933035 V
Eta Concentration : 0.0002554337193784237 V
Eta Ohmic : 0.002286515162983545 V
Loss : 0.2904840341016923 V
PEM Efficiency : 0.5770935678835305
Power : 1.1703457556678 W
Power-Stack : 1.1703457556678 W
Power-Thermal : 0.42865424433220006 W
VStack : 0.9002659658983077 V
Vcell : 0.9002659658983077 V
###########
I : 1.4
Enernst : 1.19075 V
Eta Activation : 0.29285010429372843 V
Eta Concentration : 0.00027526647199823583 V
Eta Ohmic : 0.0024632062494824017 V
Loss : 0.295588577015209 V
PEM Efficiency : 0.5738214249902506
Power : 1.2532259921787072 W
Power-Stack : 1.2532259921787072 W
Power-Thermal : 0.4687740078212926 W
VStack : 0.895161422984791 V
Vcell : 0.895161422984791 V
###########
I : 1.5
Enernst : 1.19075 V
Eta Activation : 0.29741936073692266 V
Eta Concentration : 0.00029512586364904603 V
Eta Ohmic : 0.002640013349713048 V
Loss : 0.30035449995028474 V
PEM Efficiency : 0.5707663461857149
Power : 1.3355932500745729 W
Power-Stack : 1.3355932500745729 W
Power-Thermal : 0.5094067499254271 W
VStack : 0.8903955000497152 V
Vcell : 0.8903955000497152 V
###########
I : 1.6
Enernst : 1.19075 V
Eta Activation : 0.3016936146878957 V
Eta Concentration : 0.0003150119659893443 V
Eta Ohmic : 0.0028169366776829123 V
Loss : 0.3048255633315679 V
PEM Efficiency : 0.5679002799156615
Power : 1.4174790986694914 W
Power-Stack : 1.4174790986694914 W
Power-Thermal : 0.5505209013305088 W
VStack : 0.885924436668432 V
Vcell : 0.885924436668432 V
###########
I : 1.7
Enernst : 1.19075 V
Eta Activation : 0.3057086591103234 V
Eta Concentration : 0.00033492485096715016 V
Eta Ohmic : 0.0029939764517456784 V
Loss : 0.30903756041303626 V
PEM Efficiency : 0.5652002817865153
Power : 1.4989111472978385 W
Power-Stack : 1.4989111472978385 W
Power-Thermal : 0.5920888527021615 W
VStack : 0.8817124395869638 V
Vcell : 0.8817124395869638 V
###########
I : 1.8
Enernst : 1.19075 V
Eta Activation : 0.30949414368419487 V
Eta Concentration : 0.0003548645908215691 V
Eta Ohmic : 0.0031711328944759895 V
Loss : 0.31302014116949245 V
PEM Efficiency : 0.5626473454041715
Power : 1.5799137458949137 W
Power-Stack : 1.5799137458949137 W
Power-Thermal : 0.6340862541050863 W
VStack : 0.8777298588305076 V
Vcell : 0.8777298588305076 V
###########
I : 1.9
Enernst : 1.19075 V
Eta Activation : 0.3130749049111216 V
Eta Concentration : 0.0003748312580843772 V
Eta Ohmic : 0.003348406232555746 V
Loss : 0.3167981424017617 V
PEM Efficiency : 0.5602255497424605
Power : 1.6605085294366528 W
Power-Stack : 1.6605085294366528 W
Power-Thermal : 0.6764914705633471 W
VStack : 0.8739518575982383 V
Vcell : 0.8739518575982383 V
###########
I : 2.0
Enernst : 1.19075 V
Eta Activation : 0.3164719546471556 V
Eta Concentration : 0.0003948249255815907 V
Eta Ohmic : 0.0035257966966703337 V
Loss : 0.32039257626940754 V
PEM Efficiency : 0.5579214254683285
Power : 1.7407148474611849 W
Power-Stack : 1.7407148474611849 W
Power-Thermal : 0.7192851525388151 W
VStack : 0.8703574237305924 V
Vcell : 0.8703574237305924 V
###########
I : 2.1
Enernst : 1.19075 V
Eta Activation : 0.31970322720026056 V
Eta Concentration : 0.000414845666435071 V
Eta Ohmic : 0.003703304521413451 V
Loss : 0.32382137738810907 V
PEM Efficiency : 0.5557234760332633
Power : 1.8205501074849708 W
Power-Stack : 1.8205501074849708 W
Power-Thermal : 0.7624498925150291 W
VStack : 0.8669286226118909 V
Vcell : 0.8669286226118909 V
###########
I : 2.2
Enernst : 1.19075 V
Eta Activation : 0.32278415246972747 V
Eta Concentration : 0.00043489355406412477 V
Eta Ohmic : 0.0038809299451994456 V
Loss : 0.32709997596899104 V
PEM Efficiency : 0.5536218102762878
Power : 1.90003005286822 W
Power-Stack : 1.90003005286822 W
Power-Thermal : 0.8059699471317803 W
VStack : 0.863650024031009 V
Vcell : 0.863650024031009 V
###########
I : 2.3
Enernst : 1.19075 V
Eta Activation : 0.3257281015786805 V
Eta Concentration : 0.00045496866218711405 V
Eta Ohmic : 0.004058673210182234 V
Loss : 0.33024174345104984 V
PEM Efficiency : 0.5516078567621475
Power : 1.979168990062585 W
Power-Stack : 1.979168990062585 W
Power-Thermal : 0.8498310099374146 W
VStack : 0.8605082565489501 V
Vcell : 0.8605082565489501 V
###########
I : 2.4
Enernst : 1.19075 V
Eta Activation : 0.32854673759442776 V
Eta Concentration : 0.0004750710648230946 V
Eta Ohmic : 0.004236534562180054 V
Loss : 0.3332583432214309 V
PEM Efficiency : 0.5496741389606211
Power : 2.0579799762685655 W
Power-Stack : 2.0579799762685655 W
Power-Thermal : 0.8940200237314341 W
VStack : 0.8574916567785691 V
Vcell : 0.8574916567785691 V
###########
I : 2.5
Enernst : 1.19075 V
Eta Activation : 0.33125029460641553 V
Eta Concentration : 0.0004952008362934398 V
Eta Ohmic : 0.004414514250605397 V
Loss : 0.3361600096933144 V
PEM Efficiency : 0.5478140963504394
Power : 2.136474975766714 W
Power-Stack : 2.136474975766714 W
Power-Thermal : 0.938525024233286 W
VStack : 0.8545899903066856 V
Vcell : 0.8545899903066856 V
###########
I : 2.6
Enernst : 1.19075 V
Eta Activation : 0.3338478020360954 V
Eta Concentration : 0.0005153580512235011 V
Eta Ohmic : 0.004592612528399569 V
Loss : 0.3389557726157184 V
PEM Efficiency : 0.5460219406309498
Power : 2.214664991199132 W
Power-Stack : 2.214664991199132 W
Power-Thermal : 0.9833350088008679 W
VStack : 0.8517942273842816 V
Vcell : 0.8517942273842816 V
###########
I : 2.7
Enernst : 1.19075 V
Eta Activation : 0.336347266590727 V
Eta Concentration : 0.0005355427845442633 V
Eta Ohmic : 0.004770829651971409 V
Loss : 0.34165363902724266 V
PEM Efficiency : 0.5442925390851008
Power : 2.292560174626445 W
Power-Stack : 2.292560174626445 W
Power-Thermal : 1.0284398253735554 W
VStack : 0.8490963609727573 V
Vcell : 0.8490963609727573 V
###########
I : 2.8
Enernst : 1.19075 V
Eta Activation : 0.33875582111049346 V
Eta Concentration : 0.0005557551114940101 V
Eta Ohmic : 0.00494916588113977 V
Loss : 0.34426074210312724 V
PEM Efficiency : 0.542621319164662
Power : 2.3701699221112436 W
Power-Stack : 2.3701699221112436 W
Power-Thermal : 1.073830077888756 W
VStack : 0.8464892578968728 V
Vcell : 0.8464892578968728 V
###########
I : 2.9
Enernst : 1.19075 V
Eta Activation : 0.3410798472843882 V
Eta Concentration : 0.000575995107620019 V
Eta Ohmic : 0.005127621479079398 V
Loss : 0.34678346387108766 V
PEM Efficiency : 0.5410041898262259
Power : 2.447502954773846 W
Power-Stack : 2.447502954773846 W
Power-Thermal : 1.1194970452261541 W
VStack : 0.8439665361289124 V
Vcell : 0.8439665361289124 V
###########
I : 3.0
Enernst : 1.19075 V
Eta Activation : 0.3433250775536877 V
Eta Concentration : 0.0005962628487802421 V
Eta Ohmic : 0.005306196712269878 V
Loss : 0.3492275371147378 V
PEM Efficiency : 0.5394374762085015
Power : 2.524567388655787 W
Power-Stack : 2.524567388655787 W
Power-Thermal : 1.1654326113442133 W
VStack : 0.8415224628852622 V
Vcell : 0.8415224628852622 V
###########
I : 3.1
Enernst : 1.19075 V
Eta Activation : 0.3454966803001176 V
Eta Concentration : 0.0006165584111450235 V
Eta Ohmic : 0.005484891850447433 V
Loss : 0.35159813056171 V
PEM Efficiency : 0.5379178650245449
Power : 2.601370795258699 W
Power-Stack : 2.601370795258699 W
Power-Thermal : 1.2116292047413009 W
VStack : 0.83915186943829 V
Vcell : 0.83915186943829 V
###########
I : 3.2
Enernst : 1.19075 V
Eta Activation : 0.3475993315046607 V
Eta Concentration : 0.0006368818711988125 V
Eta Ohmic : 0.00566370716655928 V
Loss : 0.3538999205424188 V
PEM Efficiency : 0.5364423586266546
Power : 2.6779202542642597 W
Power-Stack : 2.6779202542642597 W
Power-Thermal : 1.2580797457357402 W
VStack : 0.8368500794575812 V
Vcell : 0.8368500794575812 V
###########
I : 3.3
Enernst : 1.19075 V
Eta Activation : 0.34963727537625955 V
Eta Concentration : 0.0006572333057418867 V
Eta Ohmic : 0.005842642936720367 V
Loss : 0.35613715161872184 V
PEM Efficiency : 0.5350082361418449
Power : 2.7542223996582176 W
Power-Stack : 2.7542223996582176 W
Power-Thermal : 1.304777600341782 W
VStack : 0.8346128483812781 V
Vcell : 0.8346128483812781 V
###########
I : 3.4
Enernst : 1.19075 V
Eta Activation : 0.35161437592708844 V
Eta Concentration : 0.0006776127918921064 V
Eta Ohmic : 0.00602169944017227 V
Loss : 0.3583136881591528 V
PEM Efficiency : 0.5336130204107994
Power : 2.83028346025888 W
Power-Stack : 2.83028346025888 W
Power-Thermal : 1.3517165397411197 W
VStack : 0.8324363118408471 V
Vcell : 0.8324363118408471 V
###########
I : 3.5
Enernst : 1.19075 V
Eta Activation : 0.3535341610697534 V
Eta Concentration : 0.0006980204070866538 V
Eta Ohmic : 0.006200876959244138 V
Loss : 0.3604330584360842 V
PEM Efficiency : 0.5322544497204589
Power : 2.9061092954737053 W
Power-Stack : 2.9061092954737053 W
Power-Thermal : 1.3988907045262948 W
VStack : 0.8303169415639158 V
Vcell : 0.8303169415639158 V
###########
I : 3.6
Enernst : 1.19075 V
Eta Activation : 0.3553998605009599 V
Eta Concentration : 0.0007184562290838106 V
Eta Ohmic : 0.0063801757793154595 V
Loss : 0.3624984925093591 V
PEM Efficiency : 0.5309304535196415
Power : 2.9817054269663075 W
Power-Stack : 2.9817054269663075 W
Power-Thermal : 1.4462945730336927 W
VStack : 0.8282515074906409 V
Vcell : 0.8282515074906409 V
###########
I : 3.7
Enernst : 1.19075 V
Eta Activation : 0.3572144383935416 V
Eta Concentration : 0.0007389203359647302 V
Eta Ohmic : 0.0065595961887805875 V
Loss : 0.36451295491828695 V
PEM Efficiency : 0.5296391314626365
Power : 3.0570770668023384 W
Power-Stack : 3.0570770668023384 W
Power-Thermal : 1.4939229331976618 W
VStack : 0.826237045081713 V
Vcell : 0.826237045081713 V
###########
I : 3.8
Enernst : 1.19075 V
Eta Activation : 0.35898062172788664 V
Eta Concentration : 0.0007594128061352231 V
Eta Ohmic : 0.0067391384790148525 V
Loss : 0.36647917301303673 V
PEM Efficiency : 0.5283787352480533
Power : 3.13222914255046 W
Power-Stack : 3.13222914255046 W
Power-Thermal : 1.5417708574495397 W
VStack : 0.8242708269869632 V
Vcell : 0.8242708269869632 V
###########
I : 3.9
Enernst : 1.19075 V
Eta Activation : 0.36070092494262745 V
Eta Concentration : 0.0007799337183275707 V
Eta Ohmic : 0.0069188029443421825 V
Loss : 0.3683996616052972 V
PEM Efficiency : 0.5271476528171172
Power : 3.207166319739341 W
Power-Stack : 3.207166319739341 W
Power-Thermal : 1.5898336802606587 W
VStack : 0.8223503383947028 V
Vcell : 0.8223503383947028 V
###########
Report is generating ...
Done!
>>> Amphlett_Data["Status"]
True
>>> assert isclose(Amphlett_Data["P"][5], 0.4825573089702401, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(Amphlett_Data["I"][5], 0.5, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(Amphlett_Data["V"][5], 0.9651146179404801, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(Amphlett_Data["EFF"][5], 0.6186632166285129, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(Amphlett_Data["Ph"][5], 0.13244269102975992, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(Amphlett_Data["V0"], 1.004092712293457, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(Amphlett_Data["K"], -0.055817073316848265, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(Amphlett_Data["Eta_Active"][5], 0.22466052101362555, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(Amphlett_Data["Eta_Conc"][5], 9.772219884285375e-05, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(Amphlett_Data["Eta_Ohmic"][5], 0.0008771388470514419, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(Amphlett_Data["VE"][5], 0.9761841756350329, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> Test_Vector={"T":3432222.15,"PH2":1,"PO2":1,"i-start":5,"i-stop":0,"i-step":-2,"A":50.6,"l":0.0178,"lambda":23,"N":1,"R":0,"JMax":1.5,"Name":"test1"}
>>> Amphlett_Data=Static_Analysis(InputMethod=Test_Vector,TestMode=True)
###########
Amphlett-Model Simulation
###########
Analyzing . . .
I : 0
Enernst : -2915.9064000000003 V
Eta Activation : 0 V
Eta Concentration : 0 V
Eta Ohmic : 0 V
Loss : 0 V
PEM Efficiency : -1869.1707692307693
Power : -0.0 W
Power-Stack : -0.0 W
Power-Thermal : 0.0 W
VStack : -2915.9064000000003 V
Vcell : -2915.9064000000003 V
###########
I : 2
Enernst : -2915.9064000000003 V
Eta Activation : -5970.253342221295 V
Eta Concentration : 3.9490801543151313 V
Eta Ohmic : 0.21725850475910816 V
Loss : -5966.08700356222 V
PEM Efficiency : 1955.2439766424486
Power : 6100.36120712444 W
Power-Stack : 6100.36120712444 W
Power-Thermal : -6097.90120712444 W
VStack : 3050.18060356222 V
Vcell : 3050.18060356222 V
###########
I : 4
Enernst : -2915.9064000000003 V
Eta Activation : -5511.099566700011 V
Eta Concentration : 8.00651611141284 V
Eta Ohmic : 2.4703467982605276 V
Loss : -5500.622703790337 V
PEM Efficiency : 1656.8694255066262
Power : 10338.865215161348 W
Power-Stack : 10338.865215161348 W
Power-Thermal : -10333.945215161348 W
VStack : 2584.716303790337 V
Vcell : 2584.716303790337 V
###########
Report is generating ...
Warning : The value of I(>0) leads to minus amount of V, please check your inputs
Done!
>>> sorted(os.listdir("Amphlett")) == ['test1.csv', 'test1.html', 'test1.opem']
True
>>> Test_Vector={"T":3432222.15,"PH2":1,"PO2":1,"i-start":5,"i-stop":0,"i-step":-2,"A":50.6,"l":0.0178,"lambda":23,"N":1,"R":0,"JMax":1.5,"Name":"test2"}
>>> Amphlett_Data=Static_Analysis(InputMethod=Test_Vector,TestMode=True,PrintMode=False,Folder=os.path.join(os.getcwd(), "Folder_Test"))
>>> sorted(os.listdir(os.path.join("Folder_Test", "Amphlett"))) == ['test2.csv', 'test2.html', 'test2.opem']
True
>>> shutil.rmtree("Amphlett")
>>> shutil.rmtree("Folder_Test")

'''
