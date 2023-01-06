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