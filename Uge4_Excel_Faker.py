# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 10:43:45 2024

@author: KOM
"""

from faker import Faker
import pandas as pd
import os.path
# "C:/Users/KOM/Desktop/Opgaver"
fake=Faker(locale="da")


thin_section_list=[]
def Generate_numbers(thin_section):
    for i in range(1,thin_section):
    #  "SiO2","TiO2", "Al2O3", "FeO","MnO","MgO","CaO","Na2O","K2O","F","Cl"
        thin_section={}
        
        thin_section["SiO2"]=fake.random_int(min=0, max=100, step=1)
        thin_section["TiO2"]=fake.random_int(min=0, max=100, step=1)
        thin_section["Al2O3"]=fake.random_int(min=0, max=100, step=1)
        thin_section["FeO"]=fake.random_int(min=0, max=100, step=1)
        thin_section["MnO"]=fake.random_int(min=0, max=100, step=1)
        thin_section["MgO"]=fake.random_int(min=0, max=100, step=1)
        thin_section["CaO"]=fake.random_int(min=0, max=100, step=1)
        thin_section["Na2O"]=fake.random_int(min=0, max=100, step=1)
        thin_section["K2O"]=fake.random_int(min=0, max=100, step=1)
        thin_section["F"]=fake.random_int(min=0, max=100, step=1)
        thin_section["Cl"]=fake.random_int(min=0, max=100, step=1)
       
        thin_section_list.append(thin_section)
    return pd.DataFrame(thin_section_list)
    
data = Generate_numbers(10000)
data.to_excel(r"C:/Users/KOM/Desktop/Opgaver\Thin_section_data.xlsx", index = False)

