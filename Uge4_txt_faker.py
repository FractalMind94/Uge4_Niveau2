# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 10:21:42 2024

@author: KOM
"""
import random
from faker import Faker


fake=Faker(locale="da")
bjergart=["Dunit", "Basalt","Granit", "Granulit","Amfibolit", "Gnejs", "Harzburgite" ]

thin_section_list=[]
def Generate_numbers(thin_section):
    for i in range(1,thin_section):
    #  "SiO2","TiO2", "Al2O3", "FeO","MnO","MgO","CaO","Na2O","K2O","F","Cl"
        thin_section={}
        
        thin_section["SiO2"]=fake.random_int(min=1, max=100, step=1)
        thin_section["TiO2"]=fake.random_int(min=1, max=100, step=1)
        thin_section["Al2O3"]=fake.random_int(min=1, max=100, step=1)
        thin_section["FeO"]=fake.random_int(min=1, max=100, step=1)
        thin_section["MnO"]=fake.random_int(min=1, max=100, step=1)
        thin_section["MgO"]=fake.random_int(min=1, max=100, step=1)
        thin_section["CaO"]=fake.random_int(min=1, max=100, step=1)
        thin_section["Na2O"]=fake.random_int(min=1, max=100, step=1)
        thin_section["K2O"]=fake.random_int(min=1, max=100, step=1)
        thin_section["F"]=fake.random_int(min=1, max=100, step=1)
        thin_section["Cl"]=fake.random_int(min=1, max=100, step=1)
        thin_section["Bjergart"]=random.choice(bjergart)
       
        thin_section_list.append(thin_section)
        with open(r"C:/Users/KOM/Desktop/Opgaver\thin_section_data.txt", "w") as output: # definér hvilken sti den skal bruge
            for line in thin_section_list:
                output.write(str(line) + "\n")# gemmer i ny linje efter hver gennemgang
 
    
data = Generate_numbers(1000)
# data.to_excel(r"C:/Users/KOM/Desktop/Opgaver\Thin_section_data.xlsx", index = False)
    