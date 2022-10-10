from io import RawIOBase
from os import initgroups
import sys
import re
import math
import numpy as np
#
# # First day - Part 1 and Part 2
# def AoC1(input_data_list):
#     for i in range(len(input_data_list)):
#         for j in range(len(input_data_list)):
#             for k in range(len(input_data_list)):
#                 temp_val = input_data_list[i] + input_data_list[j] + input_data_list[k]
#                 if temp_val == 2020:
#                     ans = input_data_list[i] * input_data_list[j] * input_data_list[k]
#                     return ans
#
# # Second day - Part 1 and Part 2
# def AoC2(input_data_list):
#     # Make dict
#     better_format_input = []
#     for element in input_data_list:
#         better_format_input.append(element.replace(" ", "").split(':'))
#
#     valid_count = 0
#     for element in better_format_input:
#         #no_hyphon = element[0][element[0].find()]
#         letter_for_rule = element[0][-1]
#         password_rule = re.split('[a-z|,]+', element[0])
#         password_rule[1] = letter_for_rule
#         del element[0]
#
#         numerical_rule = password_rule[0].split("-")
#         numerical_rule[0] = int(numerical_rule[0])
#         numerical_rule[1] = int(numerical_rule[1])
#         password_rule[0] = numerical_rule
#
#         letter_instances = []
#         [letter_instances.append(instance) for instance, ltr in enumerate(element[0]) if ltr == password_rule[1]]
#
#         # P1
# #        instances = len(letter_instances)
# #        if instances >= password_rule[0][0] and instances <= password_rule[0][1]:
# #            valid_count += 1
# #        else:
# #            valid_count = valid_count
#
#
#         # P2
#         for instance in letter_instances:
#             temp_count = valid_count
#             if instance == password_rule[0][0] - 1:
#                 # We have first character at right spot
#                 for instance_2_index in range(len(letter_instances)):
#                     if letter_instances[instance_2_index] == password_rule[0][1] - 1:
#                         valid_count = valid_count
#                         break
#                     elif letter_instances[instance_2_index] != password_rule[0][1] - 1 and instance_2_index == len(letter_instances) - 1:
#                         valid_count += 1
#                         break
#                     else:
#                         continue
#             elif instance == password_rule[0][1] - 1:
#                 # We have first character at right spot
#                 for instance_2_index in range(len(letter_instances)):
#                     if letter_instances[instance_2_index] == password_rule[0][0] - 1:
#                         valid_count = valid_count
#                         break
#                     elif letter_instances[instance_2_index] != password_rule[0][0] - 1 and instance_2_index == len(letter_instances) - 1:
#                         valid_count += 1
#                         break
#                     else:
#                         continue
#             else:
#                 valid_count = valid_count
#
#     return valid_count
#
# # Third day - Part 1 and 2
# def AoC3(input_data_list):
#     # Find out how many times I will need to repeat the seq
#     new_piste = []
#     length_of_map = len(input_data_list)
#     breadth_of_map = len(input_data_list[0])
#     right_operation = length_of_map * 3
#     maps_needed = math.ceil(right_operation/breadth_of_map)
#     for element in input_data_list:
#         new_piste.append(element*maps_needed)
#     onwards = True
#     tree_count2 = 0
#
#     pos_x = 0
#     pos_y = 0
#     while onwards:
#         pos_x += 3
#         pos_y += 1
#         if new_piste[pos_y][pos_x] == '#':
#             tree_count2 += 1
#         else:
#             tree_count2 = tree_count2
#
#         if pos_y == len(new_piste) - 1:
#             onwards = False
#     return tree_count2
#
# # Fourth day
# # Part 1 - add double return to input after last line
# def AoC4a(input_data_list):
#     passports_uniform_format = []
#     # Use spaces in input_data_list to separate different passports
#     onwards = True
#     while onwards:
#         for i in range(len(input_data_list)):
#             j_save = [0]
#             if input_data_list[i] == '':  # space = new line
#                 # Concatenate ALL previous lists elements as they are same passport
#                 temp_data = input_data_list[0]
#                 for j in range(i - 1):
#                     temp_data = temp_data + ' ' + input_data_list[j + 1]
#                     j_save.append(j + 1)
#
#                 passports_uniform_format.append(temp_data)
#                 j_save.append(j_save[-1] + 1)
#                 # Delete elements
#                 for k in sorted(j_save, reverse=True):
#                     del input_data_list[k]
#                 break
#             else:
#                 continue
#         if len(input_data_list) == 0:
#             onwards = False
#         else:
#             continue
#
#     valid_count = 0
#     for element in passports_uniform_format:
#         byr_present = element.find('byr')
#         iyr_present = element.find('iyr')
#         hgt_present = element.find('hgt')
#         eyr_present = element.find('eyr')
#         hcl_present = element.find('hcl')
#         ecl_present = element.find('ecl')
#         pid_present = element.find('pid')
#
#         if byr_present != -1 and iyr_present != -1 and hgt_present != -1 and eyr_present != -1 and hcl_present != -1 and ecl_present != -1 and pid_present != -1:
#             valid_count += 1
#         else:
#             valid_count = valid_count
#
#     return valid_count
# # Part 2 - add double return to input after last line
# def AoC4b(input_data_list):
#     passports_uniform_format = []
#
#     # Use spaces in input_data_list to separate different passports
#     onwards = True
#     while onwards:
#         for i in range(len(input_data_list)):
#             j_save = [0]
#             if input_data_list[i] == '':  # space = new line
#                 # Concatenate ALL previous lists elements as they are same passport
#                 temp_data = input_data_list[0]
#                 for j in range(i - 1):
#                     temp_data = temp_data + ' ' + input_data_list[j + 1]
#                     j_save.append(j + 1)
#
#                 passports_uniform_format.append(temp_data)
#                 j_save.append(j_save[-1] + 1)
#                 # Delete elements
#                 for k in sorted(j_save, reverse=True):
#                     del input_data_list[k]
#                 break
#             else:
#                 continue
#         if len(input_data_list) == 0:
#             onwards = False
#         else:
#             continue
#         delete_these = []
#         for index, element in enumerate(passports_uniform_format):
#             byr_present = element.find('byr')
#             iyr_present = element.find('iyr')
#             hgt_present = element.find('hgt')
#             eyr_present = element.find('eyr')
#             hcl_present = element.find('hcl')
#             ecl_present = element.find('ecl')
#             pid_present = element.find('pid')
#
#             if byr_present != -1 and iyr_present != -1 and hgt_present != -1 and eyr_present != -1 and hcl_present != -1 and ecl_present != -1 and pid_present != -1:
#                 continue
#             else:
#                 delete_these.append(index)
#
#     for index in reversed(delete_these):
#         del passports_uniform_format[index]
#
#     new_format_passports = []
#     for element in passports_uniform_format:
#         new_format_passports.append(element.split())
#
#     valid_count = 0
#     for passport in new_format_passports:
#         pass_count = 0
#         for element in passport:
#             key,value = element.split(':')
#             # Rules
#             if key == 'byr':
#                 if int(value) >= 1920 and int(value) <= 2002:
#                     pass_count += 1
#                     continue
#                 else:
#                     continue
#             elif key == 'iyr':
#                 if int(value) >= 2010 and int(value) <= 2020:
#                     pass_count += 1
#                     continue
#                 else:
#                     continue
#             elif key == 'eyr':
#                 if int(value) >= 2020 and int(value) <= 2030:
#                     pass_count += 1
#                     continue
#                 else:
#                     continue
#             elif key == 'hgt':
#                 if value[-2:] == 'cm':
#                     if int(value[:-2]) >= 150 and int(value[:-2]) <= 193:
#                         pass_count += 1
#                         continue
#                     else:
#                         continue
#                 elif value[-2:] == 'in': # inches given
#                     if int(value[:-2]) >= 59 and int(value[:-2])<= 76:
#                         pass_count += 1
#                         continue
#                     else:
#                         continue
#                 else:
#                     continue
#             elif key == 'hcl':
#                 if value[0] == '#' and len(value) == 7:
#                     if value[1:].isalnum() == True:
#                         pass_count += 1
#                         continue
#                     else:
#                         continue
#                 else:
#                     continue
#             elif key == 'ecl':
#                 eye_colours = ['amb','blu','brn','gry','grn','hzl','oth']
#                 if (value in eye_colours):
#                     pass_count += 1
#                     continue
#                 else:
#                     continue
#             elif key == 'pid':
#                 if len(value) == 9:
#                     pass_count += 1
#                     continue
#                 else:
#                     continue
#         if pass_count == 7:
#             valid_count += 1
#
#     return valid_count
#
# # Fifth day
# def Ao5findIt(lower,upper,instruction,row_or_col1,row_or_col2):
#     mid_point = int(((upper + 1)-lower) / 2) + lower
#     if instruction == row_or_col1:
#         lower = lower
#         upper = mid_point - 1
#     elif instruction == row_or_col2:
#         lower = mid_point
#         upper = upper
#     else:
#         error('Something weird going on here')
#
#     return lower, upper
# def AoC5(input_data_list):
#     row_and_col = []
#     seat_IDs = []
#     for line in input_data_list:
#         lower_row = 0
#         upper_row = 127
#         lower_column = 0
#         upper_column = 7
#
#         # Find row
#         for char in line[0:7]:
#             lower_row,upper_row = Ao5findIt(lower_row,upper_row,char,'F','B')
#
#         # Find column
#         for char in line[7:]:
#             lower_column,upper_column = Ao5findIt(lower_column,upper_column,char,'L','R')
#
#         row_and_col.append([lower_row,lower_column])
#         seat_IDs.append((lower_row*8)+lower_column)
#
#     # Find missing seats
#     missing_seats = []
#     max_ID = (127 * 8)+8
#     check_range = range(1,max_ID)
#
#     for element in check_range:
#         if element in seat_IDs:
#             continue
#         else:
#             missing_seats.append(element)
#
#     return missing_seats
#
# # Sixth day
# # Part 1 - add double return to input after last line
# def AoC6a(input_data_list):
#     data = []
#     temp = []
#     for element in input_data_list:
#         if element != '':
#             temp.append(element)
#         else:
#             data.append(temp)
#             temp = []
#
#     yes_count_groups = 0
#     for element in data:
#         yes_count = 0
#         letter_vec = []
#         for person in element:
#             for question in person:
#                 if question in letter_vec:
#                     yes_count = yes_count
#
#                 else:
#                     yes_count += 1
#                     letter_vec.append(question)
#         yes_count_groups += yes_count
#
#     return yes_count_groups
# # Part 2 - add double return to input after last line
# def AoC6b(input_data_list):
#     data = []
#     temp = []
#     for element in input_data_list:
#         if element != '':
#             temp.append(element)
#         else:
#             data.append(temp)
#             temp = []
#     yes_count_groups = 0
#     for element in data:
#         letter_vec = []
#         people = len(element)
#         if people == 1:
#             yes_count_groups += len(element[0])
#             continue
#         for i, person in enumerate(element):
#             if i == 0:
#                 letter_vec = [char for char in person]
#             else:
#                 for q in letter_vec:
#                     yes_count = 0
#                     for stud in element[1:]:
#                         if stud.find(q) > -1:
#                             yes_count += 1
#                         if yes_count == len(element)-1:
#                             yes_count_groups += 1
#                         else:
#                             continue
#                 break
#     return yes_count_groups
#
# # Seventh day
# # Part 1 - a took a few attempts
# def findShinyGold(dict_of_bags,shiny_gold_bags,key,keys):
#     if key in keys:
#         return shiny_gold_bags
#     loop_num = len(dict_of_bags[key])
#     for i in range(loop_num):
#         if dict_of_bags[key][i].find('shiny gold bag') > -1 or dict_of_bags[key][i].find('shiny gold bags') > -1:
#             shiny_gold_bags += 1
#             keys.append(key)
#             return shiny_gold_bags
#         elif dict_of_bags[key][i] == 'no other bags':
#             return shiny_gold_bags
#         else:
#             key_form = dict_of_bags[key][i][2:]
#             if key_form[-1] != 's':
#                 key_form += 's'
#             shiny_gold_bags = findShinyGold(dict_of_bags,shiny_gold_bags,key_form,keys)
#             keys.append(key_form)
#             continue
#     return shiny_gold_bags
# def AoC7a1(input_data_list):
#     dict_of_bags = {}
#     for element in input_data_list:
#         temp_1 = element.replace('.','')
#         temp_2 = temp_1.split(' contain ')
#         if temp_2[0] == 'shiny gold bags':
#             continue
#         else:
#             dict_of_bags[temp_2[0]] = temp_2[1].split(', ')
#
#
#     shiny_gold_bags = 0
#     bags = []
#     for x in range(len(dict_of_bags)):
#         keys =[]
#         print(list(dict_of_bags.keys())[x])
#         shiny_gold_bags = findShinyGold(dict_of_bags,shiny_gold_bags,list(dict_of_bags.keys())[x],keys)
#         print(shiny_gold_bags)
#         bags.append(shiny_gold_bags)
#
#     count = 0
#     for bag in bags:
#         if bag != 0:
#             count += 1
#     return count
# def AoC7a2(input_data_list):
#     dict_of_bags = {}
#     for element in input_data_list:
#         temp_1 = element.replace('.','')
#         temp_2 = temp_1.split(' contain ')
#         if temp_2[0] == 'shiny gold bags':
#             continue
#         else:
#             dict_of_bags[temp_2[0]] = temp_2[1].split(', ')
#
#     bags_with_shiny_gold = []
#     bags_with_nothing = []
#     for key in dict_of_bags:
#         further_bags = len(dict_of_bags[key])
#         for i in range(further_bags):
#             if dict_of_bags[key][i].find('shiny gold bag') > -1 or dict_of_bags[key][i].find('shiny gold bags') > -1:
#                 bags_with_shiny_gold.append(key)
#             elif dict_of_bags[key][i] == 'no other bags':
#                 bags_with_nothing.append(key)
#                 continue
#             else:
#                 continue
#
#     shiny_gold_count = 0
#     for key in dict_of_bags:
#         further_bags = len(dict_of_bags[key])
#         for i in range(further_bags):
#             if dict_of_bags[key][i].find('shiny gold bag') > -1 or dict_of_bags[key][i].find('shiny gold bags') > -1:
#                 shiny_gold_count += 1
#                 break
#             elif dict_of_bags[key][i] == 'no other bags':
#                 break
#             else:
#                 nothing_in_bag = False
#                 test = dict_of_bags[key][i][2:]
#                 for bag in bags_with_nothing:
#                     if bag.find(dict_of_bags[key][i][2:]) > -1:
#                         nothing_in_bag = True
#                         break
#                     else:
#                         continue
#
#                 if nothing_in_bag != True:
#                     for bag in bags_with_shiny_gold:
#                         if bag.find(dict_of_bags[key][i][2:]) > -1:
#                             shiny_gold_count += 1
#                             break
#                     break
#                 else:
#                     continue
#
#     return shiny_gold_count
# def AoC7a3(input_data_list):
#     dict_of_bags = {}
#     for element in input_data_list:
#         temp_1 = element.replace('.','')
#         temp_2 = temp_1.split(' contain ')
#         if temp_2[0] == 'shiny gold bags':
#             continue
#         else:
#             dict_of_bags[temp_2[0]] = temp_2[1].split(', ')
#
#     bags_with_shiny_gold = []
#     bags_with_nothing = []
#     for key in dict_of_bags:
#         further_bags = len(dict_of_bags[key])
#         for i in range(further_bags):
#             if dict_of_bags[key][i].find('shiny gold bag') > -1 or dict_of_bags[key][i].find('shiny gold bags') > -1:
#                 bags_with_shiny_gold.append(key)
#             elif dict_of_bags[key][i] == 'no other bags':
#                 bags_with_nothing.append(key)
#                 continue
#             else:
#                 continue
#
#     shiny_gold_count = 0
#     for key in dict_of_bags:
#         further_bags = len(dict_of_bags[key])
#         for i in range(further_bags):
#             if dict_of_bags[key][i][-1] != 's':
#                 val_with_s = dict_of_bags[key][i]+'s'
#                 if val_with_s[2:] == 'shiny gold bags' or val_with_s[2:] in bags_with_shiny_gold:
#                     shiny_gold_count += 1
#                     break
#                 else:
#                     continue
#             else:
#                 if dict_of_bags[key][i][2:] == 'shiny gold bags' or dict_of_bags[key][i][2:] == 'shiny gold bag' or dict_of_bags[key][i][2:] in bags_with_shiny_gold:
#                     shiny_gold_count += 1
#                     break
#                 else:
#                     continue
#
#
#     return shiny_gold_count
# def AoC7a4(input_data_list):
#     dict_of_bags = {}
#     for element in input_data_list:
#         temp_1 = element.replace('.','')
#         temp_2 = temp_1.split(' contain ')
#         if temp_2[0] == 'shiny gold bags':
#             continue
#         else:
#             dict_of_bags[temp_2[0]] = temp_2[1].split(', ')
#
#     bags_with_shiny_gold = []
#     bags_with_nothing = []
#     for key in dict_of_bags:
#         further_bags = len(dict_of_bags[key])
#         for i in range(further_bags):
#             if dict_of_bags[key][i].find('shiny gold bag') > -1 or dict_of_bags[key][i].find('shiny gold bags') > -1:
#                 bags_with_shiny_gold.append(key)
#             elif dict_of_bags[key][i] == 'no other bags':
#                 bags_with_nothing.append(key)
#                 continue
#             else:
#                 continue
#
#     shiny_gold_count = 0
#     for key in dict_of_bags:
#         if key in bags_with_shiny_gold:
#             shiny_gold_count += 1
#             continue
#         further_bags = len(dict_of_bags[key])
#         for i in range(further_bags):
#             if dict_of_bags[key][i][-1] != 's':
#                 val_with_s = dict_of_bags[key][i]+'s'
#                 print(val_with_s[2:])
#                 if val_with_s[2:] in bags_with_shiny_gold:
#                     shiny_gold_count += 1
#                     break
#                 else:
#                     continue
#             else:
#                 if dict_of_bags[key][i][2:] in bags_with_shiny_gold:
#                     shiny_gold_count += 1
#                     break
#                 else:
#                     continue
#     return shiny_gold_count, bags_with_shiny_gold



# # Winner
# def findGold(dict_of_bags,bags_with_shiny_gold,bags_with_nothing,key,count):
#     bags_inside = len(dict_of_bags[key])
#     for i in range(bags_inside):
#         if dict_of_bags[key][i][-1] != 's':
#             val_with_s = dict_of_bags[key][i] + 's'
#             if val_with_s[2:] in bags_with_nothing:
#                 if i == bags_inside - 1:
#                     break
#                 else:
#                     continue
#             elif val_with_s[2:] in bags_with_shiny_gold:
#                 count += 1
#                 break
#             else:
#                 temp_count = count
#                 count = findGold(dict_of_bags, bags_with_shiny_gold, bags_with_nothing, val_with_s[2:], count)
#                 if count > temp_count:
#                     return count
#                 else:
#                     continue
#         else:
#             if dict_of_bags[key][i][2:] in bags_with_nothing:
#                 if i == bags_inside - 1:
#                     break
#                 else:
#                     continue
#             elif dict_of_bags[key][i][2:] in bags_with_shiny_gold:
#                 count += 1
#                 break
#             else:
#                 temp_count = count
#                 count = findGold(dict_of_bags, bags_with_shiny_gold, bags_with_nothing, dict_of_bags[key][i][2:], count)
#                 if count > temp_count:
#                     return count
#                 else:
#                     continue
#     return count
# def AoC7a(input_data_list):
#     dict_of_bags = {}
#     for element in input_data_list:
#         temp_1 = element.replace('.', '')
#         temp_2 = temp_1.split(' contain ')
#         if temp_2[0] == 'shiny gold bags':
#             continue
#         else:
#             dict_of_bags[temp_2[0]] = temp_2[1].split(', ')
#
#     bags_with_shiny_gold = []
#     bags_with_nothing = []
#     for key in dict_of_bags:
#         further_bags = len(dict_of_bags[key])
#         for i in range(further_bags):
#             if dict_of_bags[key][i].find('shiny gold bag') > -1 or dict_of_bags[key][i].find('shiny gold bags') > -1:
#                 bags_with_shiny_gold.append(key)
#             elif dict_of_bags[key][i] == 'no other bags':
#                 bags_with_nothing.append(key)
#                 continue
#             else:
#                 continue
#     count = 0
#     for key in dict_of_bags:
#         if key in bags_with_nothing:
#             continue
#         elif key in bags_with_shiny_gold:
#             count += 1
#         else:
#             count = findGold(dict_of_bags, bags_with_shiny_gold, bags_with_nothing,key,count)
#
#     return count
#
# # Part 2 - Found extremely difficult
# # But final solution was very simple in the end...
# def findContents(key,dict_of_bags,count,thing,key_input_number):
#     bags_types_inside = len(dict_of_bags[key])
#     for i in range(bags_types_inside):
#         if dict_of_bags[key][i] != 'no other bags':
#             count += key_input_number * int(dict_of_bags[key][i][0])
#             thing.append(int(dict_of_bags[key][i][0]))
#             right_format_key = dict_of_bags[key][i][2:]
#             if right_format_key[-1] != 's':
#                 right_format_key += 's'
#             count,thing = findContents(right_format_key, dict_of_bags, count,thing,int(dict_of_bags[key][i][0]))
#         else:
#             return count, thing
#     return count, thing
# def AoC7b1(input_data_list):
#     dict_of_bags = {}
#     shiny_gold_bag_contents = []
#     for element in input_data_list:
#         temp_1 = element.replace('.', '')
#         temp_2 = temp_1.split(' contain ')
#         if temp_2[0] == 'shiny gold bags':
#             shiny_gold_bag_contents = temp_2[1].split(', ')
#             continue
#         else:
#             dict_of_bags[temp_2[0]] = temp_2[1].split(', ')
#
#     count = 0
#     thing = []
#     for key in shiny_gold_bag_contents:
#         thing.append(int(key[0]))
#         right_format_key = key[2:]
#         if right_format_key[-1] != 's':
#             right_format_key += 's'
#         count, thing = findContents(right_format_key,dict_of_bags,count,thing,int(key[0]))
#         count += int(key[0])
#     return count, thing
# def countBags(bag_of_interest, dict_of_bags,count2):
#     count1 = 0
#     for element in bag_of_interest:
#         if element != 'no other bags':
#             # Save sum of bags at current level
#             count1 += int(element[0])
#             # Save outer bag num
#             outer_bag_num = int(element[0])
#             if element[-1] != 's':
#                 temp = element[2:] + 's'
#                 count_temp = countBags(dict_of_bags[temp], dict_of_bags,count2)
#             else:
#                 count_temp = countBags(dict_of_bags[element[2:]], dict_of_bags,count2)
#         else:
#             return count2
#         count2 += (count_temp * outer_bag_num)
#     count2 += count1
#     return count2
# def countBags1(bag_of_interest,dict_of_bags,count2):
#     for element in bag_of_interest:
#         if element != 'no other bags':
#             # Save outer bag num
#             outer_bag_num = int(element[0])
#             if element[-1] != 's':
#                 temp = element[2:] + 's'
#                 count2 += countBags1(dict_of_bags[temp], dict_of_bags, count2)
#             else:
#                 count2 += countBags1(dict_of_bags[element[2:]], dict_of_bags, count2)
#         else:
#             return count2
#
#     count2 += count2 * outer_bag_num
#     count2 += outer_bag_num
#     return count2
# def AoC7b2(input_data_list):
#     dict_of_bags = {}
#     for element in input_data_list:
#         temp_1 = element.replace('.', '')
#         temp_2 = temp_1.split(' contain ')
#         dict_of_bags[temp_2[0]] = temp_2[1].split(', ')
#
#     bags_with_shiny_gold = []
#     bags_with_nothing = []
#     bags_in_bag = []
#     for key in dict_of_bags:
#         further_bags = len(dict_of_bags[key])
#         bags_inside = 0
#         for i in range(further_bags):
#             if dict_of_bags[key][i].find('shiny gold bag') > -1 or dict_of_bags[key][i].find('shiny gold bags') > -1:
#                 bags_with_shiny_gold.append(key)
#                 bags_inside += int(dict_of_bags[key][i][0])
#             elif dict_of_bags[key][i] == 'no other bags':
#                 bags_with_nothing.append(key)
#                 bags_inside += int(0)
#             else:
#                 bags_inside += int(dict_of_bags[key][i][0])
#                 continue
#         bags_in_bag.append([key,bags_inside])
#
#     ans = foo(dict_of_bags, 'shiny gold bags')
#     return ans
# # Winner
# def bagsInside(dict_of_bags,bag_x):
#     ans = 0
#     for element in dict_of_bags[bag_x]:
#         if element != 'no other bags':
#             if element[-1] != 's':
#                 temp = element + 's'
#                 ans += int(element[0]) + (int(element[0])*bagsInside(dict_of_bags,temp[2:]))
#             else:
#                 ans += int(element[0]) + (int(element[0])*bagsInside(dict_of_bags,element[2:]))
#         else:
#             ans = 0
#             return ans
#
#     return ans
# def AoC7b(input_data_list):
#     dict_of_bags = {}
#     for element in input_data_list:
#         temp_1 = element.replace('.', '')
#         temp_2 = temp_1.split(' contain ')
#         dict_of_bags[temp_2[0]] = temp_2[1].split(', ')
#
#     ans = bagsInside(dict_of_bags, 'shiny gold bags')
#     return ans
#
# # Eighth day
# # Part 1
# def AoC8a(input_data_list):
#     data = []
#     for m, element in enumerate(input_data_list):
#         data.append(element.split(' '))
#
#     # Convert input into a list with incremental key
#     dict_instructions = {}
#     for i, element in enumerate(data):
#         dict_instructions[i] = element
#
#     # Execute game instructions
#     # Stopping when any instruction is repeated
#     acc = 0 # Initialise accumulator
#     pointer = 0
#     keep_going = True
#     instruction_history = []
#     while keep_going:
#         if pointer in instruction_history:
#             ans = acc
#             keep_going = False
#
#         # Save instruction history
#         instruction_history.append(pointer)
#         instr = dict_instructions[pointer][0]
#         sign = dict_instructions[pointer][1][0]
#         if sign == '-':
#             val = -1 * int(dict_instructions[pointer][1][1:])
#         else:
#             val = int(dict_instructions[pointer][1][1:])
#
#         if instr == 'jmp':
#             pointer += val
#         elif instr == 'acc':
#             pointer += 1
#             acc += val
#         elif instr == 'nop':
#             pointer += 1
#         else:
#             raise ValueError('Invalid instruction', instr)
#
#     return ans
# # Part 2
# def AoC8b(input_data_list):
#     data = []
#     for m, element in enumerate(input_data_list):
#         data.append(element.split(' '))
#
#     # Convert input into a list with incremental key
#     dict_instructions = {}
#     for i, element in enumerate(data):
#         dict_instructions[i] = element
#
#     # Get keys of instr that are nop or jmp
#     nop_or_jmp_keys = []
#     for key in dict_instructions:
#         if dict_instructions[key][0] == 'jmp' or dict_instructions[key][0] == 'nop':
#             nop_or_jmp_keys.append(key)
#
#     # Try flipping each occurence of nop and jmp
#     for key in nop_or_jmp_keys:
#         # Execute game instructions
#         # Stopping when any instruction is repeated
#         acc = 0  # Initialise accumulator
#         pointer = 0
#         keep_going = True
#         instruction_history = []
#         while keep_going:
#             if pointer == len(input_data_list):
#                 return acc
#
#             if pointer in instruction_history:
#                 keep_going = False
#
#             # Save instruction history
#             instruction_history.append(pointer)
#             instr = dict_instructions[pointer][0]
#             if pointer == key and instr == 'nop':
#                 instr = 'jmp'
#             elif pointer == key and instr == 'jmp':
#                 instr = 'nop'
#             else:
#                 instr = instr
#
#             sign = dict_instructions[pointer][1][0]
#             if sign == '-':
#                 val = -1 * int(dict_instructions[pointer][1][1:])
#             else:
#                 val = int(dict_instructions[pointer][1][1:])
#
#             if instr == 'jmp':
#                 pointer += val
#             elif instr == 'acc':
#                 pointer += 1
#                 acc += val
#             elif instr == 'nop':
#                 pointer += 1
#             else:
#                 raise ValueError('Invalid instruction', instr)
#
# # Seventeenth day
# # Part 1
# # Appalling first try
# # Went to learn about arrays and operations
# def findNeighbours(pocket,dim,row,col):
#     neighbours_states = []
#     pos_vector = [-1,0,1]
#     if dim==0 or row == 0 or col == 0:
#         return neighbours_states
#     for i in pos_vector:
#         for j in pos_vector:
#             for k in pos_vector:
#                 if i == 0 and j == 0 and k == 0:
#                     continue
#                 else:
#                     neighbours_states.append(pocket[dim+i][row+j][col+k])
#     return neighbours_states
# def AoC17a(input_data_list):
#     # Split up chars
#     brute_force = 20
#     mid_dim = math.ceil(brute_force/2)
#     data_for_later = []
#     data = []
#     for element in input_data_list:
#         data.append(list(element))
#         data_for_later.append(list(element))
#     for i, element in enumerate(input_data_list):
#         for j in range(len(element)):
#             data[i][j] = '.'
#     for i, element in enumerate(data):
#         for j in range(brute_force):
#             data[i].append('.')
#     for j in range(brute_force):
#         data.append(element)
#
#     # Create giant array
#     pocket = np.array([data]*brute_force)
#
#     # Add in active starting sheet at the mid dimension
#
#     for i in range(len(data_for_later)):
#         for j in range(len(data_for_later[0])):
#             pocket[mid_dim][math.floor(brute_force/2)+i][math.floor(brute_force/2)+j] = data_for_later[i][j]
#     col = 0
#     row = 0
#     dim = 0
#     for cycle in range(6):
#         for dim in range(len(pocket)):
#             if col == len(pocket[dim])-10 or dim == len(pocket)-10 or row == len(pocket[dim])-10:
#                 break
#             for row in range(len(pocket[dim])):
#                 for col in range(len(pocket[dim][row])):
#                     neighbours_states = findNeighbours(pocket,dim,row,col)
#                     num_active = neighbours_states.count('#')
#                     if pocket[dim][row][col] == '#':
#                         remain_active = num_active == 2 or num_active == 3
#                         if remain_active is False:
#                             pocket[dim][row][col] = '.'
#                         else:
#                             continue
#                     else:
#                         convert_to_active = num_active == 3
#                         if convert_to_active is True:
#                             pocket[dim][row][col] = '#'
#                         else:
#                             continue
#
#     return pocket
#
# # Ninth day
# # Part 1 - COVID +VE DAY
# # Note: need to change preamble number accordingly
# def AoC9a(input_data_list):
#     data = []
#     preamble_length = 25
#     for element in input_data_list:
#         data.append(int(element))
#     look_back = data[0:preamble_length]
#     index_incr = 1
#     for i in range(preamble_length,len(data)):
#         val = data[i]
#         check = True
#         for int1 in look_back:
#             for int2 in reversed(look_back):
#                 if int1 != int2 and val == int1 + int2:
#                     check = False
#                 else:
#                     continue
#         if check is True:
#             return val
#         # Amend look back list
#         look_back = data[index_incr:preamble_length + index_incr]
#         index_incr += 1
#
#     return data
# # Part 2 - COVID +VE DAY
# # Note: need to change preamble number accordingly
# def AoC9b(input_data_list):
#     special_num = AoC9a(input_data_list)
#     data = []
#     for element in input_data_list:
#         data.append(int(element))
#
#     # Use greedy method
#     # Sum consecutive vals from data
#     not_met = True
#     i = 0
#     while not_met:
#         sum = 0
#         nums = []
#         for j in range(i,len(data)):
#             sum += data[j]
#             nums.append(data[j])
#             if sum == special_num:
#                 return max(nums) + min(nums)
#             elif sum > special_num:
#                 i += 1
#                 break
#             else:
#                 continue
#
#     return special_num

# # Tenth day
# # Part 1
# def findValidRatingsPart1(data,current_rating):
#     # Take the first rating that is differs
#     # from my current rating by less than or equal to three
#     for element in data:
#         diff = element - current_rating
#         if diff <= 3 and diff > 0:
#             return element,diff
#         else:
#             continue
# def AoC10a(input_data_list):
#     data = []
#     for element in input_data_list:
#         data.append(int(element))
#     data.sort()
#     # Set current voltage to equal outlet
#     current_rating = 0
#     diff_vect = []
#     cond = True
#     while cond:
#         current_rating,diff = findValidRatingsPart1(data,current_rating)
#         diff_vect.append(diff)
#         if current_rating == data[len(data)-1]:
#             cond = False
#
#     # Append one last three for in built adapter
#     diff_vect.append(3)
#
#     # Find product of instances of a difference of 1 and 3
#     ans = diff_vect.count(1)*diff_vect.count(3)
#     return ans
# # Part 2
# def findValidRatingsPart2(data,current_rating):
#     # Take the first rating that is differs
#     # from my current rating by less than or equal to three
#     elements = []
#     diffs = []
#     for element in data:
#         diff = element - current_rating
#         if diff <= 3 and diff > 0:
#             if len(elements) < 1:
#                 output_rating = element
#                 diff_to_save = diff
#             elements.append(element)
#             diffs.append(diff)
#         else:
#             continue
#
#     return elements, diffs, output_rating, diff_to_save
# def AoC10b(input_data_list):
#     data = []
#     for element in input_data_list:
#         data.append(int(element))
#     data.sort()
#     # Set current voltage to equal outlet
#     current_rating = 0
#     rating_tracker = [0]
#     diff_vect = []
#     diff_gen = []
#     elements = []
#     cond = True
#     while cond:
#         elements_to_add, diffs, current_rating, diff_to_save = findValidRatingsPart2(data,current_rating)
#         elements.append(elements_to_add)
#         diff_vect.append(diffs)
#         diff_gen.append(diff_to_save)
#         rating_tracker.append(current_rating)
#         if current_rating == data[len(data)-1]:
#             cond = False
#
#     # Append one last three for in built adapter
#     diff_gen.append(3)
#     rating_tracker.append(max(data)+3)
#
#     # Now get combinations of lists in elements that are longer than length = 1
#     solutions = []
#     # Append first solution that we have already calculated
#     solutions.append(rating_tracker)
#
#     # Find choice indices
#     choice_indices = []
#     for i, list in enumerate(elements):
#         if len(list) > 1:
#             choice_indices.append(i)
#
#     count_vect = []
#     for index in choice_indices:
#         count = 0
#         for choice in elements[index]:
#             count += 1
#         count_vect.append(count)
#
#     return count_vect, np.prod(count_vect)
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
