#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 19:29:24 2020

@author: christinasusangoss
"""
import matplotlib.pyplot as plt
import numpy as np


# List of touples that are of the form ('Name', height, parent-height)
groups1 = [('A', 0.05, 0.06), ('D', 0.06, 0.21), ('K', 0.21, 0.22), ('P', 0.22, 0.25),\
          ('M', 0.21, 0.25), ('R', 0.25, 0.38), ('Z', 0.38, 0.39), ('AA', 0.39, 0.42),\
          ('DD', 0.42, 0.47), ('II', 0.47, 0.5), ('GG', 0.45, 0.5), ('JJ', 0.5, 0.9)]
# May want to define a second set of groups once we figure out the alternative likeihoods

# Data that will be used, data of type (object number, 'Group')
data = [(1, 'D'), (2, 'P'), (1, 'GG')]
# Maybe create function to take an object number and give it the right group label

# Check which hypothesis data is consistent with 
def data_is_consistent_with_hypothesis(data_point): 
    if data_point == 'A':
        return ['A', 'D', 'K', 'P', 'R', 'Z', 'AA', 'DD', 'II', 'JJ']
    elif data_point == 'D':
        return ['D', 'K', 'P', 'R', 'Z', 'AA', 'DD', 'II', 'JJ']
    elif data_point == 'K':
        return ['K', 'P', 'R', 'Z', 'AA', 'DD', 'II', 'JJ']
    elif data_point == 'P':
        return ['P', 'R', 'Z', 'AA', 'DD', 'II', 'JJ']
    elif data_point == 'M':
        return ['M', 'R', 'Z', 'AA', 'DD', 'II', 'JJ']
    elif data_point == 'Z':
        return ['Z', 'AA', 'DD', 'II', 'JJ']
    elif data_point == 'AA':
        return ['AA', 'DD', 'II', 'JJ']
    elif data_point == 'DD':
        return ['DD', 'II', 'JJ']
    elif data_point == 'II':
        return ['II', 'JJ']
    elif data_point == 'GG':
        return ['GG', 'JJ']
    
def Plausible_Hypotheses(data, groups): # Creates a list of plausible hypotheses  
    # hypotheses have the form ('Name', height, parentheight)
    hypotheses = []
    l = ['A', 'D', 'K', 'P', 'M', 'R', 'Z', 'AA', 'DD', 'II', 'GG', 'JJ']
    s = set(l)
    for point in data:
        s = s & set(data_is_consistent_with_hypothesis(point[1]))
    hyp_names = list(s)
    for hypothesis in groups:
        if hypothesis[0] in hyp_names:
            hypotheses.append(hypothesis)
    return hypotheses
            
    
def Literal_probability(data, hypothesis): # The classic probability function
    return 0
    # (1/size(h))^n + P(h)/sum of all possible hypotheses
    
def Literal_likelihood(data, hypothesis): # Create literal likelihood
    n = len(data)
    likelihood = (1/hypothesis[1])**n
    return likelihood
    
    
def Pragmatic_Likelihood(data, hypothesis): # Calculate the pragmatically reasoned liklihood
    # literal probability of h|data/ sum over all hypotheses -> do we add a prior
    # and what is it?
    return 0

# Stealing a lot of this from wordlearning.py   
# likelihood = 0 if classic, likelihood = 1 if pragmatic
def Posteriors(data, groups, likelihood): #Calculate the appropriate posteriors
    # We will use the variable normalizing_constant to keep track of the denominator in Bayes rule
    normalizing_constant = 0	
    # We define a dictionary, posteriors, that will keep track of each hypothesis' posterior probability
    # It will eventually have six keys (one corresponding to each hypothesis), which will have posteriors as values		 
    posteriors = {}	
    
    # Create a list of plausible hypotheses
    hypotheses = Plausible_Hypotheses(data, groups)
    
    # Loop through hypotheses
    for hypothesis in hypotheses:
        # Define name and prior
        hyp_meaning = hypothesis[0]	
        prior = hypothesis[2] - hypothesis[1]
        
        # If we're doing Xu and Tennenbaums work
        if likelihood == 0:
            hyp_like = Literal_likelihood(data, hypothesis)
        
        # If we're doing Pragmatic Reasoning
        if likelihood == 1:
            hyp_like = Pragmatic_Likelihood(data, hypothesis)
        
        # Do the posteriors
        posterior = hyp_like * prior
        normalizing_constant = normalizing_constant + posterior
        posteriors[hyp_meaning] = posterior
        
    # Normalize all posteriors
    for hypothesis in posteriors:
        posteriors[hypothesis] = posteriors[hypothesis] / normalizing_constant
        
    return posteriors
            

    
def Model_averaging(data, groups, likelihood_flag): #Do model averaging and create plots
    posteriors = Posteriors(data, groups, likelihood_flag)
    hypotheses = Plausible_Hypotheses(data, groups)
    
    # Do model averaging
    # Probability of Dalmation: A + D
    specific = ['A', 'D']
    p_spec = 0
    for hypothesis in hypotheses:
        if hypothesis[0] in specific:
            p_spec = p_spec + posteriors[hypothesis[0]]
    # Probabiity of Dog: A + D + K + P + M + R
    dog = ['K', 'P', 'M', 'R']
    p_dog = 0
    for hypothesis in hypotheses:
        if hypothesis[0] in dog:
            p_dog = p_dog + posteriors[hypothesis[0]]
    # Probability of Animal: A + D + K + P + R + M + Z + AA + DD + II + GG + JJ
    animal = ['Z', 'AA', 'DD', 'II', 'GG', 'JJ']
    p_animal = 0
    for hypothesis in hypotheses:
        if hypothesis[0] in animal:
            p_animal = p_animal + posteriors[hypothesis[0]]
            
    # Make a bar chart
    N = 3
    ind = np.arange(N) 
    plt.bar(ind, (p_spec+p_dog+p_animal, p_dog+p_animal, p_animal))
    plt.xticks(ind, ('Breed', 'Dog', 'Animal'))
    plt.ylabel('Probability')
    plt.show()
    
    return [p_spec+p_dog+p_animal, p_dog+p_animal, p_animal]
    
    