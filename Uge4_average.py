# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 14:19:57 2024

@author: KOM
"""

import json


def thin_section():
    with open(r"C:/Users/KOM/Desktop/Opgaver/thin_section_data.txt") as data: # definér hvilken sti den skal bruge
        for line in data:
            yield line.strip()  # Fjern al mellemrum med strip()

def preprocess_line(line):
    # Erstat single quotes with double quotes. Var et problem ved første forsoeg?
    return line.replace("'", '"')

def Average_values(lines, keywords):
    count=0
    total=0
    for line in lines:
        preprocessed_line = preprocess_line(line)
        data_dict = json.loads(preprocessed_line)
    
        if data_dict.get('Bjergart') in keywords:
            count+=1
            total+=data_dict['SiO2'] # (tilfoej for ekstra - +data_dict['']) kan skiftes med foelgende vaerdier - 
            #SiO2, TiO2, Al2O3, FeO, MnO, MgO, CaO, Na2O, K2O, F, Cl
    print(total/count) # alternativt return
            

t = thin_section()
keywords = ['Dunit', 'Granulit']  # vaelg keywords - "Dunit", "Basalt","Granit", "Granulit","Amfibolit", "Gnejs", "Harzburgite"
Average_values(t, keywords)
