#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 19:29:24 2020

@author: christinasusangoss
"""
# List of touples that are of the form ('Name', height, parent-height)
groups1 = [('A', 0.05, 0.06), ('D', 0.06, 0.21), ('K', 0.21, 0.22), ('P', 0.22, 0.25),\
          ('M', 0.21, 0.25), ('R', 0.25, 0.38), ('Z', 0.38, 0.39), ('AA', 0.39, 0.42),\
          ('DD', 0.42, 0.47), ('II', 0.47, 0.5), ('GG', 0.45, 0.5), ('JJ', 0.5, 0.9)]
# May want to define a second set of groups once we figure out the alternative likeihoods

# Data that will be used, data of type (object number, 'Group')
data = []
# Maybe create function to take an object number and give it the right group label

# Check if data is consistent with hypothesis
def data_is_consistent_with_hypothesis(data_point,hypothesis): 
    if data == 'A':
        return hypothesis in ['A', 'D', 'K', 'P', 'R', 'Z', 'AA', 'DD', 'II', 'JJ']
    elif data == 'D':
        return hypothesis in ['D', 'K', 'P', 'R', 'Z', 'AA', 'DD', 'II', 'JJ']
    elif data == 'K':
        return hypothesis in ['K', 'P', 'R', 'Z', 'AA', 'DD', 'II', 'JJ']
    elif data == 'P':
        return hypothesis in ['P', 'R', 'Z', 'AA', 'DD', 'II', 'JJ']
    elif data == 'M':
        return hypothesis in ['M', 'R', 'Z', 'AA', 'DD', 'II', 'JJ']
    elif data == 'Z':
        return hypothesis in ['Z', 'AA', 'DD', 'II', 'JJ']
    elif data == 'AA':
        return hypothesis in ['AA', 'DD', 'II', 'JJ']
    elif data == 'DD':
        return hypothesis in ['DD', 'II', 'JJ']
    elif data == 'II':
        return hypothesis in ['II', 'JJ']
    elif data == 'GG':
        return hypothesis in ['GG', 'JJ']
    
def Plausible_Hypotheses(data, groups): # Creates a list of plausible hypotheses    
    
def Literal_probability(): # The classic probability function
    # (1/size(h))^n + P(h)/sum of all possible hypotheses
    
def Literal_likelihood(data, hypothesis): # Create literal likelihood    
    
def Pragmatic_Likelihood(data, hypothesis): # Calculate the pragmatically reasoned liklihood
    # literal probability of h|data/ sum over all hypotheses -> do we add a prior
    # and what is it?

# Stealing a lot of this from wordlearning.py   
# likelihood = 0 if classic, likelihood = 1 if pragmatic
def Posteriors(data, groups, likelihood): #Calculate the appropriate posteriors
    # We will use the variable normalizing_constant to keep track of the denominator in Bayes rule
    normalizing_constant = 0	
    # We define a dictionary, posteriors, that will keep track of each hypothesis' posterior probability
    # It will eventually have six keys (one corresponding to each hypothesis), which will have posteriors as values		 
    posteriors = {}	
    
    # Create a list of plausible hypotheses
    hypotheses = Plausible_Hypothese(data, groups)
    
    # Loop through hypotheses
    for hypothesis in hypotheses:
        # Define name and prior
        hyp_meaning = hypothesis[0]	
        prior = hypothesis[2] - hypothesis[1]
        
        # If we're doing Xu and Tennenbaums work
        if likelihood = 0:
            hyp_like = Literal_likelihood(data, hypothesis)
        
        # If we're doing Pragmatic Reasoning
        if likelihood = 1:
            hyp_like = Pragmatic_Likelihood(data, hypothesis)
        
        # Do the posteriors
        posterior = hyp_like * prior
        normalizing_constant = normalizing_constant + posterior
        posteriors[hyp_meaning] = posterior
        
    # Normalize all posteriors
    for hypothesis in posteriors:
        posteriors[hypothesis] = posteriors[hypothesis] / normalizing_constant
            

    
def Model_averaging(): #Do model averaging and create plots