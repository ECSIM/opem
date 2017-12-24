<div align="center">
<img src="otherfile/logo.png" width=250px height=250px>
<br/>
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/built%20with-Python3-green.svg" alt="built with Python3" /></a>
<a href="https://travis-ci.org/ECSIM/opem"><img src="https://travis-ci.org/ECSIM/opem.svg?branch=master"></a>
<a href="https://ci.appveyor.com/project/sepandhaghighi/opem"><img src="https://ci.appveyor.com/api/projects/status/h6qq5c806p1vu3v2?svg=true"></a>
<a href="https://codecov.io/gh/ECSIM/opem">
  <img src="https://codecov.io/gh/ECSIM/opem/branch/master/graph/badge.svg" />
</a>
<a class="badge-align" href="https://www.codacy.com/app/sepand-haghighi/opem?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ECSIM/opem&amp;utm_campaign=Badge_Grade"><img src="https://api.codacy.com/project/badge/Grade/361480463fb1477180f066e8f945037d"/></a>

</div>
	
----------

## Overview			
OPEM is an open source PEM cell simulation tool

## Installation		

### Source Code
- Download [Version 0.1](https://github.com/ecsim/opem/archive/v0.1.zip) or [Latest Source ](https://github.com/ecsim/opem/archive/master.zip)
- Run `pip install -r requirements.txt` or `pip3 install -r requirements.txt` (Need root access)
- Run `python3 setup.py install` or `python setup.py install` (Need root access)				

### PyPI


- Check [Python Packaging User Guide](https://packaging.python.org/installing/)     
- Run `pip install opem` or `pip3 install opem` (Need root access)

## Usage

### CLI (Command Line Interface)
- Open `CMD` (Windows) or `Terminal` (UNIX)
- Run `python -m opem` or `python3 -m opem`
- Enter PEM cell parameters
	-  T :  Cell Operation Temperature [K]
	-  PH2 : Partial Pressure [atm]
	-  PO2 : Partial Pressure [atm]
	-  i-start : Cell load current start point [A]
	-  i-step : Cell load current step
	-  i-stop : Cell load current end point [A]
	-  A : active area [cm2]
	-  l : Membrane Thickness [cm]
	-  lambda : is an adjustable parameter with a possible maximum value of 23
	-  R : R-Electronic [ohm] (*Optional) 
	-  B : Tafel Slope 
	-  JMax : maximum current density [A/cm2]
	-  N : Number Of Single Cells
- Find Your Result In `Simulation-Result.opem` file (Open with Notepad)		

		

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
- [ ] GUI
  - [ ] Plot Graphs
  - [ ] Input/Output
- [ ] Dynamic Analysis


## Contribution			

You can fork the repository, improve or fix some part of it and then send the pull requests back if you want to see them here. I really appreciate that. ❤️			

Remember to write a few tests for your code before sending pull requests. 



## License

<a href="https://github.com/ecsim/opem/blob/master/LICENSE"><img src="https://img.shields.io/github/license/mashape/apistatus.svg"/></a>


## Donate to our project
								
<h3>Bitcoin :</h3>					

```12Xm1qL4MXYWiY9sRMoa3VpfTfw6su3vNq```			



<h3>Payping (For Iranian citizens) :</h3>

<a href="http://www.payping.net/sepandhaghighi" target="__blank"><img src="http://www.qpage.ir/images/payping.png" height=100px width=100px></a>	
