# -*- coding: utf-8 -*-
HHV=1.482
uF=0.95
n=8*(10**-3)
m=3*(10**-5)
xi1=-0.948
xi3=7.6*(10**-5)
xi4=-1.93*(10**-4)
Version=0.1
InputParams={"T":"Cell Operation Temperature [K]","PH2":"Partial Pressure [atm]","PO2":"Partial Pressure [atm]",
           "i-start":"Cell operating current start point [A]","i-step":"Cell operating current step","i-stop":"Cell operating current end point [A]","A":"active area [cm2]","l":"Membrane Thickness [cm]","lambda":"is an adjustable parameter with a min value of 14 and max value of 23",
           "N":"Number Of Single Cells","R":"R-Electronic [ohm] (*Optional)","B":"An empirical constant depending on the cell and its operation state (Tafel Slope) [V]","JMax":"maximum current density [A/cm2]"}
OutputParams={"Enernst":"V","Eta Activation":"V","Eta Ohmic":"V","Eta Concentration":"V","Loss":"V","Vcell":"V","PEM Efficiency":"","Power":"W","VStack":"V"}

