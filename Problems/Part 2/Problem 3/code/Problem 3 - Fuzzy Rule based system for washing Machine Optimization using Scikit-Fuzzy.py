# -*- coding: utf-8 -*-
"""Fuzzy Rule-Based System for Washing Machine Optimization using Scikit-Fuzzy.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TQZR7uiBx0bYN0vLkSrFgR8Lb8ktoDNQ

# Problem 3

#### Consider the fuzzy rule-based system, shown in [https://www.ime.unicamp.br/~valle/Teaching/MS580/Aula06.pdf], developed for automate the operation of a washing machine, aiming to save items such as detergent, water, electricity.


#### a) Discuss this application and present your knowledge base with fuzzy rules, as well as describe the modeling process,showing and discussing the membership functions used in the fuzzification stage, as well as the solution for the defuzzification), and discuss and show how the inference is made about knowledge.

#### b) Run and show this application running using the Scikit-Fuzzy tool, shown in class.

#### As delivery related to the issue, documentation is still expected with all the aforementioned modeling steps, as well as:
#### (i) Description of the problem, clearly indicating the objectives of the application, the variables used;
####(ii) Description of the solution;
####(iii) Share the notebook used by using Scikit-Fuzzy.

#### Note: Consider Mamdani's methodology and inference.


---



**This notebook only contains the solution to alternative b.**
"""

!pip install scikit-fuzzy

import numpy as np
from skfuzzy import control as ctrl
from skfuzzy import membership as mf

# Define the input and output variables
weight = ctrl.Antecedent(np.arange(0, 11, 1), 'weight')
dirt = ctrl.Antecedent(np.arange(0, 11, 1), 'dirt')
detergent = ctrl.Consequent(np.arange(0, 11, 1), 'detergent')

# Define the membership functions for the input variables
weight['Very Light'] = mf.trimf(weight.universe, [0, 0, 2])
weight['Light'] = mf.trimf(weight.universe, [1, 3, 5])
weight['Heavy'] = mf.trimf(weight.universe, [4, 6, 8])
weight['Very Heavy'] = mf.trimf(weight.universe, [7, 10, 10])

dirt['Almost Clean'] = mf.trimf(dirt.universe, [0, 0, 2])
dirt['Dirty'] = mf.trimf(dirt.universe, [1, 3, 5])
dirt['Very Dirty'] = mf.trimf(dirt.universe, [4, 6, 8])
dirt['Extra Dirty'] = mf.trimf(dirt.universe, [7, 10, 10])

# Define the membership functions for the output variable
detergent['Very Little'] = mf.trimf(detergent.universe, [0, 0, 2])
detergent['Little'] = mf.trimf(detergent.universe, [1, 3, 5])
detergent['Moderate'] = mf.trimf(detergent.universe, [3, 5, 7])
detergent['Exaggerated'] = mf.trimf(detergent.universe, [6, 8, 10])
detergent['Maximum'] = mf.trimf(detergent.universe, [9, 10, 10])

# Define the fuzzy rules
rule1 = ctrl.Rule(weight['Very Light'] & dirt['Almost Clean'], detergent['Very Little'])
rule2 = ctrl.Rule(weight['Very Light'] & dirt['Dirty'], detergent['Little'])
rule3 = ctrl.Rule(weight['Very Light'] & dirt['Very Dirty'], detergent['Moderate'])
rule4 = ctrl.Rule(weight['Very Light'] & dirt['Extra Dirty'], detergent['Moderate'])
rule5 = ctrl.Rule(weight['Light'] & dirt['Almost Clean'], detergent['Little'])
rule6 = ctrl.Rule(weight['Light'] & dirt['Dirty'], detergent['Little'])
rule7 = ctrl.Rule(weight['Light'] & dirt['Very Dirty'], detergent['Exaggerated'])
rule8 = ctrl.Rule(weight['Light'] & dirt['Extra Dirty'], detergent['Exaggerated'])
rule9 = ctrl.Rule(weight['Heavy'] & dirt['Almost Clean'], detergent['Moderate'])
rule10 = ctrl.Rule(weight['Heavy'] & dirt['Dirty'], detergent['Exaggerated'])
rule11 = ctrl.Rule(weight['Heavy'] & dirt['Very Dirty'], detergent['Exaggerated'])
rule12 = ctrl.Rule(weight['Heavy'] & dirt['Extra Dirty'], detergent['Maximum'])
rule13 = ctrl.Rule(weight['Very Heavy'] & dirt['Almost Clean'], detergent['Exaggerated'])
rule14 = ctrl.Rule(weight['Very Heavy'] & dirt['Dirty'], detergent['Maximum'])
rule15 = ctrl.Rule(weight['Very Heavy'] & dirt['Very Dirty'], detergent['Maximum'])
rule16 = ctrl.Rule(weight['Very Heavy'] & dirt['Extra Dirty'], detergent['Maximum'])

# Create the fuzzy control system
system = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15, rule16])

# Create the simulation
simulation = ctrl.ControlSystemSimulation(system)

# Set the input values
simulation.input['weight'] = 3
simulation.input['dirt'] = 4

# Run the simulation
simulation.compute()

# Display the output value
print("Detergent amount:", simulation.output['detergent'])