# -*- coding: utf-8 -*-
'''
>>> import coverage
>>> from opem.Amphlett import *
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
>>> PowerStack_Calc(2,2)
4
>>> PowerStack_Calc(None,2)
[Error] Power Stack Calculation Error
>>> T='20000000000'
>>> PH2='10000000'
>>> PO2='1000000000'
>>> i='160000000'
>>> A='30000000000'
>>> l='50000000000'
>>> lambda_param='50000000000'
>>> N='80000000000'
>>> Enernst_Calc(T,PH2,PO2)
[Error] Enernst Calculation Failed
>>> CH2_Calc(PH2,T)
[Error] CH2 Calculation Failed
>>> CO2_Calc(PO2,T)
[Error] CO2 Calculation Failed
>>> Rho_Calc(i,A,T,lambda_param)
[Error] Rho Calculation Failed
>>> Xi2_Calc(A,PH2,T)
[Error] CH2 Calculation Failed
[Error] Xi2 Calculation Failed
>>> Eta_Conc_Calc(i,A,Jn,JMax)
[Error] Eta Concentration Calculation Failed
>>> Eta_Ohmic_Calc(i,l,A,T,lambda_param)
[Error] Rho Calculation Failed
[Error] Eta Ohmic Calculation Failed
>>> Eta_Act_Calc(T,PO2,PH2,i,A)
[Error] CO2 Calculation Failed
[Error] CH2 Calculation Failed
[Error] Xi2 Calculation Failed
[Error] Eta Activation Calculation Failed
>>> Efficiency_Calc("11111")
[Error] PEM Efficiency Calculation Failed
>>> VStack_Calc(12,None)
[Error] VStack Calculation Error
>>> Static_Analysis(InputMethod={},TestMode=True)
###########
Amphlett-Model Simulation
###########
Analyzing . . .
[Error] Amphlett Simulation Failed!(Check Your Inputs)
>>> Loss_Calc(122,22,None)
[Error] Loss Calculation Error
>>> Vcell_Calc(122,None)
[Error] Vcell Calculation Error
>>> Power_Calc(122,None)
[Error] Power Calculation Error
>>> Test_Vector={"T":343.15,"PH2":1,"PO2":1,"i-start":0,"i-stop":4,"i-step":0.1,"A":50.6,"l":0.0178,"lambda":23,"N":1,"R":0,"JMax":1.5,"B":0.016}
>>> Static_Analysis(InputMethod=Test_Vector,TestMode=True)
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
VStack : 1.19075 V
Vcell : 1.19075 V
###########
I : 0.1
Enernst : 1.19075 V
Eta Activation : 0.11807074742083559 V
Eta Concentration : 2.109426805213159e-05 V
Eta Ohmic : 0.00017520002843124318 V
Loss : 0.11826704171731897 V
PEM Efficiency : 0.6874890758222313
Power : 0.1072482958282681 W
Power-Stack : 0.1072482958282681 W
VStack : 1.072482958282681 V
Vcell : 1.072482958282681 V
###########
I : 0.2
Enernst : 1.19075 V
Eta Activation : 0.1639764642376006 V
Eta Concentration : 4.221638333089875e-05 V
Eta Ohmic : 0.0003505137928660484 V
Loss : 0.16436919441379755 V
PEM Efficiency : 0.6579364138373093
Power : 0.2052761611172405 W
Power-Stack : 0.2052761611172405 W
VStack : 1.0263808055862025 V
Vcell : 1.0263808055862025 V
###########
I : 0.30000000000000004
Enernst : 1.19075 V
Eta Activation : 0.19082958714413273 V
Eta Concentration : 6.336641945755048e-05 V
Eta Ohmic : 0.0005259414221215359 V
Loss : 0.19141889498571182 V
PEM Efficiency : 0.6405968621886462
Power : 0.2997993315042865 W
Power-Stack : 0.2997993315042865 W
VStack : 0.9993311050142881 V
Vcell : 0.9993311050142881 V
###########
I : 0.4
Enernst : 1.19075 V
Eta Activation : 0.20988218105436562 V
Eta Concentration : 8.454445034568427e-05 V
Eta Ohmic : 0.0007014830568214833 V
Loss : 0.21066820856153282 V
PEM Efficiency : 0.628257558614402
Power : 0.3920327165753869 W
Power-Stack : 0.3920327165753869 W
VStack : 0.9800817914384672 V
Vcell : 0.9800817914384672 V
###########
I : 0.5
Enernst : 1.19075 V
Eta Activation : 0.22466052101362555 V
Eta Concentration : 0.00010575055020278165 V
Eta Ohmic : 0.0008771388470514419 V
Loss : 0.22564341041087976 V
PEM Efficiency : 0.618658070249436
Power : 0.4825532947945601 W
Power-Stack : 0.4825532947945601 W
VStack : 0.9651065895891202 V
Vcell : 0.9651065895891202 V
###########
I : 0.6
Enernst : 1.19075 V
Eta Activation : 0.23673530396089773 V
Eta Concentration : 0.00012698479353178086 V
Eta Ohmic : 0.0010529089510685316 V
Loss : 0.23791519770549804 V
PEM Efficiency : 0.610791539932373
Power : 0.5717008813767012 W
Power-Stack : 0.5717008813767012 W
VStack : 0.9528348022945019 V
Vcell : 0.9528348022945019 V
###########
I : 0.7
Enernst : 1.19075 V
Eta Activation : 0.2469443874769634 V
Eta Concentration : 0.000148247255132642 V
Eta Ohmic : 0.001228793534444728 V
Loss : 0.24832142826654077 V
PEM Efficiency : 0.60412087931632
Power : 0.6597000002134213 W
Power-Stack : 0.6597000002134213 W
VStack : 0.9424285717334592 V
Vcell : 0.9424285717334592 V
###########
I : 0.7999999999999999
Enernst : 1.19075 V
Eta Activation : 0.25578789787113065 V
Eta Concentration : 0.00016953801010392253 V
Eta Ohmic : 0.0014047927694433352 V
Loss : 0.2573622286506779 V
PEM Efficiency : 0.5983254944546936
Power : 0.7467102170794576 W
Power-Stack : 0.7467102170794576 W
VStack : 0.933387771349322 V
Vcell : 0.933387771349322 V
###########
I : 0.8999999999999999
Enernst : 1.19075 V
Eta Activation : 0.26358842686742984 V
Eta Concentration : 0.00019085713384438152 V
Eta Ohmic : 0.0015809068345387155 V
Loss : 0.2653601908358129 V
PEM Efficiency : 0.5931985956180685
Power : 0.8328508282477682 W
Power-Stack : 0.8328508282477682 W
VStack : 0.925389809164187 V
Vcell : 0.925389809164187 V
###########
I : 0.9999999999999999
Enernst : 1.19075 V
Eta Activation : 0.2705662378303906 V
Eta Concentration : 0.00021220470205456714 V
Eta Ohmic : 0.001757135914031674 V
Loss : 0.2725355784464768 V
PEM Efficiency : 0.5885989881753353
Power : 0.9182144215535231 W
Power-Stack : 0.9182144215535231 W
VStack : 0.9182144215535232 V
Vcell : 0.9182144215535232 V
###########
I : 1.0999999999999999
Enernst : 1.19075 V
Eta Activation : 0.2768784356529624 V
Eta Concentration : 0.0002335807907384422 V
Eta Ohmic : 0.0019334801977325356 V
Loss : 0.27904549664143335 V
PEM Efficiency : 0.5844259636913889
Power : 1.0028749536944233 W
Power-Stack : 1.0028749536944233 W
VStack : 0.9117045033585667 V
Vcell : 0.9117045033585667 V
###########
I : 1.2
Enernst : 1.19075 V
Eta Activation : 0.28264102077766273 V
Eta Concentration : 0.00025498547620500224 V
Eta Ohmic : 0.002109939880694226 V
Loss : 0.285005946134562 V
PEM Efficiency : 0.5806051627342551
Power : 1.0868928646385256 W
Power-Stack : 1.0868928646385256 W
VStack : 0.905744053865438 V
Vcell : 0.905744053865438 V
###########
I : 1.3
Enernst : 1.19075 V
Eta Activation : 0.28794208521933035 V
Eta Concentration : 0.0002764188350699048 V
Eta Ohmic : 0.002286515162983545 V
Loss : 0.2905050192173838 V
PEM Efficiency : 0.5770801158862924
Power : 1.1703184750174012 W
Power-Stack : 1.1703184750174012 W
VStack : 0.9002449807826162 V
Vcell : 0.9002449807826162 V
###########
I : 1.4000000000000001
Enernst : 1.19075 V
Eta Activation : 0.29285010429372843 V
Eta Concentration : 0.00029788094425712723 V
Eta Ohmic : 0.002463206249482402 V
Loss : 0.29561119148746795 V
PEM Efficiency : 0.5738069285336743
Power : 1.253194331917545 W
Power-Stack : 1.253194331917545 W
VStack : 0.895138808512532 V
Vcell : 0.895138808512532 V
###########
I : 1.5000000000000002
Enernst : 1.19075 V
Eta Activation : 0.2974193607369227 V
Eta Concentration : 0.00031937188100060893 V
Eta Ohmic : 0.0026400133497130485 V
Loss : 0.30037874596763636 V
PEM Efficiency : 0.5707508038668997
Power : 1.3355568810485456 W
Power-Stack : 1.3355568810485456 W
VStack : 0.8903712540323636 V
Vcell : 0.8903712540323636 V
###########
I : 1.6000000000000003
Enernst : 1.19075 V
Eta Activation : 0.3016936146878957 V
Eta Concentration : 0.0003408917228459314 V
Eta Ohmic : 0.0028169366776829123 V
Loss : 0.3048514430884245 V
PEM Efficiency : 0.567883690327933
Power : 1.4174376910585211 W
Power-Stack : 1.4174376910585211 W
VStack : 0.8858985569115755 V
Vcell : 0.8858985569115755 V
###########
I : 1.7000000000000004
Enernst : 1.19075 V
Eta Activation : 0.30570865911032347 V
Eta Concentration : 0.00036244054765199196 V
Eta Ohmic : 0.002993976451745679 V
Loss : 0.30906507610972117 V
PEM Efficiency : 0.5651826435194095
Power : 1.4988643706134743 W
Power-Stack : 1.4988643706134743 W
VStack : 0.8816849238902789 V
Vcell : 0.8816849238902789 V
###########
I : 1.8000000000000005
Enernst : 1.19075 V
Eta Activation : 0.30949414368419487 V
Eta Concentration : 0.00038401843359268825 V
Eta Ohmic : 0.0031711328944759904 V
Loss : 0.3130492950122636 V
PEM Efficiency : 0.5626286570434207
Power : 1.579861268977926 W
Power-Stack : 1.579861268977926 W
VStack : 0.8777007049877363 V
Vcell : 0.8777007049877363 V
###########
I : 1.9000000000000006
Enernst : 1.19075 V
Eta Activation : 0.31307490491112167 V
Eta Concentration : 0.00040562545915863245 V
Eta Ohmic : 0.003348406232555747 V
Loss : 0.316828936602836 V
PEM Efficiency : 0.5602058098699768
Power : 1.660450020454612 W
Power-Stack : 1.660450020454612 W
VStack : 0.8739210633971639 V
Vcell : 0.8739210633971639 V
###########
I : 2.0000000000000004
Enernst : 1.19075 V
Eta Activation : 0.3164719546471556 V
Eta Concentration : 0.0004272617031588504 V
Eta Ohmic : 0.0035257966966703346 V
Loss : 0.32042501304698484 V
PEM Efficiency : 0.5579006326621893
Power : 1.7406499739060308 W
Power-Stack : 1.7406499739060308 W
VStack : 0.8703249869530152 V
Vcell : 0.8703249869530152 V
###########
I : 2.1000000000000005
Enernst : 1.19075 V
Eta Activation : 0.31970322720026056 V
Eta Concentration : 0.0004489272447225199 V
Eta Ohmic : 0.003703304521413452 V
Loss : 0.3238554589663965 V
PEM Efficiency : 0.5557016288676945
Power : 1.8204785361705678 W
Power-Stack : 1.8204785361705678 W
VStack : 0.8668945410336035 V
Vcell : 0.8668945410336035 V
###########
I : 2.2000000000000006
Enernst : 1.19075 V
Eta Activation : 0.32278415246972747 V
Eta Concentration : 0.00047062216330069346 V
Eta Ohmic : 0.0038809299451994465 V
Loss : 0.3271357045782276 V
PEM Efficiency : 0.553598907321649
Power : 1.8999514499278998 W
Power-Stack : 1.8999514499278998 W
VStack : 0.8636142954217724 V
Vcell : 0.8636142954217724 V
###########
I : 2.3000000000000007
Enernst : 1.19075 V
Eta Activation : 0.3257281015786805 V
Eta Concentration : 0.0004923465386680586 V
Eta Ohmic : 0.004058673210182236 V
Loss : 0.33027912132753073 V
PEM Efficiency : 0.5515838965849162
Power : 1.97908302094668 W
Power-Stack : 1.97908302094668 W
VStack : 0.8604708786724693 V
Vcell : 0.8604708786724693 V
###########
I : 2.400000000000001
Enernst : 1.19075 V
Eta Activation : 0.3285467375944278 V
Eta Concentration : 0.0005141004509246927 V
Eta Ohmic : 0.004236534562180055 V
Loss : 0.33329737260753256 V
PEM Efficiency : 0.5496491201233765
Power : 2.0578863057419223 W
Power-Stack : 2.0578863057419223 W
VStack : 0.8574526273924674 V
Vcell : 0.8574526273924674 V
###########
I : 2.500000000000001
Enernst : 1.19075 V
Eta Activation : 0.33125029460641553 V
Eta Concentration : 0.0005358839804978295 V
Eta Ohmic : 0.004414514250605399 V
Loss : 0.33620069283751874 V
PEM Efficiency : 0.5477880174118469
Power : 2.1363732679062037 W
Power-Stack : 2.1363732679062037 W
VStack : 0.8545493071624812 V
Vcell : 0.8545493071624812 V
###########
I : 2.600000000000001
Enernst : 1.19075 V
Eta Activation : 0.33384780203609543 V
Eta Concentration : 0.000557697208143656 V
Eta Ohmic : 0.004592612528399571 V
Loss : 0.33899811177263867 V
PEM Efficiency : 0.5459948001457445
Power : 2.2145549093911403 W
Power-Stack : 2.2145549093911403 W
VStack : 0.8517518882273614 V
Vcell : 0.8517518882273614 V
###########
I : 2.700000000000001
Enernst : 1.19075 V
Eta Activation : 0.336347266590727 V
Eta Concentration : 0.0005795402149490941 V
Eta Ohmic : 0.004770829651971411 V
Loss : 0.3416976364576475 V
PEM Efficiency : 0.5442643356040721
Power : 2.2924413815643527 W
Power-Stack : 2.2924413815643527 W
VStack : 0.8490523635423525 V
Vcell : 0.8490523635423525 V
###########
I : 2.800000000000001
Enernst : 1.19075 V
Eta Activation : 0.3387558211104935 V
Eta Concentration : 0.0006014130823336223 V
Eta Ohmic : 0.004949165881139772 V
Loss : 0.3443064000739669 V
PEM Efficiency : 0.5425920512346366
Power : 2.370042079792894 W
Power-Stack : 2.370042079792894 W
VStack : 0.8464435999260331 V
Vcell : 0.8464435999260331 V
###########
I : 2.9000000000000012
Enernst : 1.19075 V
Eta Activation : 0.3410798472843883 V
Eta Concentration : 0.0006233158920510905 V
Eta Ohmic : 0.0051276214790794 V
Loss : 0.3468307846555188 V
PEM Efficiency : 0.5409738559900521
Power : 2.447365724498997 W
Power-Stack : 2.447365724498997 W
VStack : 0.8439192153444812 V
Vcell : 0.8439192153444812 V
###########
I : 3.0000000000000013
Enernst : 1.19075 V
Eta Activation : 0.34332507755368774 V
Eta Concentration : 0.0006452487261915484 V
Eta Ohmic : 0.00530619671226988 V
Loss : 0.3492765229921492 V
PEM Efficiency : 0.5394060750050325
Power : 2.5244204310235534 W
Power-Stack : 2.5244204310235534 W
VStack : 0.8414734770078508 V
Vcell : 0.8414734770078508 V
###########
I : 3.1000000000000014
Enernst : 1.19075 V
Eta Activation : 0.34549668030011765 V
Eta Concentration : 0.0006672116671831044 V
Eta Ohmic : 0.005484891850447436 V
Loss : 0.35164878381774817 V
PEM Efficiency : 0.5378853949886229
Power : 2.6012137701649816 W
Power-Stack : 2.6012137701649816 W
VStack : 0.8391012161822518 V
Vcell : 0.8391012161822518 V
###########
I : 3.2000000000000015
Enernst : 1.19075 V
Eta Activation : 0.3475993315046607 V
Eta Concentration : 0.0006892047977937692 V
Eta Ohmic : 0.005663707166559282 V
Loss : 0.35395224346901377 V
PEM Efficiency : 0.5364088182890937
Power : 2.677752820899157 W
Power-Stack : 2.677752820899157 W
VStack : 0.8367977565309862 V
Vcell : 0.8367977565309862 V
###########
I : 3.3000000000000016
Enernst : 1.19075 V
Eta Activation : 0.34963727537625955 V
Eta Concentration : 0.0007112282011333409 V
Eta Ohmic : 0.00584264293672037 V
Loss : 0.35619114651411327 V
PEM Efficiency : 0.5349736240294146
Power : 2.7540442165034276 W
Power-Stack : 2.7540442165034276 W
VStack : 0.8345588534858868 V
Vcell : 0.8345588534858868 V
###########
I : 3.4000000000000017
Enernst : 1.19075 V
Eta Activation : 0.3516143759270885 V
Eta Concentration : 0.0007332819606552831 V
Eta Ohmic : 0.006021699440172273 V
Loss : 0.3583693573279161 V
PEM Efficiency : 0.5335773350462076
Power : 2.8300941850850867 W
Power-Stack : 2.8300941850850867 W
VStack : 0.8323806426720839 V
Vcell : 0.8323806426720839 V
###########
I : 3.5000000000000018
Enernst : 1.19075 V
Eta Activation : 0.35353416106975344 V
Eta Concentration : 0.0007553661601586168 V
Eta Ohmic : 0.006200876959244142 V
Loss : 0.36049040418915623 V
PEM Efficiency : 0.5322176896223357
Power : 2.9059085853379547 W
Power-Stack : 2.9059085853379547 W
VStack : 0.8302595958108437 V
Vcell : 0.8302595958108437 V
###########
I : 3.600000000000002
Enernst : 1.19075 V
Eta Activation : 0.35539986050095995 V
Eta Concentration : 0.0007774808837898448 V
Eta Ohmic : 0.006380175779315463 V
Loss : 0.3625575171640653 V
PEM Efficiency : 0.5308926172025222
Power : 2.981492938209366 W
Power-Stack : 2.981492938209366 W
VStack : 0.8281924828359346 V
Vcell : 0.8281924828359346 V
###########
I : 3.700000000000002
Enernst : 1.19075 V
Eta Activation : 0.35721443839354167 V
Eta Concentration : 0.0007996262160448594 V
Eta Ohmic : 0.00655959618878059 V
Loss : 0.3645736607983671 V
PEM Efficiency : 0.5296002174369441
Power : 3.056852455046043 W
Power-Stack : 3.056852455046043 W
VStack : 0.8261763392016328 V
Vcell : 0.8261763392016328 V
###########
I : 3.800000000000002
Enernst : 1.19075 V
Eta Activation : 0.3589806217278867 V
Eta Concentration : 0.000821802241770895 V
Eta Ohmic : 0.006739138479014856 V
Loss : 0.3665415624486725 V
PEM Efficiency : 0.5283387420200817
Power : 3.131992062695046 W
Power-Stack : 3.131992062695046 W
VStack : 0.8242084375513274 V
Vcell : 0.8242084375513274 V
###########
I : 3.900000000000002
Enernst : 1.19075 V
Eta Activation : 0.3607009249426275 V
Eta Concentration : 0.0008440090461684635 V
Eta Ohmic : 0.006918802944342186 V
Loss : 0.3684637369331381 V
PEM Efficiency : 0.527106578889014
Power : 3.206916425960763 W
Power-Stack : 3.206916425960763 W
VStack : 0.8222862630668619 V
Vcell : 0.8222862630668619 V
###########
Done!
>>> from opem.Chamberline_Kim import *
>>> E0=0.982
>>> b=0.0689
>>> R=0.328
>>> m=0.000125
>>> n=9.45
>>> i=1
>>> A=50.0
>>> Vcell_Calc(E0,b,R,m,n,i,A)
1.244827379954939
>>> Test_Vector={"A":50.0,"E0":0.982,"b":0.0689,"R":0.328,"m":0.000125,"n":9.45,"N":1,"i-start":1,"i-stop":4,"i-step":0.1}
>>> Static_Analysis(InputMethod=Test_Vector, TestMode=True)
###########
Chamberline-Kim-Model Simulation
###########
Analyzing . . .
I : 1
PEM Efficiency : 0.797966269201884
Power : 1.244827379954939 W
Power-Stack : 1.244827379954939 W
VStack : 1.244827379954939 V
Vcell : 1.244827379954939 V
###########
I : 1.1
PEM Efficiency : 0.7933343765568479
Power : 1.3613617901715511 W
Power-Stack : 1.3613617901715511 W
VStack : 1.2376016274286827 V
Vcell : 1.2376016274286827 V
###########
I : 1.2000000000000002
PEM Efficiency : 0.7890689791314186
Power : 1.4771371289340158 W
Power-Stack : 1.4771371289340158 W
VStack : 1.230947607445013 V
Vcell : 1.230947607445013 V
###########
I : 1.3000000000000003
PEM Efficiency : 0.7851113286904084
Power : 1.592205774584149 W
Power-Stack : 1.592205774584149 W
VStack : 1.2247736727570373 V
Vcell : 1.2247736727570373 V
###########
I : 1.4000000000000004
PEM Efficiency : 0.7814157591393215
Power : 1.7066120179602786 W
Power-Stack : 1.7066120179602786 W
VStack : 1.2190085842573415 V
Vcell : 1.2190085842573415 V
###########
I : 1.5000000000000004
PEM Efficiency : 0.7779460692405816
Power : 1.8203938020229615 W
Power-Stack : 1.8203938020229615 W
VStack : 1.2135958680153074 V
Vcell : 1.2135958680153074 V
###########
I : 1.6000000000000005
PEM Efficiency : 0.7746730751436158
Power : 1.9335839955584657 W
Power-Stack : 1.9335839955584657 W
VStack : 1.2084899972240406 V
Vcell : 1.2084899972240406 V
###########
I : 1.7000000000000006
PEM Efficiency : 0.771572906202878
Power : 2.046211347250033 W
Power-Stack : 2.046211347250033 W
VStack : 1.2036537336764896 V
Vcell : 1.2036537336764896 V
###########
I : 1.8000000000000007
PEM Efficiency : 0.7686257886450131
Power : 2.158301214515198 W
Power-Stack : 2.158301214515198 W
VStack : 1.1990562302862204 V
Vcell : 1.1990562302862204 V
###########
I : 1.9000000000000008
PEM Efficiency : 0.7658151585364871
Power : 2.2698761299021486 W
Power-Stack : 2.2698761299021486 W
VStack : 1.1946716473169199 V
Vcell : 1.1946716473169199 V
###########
I : 2.000000000000001
PEM Efficiency : 0.7631270025420254
Power : 2.38095624793112 W
Power-Stack : 2.38095624793112 W
VStack : 1.1904781239655595 V
Vcell : 1.1904781239655595 V
###########
I : 2.100000000000001
PEM Efficiency : 0.7605493596935309
Power : 2.4915597023560085 W
Power-Stack : 2.4915597023560085 W
VStack : 1.1864570011219082 V
Vcell : 1.1864570011219082 V
###########
I : 2.200000000000001
PEM Efficiency : 0.7580719391696471
Power : 2.60170289523023 W
Power-Stack : 2.60170289523023 W
VStack : 1.1825922251046495 V
Vcell : 1.1825922251046495 V
###########
I : 2.300000000000001
PEM Efficiency : 0.7556858231082223
Power : 2.7114007333123027 W
Power-Stack : 2.7114007333123027 W
VStack : 1.1788698840488268 V
Vcell : 1.1788698840488268 V
###########
I : 2.4000000000000012
PEM Efficiency : 0.753383232714607
Power : 2.820666823283491 W
Power-Stack : 2.820666823283491 W
VStack : 1.1752778430347872 V
Vcell : 1.1752778430347872 V
###########
I : 2.5000000000000013
PEM Efficiency : 0.7511573421474446
Power : 2.9295136343750356 W
Power-Stack : 2.9295136343750356 W
VStack : 1.1718054537500135 V
Vcell : 1.1718054537500135 V
###########
I : 2.6000000000000014
PEM Efficiency : 0.7490021289286691
Power : 3.037952634934684 W
Power-Stack : 3.037952634934684 W
VStack : 1.168443321128724 V
Vcell : 1.168443321128724 V
###########
I : 2.7000000000000015
PEM Efficiency : 0.7469122526002784
Power : 3.1459944079523745 W
Power-Stack : 3.1459944079523745 W
VStack : 1.1651831140564344 V
Vcell : 1.1651831140564344 V
###########
I : 2.8000000000000016
PEM Efficiency : 0.7448829554595717
Power : 3.253648749447411 W
Power-Stack : 3.253648749447411 W
VStack : 1.1620174105169319 V
Vcell : 1.1620174105169319 V
###########
I : 2.9000000000000017
PEM Efficiency : 0.7429099807210011
Power : 3.360924752781811 W
Power-Stack : 3.360924752781811 W
VStack : 1.1589395699247618 V
Vcell : 1.1589395699247618 V
###########
I : 3.0000000000000018
PEM Efficiency : 0.7409895045575802
Power : 3.4678308813294776 W
Power-Stack : 3.4678308813294776 W
VStack : 1.1559436271098251 V
Vcell : 1.1559436271098251 V
###########
I : 3.100000000000002
PEM Efficiency : 0.7391180792895339
Power : 3.574375031444188 W
Power-Stack : 3.574375031444188 W
VStack : 1.153024203691673 V
Vcell : 1.153024203691673 V
###########
I : 3.200000000000002
PEM Efficiency : 0.7372925855955156
Power : 3.680564587292816 W
Power-Stack : 3.680564587292816 W
VStack : 1.1501764335290043 V
Vcell : 1.1501764335290043 V
###########
I : 3.300000000000002
PEM Efficiency : 0.7355101920796727
Power : 3.7864064688261574 W
Power-Stack : 3.7864064688261574 W
VStack : 1.1473958996442895 V
Vcell : 1.1473958996442895 V
###########
I : 3.400000000000002
PEM Efficiency : 0.7337683208763324
Power : 3.8919071739280695 W
Power-Stack : 3.8919071739280695 W
VStack : 1.1446785805670785 V
Vcell : 1.1446785805670785 V
###########
I : 3.500000000000002
PEM Efficiency : 0.7320646182417239
Power : 3.9970728155998145 W
Power-Stack : 3.9970728155998145 W
VStack : 1.1420208044570892 V
Vcell : 1.1420208044570892 V
###########
I : 3.6000000000000023
PEM Efficiency : 0.7303969292894269
Power : 4.101909154889425 W
Power-Stack : 4.101909154889425 W
VStack : 1.1394192096915061 V
Vcell : 1.1394192096915061 V
###########
I : 3.7000000000000024
PEM Efficiency : 0.7287632761880597
Power : 4.206421630157483 W
Power-Stack : 4.206421630157483 W
VStack : 1.136870710853373 V
Vcell : 1.136870710853373 V
###########
I : 3.8000000000000025
PEM Efficiency : 0.7271618392669932
Power : 4.310615383174739 W
Power-Stack : 4.310615383174739 W
VStack : 1.1343724692565096 V
Vcell : 1.1343724692565096 V
###########
I : 3.9000000000000026
PEM Efficiency : 0.7255909405767029
Power : 4.414495282468664 W
Power-Stack : 4.414495282468664 W
VStack : 1.1319218672996567 V
Vcell : 1.1319218672996567 V
###########
Done!
>>> cov.stop()
>>> cov.save()

'''