# -*- coding: utf-8 -*-
'''
>>> import os
>>> from math import isclose
>>> from opem.Dynamic.Padulles_Hauer import *
>>> import shutil
>>> ABS_TOL = 1e-12
>>> REL_TOL = 0
>>> Test_Vector={"T":343,"E0":0.6,"N0":5,"KO2":0.0000211,"KH2":0.0000422,"KH2O":0.000007716,"tH2":3.37,"tO2":6.74,"t1":2,"t2":2,"tH2O":18.418,"B":0.04777,"C":0.0136,"Rint":0.00303,"rho":1.168,"qMethanol":0.0002,"CV":2,"i-start":0.1,"i-stop":4,"i-step":0.1,"Name":"test1"}
>>> Padulles_Hauer_Data=Dynamic_Analysis(InputMethod=Test_Vector, TestMode=True)
###########
Padulles-Hauer-Model Simulation
###########
Analyzing . . .
I : 0.1
E : 2.9234154992732004 V
FC Efficiency : 0.41518043908246366
FC Power : 0.3238407424843217 W
FC Voltage : 3.2384074248432166 V
PH2 : 0.19717074233280188 atm
PH2O : 0.2426831613626925 atm
PO2 : 0.1906263686382979 atm
Power-Thermal : 0.2911592575156784 W
###########
I : 0.2
E : 2.9234139617015558 V
FC Efficiency : 0.4108963136482338
FC Power : 0.6409982492912448 W
FC Voltage : 3.204991246456224 V
PH2 : 0.1971566919511875 atm
PH2O : 0.24266586776736396 atm
PO2 : 0.1906184358000996 atm
Power-Thermal : 0.5890017507087553 W
###########
I : 0.3
E : 2.9234124240659227 V
FC Efficiency : 0.4083740564879825
FC Power : 0.955595292181879 W
FC Voltage : 3.1853176406062635 V
PH2 : 0.19714264156957312 atm
PH2O : 0.24264857417203542 atm
PO2 : 0.1906105029619013 atm
Power-Thermal : 0.889404707818121 W
###########
I : 0.4
E : 2.9234108863662946 V
FC Efficiency : 0.4065731449109761
FC Power : 1.2685082121222457 W
FC Voltage : 3.171270530305614 V
PH2 : 0.19712859118795872 atm
PH2O : 0.24263128057670688 atm
PO2 : 0.19060257012370302 atm
Power-Thermal : 1.1914917878777547 W
###########
I : 0.5
E : 2.9234093486026658 V
FC Efficiency : 0.4051674903968853
FC Power : 1.5801532125478528 W
FC Voltage : 3.1603064250957056 V
PH2 : 0.19711454080634436 atm
PH2O : 0.24261398698137834 atm
PO2 : 0.1905946372855047 atm
Power-Thermal : 1.4948467874521474 W
###########
I : 0.6
E : 2.923407810775032 V
FC Efficiency : 0.4040118444230801
FC Power : 1.8907754319000147 W
FC Voltage : 3.1512923865000246 V
PH2 : 0.19710049042472996 atm
PH2O : 0.2425966933860498 atm
PO2 : 0.1905867044473064 atm
Power-Thermal : 1.7992245680999854 W
###########
I : 0.7
E : 2.923406272883388 V
FC Efficiency : 0.4030287270042349
FC Power : 2.2005368494431226 W
FC Voltage : 3.1436240706330323 V
PH2 : 0.19708644004311557 atm
PH2O : 0.24257939979072127 atm
PO2 : 0.19057877160910808 atm
Power-Thermal : 2.1044631505568776 W
###########
I : 0.8
E : 2.9234047349277277 V
FC Efficiency : 0.4021718894938075
FC Power : 2.509552590441359 W
FC Voltage : 3.1369407380516985 V
PH2 : 0.19707238966150117 atm
PH2O : 0.24256210619539273 atm
PO2 : 0.1905708387709098 atm
Power-Thermal : 2.4104474095586417 W
###########
I : 0.9
E : 2.9234031969080454 V
FC Efficiency : 0.4014115005665013
FC Power : 2.81790873397684 W
FC Voltage : 3.1310097044187106 V
PH2 : 0.19705833927988675 atm
PH2O : 0.24254481260006414 atm
PO2 : 0.19056290593271147 atm
Power-Thermal : 2.7170912660231608 W
###########
I : 1.0
E : 2.9234016588243374 V
FC Efficiency : 0.40072719160282416
FC Power : 3.1256720945020287 W
FC Voltage : 3.1256720945020287 V
PH2 : 0.19704428889827239 atm
PH2O : 0.2425275190047356 atm
PO2 : 0.1905549730945132 atm
Power-Thermal : 3.0243279054979717 W
###########
I : 1.1
E : 2.9234001206765963 V
FC Efficiency : 0.40010443449551725
FC Power : 3.4328960479715387 W
FC Voltage : 3.1208145890650347 V
PH2 : 0.197030238516658 atm
PH2O : 0.24251022540940706 atm
PO2 : 0.19054704025631486 atm
Power-Thermal : 3.3321039520284623 W
###########
I : 1.2
E : 2.9233985824648183 V
FC Efficiency : 0.39953250222749515
FC Power : 3.7396242208493544 W
FC Voltage : 3.116353517374462 V
PH2 : 0.1970161881350436 atm
PH2O : 0.24249293181407852 atm
PO2 : 0.19053910741811658 atm
Power-Thermal : 3.640375779150646 W
###########
I : 1.3
E : 2.923397044188998 V
FC Efficiency : 0.3990032485837277
FC Power : 4.045892940639 W
FC Voltage : 3.1122253389530767 V
PH2 : 0.19700213775342923 atm
PH2O : 0.24247563821874998 atm
PO2 : 0.19053117457991825 atm
Power-Thermal : 3.9491070593610007 W
###########
I : 1.4
E : 2.923395505849129 V
FC Efficiency : 0.3985103413824903
FC Power : 4.351732927896794 W
FC Voltage : 3.1083806627834245 V
PH2 : 0.19698808737181484 atm
PH2O : 0.24245834462342142 atm
PO2 : 0.19052324174171997 atm
Power-Thermal : 4.258267072103206 W
###########
I : 1.5
E : 2.923393967445207 V
FC Efficiency : 0.3980487608857143
FC Power : 4.657170502362857 W
FC Voltage : 3.1047803349085714 V
PH2 : 0.19697403699020044 atm
PH2O : 0.24244105102809288 atm
PO2 : 0.19051530890352164 atm
Power-Thermal : 4.567829497637144 W
###########
I : 1.6
E : 2.923392428977226 V
FC Efficiency : 0.39761446042126253
FC Power : 4.962228466057358 W
FC Voltage : 3.101392791285848 V
PH2 : 0.19695998660858605 atm
PH2O : 0.24242375743276434 atm
PO2 : 0.19050737606532336 atm
Power-Thermal : 4.877771533942644 W
###########
I : 1.7
E : 2.9233908904451815 V
FC Efficiency : 0.3972041300730298
FC Power : 5.2669267647683755 W
FC Voltage : 3.098192214569633 V
PH2 : 0.19694593622697168 atm
PH2O : 0.2424064638374358 atm
PO2 : 0.19049944322712503 atm
Power-Thermal : 5.188073235231625 W
###########
I : 1.8
E : 2.9233893518490675 V
FC Efficiency : 0.39681502801851076
FC Power : 5.571282993379892 W
FC Voltage : 3.0951572185443843 V
PH2 : 0.19693188584535729 atm
PH2O : 0.24238917024210727 atm
PO2 : 0.19049151038892673 atm
Power-Thermal : 5.498717006620109 W
###########
I : 1.9
E : 2.9233878131888784 V
FC Efficiency : 0.3964448575287326
FC Power : 5.875312788575817 W
FC Voltage : 3.0922698887241142 V
PH2 : 0.1969178354637429 atm
PH2O : 0.24237187664677873 atm
PO2 : 0.19048357755072845 atm
Power-Thermal : 5.809687211424183 W
###########
I : 2.0
E : 2.9233862744646095 V
FC Efficiency : 0.3960916755547374
FC Power : 6.1790301386539035 W
FC Voltage : 3.0895150693269517 V
PH2 : 0.19690378508212852 atm
PH2O : 0.2423545830514502 atm
PO2 : 0.19047564471253012 atm
Power-Thermal : 6.120969861346097 W
###########
I : 2.1
E : 2.923384735676255 V
FC Efficiency : 0.39575382364054146
FC Power : 6.482447631232071 W
FC Voltage : 3.086879824396224 V
PH2 : 0.19688973470051413 atm
PH2O : 0.24233728945612165 atm
PO2 : 0.19046771187433184 atm
Power-Thermal : 6.432552368767931 W
###########
I : 2.2
E : 2.92338319682381 V
FC Efficiency : 0.3954298749226794
FC Power : 6.78557665367318 W
FC Voltage : 3.0843530243968997 V
PH2 : 0.19687568431889974 atm
PH2O : 0.2423199958607931 atm
PO2 : 0.1904597790361335 atm
Power-Thermal : 6.744423346326822 W
###########
I : 2.3
E : 2.923381657907269 V
FC Efficiency : 0.39511859292081414
FC Power : 7.088427556999405 W
FC Voltage : 3.0819250247823504 V
PH2 : 0.19686163393728537 atm
PH2O : 0.24230270226546458 atm
PO2 : 0.19045184619793523 atm
Power-Thermal : 7.0565724430005945 W
###########
I : 2.4
E : 2.9233801189266266 V
FC Efficiency : 0.39481889910524637
FC Power : 7.391009791250212 W
FC Voltage : 3.079587413020922 V
PH2 : 0.19684758355567097 atm
PH2O : 0.242285408670136 atm
PO2 : 0.1904439133597369 atm
Power-Thermal : 7.368990208749787 W
###########
I : 2.5
E : 2.923378579881877 V
FC Efficiency : 0.39452984708947947
FC Power : 7.693332018244849 W
FC Voltage : 3.07733280729794 V
PH2 : 0.19683353317405658 atm
PH2O : 0.24226811507480747 atm
PO2 : 0.19043598052153862 atm
Power-Thermal : 7.681667981755151 W
###########
I : 2.6
E : 2.923377040773016 V
FC Efficiency : 0.39425060188740335
FC Power : 7.995402206276542 W
FC Voltage : 3.0751546947217467 V
PH2 : 0.19681948279244216 atm
PH2O : 0.2422508214794789 atm
PO2 : 0.1904280476833403 atm
Power-Thermal : 7.99459779372346 W
###########
I : 2.7
E : 2.923375501600037 V
FC Efficiency : 0.3939804230873111
FC Power : 8.297227710218774 W
FC Voltage : 3.073047300081027 V
PH2 : 0.19680543241082776 atm
PH2O : 0.24223352788415034 atm
PO2 : 0.190420114845142 atm
Power-Thermal : 8.307772289781228 W
###########
I : 2.8
E : 2.923373962362936 V
FC Efficiency : 0.3937186510874208
FC Power : 8.59881533974927 W
FC Voltage : 3.0710054784818825 V
PH2 : 0.1967913820292134 atm
PH2O : 0.2422162342888218 atm
PO2 : 0.19041218200694368 atm
Power-Thermal : 8.62118466025073 W
###########
I : 2.9
E : 2.9233724230617057 V
FC Efficiency : 0.3934646957478549
FC Power : 8.900171417816479 W
FC Voltage : 3.0690246268332686 V
PH2 : 0.196777331647599 atm
PH2O : 0.24219894069349326 atm
PO2 : 0.1904042491687454 atm
Power-Thermal : 8.934828582183522 W
###########
I : 3.0
E : 2.923370883696343 V
FC Efficiency : 0.39321802696722546
FC Power : 9.201301831033076 W
FC Voltage : 3.0671006103443585 V
PH2 : 0.1967632812659846 atm
PH2O : 0.24218164709816473 atm
PO2 : 0.19039631633054707 atm
Power-Thermal : 9.248698168966925 W
###########
I : 3.1
E : 2.9233693442668414 V
FC Efficiency : 0.39297816680494896
FC Power : 9.502212073343667 W
FC Voltage : 3.0652297010786023 V
PH2 : 0.19674923088437024 atm
PH2O : 0.2421643535028362 atm
PO2 : 0.1903883834923488 atm
Power-Thermal : 9.562787926656334 W
###########
I : 3.2
E : 2.9233678047731946 V
FC Efficiency : 0.39274468285467545
FC Power : 9.8029072840527 W
FC Voltage : 3.0634085262664685 V
PH2 : 0.19673518050275585 atm
PH2O : 0.24214705990750765 atm
PO2 : 0.19038045065415046 atm
Power-Thermal : 9.877092715947303 W
###########
I : 3.3
E : 2.9233662652153996 V
FC Efficiency : 0.3925171826377131
FC Power : 10.103392281094736 W
FC Voltage : 3.0616340245741624 V
PH2 : 0.19672113012114145 atm
PH2O : 0.2421297663121791 atm
PO2 : 0.19037251781595219 atm
Power-Thermal : 10.191607718905265 W
###########
I : 3.4
E : 2.923364725593449 V
FC Efficiency : 0.39229530883366054
FC Power : 10.403671590268678 W
FC Voltage : 3.059903408902552 V
PH2 : 0.19670707973952706 atm
PH2O : 0.24211247271685057 atm
PO2 : 0.19036458497775385 atm
Power-Thermal : 10.506328409731324 W
###########
I : 3.5
E : 2.923363185907339 V
FC Efficiency : 0.39207873520256487
FC Power : 10.703749471030022 W
FC Voltage : 3.0582141345800062 V
PH2 : 0.1966930293579127 atm
PH2O : 0.24209517912152204 atm
PO2 : 0.19035665213955555 atm
Power-Thermal : 10.82125052896998 W
###########
I : 3.6
E : 2.923361646157063 V
FC Efficiency : 0.3918671630816706
FC Power : 11.003629939333312 W
FC Voltage : 3.0565638720370307 V
PH2 : 0.1966789789762983 atm
PH2O : 0.2420778855261935 atm
PO2 : 0.19034871930135727 atm
Power-Thermal : 11.13637006066669 W
###########
I : 3.7
E : 2.923360106342616 V
FC Efficiency : 0.3916603183622587
FC Power : 11.303316787934786 W
FC Voltage : 3.054950483225618 V
PH2 : 0.1966649285946839 atm
PH2O : 0.24206059193086493 atm
PO2 : 0.19034078646315894 atm
Power-Thermal : 11.451683212065214 W
###########
I : 3.8
E : 2.9233585664639925 V
FC Efficiency : 0.3914579488697281
FC Power : 11.602813604498742 W
FC Voltage : 3.0533720011838796 V
PH2 : 0.19665087821306954 atm
PH2O : 0.2420432983355364 atm
PO2 : 0.19033285362496066 atm
Power-Thermal : 11.767186395501259 W
###########
I : 3.9
E : 2.9233570265211877 V
FC Efficiency : 0.3912598220840501
FC Power : 11.902123787796803 W
FC Voltage : 3.051826612255591 V
PH2 : 0.19663682783145514 atm
PH2O : 0.24202600474020786 atm
PO2 : 0.19032492078676233 atm
Power-Thermal : 12.082876212203196 W
###########
Report is generating ...
Done!
>>> Padulles_Hauer_Data["Status"]
True
>>> assert isclose(Padulles_Hauer_Data["P"][5], 1.8907754319000147, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(Padulles_Hauer_Data["I"][5], 0.6, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(Padulles_Hauer_Data["V"][5], 3.1512923865000246, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(Padulles_Hauer_Data["EFF"][5], 0.4040118444230801, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(Padulles_Hauer_Data["PO2"][5], 0.1905867044473064, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(Padulles_Hauer_Data["PH2"][5], 0.19710049042472996, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(Padulles_Hauer_Data["PH2O"][5], 0.2425966933860498, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(Padulles_Hauer_Data["Ph"][5], 1.7992245680999854, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(Padulles_Hauer_Data["V0"], 3.1748727715256186, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(Padulles_Hauer_Data["K"], -0.03643090556526363, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(Padulles_Hauer_Data["VE"][5], 3.1530142281864606, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> Padulles_Hauer_Data=Dynamic_Analysis(InputMethod={}, TestMode=True,PrintMode=False)
>>> Padulles_Hauer_Data["Status"]
False
>>> qH2_Calc(qMethanol=None,CV=2,t1=2,t2=2)
[Error] qH2 Calculation Failed (qMethanol:None, CV:2, t1:2, t2:2)
>>> Test_Vector={"T":2,"E0":-0.6,"N0":5,"KO2":0.0000211,"KH2":0.0000422,"KH2O":0.000007716,"tH2":3.37,"tO2":6.74,"t1":2,"t2":2,"tH2O":18.418,"B":0.04777,"C":0.0136,"Rint":0.00303,"rho":1.168,"qMethanol":0.0002,"CV":2,"i-start":4,"i-stop":0.1,"i-step":-2,"Name":"test1"}
>>> Padulles_Hauer_Data=Dynamic_Analysis(InputMethod=Test_Vector, TestMode=True)
###########
Padulles-Hauer-Model Simulation
###########
Analyzing . . .
I : 0.1
E : -3.00044655685555 V
FC Efficiency : -0.3442890552930171
FC Power : -0.2685454631285534 W
FC Voltage : -2.6854546312855336 V
PH2 : 0.19717074233280188 atm
PH2O : 0.2426831613626925 atm
PO2 : 0.1906263686382979 atm
Power-Thermal : 0.8835454631285535 W
###########
I : 2.0
E : -3.000446727262597 V
FC Efficiency : -0.3633740938974685
FC Power : -5.6686358648005095 W
FC Voltage : -2.8343179324002548 V
PH2 : 0.19690378508212852 atm
PH2O : 0.2423545830514502 atm
PO2 : 0.19047564471253012 atm
Power-Thermal : 17.96863586480051 W
###########
Report is generating ...
Warning : The value of I(>0.1) leads to minus amount of V, please check your inputs
Done!
>>> sorted(os.listdir("Padulles-Hauer")) == ['test1.csv', 'test1.html', 'test1.opem']
True
>>> Test_Vector={"T":2,"E0":-0.6,"N0":5,"KO2":0.0000211,"KH2":0.0000422,"KH2O":0.000007716,"tH2":3.37,"tO2":6.74,"t1":2,"t2":2,"tH2O":18.418,"B":0.04777,"C":0.0136,"Rint":0.00303,"rho":1.168,"qMethanol":0.0002,"CV":2,"i-start":4,"i-stop":0.1,"i-step":-2,"Name":"test2"}
>>> Padulles_Hauer_Data=Dynamic_Analysis(InputMethod=Test_Vector, TestMode=True, PrintMode=False, Folder=os.path.join(os.getcwd(), "Folder_Test"))
>>> sorted(os.listdir(os.path.join("Folder_Test", "Padulles-Hauer"))) == ['test2.csv', 'test2.html', 'test2.opem']
True
>>> shutil.rmtree("Padulles-Hauer")
>>> shutil.rmtree("Folder_Test")

'''
