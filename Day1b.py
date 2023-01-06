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