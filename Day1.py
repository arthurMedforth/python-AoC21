
# First day - Part 1 and Part 2
def AoC1(input_data_list):
    for i in range(len(input_data_list)):
        for j in range(len(input_data_list)):
            for k in range(len(input_data_list)):
                temp_val = input_data_list[i] + input_data_list[j] + input_data_list[k]
                if temp_val == 2020:
                    ans = input_data_list[i] * input_data_list[j] * input_data_list[k]
                    return ans
