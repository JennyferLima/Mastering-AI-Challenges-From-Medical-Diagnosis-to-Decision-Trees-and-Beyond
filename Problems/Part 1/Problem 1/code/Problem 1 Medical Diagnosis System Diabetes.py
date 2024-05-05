# -*- coding: utf-8 -*-
"""Medical Diagnosis System Diabetes

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12_ZdYKakNew8fQIb3GMKKpo3M1X48KSU

# Part 1:

#### Consider the following scenario, along with the observations, for the question involving the 3 problems described below, from which you will choose 2.Using some Artificial Intelligence tool, as suggested in each question from 1 to 3, build and implement a solution for 2 of the following 3 problems, considering a Knowledge-Based System approach (rule-based and/or case-based), with the functionalities present in the conceptual architecture presented during the course and shown below, namely: knowledge base, inference engine, explainability, and user interface.
\\
#### Note 1: Consider, as a suggestion, possible inspiration from the functionalities of the old Mycin System (knowledge representation in the form of rules, inference engine with backward chaining and depth-first search, explanation, interaction with users in natural language), as presented in class. Alternatively, you could consider knowledge representation through a Bayesian network, or fuzzy rules, or even a case base.
\\
#### Note 2: For building the knowledge base, which should be done automatically or semi-automatically, consider an available database, then apply machine learning techniques (as seen in detail in class).
\\
#### Problem 1: Medical diagnostic aid system for a specific disease (e.g., Type 2 Diabetes) or a range of diseases. Functionally, the system will consider as input patient data on signs and symptoms, collected in the interaction of the system with the patient.

#### Note: I suggest a knowledge representation approach via Bayesian network, making use of the Netica tool. Alternatively, you could use a rule-based tool, such as Expert Sinta, or even Drools, or any other you may choose.
\\
#### Problem 2: System for credit risk analysis in a particular bank, considering the example discussed and developed in the classroom, whose statement is described below. Develop a Knowledge-based System to fulfill the task of deciding on the risk of lending money to each of its clients' demands, also having the characteristic of justifying each decision provided. Consider 3 risk categories: High, Moderate, and Low.

#### (i) Invest in modeling, including the identification of attributes (variables) that are relevant to compose the input for the risk classification model, and implement a solution to this problem with the help of an appropriate tool.
#### (ii) Present a test plan for the developed system.
\\
#### Note: I suggest a knowledge representation and reasoning approach via rules of the IF... THEN... type. Thus, you could use a rule-based tool, such as Expert Sinta, or even Drools, or any other you choose. Alternatively, you could use a knowledge representation and reasoning approach via a Bayesian network, making use of the Netica tool, or use fuzzy logic, making use of the Scikit Fuzzy tool.

\\

---


**This notebook only contains the solution to problem 1.**
"""

# Install the required libraries
!pip install pgmpy

# Import the necessary classes
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Define the state names for the symptoms
state_names = {'Symptom1': ['Absent', 'Present'],
               'Symptom2': ['Absent', 'Present'],
               'Symptom3': ['Absent', 'Present'],
               'Diagnosis': ['Negative', 'Positive']}

# Define the structure of the Bayesian network
structure = [('Symptom1', 'Diagnosis'), ('Symptom2', 'Diagnosis'), ('Symptom3', 'Diagnosis')]

# Build the Bayesian network
model = BayesianNetwork(structure)

# Define the conditional probability distributions (CPDs) for the symptoms
cpd_symptom1 = TabularCPD(variable='Symptom1', variable_card=2, values=[[0.5], [0.5]], state_names=state_names)
cpd_symptom2 = TabularCPD(variable='Symptom2', variable_card=2, values=[[0.6], [0.4]], state_names=state_names)
cpd_symptom3 = TabularCPD(variable='Symptom3', variable_card=2, values=[[0.7], [0.3]], state_names=state_names)

# Define CPD for the Diagnosis
cpd_diagnosis = TabularCPD(variable='Diagnosis', variable_card=2,
                            values=[[0.8, 0.2, 0.6, 0.4, 0.5, 0.5, 0.3, 0.7],  # Probabilidade de diagnóstico dado os sintomas
                                    [0.2, 0.8, 0.4, 0.6, 0.5, 0.5, 0.7, 0.3]],
                            evidence=['Symptom1', 'Symptom2', 'Symptom3'],
                            evidence_card=[2, 2, 2],
                            state_names=state_names)

# Add CPDs to the model
model.add_cpds(cpd_symptom1, cpd_symptom2, cpd_symptom3, cpd_diagnosis)

# Check the model consistency
model.check_model()

# Perform inference
inference = VariableElimination(model)

# Function to perform diagnosis based on the observed symptoms
def perform_diagnosis(symptom1, symptom2, symptom3):
    evidence = {'Symptom1': symptom1, 'Symptom2': symptom2, 'Symptom3': symptom3}
    probability = inference.query(variables=['Diagnosis'], evidence=evidence)
    return probability

# Define symptom data
symptom1 = 'Present'
symptom2 = 'Absent'
symptom3 = 'Present'

# Get the diagnosis
result = perform_diagnosis(symptom1, symptom2, symptom3)
print("Probability of Diagnosis:", result)