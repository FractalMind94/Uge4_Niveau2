# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 13:40:24 2024

@author: KOM
"""

import json
import matplotlib.pyplot as plt

def thin_section():
    with open(r"C:/Users/KOM/Desktop/Opgaver/thin_section_data.txt") as data:
        for line in data:
            yield line.strip()   # Fjern al mellemrum med strip()

def preprocess_line(line):
  # Erstat single quotes with double quotes. Var et problem ved første forsoeg?
    return line.replace("'", '"')

def plot_keyword_values(lines, keywords):
    plt.figure(figsize=(10, 6))
    for line in lines:
        preprocessed_line = preprocess_line(line)
        data_dict = json.loads(preprocessed_line)

        # Check if the 'Bjergart' field matches any of the keywords
        if data_dict.get('Bjergart') in keywords:
            
            plt.plot(data_dict['SiO2'], data_dict['Al2O3'], 'o')  # Plot the values with label
            
    plt.xlabel('SiO2')
    plt.ylabel('Al2O3')
    plt.title('SiO2 vs Al2O3 for Keywords')
    plt.legend()
    plt.grid(False)
    plt.show()

# Main code
t = thin_section()
keywords = ['Dunit', 'Granulit']  # Specify the keywords
plot_keyword_values(t, keywords)