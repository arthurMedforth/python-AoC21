from io import RawIOBase
from os import initgroups
import sys
import re
import math
import numpy as np

def AoC2021_1a(input_data_list):
    count = 0
    for i, element in enumerate(input_data_list):
        if i == 0:
            continue
        else:
            if int(element) > int(input_data_list[i-1]):
                count += 1

    return count


def AoC2021_1b(input_data_list):
    count = 0
    for i in range(len(input_data_list)):
        if i + 2 > len(input_data_list) - 1:
            return count

        if i == 0:
            sum = int(input_data_list[i]) + int(input_data_list[i+1]) + int(input_data_list[i+2])
            continue
        else:
            new_sum = int(input_data_list[i]) + int(input_data_list[i+1]) + int(input_data_list[i+2])
            if new_sum > sum:
                sum = new_sum
                count += 1
            else: 
                sum = new_sum
                continue

def AoC2021_2a(input_data_list):
    depth = 0
    x_coord = 0
    for i in range(len(input_data_list)):
        move, val = input_data_list[i].split()
        val = int(val)
        if move == 'forward':
            x_coord += val
            continue
        elif move == 'up':
            depth -= val
            continue
        elif move == 'down':
            depth += val
            continue
    
    return depth*x_coord

def AoC2021_2b(input_data_list):
    depth = 0
    x_coord = 0
    aim = 0
    for i in range(len(input_data_list)):
        move, val = input_data_list[i].split()
        val = int(val)
        if move == 'forward':
            x_coord += val
            depth += val*aim
            continue
        elif move == 'up':
            aim -= val
            continue
        elif move == 'down':
            aim += val
            continue
    
    return depth*x_coord

def AoC2021_3a(input_data_list):
    array = np.array(input_data_list)
    gamma = []
    epsilon = []
    for i in range(len(input_data_list[0])):
        main_list = []
        for j in range(len(input_data_list)):
            main_list.append(input_data_list[j][i])
        num_zeros = main_list.count('0')
        num_ones = main_list.count('1')
        if num_zeros>num_ones:
            gamma.append('0')
            epsilon.append('1')
        elif num_zeros<num_ones:
            gamma.append('1')
            epsilon.append('0')
        else:
            raise('Error')
    gamma = ''.join(gamma)
    epsilon = ''.join(epsilon)
    return int(gamma,2)*int(epsilon,2)

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
