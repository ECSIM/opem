# -*- coding: utf-8 -*-
HHV = 1.482
uF = 0.95
n = 8 * (10 ** -3)
m = 3 * (10 ** -5)
xi1 = -0.948
xi3 = 7.6 * (10 ** -5)
xi4 = -1.93 * (10 ** -4)
#F=96500
#R1=8.314
R=8314.47
F=96484600
Amphlett_InputParams = {"T": "Cell Operation Temperature [K]", "PH2": "Partial Pressure [atm]", "PO2": "Partial Pressure [atm]",
               "i-start": "Cell operating current start point [A]", "i-step": "Cell operating current step",
               "i-stop": "Cell operating current end point [A]", "A": "active area [cm^2]",
               "l": "Membrane Thickness [cm]",
               "lambda": "is an adjustable parameter with a min value of 14 and max value of 23",
               "N": "Number Of Single Cells", "R": "R-Electronic [ohm] (*Optional)",
               "B": "An empirical constant depending on the cell and its operation state (Tafel Slope) [V]",
               "JMax": "maximum current density [A/(cm^2)]"}
Amphlett_OutputParams = {"Enernst": "V", "Eta Activation": "V", "Eta Ohmic": "V", "Eta Concentration": "V", "Loss": "V",
                "Vcell": "V", "PEM Efficiency": "", "Power": "W", "VStack": "V","Power-Stack":"W"}


Larminiee_InputParams = {"E0":"Fuel Cell reversible no loss voltage [V]",
               "i-start": "Cell operating current start point [A]", "i-step": "Cell operating current step",
               "i-stop": "Cell operating current end point [A]",
               "RM": "The membrane and contact resistances [ohm]",
               "B": "Constant in the mass transfer term [V]",
               "i_n": "Internal current [A]",
               "i_0":"Exchange current at which the overvoltage begins to move from zero [A]",
               "i_L":"limiting current [A]",
                "A": "The slope of the Tafel line [V]","N": "Number Of Single Cells"}
Larminiee_OutputParams = {"Vcell": "V", "PEM Efficiency": "", "Power": "W","VStack": "V","Power-Stack":"W"}

Chamberline_InputParams = {"E0": "Open circuit voltage [V]", "b": "Tafel's parameter for the oxygen reduction [V]", "R": "Resistance [ohm.cm^2]",
               "m": "Diffusion's parameters [V]", "n": "Diffusion's parameters [(A^-1)(cm^2)]",
               "i-start": "Cell operating current start point [A]", "i-step": "Cell operating current step",
               "i-stop": "Cell operating current end point [A]",
               "A": "Active area [cm^2]",
               "N": "Number Of Single Cells"}
Chamberline_OutputParams = {"Vcell": "V", "PEM Efficiency": "", "Power": "W", "VStack": "V","Power-Stack":"W"}


Padulles_InputParams={"N0":"Number of fuel cells in the stack","E0":"Opencell voltage [V]",
                     "T": "Cell Operation Temperature [K]","KH2":"Hydrogen Valve Constant [kmol.s^(-1).atm^(-1)]",
                     "KO2":"Oxygen Valve Constant [kmol.s^(-1).atm^(-1)]","tH2":"Hydrogen time constant [s]",
                     "tO2":"Oxygen time constant [s]","qH2":"Molar flow of hydrogen [kmol.s^(-1)]",
                     "rho":"Hydrogen-Oxygen flow rate","Rint":"Fuel cell internal resistance [ohm]",
                     "B":"Activation voltage constant [V]","C":"Constant [A^(-1)]",
                     "i-start": "Cell operating current start point [A]", "i-step": "Cell operating current step",
                     "i-stop": "Cell operating current end point [A]"}
Padulles_Outparams = {"FC Voltage":"V","FC Power":"W","FC Efficiency": "","PO2":"atm","PH2":"atm","E":"V"}

Padulles2_InputParams={"N0":"Number of fuel cells in the stack","E0":"Opencell voltage [V]",
                     "T": "Cell Operation Temperature [K]","KH2":"Hydrogen Valve Constant [kmol.s^(-1).atm^(-1)]",
                     "KO2":"Oxygen Valve Constant [kmol.s^(-1).atm^(-1)]","tH2":"Hydrogen time constant [s]",
                     "tO2":"Oxygen time constant [s]","qH2":"Molar flow of hydrogen [kmol.s^(-1)]",
                     "rho":"Hydrogen-Oxygen flow rate","Rint":"Fuel cell internal resistance [ohm]",
                     "B":"Activation voltage constant [V]","C":"Constant [A^(-1)]",
                     "i-start": "Cell operating current start point [A]", "i-step": "Cell operating current step",
                     "i-stop": "Cell operating current end point [A]",
                     "KH2O": "Water Valve Constant [kmol.s^(-1).atm^(-1)]",
                     "tH2O": "Water time constant [s]","qH2O":"Molar flow of water [kmol.s^(-1)]"}
Padulles2_Outparams = {"FC Voltage":"V","FC Power":"W","FC Efficiency": "","PO2":"atm","PH2":"atm","PH2O":"atm","E":"V"}