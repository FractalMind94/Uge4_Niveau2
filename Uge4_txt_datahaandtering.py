# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 10:40:24 2024

@author: KOM
"""
import pandas as pd
import matplotlib.pyplot as plt

  # Specify the keywords
keywords = ['SiO2', 'Al2O3', "FeO"]    

def thin_section():
    with open(r"C:/Users/KOM/Desktop/Opgaver\thin_section_data.txt") as data:
        # line=[]
        
        for line in data:
            # print(next(line))
            yield line.strip()
            
            # print(line)



# def filter_keyword_values(lines, keywords):# interger values
#     for line in lines:
#         data_dicts = eval(line)
#         for keyword in keywords:
#             if keyword in data_dicts:
#                 yield int(data_dicts[keyword])
                
                
    
def plot_keyword_values(lines, keywords):
    plt.figure(figsize=(10, 6))
    for line in lines:
        data_dict = eval(line)
        #for interger value 
        for keyword in keywords:
            if keyword in data_dict:
                yield int(data_dict[keyword])
            #For Graphs
            if all(word in data_dict for word in keywords):
                plt.plot(data_dict['SiO2']/data_dict['FeO'], data_dict['Al2O3'], 'o')  # Plot the values directly
    plt.xlabel('SiO2/FeO')
    plt.ylabel('Al2O3')
    plt.title('SiO2 vs Al2O3')
    plt.grid(False)
    plt.show()
       
t = thin_section()


# keyword_values = filter_keyword_values(t, keywords)
keyword_values=plot_keyword_values(t, keywords)

#Print values used
for value in keyword_values:

    print(value)




