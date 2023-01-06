from io import RawIOBase
from os import initgroups
import sys
import re
import math
import numpy as np

def AoC2021_3b(input_data_list):
    met_oxygen_criteria_list = input_data_list
    met_carbon_criteria_list = input_data_list

    for i in range(len(met_oxygen_criteria_list[0])):
        main_list = []
        zeros_indices = []
        ones_indices = []
        for j in range(len(met_oxygen_criteria_list)):
            main_list.append(met_oxygen_criteria_list[j][i])
        num_zeros = main_list.count('0')
        zeros_indices = main_list.index('0')
        num_ones = main_list.count('1')
        ones_indices = main_list.index('1')

        if num_zeros>num_ones:
            met_oxygen_criteria_list = main_list[zeros_indices]
        elif num_zeros<num_ones:
            met_oxygen_criteria_list = main_list[ones_indices]

        else:
            met_oxygen_criteria_list = main_list[ones_indices]
   
    for i in range(len(met_carbon_criteria_list[0])):
        main_list = []
        zeros_indices = []
        ones_indices = []

        for j in range(len(met_carbon_criteria_list)):
            main_list.append(met_carbon_criteria_list[j][i])

        num_zeros = main_list.count('0')
        zeros_indices = main_list.index('0')
        num_ones = main_list.count('1')
        ones_indices = main_list.index('1')

        if num_zeros>num_ones:
            met_carbon_criteria_list = main_list[ones_indices]
        elif num_zeros<num_ones:
            met_carbon_criteria_list = main_list[zeros_indices]
        else:
            met_carbon_criteria_list = main_list[zeros_indices]
        
        
    return met_carbon_criteria_list
    
################# GENERAL I/O + EXECUTION ########################################
# Read input
fin=open(sys.argv[1],'rt') # File specified in command line or other

file_lines=fin.readlines()
input_data_list = []

for i in range(len(file_lines)):
    input_data_list.append(file_lines[i].strip())

# Execute
print(AoC2021_3b(input_data_list))