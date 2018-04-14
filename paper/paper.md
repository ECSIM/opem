---
title: 'OPEM : Open Source PEM Cell Simulation Tool'
tags:
  - electrochemistry
  - simulation
  - fuel-cell
  - pem
  - chemistry
  - static-analysis
  - dynamic-analysis
authors:
 - name: Sepand Haghighi
   orcid: 0000-0001-9450-2375
   affiliation: 1
 - name: Kasra Askari
   orcid: 0000-0001-7978-9291
   affiliation: 2
 - name: Sarmin Hamidi
   orcid: 0000-0002-4621-0180
   affiliation: 3
 - name: Mohammad Mahdi Rahimi
   orcid: 0000-0002-6614-4512
   affiliation: 4

affiliations:
 - name: Sharif University of Technology
   index: 1
 - name: Isfahan University of Technology
   index: 2
 - name: University of Tehran
   index: 3
 - name: Amirkabir University of Technology
   index: 4


date: 11 April 2018
bibliography: paper.bib
---
						

# Summary
The sun and wind as renewable energy sources‏ are attracting more regard as alternative energy sources. In addition to the decreasing fuel sources, also pollution and global warming‏ are important problems. Fuel cells are a beneficial energy technology that generates electric energy through the reaction between hydrogen-rich fuel source and oxygen. The advantage of these devices owing to high efficiency relative to combustion engines, low emissions and producing only heat and water as waste products. Proton exchange membrane fuel cells (PEMFCs) have attracted much interest recently. PEM fuel cells are a high-efficiency power source without pollution for urban vehicles, corroborated by recent legislative initiatives, That's why these devices have become a great deal of attention to the option of fuel-cell-powered vehicles. Previously, some research on modeling and simulation of PEMFC has been performed. The fundamental structure of a PEMFC can be described as two electrodes (anode and cathode) separated by a solid polymer membrane that acts as an electrolyte. Best fuel for fuel cell powered vehicle is hydrogen, this gas causing the highest conversion efficiency for fuel and generating zero tail-pipe emission because the water is an only product of the reaction between hydrogen and air. By flowing Hydrogen fuel through a network of channels to the anode, hydrogen separates into protons that, flow via the membrane to the cathode. An external circuit that linked to the two electrodes containing the collection of electrons as electrical current. Through a similar network of channels the oxygen that comes from the air, named oxidant, flows to the cathode and then, the electrons coming from the external electrical circuit will be received by oxygen and finally, water and heat will be produced from the protons that flowing via the electrolyte membrane.[@Feroldi2011; @Gottesfeld1999]

With a valid mathematical model, PEMFC system performance can be better understood. Moreover, the time and cost are reduced in the analysis and design of FC systems. Nowadays, programming in other sciences has a very special place because the importance of computers cannot be ignored as a very effective application in technical and research affairs. The OPEM (software named based on open proton exchange membrane) written in Python, Python is a language that is very powerful for developers, but is also accessible to scientists. Simulation models in PEMFC include dynamic and static models. Static models focus more on electrochemical techniques and can predict the performance of PEMFC. Simulated parametric models combined with the empirical approach that describes the important concepts such PEMFC polarization losses, efficiency, and Nernst voltage. In addition, dynamic models improve static models and complete the simulation process. In dynamic models, fluid science and material merge with electrochemical principles and dynamic concepts, by considering the rules of absorption and penetration of gases based on their pressure and density, make the simulation of fuel cell more accurate and high quality. Also, sometimes several terms should be made for calculations regarding fuel cell efficiency–power-size. For the applied operating range of most fuel cells, a linear estimation is practically a very good fit. Simple linear regression used for this approximation and useful overall parameters such P(Thermal) and P(Elec) calculated by Simpson's Rule. The method for using in this software is the specified inputs are presented according to the equations of each model by the user and outputs is in the three format CSV, HTML, and OPEM. The block diagram of software shown in figure 1.

![Block diagram of software](../otherfile/OPEM_BLOCK_DIAGRAM.jpg) 


# Supported models								

Supported models include two general categories of static models and dynamic models. Static models are briefly outlined here:							


## Amphlett analysis			

That main concepts include Nernst voltage, PEMFC losses (activation polarization loss, ohmic polarization loss, and concentration polarization loss), power and efficiency of the fuel cell.[@Amphlett1995; @Correa2005; @Saadi2013]

## Larminie analysis				

That was developed to proportionate the experimental cell potential (E) vs. current density (J) data for proton exchange membrane fuel cells (PEMFCs), at various pressures, temperatures, and oxygen compositions in the cathode gas mixture.[@Sadli2006; @Saadi2013]

## Chamberline-Kim analysis

That is represented by means of its voltage-current characteristic obtained in static operating mode. In fact, Larminie-Dicks static model presents the fuel cell voltage as a function of the current magnitude.[@Kim1995; @Saadi2013]

And also dynamic models include:								


## Padulles analysis I,II

That the electrodes channel temperatures/pressures, transient response of cell voltage, gases outflow rates and the temperature of the cell under the sudden change in load current can be predicted. In model I, Nernst and fuel cell potential were modeled as a function of oxygen and hydrogen gases partial pressure that can be calculated from independent variables or constants and in model II, Nernst and fuel cell potential were modeled as a function of water, oxygen and hydrogen gases partial pressure that can be calculated from independent variables or constants.[@Padulls2000]

## Padulles-Hauer analysis

That is a model includes a methanol reformer to generate hydrogen from methanol and the PEM stack and this is an advantage for dynamic simulation of padulles analysis. [@Hauer2001; @Padulls2000]

## Padulles-Amphlett analysis

That is an integration of Padulles-Hauer dynamic model with Amphlett static model. The superiority of this model is using Amphlett equation for simulating the polarization values. [@Padulls2000; @Hauer2001; @Amphlett1995]

 

Website : [opem.ecsim.ir](http://opem.ecsim.ir)


# References
