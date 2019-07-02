<div align="center">
<img src="https://github.com/ECSIM/opem/raw/master/otherfile/logo.png" width=250px height=250px>
<br/>
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/built%20with-Python3-green.svg" alt="built with Python3" /></a>
<a href="https://codecov.io/gh/ECSIM/opem">
  <img src="https://codecov.io/gh/ECSIM/opem/branch/master/graph/badge.svg" />
</a>
<a href="https://badge.fury.io/py/opem"><img src="https://badge.fury.io/py/opem.svg" alt="PyPI version" height="18"></a>
<a href="https://anaconda.org/ECSIM/opem"><img src="https://anaconda.org/ecsim/opem/badges/version.svg"></a>
<a href="Documents/"><img src="https://img.shields.io/badge/doc-latest-orange.svg"></a>

</div>
	
----------				

## Table of contents
   * [What is PEM?](http://physics.oregonstate.edu/~hetheriw/energy/topics/doc/electrochemistry/fc/basic/The_Polymer_Electrolyte_Fuel_Cell.htm)					
   * [Overview](https://github.com/ECSIM/opem#overview)
   * [Installation](https://github.com/ECSIM/opem/blob/master/INSTALL.md)
   * [Usage](https://github.com/ECSIM/opem#usage)
   		* [Executable](https://github.com/ECSIM/opem#executable)
   		* [Library](https://github.com/ECSIM/opem#library)	
   		* [Telegram Bot](https://github.com/ECSIM/opem#telegram-bot)
   		* [Try OPEM in Your Browser!](https://github.com/ECSIM/opem#try-opem-in-your-browser)
   		* [MATLAB](https://github.com/ECSIM/opem/tree/master/MATLAB)
   * [Issues & Bug Reports](https://github.com/ECSIM/opem#issues--bug-reports)
   * [Contribution](https://github.com/ECSIM/opem/blob/master/.github/CONTRIBUTING.md)
   * [Todo](https://github.com/ECSIM/opem#todo)
   * [Outputs](https://github.com/ECSIM/opem#outputs)
   * [Dependencies](https://github.com/ECSIM/opem#dependencies)
   * [Thanks](https://github.com/ECSIM/opem#thanks)
   * [Reference](https://github.com/ECSIM/opem#reference)
   * [Cite](https://github.com/ECSIM/opem#cite)
   * [Authors](https://github.com/ECSIM/opem/blob/master/AUTHORS.md)
   * [License](https://github.com/ECSIM/opem#license)
   * [Donate](https://github.com/ECSIM/opem#donate-to-our-project)
   * [Changelog](https://github.com/ECSIM/opem/blob/master/CHANGELOG.md)
   * [Code of Conduct](https://github.com/ECSIM/opem/blob/master/.github/CODE_OF_CONDUCT.md)

## Overview		


<p align="justify">
Modeling and simulation of proton-exchange membrane fuel cells (PEMFC) may work as a powerful tool in the research & development of renewable energy sources. The Open-Source PEMFC Simulation Tool (OPEM) is a modeling tool for evaluating the performance of proton exchange membrane fuel cells. This package is a combination of models (static/dynamic) that predict the optimum operating parameters of PEMFC. OPEM contained generic models that will accept as input, not only values of the operating variables such as anode and cathode feed gas, pressure and compositions, cell temperature and current density, but also cell parameters including the active area and membrane thickness. In addition, some of the different models of PEMFC that have been proposed in the OPEM, just focus on one particular FC stack, and some others take into account a part or all auxiliaries such as reformers. OPEM is a platform for collaborative development of PEMFC models.
</p>

<div align="center">

<img src="https://github.com/ECSIM/opem/raw/master/otherfile/OPEM_BLOCK_DIAGRAM.jpg">
<p>Fig1. OPEM Block Diagram</p>


</div>

<table>
	<tr> 
		<td align="center">Open Hub</td>
		<td align="center"><a href="https://www.openhub.net/p/opem"><img src="https://www.openhub.net/p/opem/widgets/project_thin_badge.gif"></a></td>	
	</tr>
	<tr>
		<td align="center">PyPI Counter</td>
		<td align="center"><a href="http://pepy.tech/count/opem"><img src="http://pepy.tech/badge/opem"></a></td>
	</tr>
	<tr>
		<td align="center">Github Stars</td>
		<td align="center"><a href="https://github.com/ecsim/opem"><img src="https://img.shields.io/github/stars/ECSIM/opem.svg?style=social&label=Stars"></a></td>
	</tr>
</table>

<table>
	<tr> 
		<td align="center">Branch</td>
		<td align="center">master</td>	
		<td align="center">develop</td>	
	</tr>
	<tr>
		<td align="center">Travis</td>
		<td align="center"><a href="https://travis-ci.org/ECSIM/opem"><img src="https://travis-ci.org/ECSIM/opem.svg?branch=master"></a></td>
		<td align="center"><a href="https://travis-ci.org/ECSIM/opem"><img src="https://travis-ci.org/ECSIM/opem.svg?branch=develop"></a></td>
	</tr>
	<tr>
		<td align="center">AppVeyor</td>
		<td align="center"><a href="https://ci.appveyor.com/project/ECSIM/opem"><img src="https://ci.appveyor.com/api/projects/status/h6qq5c806p1vu3v2/branch/master?svg=true"></a></td>
		<td align="center"><a href="https://ci.appveyor.com/project/ECSIM/opem"><img src="https://ci.appveyor.com/api/projects/status/h6qq5c806p1vu3v2/branch/develop?svg=true"></a></td>
	</tr>
</table>

<table>
	<tr> 
		<td align="center">Code Quality</td>
		<td align="center"><a class="badge-align" href="https://www.codacy.com/app/sepand-haghighi/opem?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ECSIM/opem&amp;utm_campaign=Badge_Grade"><img src="https://api.codacy.com/project/badge/Grade/361480463fb1477180f066e8f945037d"/></a></td>	
		<td align="center"><a href="https://www.codefactor.io/repository/github/ecsim/opem"><img src="https://www.codefactor.io/repository/github/ecsim/opem/badge" alt="CodeFactor" /></a></td>
	</tr>
</table>


## Usage

### Executable
- Open `CMD` (Windows) or `Terminal` (UNIX)
- Run `python -m opem` or `python3 -m opem` (or run `OPEM.exe`)
- Enter PEM cell parameters (or run standard test vectors)
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
				<td align="center">Cell operation temperature</td>
				<td align="center">K</td>
			</tr>
			<tr>
				<td align="center">PH2</td>
				<td align="center">Partial pressure</td>
				<td align="center">atm</td>
			</tr>
			<tr>
				<td align="center">PO2</td>
				<td align="center">Partial pressure</td>
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
				<td align="center">Membrane thickness</td>
				<td align="center">cm</td>
			</tr>
			<tr>
				<td align="center">lambda</td>
				<td align="center">An adjustable parameter with a min value of 14 and max value of 23</td>
				<td align="center">--</td>
			</tr>
			<tr>
				<td align="center">R(*Optional)</td>
				<td align="center">R-Electronic</td>
				<td align="center">ohm</td>
			</tr>
			<tr>
				<td align="center">B</td>
				<td align="center">An empirical constant depending on the cell and its operation state (Tafel slope)</td>
				<td align="center">V</td>
			</tr>
			<tr>
				<td align="center">JMax</td>
				<td align="center">Maximum current density</td>
				<td align="center">A/(cm^2)</td>
			</tr>
			<tr>
				<td align="center">N</td>
				<td align="center">Number of single cells</td>
				<td align="center">--</td>
			</tr>
				
		</table> 
		</html>
		* For more information about this model visit <a href="https://github.com/ECSIM/opem/blob/master/Documents/Amphlett.ipynb">here</a>
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
				<td align="center">Fuel cell reversible no loss voltage</td>
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
				<td align="center">Number of single cells</td>
				<td align="center">--</td>
			</tr>
				
		</table>
		</html>
		* For more information about this model visit <a href="https://github.com/ECSIM/opem/blob/master/Documents/Larminie_Dicks.ipynb">here</a>
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
				<td align="center">Number of single cells</td>
				<td align="center">--</td>
			</tr>
				
		</table>
		</html>
		* For more information about this model visit <a href="https://github.com/ECSIM/opem/blob/master/Documents/Chamberline_Kim.ipynb">here</a>
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
				<td align="center">Fuel cell temperature</td>
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
				<td align="center">Fuel cell internal resistance</td>
				<td align="center">ohm</td>
			</tr>
			<tr>
				<td align="center">rho</td>
				<td align="center">Hydrogen-Oxygen flow ratio</td>
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
		* For more information about this model visit <a href="https://github.com/ECSIM/opem/blob/master/Documents/Padulles1.ipynb">here</a>				

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
				<td align="center">Fuel cell temperature</td>
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
				<td align="center">Fuel cell internal resistance</td>
				<td align="center">ohm</td>
			</tr>
			<tr>
				<td align="center">rho</td>
				<td align="center">Hydrogen-Oxygen flow ratio</td>
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
		* For more information about this model visit <a href="https://github.com/ECSIM/opem/blob/master/Documents/Padulles2.ipynb">here</a>
	6. Padulles-Hauer Dynamic Model
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
				<td align="center">Fuel cell temperature</td>
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
				<td align="center">Fuel cell internal resistance</td>
				<td align="center">ohm</td>
			</tr>
			<tr>
				<td align="center">rho</td>
				<td align="center">Hydrogen-Oxygen flow ratio</td>
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
		* For more information about this model visit <a href="https://github.com/ECSIM/opem/blob/master/Documents/Padulles_Hauer.ipynb">here</a>
	7. Padulles-Amphlett Dynamic Model
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
				<td align="center">Fuel cell temperature</td>
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
				<td align="center">A</td>
				<td align="center">Active area</td>
				<td align="center">cm^2</td>
			</tr>
			<tr>
				<td align="center">l</td>
				<td align="center">Membrane thickness</td>
				<td align="center">cm</td>
			</tr>
			<tr>
				<td align="center">lambda</td>
				<td align="center">An adjustable parameter with a min value of 14 and max value of 23</td>
				<td align="center">--</td>
			</tr>
			<tr>
				<td align="center">R(*Optional)</td>
				<td align="center">R-Electronic</td>
				<td align="center">ohm</td>
			</tr>
			<tr>
				<td align="center">B</td>
				<td align="center">An empirical constant depending on the cell and its operation state (Tafel slope)</td>
				<td align="center">V</td>
			</tr>
			<tr>
				<td align="center">JMax</td>
				<td align="center">Maximum current density</td>
				<td align="center">A/(cm^2)</td>
			</tr>
			<tr>
				<td align="center">CV</td>
				<td align="center">Conversion factor</td>
				<td align="center">--</td>
			</tr>
			<tr>
				<td align="center">rho</td>
				<td align="center">Hydrogen-Oxygen flow ratio</td>
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
		* For more information about this model visit <a href="https://github.com/ECSIM/opem/blob/master/Documents/Padulles_Amphlett.ipynb">here</a>
		
		
	- Find your reports in `Model_Name` folder			
	
	#### Screen Record
	<div align="center">
		<a href="https://asciinema.org/a/170416" target="_blank"><img src="https://asciinema.org/a/170416.png" /></a>
		<p>Screen Record</p>
	</div>

### Library				


1. Amphlett Static Model
	```pycon
	>>> from opem.Static.Amphlett import Static_Analysis
	>>> Test_Vector={"T": 343.15,"PH2": 1,"PO2": 1,"i-start": 0,"i-stop": 75,"i-step": 0.1,"A": 50.6,"l": 0.0178,"lambda": 23,"N": 1,"R": 0,"JMax": 1.5,"B": 0.016,"Name": "Amphlett_Test"}
	>>> data=Static_Analysis(InputMethod=Test_Vector,TestMode=True,PrintMode=False,ReportMode=False)
	 ```
	<html>
		<table>
			<tr>
				<td align="center" >Key</td>
				<td align="center">Description</td>
				<td  align="center">Type</td>
			</tr>
			<tr>
				<td align="center" >Status</td>
				<td align="center">Simulation status</td>
				<td  align="center">Bool</td>
			</tr>
			<tr>
				<td align="center" >P</td>
				<td align="center">Power</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >I</td>
				<td align="center">Cell operating current</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >V</td>
				<td align="center">FC voltage</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >EFF</td>
				<td align="center">Efficiency</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >Ph</td>
				<td align="center">Thermal power</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >V0</td>
				<td align="center">Linear-Apx intercept</td>
				<td  align="center">Float</td>
			</tr>
			<tr>
				<td align="center" >K</td>
				<td align="center">Linear-Apx slope</td>
				<td  align="center">Float</td>
			</tr>
			<tr>
				<td align="center" >Eta_Active</td>
				<td align="center">Eta activation</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >Eta_Conc</td>
				<td align="center">Eta concentration</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >Eta_Ohmic</td>
				<td align="center">Eta ohmic</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >VE</td>
				<td align="center">Estimated FC voltage</td>
				<td  align="center">List</td>
			</tr>
		</table>
		</html>
		
	- For more information about this model visit <a href="https://github.com/ECSIM/opem/blob/master/Documents/Amphlett.ipynb">here</a>
2. Larminie-Dicks Static Model
	```pycon
	>>> from opem.Static.Larminie_Dicks import Static_Analysis
	>>> Test_Vector = {"A": 0.0587,"E0": 1.178,"B": 0.0517,"RM": 0.0018,"i_0": 0.00654,"i_L": 100.0,"i_n": 0.23,"N": 23,"i-start": 0.1,"i-stop": 98,"i-step": 0.1,"Name": "Larminiee_Test"}
	>>> data=Static_Analysis(InputMethod=Test_Vector,TestMode=True,PrintMode=False,ReportMode=False)
	 ```
	<html>
		<table>
			<tr>
				<td align="center" >Key</td>
				<td align="center">Description</td>
				<td  align="center">Type</td>
			</tr>
			<tr>
				<td align="center" >Status</td>
				<td align="center">Simulation status</td>
				<td  align="center">Bool</td>
			</tr>
			<tr>
				<td align="center" >P</td>
				<td align="center">Power</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >I</td>
				<td align="center">Cell operating current</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >V</td>
				<td align="center">FC voltage</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >EFF</td>
				<td align="center">Efficiency</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >Ph</td>
				<td align="center">Thermal power</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >V0</td>
				<td align="center">Linear-Apx intercept</td>
				<td  align="center">Float</td>
			</tr>
			<tr>
				<td align="center" >K</td>
				<td align="center">Linear-Apx slope</td>
				<td  align="center">Float</td>
			</tr>
			<tr>
				<td align="center" >VE</td>
				<td align="center">Estimated FC voltage</td>
				<td  align="center">List</td>
			</tr>
		</table>
		</html>	
			
	- For more information about this model visit <a href="https://github.com/ECSIM/opem/blob/master/Documents/Larminie_Dicks.ipynb">here</a>
3. Chamberline-Kim Static Model
	```pycon
	>>> from opem.Static.Chamberline_Kim import Static_Analysis
	>>> Test_Vector = {"A": 50.0,"E0": 0.982,"b": 0.0689,"R": 0.328,"m": 0.000125,"n": 9.45,"N": 1,"i-start": 1,"i-stop": 42.5,"i-step": 0.1,"Name": "Chamberline_Test"}
	>>> data=Static_Analysis(InputMethod=Test_Vector,TestMode=True,PrintMode=False,ReportMode=False)
	```
	<html>
		<table>
			<tr>
				<td align="center" >Key</td>
				<td align="center">Description</td>
				<td  align="center">Type</td>
			</tr>
			<tr>
				<td align="center" >Status</td>
				<td align="center">Simulation status</td>
				<td  align="center">Bool</td>
			</tr>
			<tr>
				<td align="center" >P</td>
				<td align="center">Power</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >I</td>
				<td align="center">Cell operating current</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >V</td>
				<td align="center">FC voltage</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >EFF</td>
				<td align="center">Efficiency</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >Ph</td>
				<td align="center">Thermal power</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >V0</td>
				<td align="center">Linear-Apx intercept</td>
				<td  align="center">Float</td>
			</tr>
			<tr>
				<td align="center" >K</td>
				<td align="center">Linear-Apx slope</td>
				<td  align="center">Float</td>
			</tr>
			<tr>
				<td align="center" >VE</td>
				<td align="center">Estimated FC voltage</td>
				<td  align="center">List</td>
			</tr>
		</table>
		</html>
			
	- For more information about this model visit <a href="https://github.com/ECSIM/opem/blob/master/Documents/Chamberline_Kim.ipynb">here</a>
4. Padulles Dynamic Model I
	```pycon
	>>> from opem.Dynamic.Padulles1 import Dynamic_Analysis
	>>> Test_Vector = {"T": 343,"E0": 0.6,"N0": 88,"KO2": 0.0000211,"KH2": 0.0000422,"tH2": 3.37,"tO2": 6.74,"B": 0.04777,"C": 0.0136,"Rint": 0.00303,"rho": 1.168,"qH2": 0.0004,"i-start": 0,"i-stop": 100,"i-step": 0.1,"Name": "PadullesI_Test"}
	>>> data=Dynamic_Analysis(InputMethod=Test_Vector,TestMode=True,PrintMode=False,ReportMode=False)
	```
	<html>
		<table>
			<tr>
				<td align="center" >Key</td>
				<td align="center">Description</td>
				<td  align="center">Type</td>
			</tr>
			<tr>
				<td align="center" >Status</td>
				<td align="center">Simulation status</td>
				<td  align="center">Bool</td>
			</tr>
			<tr>
				<td align="center" >P</td>
				<td align="center">Power</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >I</td>
				<td align="center">Cell operating current</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >V</td>
				<td align="center">FC voltage</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >EFF</td>
				<td align="center">Efficiency</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >PO2</td>
				<td align="center">Partial pressure</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >PH2</td>
				<td align="center">Partial pressure</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >Ph</td>
				<td align="center">Thermal power</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >V0</td>
				<td align="center">Linear-Apx intercept</td>
				<td  align="center">Float</td>
			</tr>
			<tr>
				<td align="center" >K</td>
				<td align="center">Linear-Apx slope</td>
				<td  align="center">Float</td>
			</tr>
			<tr>
				<td align="center" >VE</td>
				<td align="center">Estimated FC voltage</td>
				<td  align="center">List</td>
			</tr>
		</table>
		</html>
	
	- For more information about this model visit <a href="https://github.com/ECSIM/opem/blob/master/Documents/Padulles1.ipynb">here</a>
5. Padulles Dynamic Model II
	```pycon
	>>> from opem.Dynamic.Padulles2 import Dynamic_Analysis
	>>> Test_Vector = {"T": 343,"E0": 0.6,"N0": 5,"KO2": 0.0000211,"KH2": 0.0000422,"KH2O": 0.000007716,"tH2": 3.37,"tO2": 6.74,"tH2O": 18.418,"B": 0.04777,"C": 0.0136,"Rint": 0.00303,"rho": 1.168,"qH2": 0.0004,"i-start": 0.1,"i-stop": 100,"i-step": 0.1,"Name": "Padulles2_Test"}
	>>> data=Dynamic_Analysis(InputMethod=Test_Vector,TestMode=True,PrintMode=False,ReportMode=False)
	```
	<html>
		<table>
			<tr>
				<td align="center" >Key</td>
				<td align="center">Description</td>
				<td  align="center">Type</td>
			</tr>
			<tr>
				<td align="center" >Status</td>
				<td align="center">Simulation status</td>
				<td  align="center">Bool</td>
			</tr>
			<tr>
				<td align="center" >P</td>
				<td align="center">Power</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >I</td>
				<td align="center">Cell operating current</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >V</td>
				<td align="center">FC voltage</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >EFF</td>
				<td align="center">Efficiency</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >PO2</td>
				<td align="center">Partial pressure</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >PH2</td>
				<td align="center">Partial pressure</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >PH2O</td>
				<td align="center">Partial pressure</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >Ph</td>
				<td align="center">Thermal power</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >V0</td>
				<td align="center">Linear-Apx intercept</td>
				<td  align="center">Float</td>
			</tr>
			<tr>
				<td align="center" >K</td>
				<td align="center">Linear-Apx slope</td>
				<td  align="center">Float</td>
			</tr>
			<tr>
				<td align="center" >VE</td>
				<td align="center">Estimated FC voltage</td>
				<td  align="center">List</td>
			</tr>
		</table>
		</html>
				
	- For more information about this model visit <a href="https://github.com/ECSIM/opem/blob/master/Documents/Padulles2.ipynb">here</a>
6. Padulles-Hauer Dynamic Model
	```pycon
	>>> from opem.Dynamic.Padulles_Hauer import Dynamic_Analysis
	>>> Test_Vector = {"T": 343,"E0": 0.6,"N0": 5,"KO2": 0.0000211,"KH2": 0.0000422,"KH2O": 0.000007716,"tH2": 3.37,"tO2": 6.74,"t1": 2,"t2": 2,"tH2O": 18.418,"B": 0.04777,"C": 0.0136,"Rint": 0.00303,"rho": 1.168,"qMethanol": 0.0002,"CV": 2,"i-start": 0.1,"i-stop": 100,"i-step": 0.1,"Name": "Padulles_Hauer_Test"}
	>>> data=Dynamic_Analysis(InputMethod=Test_Vector,TestMode=True,PrintMode=False,ReportMode=False)
	```
	<html>
		<table>
			<tr>
				<td align="center" >Key</td>
				<td align="center">Description</td>
				<td  align="center">Type</td>
			</tr>
			<tr>
				<td align="center" >Status</td>
				<td align="center">Simulation status</td>
				<td  align="center">Bool</td>
			</tr>
			<tr>
				<td align="center" >P</td>
				<td align="center">Power</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >I</td>
				<td align="center">Cell operating current</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >V</td>
				<td align="center">FC voltage</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >EFF</td>
				<td align="center">Efficiency</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >PO2</td>
				<td align="center">Partial pressure</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >PH2</td>
				<td align="center">Partial pressure</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >PH2O</td>
				<td align="center">Partial pressure</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >Ph</td>
				<td align="center">Thermal power</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >V0</td>
				<td align="center">Linear-Apx intercept</td>
				<td  align="center">Float</td>
			</tr>
			<tr>
				<td align="center" >K</td>
				<td align="center">Linear-Apx slope</td>
				<td  align="center">Float</td>
			</tr>
			<tr>
				<td align="center" >VE</td>
				<td align="center">Estimated FC voltage</td>
				<td  align="center">List</td>
			</tr>
		</table>
		</html>
			
	- For more information about this model visit <a href="https://github.com/ECSIM/opem/blob/master/Documents/Padulles_Hauer.ipynb">here</a>
7. Padulles-Amphlett Dynamic Model
	```pycon
	>>> from opem.Dynamic.Padulles_Amphlett import Dynamic_Analysis
	>>> Test_Vector = {"A": 50.6,"l": 0.0178,"lambda": 23,"JMax": 1.5,"T": 343,"N0": 5,"KO2": 0.0000211,"KH2": 0.0000422,"KH2O": 0.000007716,"tH2": 3.37,"tO2": 6.74,"t1": 2,"t2": 2,"tH2O": 18.418,"B": 0.016,"rho": 1.168,"qMethanol": 0.0002,"CV": 2,"i-start": 0.1,"i-stop": 75,"i-step": 0.1,"Name": "Padulles_Amphlett_Test"}
	>>> data=Dynamic_Analysis(InputMethod=Test_Vector,TestMode=True,PrintMode=False,ReportMode=False)
	```
	<html>
		<table>
			<tr>
				<td align="center" >Key</td>
				<td align="center">Description</td>
				<td  align="center">Type</td>
			</tr>
			<tr>
				<td align="center" >Status</td>
				<td align="center">Simulation status</td>
				<td  align="center">Bool</td>
			</tr>
			<tr>
				<td align="center" >P</td>
				<td align="center">Power</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >I</td>
				<td align="center">Cell operating current</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >V</td>
				<td align="center">FC voltage</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >EFF</td>
				<td align="center">Efficiency</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >PO2</td>
				<td align="center">Partial pressure</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >PH2</td>
				<td align="center">Partial pressure</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >PH2O</td>
				<td align="center">Partial pressure</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >Ph</td>
				<td align="center">Thermal power</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >V0</td>
				<td align="center">Linear-Apx intercept</td>
				<td  align="center">Float</td>
			</tr>
			<tr>
				<td align="center" >K</td>
				<td align="center">Linear-Apx slope</td>
				<td  align="center">Float</td>
			</tr>
			<tr>
				<td align="center" >Eta_Active</td>
				<td align="center">Eta activation</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >Eta_Conc</td>
				<td align="center">Eta concentration</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >Eta_Ohmic</td>
				<td align="center">Eta ohmic</td>
				<td  align="center">List</td>
			</tr>
			<tr>
				<td align="center" >VE</td>
				<td align="center">Estimated FC voltage</td>
				<td  align="center">List</td>
			</tr>
		</table>
		</html>
									
	- For more information about this model visit <a href="https://github.com/ECSIM/opem/blob/master/Documents/Padulles_Amphlett.ipynb">here</a>

	#### Modes	

	1. `TestMode` : Active test mode and get/return data as `dict`, (Default : `False`)
	2. `ReportMode` : Generate reports(`.csv`,`.opem`,`.html`) and print result in console, (Default : `True`)
	3. `PrintMode` : Control printing in console, (Default : `True`)
	
	#### Note
	
	- Return type : `dict`


### Telegram Bot
- Send `/start` command to [OPEM BOT](https://t.me/opembot)
- Choose models from menu
- Send your test vector according to the template
- Download your results


### Try OPEM in Your Browser!
OPEM can be used online in interactive Jupyter Notebooks via the Binder service! Try it out now! :	


[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ECSIM/opem/master)

- Check `.ipynb` files in `Documents` folder
- Edit and execute each part of the notes, step by step from the top panel by run button
- For executing a complete simulation, you can edit `Test_Vector` in `Full Run` section
		

## Issues & Bug Reports			

Just fill an issue and describe it. We'll check it ASAP!							
or send an email to [opem@ecsim.ir](mailto:opem@ecsim.ir "opem@ecsim.ir"). 

Gitter is another option :				

[![Gitter](https://badges.gitter.im/ECSIM/opem.svg)](https://gitter.im/ECSIM/opem?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)


## Todo		

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
- [x] GUI
  - [x] Plot Graphs
  - [x] Input/Output
- [x] Dynamic Analysis
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
  - [x] Padulles-Amphlett Dynamic Model
    - [x] Nernst Voltage
  	- [x] Voltage of PEMFC
  	- [x] Power of PEMFC
  	- [x] Efficiency of PEMFC
- [x] MATLAB

## Outputs	

1. [HTML](http://www.ecsim.ir/opem/outputs/test.html)
2. [CSV](https://github.com/ECSIM/opem/blob/master/otherfile/test.csv)
3. [OPEM](https://github.com/ECSIM/opem/blob/master/otherfile/test.opem)	

## Dependencies

<table>
	<tr> 
		<td align="center">master</td>	
		<td align="center">develop</td>	
	</tr>
	<tr>
		<td align="center"><a href="https://requires.io/github/ECSIM/opem/requirements/?branch=master"><img src="https://requires.io/github/ECSIM/opem/requirements.svg?branch=master" alt="Requirements Status" /></a></td>
		<td align="center"><a href="https://requires.io/github/ECSIM/opem/requirements/?branch=develop"><img src="https://requires.io/github/ECSIM/opem/requirements.svg?branch=develop" alt="Requirements Status" /></a></td>
	</tr>
</table>


## Thanks

* [Chart.js](https://github.com/chartjs/Chart.js "Chartjs")
* [PyInstaller](https://github.com/pyinstaller/pyinstaller)
* [Draw.io](https://www.draw.io/)

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

<blockquote>
7- A. Saadi, M. Becherif, A. Aboubou, M.Y. Ayad. 2013. "Comparison of proton exchange membrane fuel cell static models." Renewable Energy (Elsevier) 56: 64-71. doi:dx.doi.org/10.1016/j.renene.2012.10.012.
</blockquote>

<blockquote>
8- Diego Feroldi, Marta Basualdo. 2012. "Description of PEM Fuel Cells System." Green Energy and Technology (Springer) 49-72. doi:10.1007/978-1-84996-184-4_2
</blockquote>

<blockquote>
9- Gottesfeld, Shimshon. n.d. The Polymer Electrolyte Fuel Cell: Materials Issues in a Hydrogen Fueled Power Source.
 http://physics.oregonstate.edu/~hetheriw/energy/topics/doc/electrochemistry/fc/basic/The_Polymer_Electrolyte_Fuel_Cell.htm
</blockquote>

<blockquote>
10- Mohamed Becherif, Aïcha Saadi, Daniel Hissel, Abdennacer Aboubou, Mohamed Yacine Ayad. 2011.
 "Static and dynamic proton exchange membrane fuel cell models." Journal of Hydrocarbons Mines and Environmental Research 2 (1)
</blockquote>

## Cite

If you use OPEM in your research , please cite this paper :

<pre>

@article{Haghighi2018,
  doi = {10.21105/joss.00676},
  url = {https://doi.org/10.21105/joss.00676},
  year  = {2018},
  month = {jul},
  publisher = {The Open Journal},
  volume = {3},
  number = {27},
  pages = {676},
  author = {Sepand Haghighi and Kasra Askari and Sarmin Hamidi and Mohammad Mahdi Rahimi},
  title = {{OPEM} : Open Source {PEM} Cell Simulation Tool},
  journal = {Journal of Open Source Software}
}


</pre>

Download [OPEM.bib](http://www.ecsim.ir/opem/OPEM.bib)(BibTeX Format)


<table>
	<tr> 
		<td align="center">JOSS</td>
		<td align="center"><a style="border-width:0" href="https://doi.org/10.21105/joss.00676"><img src="http://joss.theoj.org/papers/10.21105/joss.00676/status.svg" alt="DOI badge" ></a></td>	
	</tr>
	<tr>
		<td align="center">Zenodo</td>
		<td align="center"><a href="https://doi.org/10.5281/zenodo.1133110"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.1133110.svg" alt="DOI"></a></td>
	</tr>
	<tr>
		<td align="center">Researchgate</td>
		<td align="center"><a href="https://www.researchgate.net/project/Open-Source-Electrochemistry-Simulation-Toolbox"><img src="https://img.shields.io/badge/Researchgate-OPEM-yellow.svg"></a></td>
	</tr>
</table>									






## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2FECSIM%2Fopem.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2FECSIM%2Fopem?ref=badge_large)


## Donate to our project
								
<h3>Bitcoin :</h3>					

```12Xm1qL4MXYWiY9sRMoa3VpfTfw6su3vNq```			



<h3>Payping (For Iranian citizens) :</h3>

<a href="http://www.payping.net/sepandhaghighi" target="__blank"><img src="http://www.qpage.ir/images/payping.png" height=100px width=100px></a>	


<h3>Say Thanks! </h3>

<a href="https://saythanks.io/to/ecsim"><img src="https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg"></a>
