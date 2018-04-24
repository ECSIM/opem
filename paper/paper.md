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
The sun and wind as renewable energy sources‏ are attracting more regard as alternative energy sources. In addition to the decreasing fuel sources, pollution and global warming‏ are important problems. Fuel cells are a beneficial energy technology that generates electric energy through the reaction between the fuel sources rich in hydrogen and oxygen. In comparsion with combustion engines, fuel cells have many advantages,  such as high efficiency and low emissions. Furthermore the by-products of fuel cells are heat and water. Proton exchange membrane fuel cells (PEMFCs) have attracted much interests recently. PEM fuel cells are Pollution-Free high-efficiency power sources for urban vehicles that recently corporate by legislative initiatives. Previously, some research on modeling and simulation of PEMFC has been performed [@Secanell2014]. The fundamental structure of a PEMFC can be described as two electrodes (anode and cathode) separated by a solid polymer membrane that acting as an electrolyte. The hydrogen gas is the Best fuel for fuel cell powered vehicles, because of the highest conversion efficiency for fuel, generating zero tail-pipe emission and producing water as an only product of the reaction between hydrogen and air .By flowing hydrogen fuel through a network of channels to the anode, hydrogen separates into protons that transfer via the membrane to the cathode. Collection of electrons in the two electrodes causes the creation of electrical current in an electrical circuit that linked to the electrodes. Through a similar network of channels the oxygen that comes from the air, named oxidant, flows to the cathode and then, the electrons coming from the external electrical circuit will be received by oxygen and finally, produce water and heat from the protons that flow via the electrolyte membrane [@Feroldi2011; @Gottesfeld1999].

With a valid mathematical model, PEMFC system performance can be better understood. Moreover, the time and cost are reduced in the analysis and design of FC systems. Nowadays, programming in other sciences has a very special place because the importance of computers cannot be ignored as a very effective application in technical and research affairs. The OPEM software (open proton exchange membrane) written in Python Programming language that is very powerful for developers but is also accessible to scientists. Simulation models in PEMFC include dynamic and static models. Static models focus more on electrochemical techniques and can predict the performance of PEMFC. Simulated parametric models combined with the empirical approach that describes the important concepts such PEMFC polarization losses, efficiency, and Nernst voltage. Dynamic models improve static models and complete the simulation process. In dynamic models, the science of fluid and material merge with electrochemical principles and dynamic concepts.  Consideration the rules of absorption and penetration of gases based on their pressure and density, causes the simulation of fuel cell to be more accurate and higher quality. In addition, sometimes several terms should be made for calculations regarding fuel cell efficiency–power-size. For the applied operating range of most fuel cells, a linear estimation is practically a very good fit. Simple linear regression used for this approximation. Also applied overall parameters (such P(Thermal) and P(Electronic)) calculated by the Simpson’s rule. In this software inputs are parameters that each users can specify according to the equations of each models. outputs are in the three formats CSV, HTML, and OPEM. The block diagram of software shown in figure 1. 

![Block diagram of software](../otherfile/OPEM_BLOCK_DIAGRAM.jpg) 


# Supported models								

Supported models include two general categories of static models and dynamic models. Static models are briefly outlined here:							


## Amphlett analysis			

That main concepts include Nernst voltage, PEMFC losses (activation polarization loss, ohmic polarization loss, and concentration polarization loss), power and efficiency of the fuel cell [@Amphlett1995; @Correa2005; @Saadi2013].

## Larminie analysis				

That represent by means of voltage-current characteristic obtained in static operating mode. In fact, Larminie-Dicks static model presents the fuel cell voltage as a function of the current magnitude [@Sadli2006; @Saadi2013].

## Chamberline-Kim analysis

That is represented by means of its voltage-current characteristic obtained in static operating mode. In fact, Larminie-Dicks static model presents the fuel cell voltage as a function of the current magnitude [@Kim1995; @Saadi2013].

And also dynamic models include:								


## Padulles analysis I,II

That the temperatures and pressures of electrodes channel, transient response of cell voltage, gases outflow rates and the temperature of the cell under the sudden change in load current can be predicted. In the model I, Nernst and fuel cell potential were modeled as a function of oxygen and hydrogen gases partial pressure that can be calculated from independent variables or constants. Also in the model II, Nernst and fuel cell potential were modeled as a function of water, oxygen and hydrogen gases partial pressure that can be calculated from independent variables or constants [@Padulls2000].

## Padulles-Hauer analysis

That is a model includes a methanol reformer to generate hydrogen from methanol and the PEM stack and this is an advantage for dynamic simulation of padulles analysis [@Hauer2001; @Padulls2000]. 

## Padulles-Amphlett analysis

That is an integration of Padulles-Hauer dynamic model with Amphlett static model. The superiority of this model is using Amphlett equation for simulating the polarization values [@Padulls2000; @Hauer2001; @Amphlett1995]. 

 

Website : [opem.ecsim.ir](http://opem.ecsim.ir)


# References
