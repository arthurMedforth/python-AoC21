def AoC2021_1a(input_data_list):
    count = 0
    for i, element in enumerate(input_data_list):
        if i == 0:
            continue
        else:
            if int(element) > int(input_data_list[i-1]):
                count += 1

    return count
