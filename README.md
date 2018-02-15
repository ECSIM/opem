<div align="center">
<img src="otherfile/logo.png" width=250px height=250px>
<br/>
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/built%20with-Python3-green.svg" alt="built with Python3" /></a>
<a href="https://travis-ci.org/ECSIM/opem"><img src="https://travis-ci.org/ECSIM/opem.svg?branch=master"></a>
<a href="https://ci.appveyor.com/project/sepandhaghighi/opem"><img src="https://ci.appveyor.com/api/projects/status/h6qq5c806p1vu3v2?svg=true"></a>
<a href="https://codecov.io/gh/ECSIM/opem">
  <img src="https://codecov.io/gh/ECSIM/opem/branch/master/graph/badge.svg" />
</a>
<a href="https://badge.fury.io/py/opem"><img src="https://badge.fury.io/py/opem.svg" alt="PyPI version" height="18"></a>
<a href="https://doi.org/10.5281/zenodo.1133110"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.1133110.svg" alt="DOI"></a>
<a class="badge-align" href="https://www.codacy.com/app/sepand-haghighi/opem?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ECSIM/opem&amp;utm_campaign=Badge_Grade"><img src="https://api.codacy.com/project/badge/Grade/361480463fb1477180f066e8f945037d"/></a>
<a href="Documents/"><img src="https://img.shields.io/badge/doc-latest-orange.svg"></a>

</div>
	
----------

## Overview			
The Open-Source PEMFC Simulation Tool (Opem) is an open-source mathematical simulation package for polymer electrolyte fuel cells. It contains a database of physical phenomena equations,  and kinetics mathematical models in order to perform static/dynamic analysis of PEMFC. The goal of the software is to prepare a platform for collaborative development of  PEMFC mathematical models.

## Installation		

### Source Code
- Download [Version 0.5](https://github.com/ecsim/opem/archive/v0.5.zip) or [Latest Source ](https://github.com/ecsim/opem/archive/master.zip)
- Run `pip install -r requirements.txt` or `pip3 install -r requirements.txt` (Need root access)
- Run `python3 setup.py install` or `python setup.py install` (Need root access)				

### PyPI


- Check [Python Packaging User Guide](https://packaging.python.org/installing/)     
- Run `pip install opem` or `pip3 install opem` (Need root access)

### Exe Version (Only Windows)
- Download [Exe-Version 0.5](https://www.dropbox.com/s/c2t9k6u86kqtrih/OPEM%28v0.4%29.zip?dl=0)
- Extract Zip File
- Run `OPEM.exe`
## Usage

### CLI (Command Line Interface)
- Open `CMD` (Windows) or `Terminal` (UNIX)
- Run `python -m opem` or `python3 -m opem`
- Enter PEM cell parameters
	1. Amphlett Static Model
		<html>
		<table>
			<tr>
				<td align="center">Input</td>
				<td align="center">Description</td>
				<td align="center">Unit</td>
			</tr>
			<tr>
				<td align="center">T</td>
				<td align="center">Cell Operation Temperature</td>
				<td align="center">K</td>
			</tr>
			<tr>
				<td align="center">PH2</td>
				<td align="center">Partial Pressure</td>
				<td align="center">atm</td>
			</tr>
			<tr>
				<td align="center">PO2</td>
				<td align="center">Partial Pressure</td>
				<td align="center">atm</td>
			</tr>
			<tr>
				<td align="center">i-start</td>
				<td align="center">Cell operating current start point</td>
				<td align="center">A</td>
			</tr>
			<tr>
				<td align="center">i-step</td>
				<td align="center">Cell operating current step</td>
				<td align="center">A</td>
			</tr>
			<tr>
				<td align="center">i-stop</td>
				<td align="center">Cell operating current end point</td>
				<td align="center">A</td>
			</tr>
			<tr>
				<td align="center">A</td>
				<td align="center">Active area</td>
				<td align="center">cm^2</td>
			</tr>
			<tr>
				<td align="center">l</td>
				<td align="center">Membrane Thickness</td>
				<td align="center">cm</td>
			</tr>
			<tr>
				<td align="center">lambda</td>
				<td align="center">is an adjustable parameter with a min value of 14 and max value of 23</td>
				<td align="center">--</td>
			</tr>
			<tr>
				<td align="center">R(*Optional)</td>
				<td align="center">R-Electronic</td>
				<td align="center">ohm</td>
			</tr>
			<tr>
				<td align="center">B</td>
				<td align="center"> An empirical constant depending on the cell and its operation state (Tafel Slope)</td>
				<td align="center">V</td>
			</tr>
			<tr>
				<td align="center">JMax</td>
				<td align="center">Maximum current density</td>
				<td align="center">A/(cm^2)</td>
			</tr>
			<tr>
				<td align="center">N</td>
				<td align="center">Number Of Single Cells</td>
				<td align="center">--</td>
			</tr>
				
		</table> 
		</html>
		* For more information about this model visit <a href="Documents/Amphlett.ipynb">here</a>
	2. Larminie-Dicks Static Model
		<html>
		<table>
			<tr>
				<td align="center">Input</td>
				<td align="center">Description</td>
				<td align="center">Unit</td>
			</tr>
			<tr>
				<td align="center">E0</td>
				<td align="center">Fuel Cell reversible no loss voltage</td>
				<td align="center">V</td>
			</tr>
			<tr>
				<td align="center">A</td>
				<td align="center">The slope of the Tafel line</td>
				<td align="center">V</td>
			</tr>
			<tr>
				<td align="center">B</td>
				<td align="center">Constant in the mass transfer term</td>
				<td align="center">V</td>
			</tr>
			<tr>
				<td align="center">i-start</td>
				<td align="center">Cell operating current start point</td>
				<td align="center">A</td>
			</tr>
			<tr>
				<td align="center">i-step</td>
				<td align="center">Cell operating current step</td>
				<td align="center">A</td>
			</tr>
			<tr>
				<td align="center">i-stop</td>
				<td align="center">Cell operating current end point</td>
				<td align="center">A</td>
			</tr>
			<tr>
				<td align="center">i_n</td>
				<td align="center">Internal current</td>
				<td align="center">A</td>
			</tr>
			<tr>
				<td align="center">i_0</td>
				<td align="center">Exchange current at which the overvoltage begins to move from zero	</td>
				<td align="center">A</td>
			</tr>
			<tr>
				<td align="center">i_L</td>
				<td align="center">Limiting current</td>
				<td align="center">A</td>
			</tr>
			<tr>
				<td align="center">RM</td>
				<td align="center">The membrane and contact resistances</td>
				<td align="center">ohm</td>
			</tr>
			<tr>
				<td align="center">N</td>
				<td align="center">Number Of Single Cells</td>
				<td align="center">--</td>
			</tr>
				
		</table>
		</html>
		* For more information about this model visit <a href="Documents/Larminie_Dicks.ipynb">here</a>
	3. Chamberline-Kim Static Model
		<html>
		<table>
			<tr>
				<td align="center" >Input</td>
				<td align="center">Description</td>
				<td  align="center">Unit</td>
			</tr>
			<tr>
				<td align="center">E0</td>
				<td align="center">Open circuit voltage</td>
				<td align="center">V</td>
			</tr>
			<tr>
				<td align="center">b</td>
				<td align="center">Tafel's parameter for the oxygen reduction</td>
				<td align="center">V</td>
			</tr>
			<tr>
				<td align="center">R</td>
				<td align="center">Resistance</td>
				<td align="center">ohm.cm^2</td>
			</tr>
			<tr>
				<td align="center">i-start</td>
				<td align="center">Cell operating current start point</td>
				<td align="center">A</td>
			</tr>
			<tr>
				<td align="center">i-step</td>
				<td align="center">Cell operating current step</td>
				<td align="center">A</td>
			</tr>
			<tr>
				<td align="center">i-stop</td>
				<td align="center">Cell operating current end point</td>
				<td align="center">A</td>
			</tr>
			<tr>
				<td align="center">A</td>
				<td align="center">Active area</td>
				<td align="center">cm^2</td>
			</tr>
			<tr>
				<td align="center">m</td>
				<td align="center">Diffusion's parameters</td>
				<td align="center">V</td>
			</tr>
			<tr>
				<td align="center">n</td>
				<td align="center">Diffusion's parameters</td>
				<td align="center">(A^-1)(cm^2)</td>
			</tr>
			<tr>
				<td align="center">N</td>
				<td align="center">Number Of Single Cells</td>
				<td align="center">--</td>
			</tr>
				
		</table>
		</html>
		* For more information about this model visit <a href="Documents/Chamberline_Kim.ipynb">here</a>
	4. Padulles Dynamic Model I
		<html>
		<table>
			<tr>
				<td align="center" >Input</td>
				<td align="center">Description</td>
				<td  align="center">Unit</td>
			</tr>
			<tr>
				<td align="center">E0</td>
				<td align="center">No load voltage</td>
				<td align="center">V</td>
			</tr>
			<tr>
				<td align="center">T</td>
				<td align="center">FuelCell temperature</td>
				<td align="center">K</td>
			</tr>
			<tr>
				<td align="center">KH2</td>
				<td align="center">Hydrogen valve constant</td>
				<td align="center">kmol.s^(-1).atm^(-1)</td>
			</tr>
			<tr>
				<td align="center">KO2</td>
				<td align="center">Oxygen valve constant</td>
				<td align="center">kmol.s^(-1).atm^(-1)</td>
			</tr>
			<tr>
				<td align="center">tH2</td>
				<td align="center">Hydrogen time constant</td>
				<td align="center">s</td>
			</tr>
			<tr>
				<td align="center">tO2</td>
				<td align="center">Oxygen time constant</td>
				<td align="center">s</td>
			</tr>
			<tr>
				<td align="center">B</td>
				<td align="center">Activation voltage constant</td>
				<td align="center">V</td>
			</tr>
			<tr>
				<td align="center">C</td>
				<td align="center">Activation constant parameter</td>
				<td align="center">A^(-1)</td>
			</tr>
			<tr>
				<td align="center">Rint</td>
				<td align="center">FuelCell internal resistance</td>
				<td align="center">ohm</td>
			</tr>
			<tr>
				<td align="center">rho</td>
				<td align="center">Hydrogen-oxygen flow ratio</td>
				<td align="center">--</td>
			</tr>
			<tr>
				<td align="center">qH2</td>
				<td align="center">Molar flow of hydrogen</td>
				<td align="center">kmol/s</td>
			</tr>
			<tr>
				<td align="center">N0</td>
				<td align="center">Number of cells</td>
				<td align="center">--</td>
			</tr>
			<tr>
				<td align="center">i-start</td>
				<td align="center">Cell operating current start point</td>
				<td align="center">A</td>
			</tr>
			<tr>
				<td align="center">i-step</td>
				<td align="center">Cell operating current step</td>
				<td align="center">A</td>
			</tr>
			<tr>
				<td align="center">i-stop</td>
				<td align="center">Cell operating current end point</td>
				<td align="center">A</td>
			</tr>
			
				
		</table>
		</html>
		* For more information about this model visit <a href="Documents/Padulles1.ipynb">here</a>				

	5. Padulles Dynamic Model II
		<html>
		<table>
			<tr>
				<td align="center" >Input</td>
				<td align="center">Description</td>
				<td  align="center">Unit</td>
			</tr>
			<tr>
				<td align="center">E0</td>
				<td align="center">No load voltage</td>
				<td align="center">V</td>
			</tr>
			<tr>
				<td align="center">T</td>
				<td align="center">FuelCell temperature</td>
				<td align="center">K</td>
			</tr>
			<tr>
				<td align="center">KH2</td>
				<td align="center">Hydrogen valve constant</td>
				<td align="center">kmol.s^(-1).atm^(-1)</td>
			</tr>
			<tr>
				<td align="center">KH2O</td>
				<td align="center">Water valve constant</td>
				<td align="center">kmol.s^(-1).atm^(-1)</td>
			</tr>
			<tr>
				<td align="center">KO2</td>
				<td align="center">Oxygen valve constant</td>
				<td align="center">kmol.s^(-1).atm^(-1)</td>
			</tr>
			<tr>
				<td align="center">tH2</td>
				<td align="center">Hydrogen time constant</td>
				<td align="center">s</td>
			</tr>
			<tr>
				<td align="center">tH2O</td>
				<td align="center">Water time constant</td>
				<td align="center">s</td>
			</tr>
			<tr>
				<td align="center">tO2</td>
				<td align="center">Oxygen time constant</td>
				<td align="center">s</td>
			</tr>
			<tr>
				<td align="center">B</td>
				<td align="center">Activation voltage constant</td>
				<td align="center">V</td>
			</tr>
			<tr>
				<td align="center">C</td>
				<td align="center">Activation constant parameter</td>
				<td align="center">A^(-1)</td>
			</tr>
			<tr>
				<td align="center">Rint</td>
				<td align="center">FuelCell internal resistance</td>
				<td align="center">ohm</td>
			</tr>
			<tr>
				<td align="center">rho</td>
				<td align="center">Hydrogen-oxygen flow ratio</td>
				<td align="center">--</td>
			</tr>
			<tr>
				<td align="center">qH2</td>
				<td align="center">Molar flow of hydrogen</td>
				<td align="center">kmol/s</td>
			</tr>
			<tr>
				<td align="center">qH2O</td>
				<td align="center">Molar flow of water</td>
				<td align="center">kmol/s</td>
			</tr>
			<tr>
				<td align="center">N0</td>
				<td align="center">Number of cells</td>
				<td align="center">--</td>
			</tr>
			<tr>
				<td align="center">i-start</td>
				<td align="center">Cell operating current start point</td>
				<td align="center">A</td>
			</tr>
			<tr>
				<td align="center">i-step</td>
				<td align="center">Cell operating current step</td>
				<td align="center">A</td>
			</tr>
			<tr>
				<td align="center">i-stop</td>
				<td align="center">Cell operating current end point</td>
				<td align="center">A</td>
			</tr>
			
				
		</table>
		</html>
		* For more information about this model visit <a href="Documents/Padulles2.ipynb">here</a>
	5. Padulles-Hauer Dynamic Model
		<html>
		<table>
			<tr>
				<td align="center" >Input</td>
				<td align="center">Description</td>
				<td  align="center">Unit</td>
			</tr>
			<tr>
				<td align="center">E0</td>
				<td align="center">No load voltage</td>
				<td align="center">V</td>
			</tr>
			<tr>
				<td align="center">T</td>
				<td align="center">FuelCell temperature</td>
				<td align="center">K</td>
			</tr>
			<tr>
				<td align="center">KH2</td>
				<td align="center">Hydrogen valve constant</td>
				<td align="center">kmol.s^(-1).atm^(-1)</td>
			</tr>
			<tr>
				<td align="center">KH2O</td>
				<td align="center">Water valve constant</td>
				<td align="center">kmol.s^(-1).atm^(-1)</td>
			</tr>
			<tr>
				<td align="center">KO2</td>
				<td align="center">Oxygen valve constant</td>
				<td align="center">kmol.s^(-1).atm^(-1)</td>
			</tr>
			<tr>
				<td align="center">tH2</td>
				<td align="center">Hydrogen time constant</td>
				<td align="center">s</td>
			</tr>
			<tr>
				<td align="center">tH2O</td>
				<td align="center">Water time constant</td>
				<td align="center">s</td>
			</tr>
			<tr>
				<td align="center">tO2</td>
				<td align="center">Oxygen time constant</td>
				<td align="center">s</td>
			</tr>
			<tr>
				<td align="center">t1</td>
				<td align="center">Reformer time constant</td>
				<td align="center">s</td>
			</tr>
			<tr>
				<td align="center">t2</td>
				<td align="center">Reformer time constant</td>
				<td align="center">s</td>
			</tr>
			<tr>
				<td align="center">B</td>
				<td align="center">Activation voltage constant</td>
				<td align="center">V</td>
			</tr>
			<tr>
				<td align="center">C</td>
				<td align="center">Activation constant parameter</td>
				<td align="center">A^(-1)</td>
			</tr>
			<tr>
				<td align="center">CV</td>
				<td align="center">Conversion factor</td>
				<td align="center">--</td>
			</tr>
			<tr>
				<td align="center">Rint</td>
				<td align="center">FuelCell internal resistance</td>
				<td align="center">ohm</td>
			</tr>
			<tr>
				<td align="center">rho</td>
				<td align="center">Hydrogen-oxygen flow ratio</td>
				<td align="center">--</td>
			</tr>
			<tr>
				<td align="center">qMethanol</td>
				<td align="center">Molar flow of methanol</td>
				<td align="center">kmol/s</td>
			</tr>
			<tr>
				<td align="center">N0</td>
				<td align="center">Number of cells</td>
				<td align="center">--</td>
			</tr>
			<tr>
				<td align="center">i-start</td>
				<td align="center">Cell operating current start point</td>
				<td align="center">A</td>
			</tr>
			<tr>
				<td align="center">i-step</td>
				<td align="center">Cell operating current step</td>
				<td align="center">A</td>
			</tr>
			<tr>
				<td align="center">i-stop</td>
				<td align="center">Cell operating current end point</td>
				<td align="center">A</td>
			</tr>
			
				
		</table>
		</html>
		* For more information about this model visit <a href="Documents/Padulles_Hauer.ipynb">here</a>
		
		
- Find Your Reports In `Model_Name` Folder

<div align="center">

<a href="https://asciinema.org/a/154228" target="_blank"><img src="https://asciinema.org/a/154228.png" /></a>

</div>
		

## Issues & Bug Reports			

Just fill an issue and describe it. We'll check it ASAP!							
or send an email to [opem@ecsim.ir](mailto:opem@ecsim.ir "opem@ecsim.ir"). 


## TODO		

- [x] Static Analysis
  - [x] Amphlett Static Model
  	- [x] Nernst Voltage
  	- [x] PEMFC losses model
  	- [x] Power of PEMFC
  	- [x] Efficiency of PEMFC
  - [x] Larminie-Dicks Static Model
  	- [x] PEMFC losses model
  	- [x] Power of PEMFC
  	- [x] Efficiency of PEMFC
  - [x] Chamberline-Kim Static Model
  	- [x] PEMFC losses model
  	- [x] Power of PEMFC
  	- [x] Efficiency of PEMFC
- [x] Flat Output
    - [x] Simulation Result
    - [X] CSV File
    - [x] HTML
- [ ] GUI
  - [ ] Plot Graphs
  - [ ] Input/Output
- [ ] Dynamic Analysis
  - [x] Padulles Dynamic Model I
    - [x] Nernst Voltage
  	- [x] Voltage of PEMFC
  	- [x] Power of PEMFC
  	- [x] Efficiency of PEMFC
  - [x] Padulles Dynamic Model II
    - [x] Nernst Voltage
  	- [x] Voltage of PEMFC
  	- [x] Power of PEMFC
  	- [x] Efficiency of PEMFC
  - [x] Padulles-Hauer Dynamic Model
    - [x] Nernst Voltage
  	- [x] Voltage of PEMFC
  	- [x] Power of PEMFC
  	- [x] Efficiency of PEMFC
  - [ ] Padulles-Hauer-Pathapati-Amphlett Dynamic Model
    - [ ] Nernst Voltage
  	- [ ] Voltage of PEMFC
  	- [ ] Power of PEMFC
  	- [ ] Efficiency of PEMFC
  - [ ] Impedance model of fuel cell
  - [ ] Dicks-Larminie Danymic Model
  - [ ] Becherif-Hissel Dynamic model
  - [ ] PEMFC Charge Transport
  - [ ] PEMFC Mass Trasport
  - [ ] PEMF Heat Transfer
  - [ ] PEMFC Catalyst Layers
  - [ ] PEMFC Flow Feild Plates


## Contribution			

You can fork the repository, improve or fix some part of it and then send the pull requests back if you want to see them here. I really appreciate that. ❤️			

Remember to write a few tests for your code before sending pull requests. 


## Reference

<blockquote>1- J. C. Amphlett, R. M. Baumert, R. F. Mann, B. A. Peppley, and P. R. Roberge. 1995. "Performance Modeling of the Ballard Mark IV Solid Polymer Electrolyte Fuel Cell." J. Electrochem. Soc. (The Electrochemical Society, Inc.) 142 (1): 9-15. doi: 10.1149/1.2043959. </blockquote>

<blockquote>2- Jeferson M. Correa, Felix A. Farret, Vladimir A. Popov, Marcelo G. Simoes. 2005. "Sensitivity Analysis of the Modeling Parameters Used in Simulation of Proton Exchange Membrane Fuel Cells." IEEE Transactions on Energy Conversion (IEEE) 20 (1): 211-218. doi:10.1109/TEC.2004.842382.</blockquote>


<blockquote>3- Junbom Kim, Seong-Min Lee, Supramaniam Srinivasan, Charles E. Chamberlin. 1995. "Modeling of Proton Exchange Membrane Fuel Cell Performance with an Empirical Equation." Journal of The Electrochemical Society (The Electrochemical Society) 142 (8): 2670-2674. doi:10.1149/1.2050072.</blockquote>

<blockquote>
4- I. Sadli, P. Thounthong, J.-P. Martin, S. Rael, B. Davat. 2006. "Behaviour of a PEMFC supplying a low voltage static converter." Journal of Power Sources (Elsevier) 156: 119–125. doi:10.1016/j.jpowsour.2005.08.021.
</blockquote>

<blockquote>
5- J. Padulles, G.W. Ault, J.R. McDonald. 2000. "An integrated SOFC plant dynamic model for power systems simulation." Journal of Power Sources (Elsevier) 86 (1-2): 495-500. doi:10.1016/S0378-7753(99)00430-9.
</blockquote>
						
<blockquote>
6- Hauer, K.-H. 2001. "Analysis tool for fuel cell vehicle hardware and software (controls) with an application to fuel economy comparisons of alternative system designs." Ph.D. dissertation, Transportation Technology
and Policy, University of California Davis.
</blockquote>

## Cite

If you use OPEM in your research , please cite this :

<pre>

@misc{https://doi.org/10.5281/zenodo.1133110,
  doi = {10.5281/zenodo.1133110},
  author = {{Sepand Haghighi} and {Kasra Askari} and {Sarmin Hamidi} and Rahimi,  Mohammad Mahdi},
  keywords = {Cell,  PEM,  Fuel Cell,  electrochemistry},
  title = {Opem : An Open Source Pem Cell Simulation Tool},
  pages = {--},
  publisher = {Zenodo},
  year = {2017}
}


</pre>

## License

<a href="https://github.com/ecsim/opem/blob/master/LICENSE"><img src="https://img.shields.io/github/license/mashape/apistatus.svg"/></a>


## Donate to our project
								
<h3>Bitcoin :</h3>					

```12Xm1qL4MXYWiY9sRMoa3VpfTfw6su3vNq```			



<h3>Payping (For Iranian citizens) :</h3>

<a href="http://www.payping.net/sepandhaghighi" target="__blank"><img src="http://www.qpage.ir/images/payping.png" height=100px width=100px></a>	
