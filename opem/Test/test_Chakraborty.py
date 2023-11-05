# -*- coding: utf-8 -*-
'''
>>> from opem.Dynamic.Chakraborty import *
>>> import shutil
>>> Test_Vector=Chakraborty_Standard_Vector = {"T": 1273,"E0": 0.6,"u":0.8,"N0": 1,"R": 3.28125 * 10**(-3),"KH2O": 0.000281,"KH2": 0.000843,"KO2": 0.00252,"rho": 1.145,"i-start": 245,"i-stop": 250,"i-step": 0.1,"Name": "test1"}
>>> Chakraborty_Data=Dynamic_Analysis(InputMethod=Test_Vector, TestMode=True)
###########
Chakraborty-Model Simulation
###########
Analyzing . . .
I : 245
E : 0.9589329253950547 V
FC Efficiency : 0.16512718339048205
FC Power : 74.94503627156266 W
FC Voltage : 0.30589810723086797 V
Nernst Gain : 0.1508714318358132 V
Ohmic Loss : 0.8039062499999999 V
PH2 : 0.0003765221431694977 atm
PH2O : 0.004518265718033972 atm
PO2 : 0.000298113305515704 atm
Power-Thermal : 226.40496372843734 W
###########
I : 245.1
E : 0.9589217338439697 V
FC Efficiency : 0.16495005788440917
FC Power : 74.89520264478574 W
FC Voltage : 0.30556998223086795 V
Nernst Gain : 0.15088262338689823 V
Ohmic Loss : 0.804234375 V
PH2 : 0.0003766758256769138 atm
PH2O : 0.004520109908122966 atm
PO2 : 0.00029823498441591454 atm
Power-Thermal : 226.57779735521424 W
###########
I : 245.2
E : 0.9589105468580699 V
FC Efficiency : 0.16477293237833635
FC Power : 74.84530339300885 W
FC Voltage : 0.30524185723086805 V
Nernst Gain : 0.15089381037279812 V
Ohmic Loss : 0.8045625 V
PH2 : 0.00037682950818432987 atm
PH2O : 0.004521954098211959 atm
PO2 : 0.000298356663316125 atm
Power-Thermal : 226.75069660699114 W
###########
I : 245.3
E : 0.9588993644336321 V
FC Efficiency : 0.16459580687226336
FC Power : 74.79533851623188 W
FC Voltage : 0.3049137322308678 V
Nernst Gain : 0.1509049927972357 V
Ohmic Loss : 0.804890625 V
PH2 : 0.0003769831906917461 atm
PH2O : 0.004523798288300953 atm
PO2 : 0.00029847834221633553 atm
Power-Thermal : 226.92366148376814 W
###########
I : 245.4
E : 0.9588881865669385 V
FC Efficiency : 0.16441868136619053
FC Power : 74.74530801445499 W
FC Voltage : 0.3045856072308679 V
Nernst Gain : 0.15091617066392937 V
Ohmic Loss : 0.80521875 V
PH2 : 0.0003771368731991622 atm
PH2O : 0.0045256424783899464 atm
PO2 : 0.000298600021116546 atm
Power-Thermal : 227.09669198554502 W
###########
I : 245.5
E : 0.958877013254275 V
FC Efficiency : 0.16424155586011763
FC Power : 74.69521188767807 W
FC Voltage : 0.3042574822308679 V
Nernst Gain : 0.1509273439765929 V
Ohmic Loss : 0.805546875 V
PH2 : 0.0003772905557065783 atm
PH2O : 0.0045274866684789404 atm
PO2 : 0.0002987217000167565 atm
Power-Thermal : 227.26978811232192 W
###########
I : 245.6
E : 0.9588658444919324 V
FC Efficiency : 0.1640644303540448
FC Power : 74.64505013590119 W
FC Voltage : 0.303929357230868 V
Nernst Gain : 0.15093851273893555 V
Ohmic Loss : 0.8058749999999999 V
PH2 : 0.0003774442382139944 atm
PH2O : 0.004529330858567933 atm
PO2 : 0.00029884337891696695 atm
Power-Thermal : 227.4429498640988 W
###########
I : 245.7
E : 0.9588546802762059 V
FC Efficiency : 0.16388730484797195
FC Power : 74.59482275912426 W
FC Voltage : 0.303601232230868 V
Nernst Gain : 0.15094967695466197 V
Ohmic Loss : 0.8062031249999999 V
PH2 : 0.00037759792072141054 atm
PH2O : 0.004531175048656927 atm
PO2 : 0.00029896505781717747 atm
Power-Thermal : 227.61617724087571 W
###########
I : 245.8
E : 0.9588435206033954 V
FC Efficiency : 0.163710179341899
FC Power : 74.54452975734732 W
FC Voltage : 0.30327310723086787 V
Nernst Gain : 0.15096083662747245 V
Ohmic Loss : 0.80653125 V
PH2 : 0.0003777516032288267 atm
PH2O : 0.004533019238745921 atm
PO2 : 0.000299086736717388 atm
Power-Thermal : 227.7894702426527 W
###########
I : 245.9
E : 0.9588323654698052 V
FC Efficiency : 0.16353305383582611
FC Power : 74.49417113057041 W
FC Voltage : 0.30294498223086785 V
Nernst Gain : 0.1509719917610626 V
Ohmic Loss : 0.8068593749999999 V
PH2 : 0.0003779052857362428 atm
PH2O : 0.004534863428834914 atm
PO2 : 0.00029920841561759847 atm
Power-Thermal : 227.9628288694296 W
###########
I : 246.0
E : 0.9588212148717443 V
FC Efficiency : 0.1633559283297533
FC Power : 74.44374687879352 W
FC Voltage : 0.30261685723086795 V
Nernst Gain : 0.1509831423591236 V
Ohmic Loss : 0.8071875 V
PH2 : 0.0003780589682436589 atm
PH2O : 0.004536707618923907 atm
PO2 : 0.00029933009451780894 atm
Power-Thermal : 228.13625312120647 W
###########
I : 246.1
E : 0.9588100688055257 V
FC Efficiency : 0.1631788028236804
FC Power : 74.3932570020166 W
FC Voltage : 0.30228873223086794 V
Nernst Gain : 0.1509942884253422 V
Ohmic Loss : 0.807515625 V
PH2 : 0.00037821265075107505 atm
PH2O : 0.004538551809012901 atm
PO2 : 0.0002994517734180194 atm
Power-Thermal : 228.3097429979834 W
###########
I : 246.2
E : 0.9587989272674675 V
FC Efficiency : 0.1630016773176076
FC Power : 74.34270150023971 W
FC Voltage : 0.30196060723086804 V
Nernst Gain : 0.1510054299634005 V
Ohmic Loss : 0.80784375 V
PH2 : 0.0003783663332584911 atm
PH2O : 0.004540395999101894 atm
PO2 : 0.00029957345231822994 atm
Power-Thermal : 228.48329849976028 W
###########
I : 246.3
E : 0.9587877902538917 V
FC Efficiency : 0.16282455181153463
FC Power : 74.29208037346277 W
FC Voltage : 0.3016324822308679 V
Nernst Gain : 0.15101656697697616 V
Ohmic Loss : 0.808171875 V
PH2 : 0.0003785200157659073 atm
PH2O : 0.004542240189190888 atm
PO2 : 0.00029969513121844046 atm
Power-Thermal : 228.65691962653725 W
###########
I : 246.4
E : 0.9587766577611254 V
FC Efficiency : 0.16264742630546178
FC Power : 74.24139362168586 W
FC Voltage : 0.3013043572308679 V
Nernst Gain : 0.1510276994697425 V
Ohmic Loss : 0.8085 V
PH2 : 0.0003786736982733234 atm
PH2O : 0.004544084379279881 atm
PO2 : 0.00029981681011865093 atm
Power-Thermal : 228.83060637831414 W
###########
I : 246.5
E : 0.9587655297854997 V
FC Efficiency : 0.16247030079938887
FC Power : 74.19064124490893 W
FC Voltage : 0.3009762322308679 V
Nernst Gain : 0.1510388274453682 V
Ohmic Loss : 0.808828125 V
PH2 : 0.00037882738078073955 atm
PH2O : 0.004545928569368874 atm
PO2 : 0.0002999384890188614 atm
Power-Thermal : 229.00435875509106 W
###########
I : 246.6
E : 0.9587544063233504 V
FC Efficiency : 0.1622931752933161
FC Power : 74.13982324313207 W
FC Voltage : 0.3006481072308681 V
Nernst Gain : 0.15104995090751758 V
Ohmic Loss : 0.8091562499999999 V
PH2 : 0.0003789810632881556 atm
PH2O : 0.004547772759457868 atm
PO2 : 0.0003000601679190719 atm
Power-Thermal : 229.1781767568679 W
###########
I : 246.7
E : 0.9587432873710175 V
FC Efficiency : 0.16211604978724317
FC Power : 74.08893961635512 W
FC Voltage : 0.300319982230868 V
Nernst Gain : 0.1510610698598504 V
Ohmic Loss : 0.8094843749999999 V
PH2 : 0.0003791347457955718 atm
PH2O : 0.0045496169495468615 atm
PO2 : 0.0003001818468192824 atm
Power-Thermal : 229.35206038364487 W
###########
I : 246.8
E : 0.9587321729248458 V
FC Efficiency : 0.16193892428117024
FC Power : 74.03799036457819 W
FC Voltage : 0.29999185723086785 V
Nernst Gain : 0.15107218430602212 V
Ohmic Loss : 0.8098125 V
PH2 : 0.0003792884283029879 atm
PH2O : 0.004551461139635855 atm
PO2 : 0.00030030352571949287 atm
Power-Thermal : 229.52600963542181 W
###########
I : 246.9
E : 0.9587210629811843 V
FC Efficiency : 0.16176179877509742
FC Power : 73.9869754878013 W
FC Voltage : 0.29966373223086795 V
Nernst Gain : 0.1510832942496836 V
Ohmic Loss : 0.810140625 V
PH2 : 0.00037944211081040406 atm
PH2O : 0.004553305329724849 atm
PO2 : 0.0003004252046197034 atm
Power-Thermal : 229.7000245121987 W
###########
I : 247.0
E : 0.9587099575363865 V
FC Efficiency : 0.16158467326902454
FC Power : 73.93589498602438 W
FC Voltage : 0.29933560723086794 V
Nernst Gain : 0.15109439969448132 V
Ohmic Loss : 0.81046875 V
PH2 : 0.0003795957933178201 atm
PH2O : 0.004555149519813842 atm
PO2 : 0.00030054688351991387 atm
Power-Thermal : 229.87410501397562 W
###########
I : 247.1
E : 0.9586988565868104 V
FC Efficiency : 0.1614075477629516
FC Power : 73.88474885924744 W
FC Voltage : 0.2990074822308678 V
Nernst Gain : 0.1511055006440574 V
Ohmic Loss : 0.810796875 V
PH2 : 0.0003797494758252363 atm
PH2O : 0.004556993709902835 atm
PO2 : 0.00030066856242012434 atm
Power-Thermal : 230.04825114075254 W
###########
I : 247.2
E : 0.9586877601288184 V
FC Efficiency : 0.16123042225687878
FC Power : 73.83353710747055 W
FC Voltage : 0.2986793572308679 V
Nernst Gain : 0.15111659710204947 V
Ohmic Loss : 0.811125 V
PH2 : 0.00037990315833265234 atm
PH2O : 0.004558837899991829 atm
PO2 : 0.0003007902413203348 atm
Power-Thermal : 230.22246289252945 W
###########
I : 247.3
E : 0.9586766681587771 V
FC Efficiency : 0.16105329675080587
FC Power : 73.78225973069364 W
FC Voltage : 0.2983512322308679 V
Nernst Gain : 0.15112768907209082 V
Ohmic Loss : 0.811453125 V
PH2 : 0.0003800568408400685 atm
PH2O : 0.004560682090080823 atm
PO2 : 0.00030091192022054533 atm
Power-Thermal : 230.39674026930638 W
###########
I : 247.4
E : 0.9586655806730577 V
FC Efficiency : 0.16087617124473302
FC Power : 73.73091672891671 W
FC Voltage : 0.2980231072308679 V
Nernst Gain : 0.15113877655781016 V
Ohmic Loss : 0.81178125 V
PH2 : 0.0003802105233474846 atm
PH2O : 0.004562526280169815 atm
PO2 : 0.00030103359912075586 atm
Power-Thermal : 230.5710832710833 W
###########
I : 247.5
E : 0.9586544976680359 V
FC Efficiency : 0.16069904573866015
FC Power : 73.6795081021398 W
FC Voltage : 0.2976949822308679 V
Nernst Gain : 0.15114985956283197 V
Ohmic Loss : 0.812109375 V
PH2 : 0.0003803642058549008 atm
PH2O : 0.004564370470258809 atm
PO2 : 0.00030115527802096633 atm
Power-Thermal : 230.7454918978602 W
###########
I : 247.6
E : 0.9586434191400915 V
FC Efficiency : 0.1605219202325873
FC Power : 73.62803385036291 W
FC Voltage : 0.297366857230868 V
Nernst Gain : 0.15116093809077633 V
Ohmic Loss : 0.8124374999999999 V
PH2 : 0.00038051788836231684 atm
PH2O : 0.004566214660347802 atm
PO2 : 0.0003012769569211768 atm
Power-Thermal : 230.91996614963708 W
###########
I : 247.7
E : 0.958632345085609 V
FC Efficiency : 0.16034479472651442
FC Power : 73.576493973586 W
FC Voltage : 0.29703873223086796 V
Nernst Gain : 0.15117201214525883 V
Ohmic Loss : 0.8127656249999999 V
PH2 : 0.000380671570869733 atm
PH2O : 0.0045680588504367955 atm
PO2 : 0.00030139863582138727 atm
Power-Thermal : 231.094506026414 W
###########
I : 247.8
E : 0.9586212755009771 V
FC Efficiency : 0.16016766922044148
FC Power : 73.52488847180905 W
FC Voltage : 0.29671060723086784 V
Nernst Gain : 0.15118308172989076 V
Ohmic Loss : 0.8130937500000001 V
PH2 : 0.0003808252533771491 atm
PH2O : 0.0045699030405257895 atm
PO2 : 0.0003015203147215978 atm
Power-Thermal : 231.26911152819096 W
###########
I : 247.9
E : 0.9586102103825889 V
FC Efficiency : 0.15999054371436866
FC Power : 73.47321734503217 W
FC Voltage : 0.29638248223086794 V
Nernst Gain : 0.15119414684827903 V
Ohmic Loss : 0.813421875 V
PH2 : 0.0003809789358845652 atm
PH2O : 0.0045717472306147835 atm
PO2 : 0.0003016419936218083 atm
Power-Thermal : 231.44378265496783 W
###########
I : 248.0
E : 0.9585991497268418 V
FC Efficiency : 0.15981341820829584
FC Power : 73.42148059325527 W
FC Voltage : 0.29605435723086804 V
Nernst Gain : 0.15120520750402616 V
Ohmic Loss : 0.81375 V
PH2 : 0.00038113261839198135 atm
PH2O : 0.004573591420703776 atm
PO2 : 0.0003017636725220188 atm
Power-Thermal : 231.61851940674472 W
###########
I : 248.1
E : 0.9585880935301375 V
FC Efficiency : 0.1596362927022229
FC Power : 73.36967821647833 W
FC Voltage : 0.2957262322308679 V
Nernst Gain : 0.15121626370073035 V
Ohmic Loss : 0.814078125 V
PH2 : 0.0003812863008993975 atm
PH2O : 0.00457543561079277 atm
PO2 : 0.00030188535142222926 atm
Power-Thermal : 231.79332178352166 W
###########
I : 248.2
E : 0.9585770417888825 V
FC Efficiency : 0.15945916719615008
FC Power : 73.31781021470144 W
FC Voltage : 0.295398107230868 V
Nernst Gain : 0.1512273154419854 V
Ohmic Loss : 0.8144062499999999 V
PH2 : 0.0003814399834068136 atm
PH2O : 0.004577279800881763 atm
PO2 : 0.00030200703032243973 atm
Power-Thermal : 231.96818978529853 W
###########
I : 248.3
E : 0.9585659944994871 V
FC Efficiency : 0.15928204169007715
FC Power : 73.2658765879245 W
FC Voltage : 0.2950699822308679 V
Nernst Gain : 0.1512383627313808 V
Ohmic Loss : 0.814734375 V
PH2 : 0.0003815936659142297 atm
PH2O : 0.004579123990970757 atm
PO2 : 0.00030212870922265026 atm
Power-Thermal : 232.1431234120755 W
###########
I : 248.4
E : 0.9585549516583662 V
FC Efficiency : 0.15910491618400432
FC Power : 73.2138773361476 W
FC Voltage : 0.294741857230868 V
Nernst Gain : 0.15124940557250174 V
Ohmic Loss : 0.8150625 V
PH2 : 0.00038174734842164585 atm
PH2O : 0.004580968181059751 atm
PO2 : 0.00030225038812286073 atm
Power-Thermal : 232.3181226638524 W
###########
I : 248.5
E : 0.9585439132619389 V
FC Efficiency : 0.15892779067793145
FC Power : 73.1618124593707 W
FC Voltage : 0.294413732230868 V
Nernst Gain : 0.151260443968929 V
Ohmic Loss : 0.8153906249999999 V
PH2 : 0.0003819010309290619 atm
PH2O : 0.004582812371148744 atm
PO2 : 0.00030237206702307125 atm
Power-Thermal : 232.4931875406293 W
###########
I : 248.6
E : 0.9585328793066288 V
FC Efficiency : 0.15875066517185857
FC Power : 73.10968195759378 W
FC Voltage : 0.29408560723086796 V
Nernst Gain : 0.1512714779242391 V
Ohmic Loss : 0.8157187499999999 V
PH2 : 0.0003820547134364781 atm
PH2O : 0.004584656561237737 atm
PO2 : 0.0003024937459232817 atm
Power-Thermal : 232.6683180424062 W
###########
I : 248.7
E : 0.9585218497888637 V
FC Efficiency : 0.15857353966578566
FC Power : 73.05748583081686 W
FC Voltage : 0.29375748223086795 V
Nernst Gain : 0.1512825074420042 V
Ohmic Loss : 0.816046875 V
PH2 : 0.0003822083959438942 atm
PH2O : 0.00458650075132673 atm
PO2 : 0.0003026154248234922 atm
Power-Thermal : 232.84351416918312 W
###########
I : 248.8
E : 0.9585108247050758 V
FC Efficiency : 0.1583964141597128
FC Power : 73.00522407903995 W
FC Voltage : 0.29342935723086794 V
Nernst Gain : 0.15129353252579217 V
Ohmic Loss : 0.816375 V
PH2 : 0.00038236207845131036 atm
PH2O : 0.004588344941415724 atm
PO2 : 0.0003027371037237027 atm
Power-Thermal : 233.01877592096005 W
###########
I : 248.9
E : 0.9584998040517012 V
FC Efficiency : 0.1582192886536399
FC Power : 72.95289670226303 W
FC Voltage : 0.2931012322308679 V
Nernst Gain : 0.15130455317916663 V
Ohmic Loss : 0.816703125 V
PH2 : 0.0003825157609587264 atm
PH2O : 0.004590189131504717 atm
PO2 : 0.0003028587826239132 atm
Power-Thermal : 233.19410329773697 W
###########
I : 249.0
E : 0.9584887878251811 V
FC Efficiency : 0.15804216314756703
FC Power : 72.90050370048611 W
FC Voltage : 0.2927731072308679 V
Nernst Gain : 0.15131556940568683 V
Ohmic Loss : 0.81703125 V
PH2 : 0.0003826694434661426 atm
PH2O : 0.0045920333215937114 atm
PO2 : 0.0003029804615241237 atm
Power-Thermal : 233.36949629951388 W
###########
I : 249.1
E : 0.9584777760219602 V
FC Efficiency : 0.15786503764149415
FC Power : 72.84804507370919 W
FC Voltage : 0.2924449822308679 V
Nernst Gain : 0.15132658120890777 V
Ohmic Loss : 0.817359375 V
PH2 : 0.00038282312597355864 atm
PH2O : 0.004593877511682705 atm
PO2 : 0.0003031021404243342 atm
Power-Thermal : 233.54495492629079 W
###########
I : 249.2
E : 0.9584667686384878 V
FC Efficiency : 0.15768791213542133
FC Power : 72.7955208219323 W
FC Voltage : 0.292116857230868 V
Nernst Gain : 0.15133758859238014 V
Ohmic Loss : 0.8176874999999999 V
PH2 : 0.0003829768084809748 atm
PH2O : 0.004595721701771698 atm
PO2 : 0.00030322381932454466 atm
Power-Thermal : 233.72047917806768 W
###########
I : 249.3
E : 0.9584557656712175 V
FC Efficiency : 0.1575107866293484
FC Power : 72.74293094515536 W
FC Voltage : 0.2917887322308679 V
Nernst Gain : 0.15134859155965044 V
Ohmic Loss : 0.818015625 V
PH2 : 0.0003831304909883909 atm
PH2O : 0.004597565891860692 atm
PO2 : 0.0003033454982247552 atm
Power-Thermal : 233.89606905484465 W
###########
I : 249.4
E : 0.9584447671166072 V
FC Efficiency : 0.15733366112327551
FC Power : 72.69027544337845 W
FC Voltage : 0.29146060723086786 V
Nernst Gain : 0.15135959011426076 V
Ohmic Loss : 0.81834375 V
PH2 : 0.0003832841734958071 atm
PH2O : 0.004599410081949685 atm
PO2 : 0.00030346717712496565 atm
Power-Thermal : 234.07172455662155 W
###########
I : 249.5
E : 0.9584337729711189 V
FC Efficiency : 0.1571565356172027
FC Power : 72.63755431660155 W
FC Voltage : 0.29113248223086796 V
Nernst Gain : 0.15137058425974906 V
Ohmic Loss : 0.8186718749999999 V
PH2 : 0.00038343785600322315 atm
PH2O : 0.004601254272038678 atm
PO2 : 0.0003035888560251761 atm
Power-Thermal : 234.24744568339844 W
###########
I : 249.6
E : 0.9584227832312189 V
FC Efficiency : 0.15697941011112976
FC Power : 72.58476756482462 W
FC Voltage : 0.29080435723086784 V
Nernst Gain : 0.15138157399964897 V
Ohmic Loss : 0.819 V
PH2 : 0.0003835915385106393 atm
PH2O : 0.004603098462127672 atm
PO2 : 0.00030371053492538665 atm
Power-Thermal : 234.42323243517538 W
###########
I : 249.7
E : 0.9584117978933779 V
FC Efficiency : 0.1568022846050569
FC Power : 72.53191518804772 W
FC Voltage : 0.29047623223086794 V
Nernst Gain : 0.15139255933748993 V
Ohmic Loss : 0.819328125 V
PH2 : 0.00038374522101805537 atm
PH2O : 0.004604942652216665 atm
PO2 : 0.0003038322138255971 atm
Power-Thermal : 234.59908481195225 W
###########
I : 249.8
E : 0.9584008169540708 V
FC Efficiency : 0.15662515909898406
FC Power : 72.47899718627082 W
FC Voltage : 0.2901481072308679 V
Nernst Gain : 0.15140354027679712 V
Ohmic Loss : 0.81965625 V
PH2 : 0.0003838989035254716 atm
PH2O : 0.004606786842305658 atm
PO2 : 0.00030395389272580765 atm
Power-Thermal : 234.7750028137292 W
###########
I : 249.9
E : 0.9583898404097764 V
FC Efficiency : 0.1564480335929111
FC Power : 72.42601355949387 W
FC Voltage : 0.2898199822308678 V
Nernst Gain : 0.15141451682109144 V
Ohmic Loss : 0.819984375 V
PH2 : 0.00038405258603288765 atm
PH2O : 0.004608631032394652 atm
PO2 : 0.0003040755716260181 atm
Power-Thermal : 234.95098644050614 W
###########
Report is generating ...
Done!
>>> Chakraborty_Data["Status"]
True
>>> Chakraborty_Data["P"][5]
74.69521188767807
>>> Chakraborty_Data["I"][5]
245.5
>>> Chakraborty_Data["V"][5]
0.3042574822308679
>>> Chakraborty_Data["EFF"][5]
0.16424155586011763
>>> Chakraborty_Data["PO2"][5]
0.0002987217000167565
>>> Chakraborty_Data["PH2"][5]
0.0003772905557065783
>>> Chakraborty_Data["PH2O"][5]
0.0045274866684789404
>>> Chakraborty_Data["Ph"][5]
227.26978811232192
>>> Chakraborty_Data["VE"][5]
0.3042574822308455
>>> Chakraborty_Data["V0"]
1.109804357228015
>>> Chakraborty_Data["K"]
-0.0032812499999884705
>>> Chakraborty_Data["Nernst Gain"][5]
0.1509273439765929
>>> Chakraborty_Data["Ohmic Loss"][5]
0.805546875
>>> Chakraborty_Data=Dynamic_Analysis(InputMethod={}, TestMode=True, PrintMode=False)
>>> Chakraborty_Data["Status"]
False
>>> Vcell_Calc(Enernst = 0.6, Nernst_Gain=0.2, Ohmic_Loss=0.1, N=1)
0.7
>>> Vcell_Calc(Enernst = 0.6, Nernst_Gain=0.2, Ohmic_Loss=0.1, N=None)
[Error] Vcell Calculation Error (Enernst:0.6, Nernst_Gain:0.2, Ohmic_Loss:0.1, N:None)
>>> Enernst_Calc(E0=0.6, N0=2, T=1273, PH2=1, PO2=1, PH2O=1)
1.2
>>> Enernst_Calc(E0=0.6, N0=2, T=1273, PH2=1, PO2=1, PH2O=None)
[Error] Enernst Calculation Failed (E0:0.6, N0:2, T:1273, PH2:1, PO2:1, PH2O:None)
>>> PH2_Calc(KH2=0.0000002, u=0.8, I=1)
0.006477717687589522
>>> PH2_Calc(KH2=0.0000002, u=0.8, I=None)
[Error] PH2 Calculation Failed (KH2:2e-07, u:0.8, I:None)
>>> PO2_Calc(KO2=0.00002, u=0.8, rHO=1.1145, I=1)
0.00016105657884531684
>>> PO2_Calc(KO2=0.00002, u=0.8, rHO=1.1145, I=None)
[Error] PO2 Calculation Failed (KO2:2e-05, u:0.8, rHO:1.1145, I:None)
>>> PH2O_Calc(KH2O=0.000002, I=1)
0.002591087075035809
>>> PH2O_Calc(KH2O=0.000002, I=None)
[Error] PH2O Calculation Failed (KH2O:2e-06, I:None)
>>> Nernst_Gain_Calc(T=1273, I=10)
0.06314815567790123
>>> Nernst_Gain_Calc(T=1273, I=None)
[Error] Nernst Gain Calculation Error (T:1273, I:None)
>>> Ohmic_Loss_Calc(Rint=2, I=10)
20
>>> Ohmic_Loss_Calc(Rint=None, I=10)
[Error] Ohmic Loss Calculation Error (Rint:None, I:10)
>>> Efficiency_Calc(0.7,0.8,1)
0.3778677462887989
>>> Efficiency_Calc(0.7,None,1)
[Error] PEM Efficiency Calculation Failed (Vcell:0.7, u:None, N:1)
>>> Test_Vector={"T": 1273,"E0": 0.6,"u":0.8,"N0": 1,"R": 3.28125 * 10**(-3),"KH2O": 0.000281,"KH2": 0.000843,"KO2": 0.00252,"rho": 1.145,"i-start": 250,"i-stop":249 ,"i-step": -0.1,"Name": "test1"}
>>> Chakraborty_Data=Dynamic_Analysis(InputMethod=Test_Vector, TestMode=True)
###########
Chakraborty-Model Simulation
###########
Analyzing . . .
I : 249
E : 0.9584887878251811 V
FC Efficiency : 0.15804216314756703
FC Power : 72.90050370048611 W
FC Voltage : 0.2927731072308679 V
Nernst Gain : 0.15131556940568683 V
Ohmic Loss : 0.81703125 V
PH2 : 0.0003826694434661426 atm
PH2O : 0.0045920333215937114 atm
PO2 : 0.0003029804615241237 atm
Power-Thermal : 233.36949629951388 W
###########
I : 249.1
E : 0.9584777760219602 V
FC Efficiency : 0.15786503764149415
FC Power : 72.84804507370919 W
FC Voltage : 0.2924449822308679 V
Nernst Gain : 0.15132658120890777 V
Ohmic Loss : 0.817359375 V
PH2 : 0.00038282312597355864 atm
PH2O : 0.004593877511682705 atm
PO2 : 0.0003031021404243342 atm
Power-Thermal : 233.54495492629079 W
###########
I : 249.2
E : 0.9584667686384878 V
FC Efficiency : 0.15768791213542133
FC Power : 72.7955208219323 W
FC Voltage : 0.292116857230868 V
Nernst Gain : 0.15133758859238014 V
Ohmic Loss : 0.8176874999999999 V
PH2 : 0.0003829768084809748 atm
PH2O : 0.004595721701771698 atm
PO2 : 0.00030322381932454466 atm
Power-Thermal : 233.72047917806768 W
###########
I : 249.3
E : 0.9584557656712175 V
FC Efficiency : 0.1575107866293484
FC Power : 72.74293094515536 W
FC Voltage : 0.2917887322308679 V
Nernst Gain : 0.15134859155965044 V
Ohmic Loss : 0.818015625 V
PH2 : 0.0003831304909883909 atm
PH2O : 0.004597565891860692 atm
PO2 : 0.0003033454982247552 atm
Power-Thermal : 233.89606905484465 W
###########
I : 249.4
E : 0.9584447671166072 V
FC Efficiency : 0.15733366112327551
FC Power : 72.69027544337845 W
FC Voltage : 0.29146060723086786 V
Nernst Gain : 0.15135959011426076 V
Ohmic Loss : 0.81834375 V
PH2 : 0.0003832841734958071 atm
PH2O : 0.004599410081949685 atm
PO2 : 0.00030346717712496565 atm
Power-Thermal : 234.07172455662155 W
###########
I : 249.5
E : 0.9584337729711189 V
FC Efficiency : 0.1571565356172027
FC Power : 72.63755431660155 W
FC Voltage : 0.29113248223086796 V
Nernst Gain : 0.15137058425974906 V
Ohmic Loss : 0.8186718749999999 V
PH2 : 0.00038343785600322315 atm
PH2O : 0.004601254272038678 atm
PO2 : 0.0003035888560251761 atm
Power-Thermal : 234.24744568339844 W
###########
I : 249.6
E : 0.9584227832312189 V
FC Efficiency : 0.15697941011112976
FC Power : 72.58476756482462 W
FC Voltage : 0.29080435723086784 V
Nernst Gain : 0.15138157399964897 V
Ohmic Loss : 0.819 V
PH2 : 0.0003835915385106393 atm
PH2O : 0.004603098462127672 atm
PO2 : 0.00030371053492538665 atm
Power-Thermal : 234.42323243517538 W
###########
I : 249.7
E : 0.9584117978933779 V
FC Efficiency : 0.1568022846050569
FC Power : 72.53191518804772 W
FC Voltage : 0.29047623223086794 V
Nernst Gain : 0.15139255933748993 V
Ohmic Loss : 0.819328125 V
PH2 : 0.00038374522101805537 atm
PH2O : 0.004604942652216665 atm
PO2 : 0.0003038322138255971 atm
Power-Thermal : 234.59908481195225 W
###########
I : 249.8
E : 0.9584008169540708 V
FC Efficiency : 0.15662515909898406
FC Power : 72.47899718627082 W
FC Voltage : 0.2901481072308679 V
Nernst Gain : 0.15140354027679712 V
Ohmic Loss : 0.81965625 V
PH2 : 0.0003838989035254716 atm
PH2O : 0.004606786842305658 atm
PO2 : 0.00030395389272580765 atm
Power-Thermal : 234.7750028137292 W
###########
I : 249.9
E : 0.9583898404097764 V
FC Efficiency : 0.1564480335929111
FC Power : 72.42601355949387 W
FC Voltage : 0.2898199822308678 V
Nernst Gain : 0.15141451682109144 V
Ohmic Loss : 0.819984375 V
PH2 : 0.00038405258603288765 atm
PH2O : 0.004608631032394652 atm
PO2 : 0.0003040755716260181 atm
Power-Thermal : 234.95098644050614 W
###########
Report is generating ...
Done!
>>> sorted(os.listdir("Chakraborty")) == ['test1.csv', 'test1.html', 'test1.opem']
True
>>> Test_Vector={"T": 1273,"E0": 0.6,"u":0.8,"N0": 1,"R": 3.28125 * 10**(-3),"KH2O": 0.000281,"KH2": 0.000843,"KO2": 0.00252,"rho": 1.145,"i-start": 250,"i-stop":249 ,"i-step": -0.1,"Name": "test2"}
>>> Chakraborty_Data=Dynamic_Analysis(InputMethod=Test_Vector, TestMode=True, PrintMode=False, Folder=os.path.join(os.getcwd(), "Folder_Test"))
>>> sorted(os.listdir(os.path.join("Folder_Test", "Chakraborty"))) == ['test2.csv', 'test2.html', 'test2.opem']
True
>>> shutil.rmtree("Chakraborty")
>>> shutil.rmtree("Folder_Test")

'''
