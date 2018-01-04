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

</div>
	
----------

## Overview			
The Open-Source PEMFC Simulation Tool (Opem) is an open-source mathematical simulation package for polymer electrolyte fuel cells. It contains a database of physical phenomena equations,  and kinetics mathematical models in order to perform static/dynamic analysis of PEMFC. The goal of the software is to prepare a platform for collaborative development of  PEMFC mathematical models.

## Installation		

### Source Code
- Download [Version 0.1](https://github.com/ecsim/opem/archive/v0.1.zip) or [Latest Source ](https://github.com/ecsim/opem/archive/master.zip)
- Run `pip install -r requirements.txt` or `pip3 install -r requirements.txt` (Need root access)
- Run `python3 setup.py install` or `python setup.py install` (Need root access)				

### PyPI


- Check [Python Packaging User Guide](https://packaging.python.org/installing/)     
- Run `pip install opem` or `pip3 install opem` (Need root access)

### Exe Version (Only Windows)
- Download and run [Exe-Version 0.1](https://www.dropbox.com/s/5r72n1ayqbs3oq3/OPEM%28V0.1%29.zip?dl=0)
## Usage

### CLI (Command Line Interface)
- Open `CMD` (Windows) or `Terminal` (UNIX)
- Run `python -m opem` or `python3 -m opem`
- Enter PEM cell parameters
	1. Amphlett Static Model
		<html>
		<table style="text-align:center;">
			<tr>
				<td >Input</td>
				<td >Description</td>
				<td >Unit</td>
			</tr>
			<tr>
				<td>T</td>
				<td>Cell Operation Temperature</td>
				<td>K</td>
			</tr>
			<tr>
				<td>PH2</td>
				<td>Partial Pressure</td>
				<td>atm</td>
			</tr>
			<tr>
				<td>PO2</td>
				<td>Partial Pressure</td>
				<td>atm</td>
			</tr>
			<tr>
				<td>i-start</td>
				<td>Cell operating current start point</td>
				<td>A</td>
			</tr>
			<tr>
				<td>i-step</td>
				<td>Cell operating current step</td>
				<td>A</td>
			</tr>
			<tr>
				<td>i-stop</td>
				<td>Cell operating current end point</td>
				<td>A</td>
			</tr>
			<tr>
				<td>A</td>
				<td>Active area</td>
				<td>cm2</td>
			</tr>
			<tr>
				<td>l</td>
				<td>Membrane Thickness</td>
				<td>cm</td>
			</tr>
			<tr>
				<td>lambda</td>
				<td>is an adjustable parameter with a min value of 14 and max value of 23</td>
				<td>--</td>
			</tr>
			<tr>
				<td>R(*Optional)</td>
				<td>R-Electronic</td>
				<td>ohm</td>
			</tr>
			<tr>
				<td>B</td>
				<td> An empirical constant depending on the cell and its operation state (Tafel Slope)</td>
				<td>V</td>
			</tr>
			<tr>
				<td>JMax</td>
				<td>Maximum current density</td>
				<td>A/cm2</td>
			</tr>
			<tr>
				<td>N</td>
				<td>Number Of Single Cells</td>
				<td>--</td>
			</tr>
				
		</table> 
		</html>
		* For more information about this model visit <a href="Documents/Amphlett.ipynb">here</a>
	2. Larminie-Dicks Static Model
	3. Chamberline-Kim Static Model
		<html>
		<table style="text-align:center;">
			<tr>
				<td >Input</td>
				<td >Description</td>
				<td >Unit</td>
			</tr>
			<tr>
				<td>E0</td>
				<td>Open circuit voltage</td>
				<td>V</td>
			</tr>
			<tr>
				<td>b</td>
				<td>Tafel's parameter for the oxygen reduction</td>
				<td>V</td>
			</tr>
			<tr>
				<td>R</td>
				<td>Resistance</td>
				<td>ohm.cm^2</td>
			</tr>
			<tr>
				<td>i-start</td>
				<td>Cell operating current start point</td>
				<td>A</td>
			</tr>
			<tr>
				<td>i-step</td>
				<td>Cell operating current step</td>
				<td>A</td>
			</tr>
			<tr>
				<td>i-stop</td>
				<td>Cell operating current end point</td>
				<td>A</td>
			</tr>
			<tr>
				<td>A</td>
				<td>Active area</td>
				<td>cm2</td>
			</tr>
			<tr>
				<td>m</td>
				<td>Diffusion's parameters</td>
				<td>V</td>
			</tr>
			<tr>
				<td>n</td>
				<td>Diffusion's parameters</td>
				<td>(A^-1)(cm^2)</td>
			</tr>
			<tr>
				<td>N</td>
				<td>Number Of Single Cells</td>
				<td>--</td>
			</tr>
				
		</table>
		</html>
		* For more information about this model visit <a href="Documents/Chamberline_Kim.ipynb">here</a>
		
		
- Find Your Result In `.opem` & `.csv` files	

<div align="center">

<a href="https://asciinema.org/a/154228" target="_blank"><img src="https://asciinema.org/a/154228.png" /></a>

</div>
		

## Issues & Bug Reports			

Just fill an issue and describe it. We'll check it ASAP!							
or send an email to [opem@ecsim.ir](mailto:opem@ecsim.ir "opem@ecsim.ir"). 


## TODO		

- [ ] Static Analysis
  - [x] Amphlett Static Model
  	- [x] Nernst Voltage
  	- [x] PEMFC losses model
  	- [x] Power of PEMFC
  	- [x] Efficiency of PEMFC
  - [ ] Larminie-Dicks Static Model
  - [ ] Chamberline-Kim Static Model
- [X] Flat Output
    - [x] Simulation Result
    - [X] CSV File
- [ ] GUI
  - [ ] Plot Graphs
  - [ ] Input/Output
- [ ] Dynamic Analysis
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

<blockquote>1-J. C. Amphlett, R. M. Baumert, R. F. Mann, B. A. Peppley, and P. R. Roberge. 1995. "Performance Modeling of the Ballard Mark IV Solid Polymer Electrolyte Fuel Cell." J. Electrochem. Soc. (The Electrochemical Society, Inc.) 142 (1): 9-15. doi: 10.1149/1.2043959. </blockquote>

<blockquote>2-Jeferson M. Correa, Felix A. Farret, Vladimir A. Popov, Marcelo G. Simoes. 2005. "Sensitivity Analysis of the Modeling Parameters Used in Simulation of Proton Exchange Membrane Fuel Cells." IEEE Transactions on Energy Conversion (IEEE) 20 (1): 211-218. doi:10.1109/TEC.2004.842382.</blockquote>


<blockquote>Junbom Kim, Seong-Min Lee, Supramaniam Srinivasan, Charles E. Chamberlin. 1995. "Modeling of Proton Exchange Membrane Fuel Cell Performance with an Empirical Equation." Journal of The Electrochemical Society (The Electrochemical Society) 142 (8): 2670-2674. doi:10.1149/1.2050072.</blockquote>


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
