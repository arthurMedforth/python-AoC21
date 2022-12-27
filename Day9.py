# Ninth day
# Part 1 - COVID +VE DAY
# Note: need to change preamble number accordingly
def AoC9a(input_data_list):
    data = []
    preamble_length = 25
    for element in input_data_list:
        data.append(int(element))
    look_back = data[0:preamble_length]
    index_incr = 1
    for i in range(preamble_length,len(data)):
        val = data[i]
        check = True
        for int1 in look_back:
            for int2 in reversed(look_back):
                if int1 != int2 and val == int1 + int2:
                    check = False
                else:
                    continue
        if check is True:
            return val
        # Amend look back list
        look_back = data[index_incr:preamble_length + index_incr]
        index_incr += 1

    return data
# Part 2 - COVID +VE DAY
# Note: need to change preamble number accordingly
def AoC9b(input_data_list):
    special_num = AoC9a(input_data_list)
    data = []
    for element in input_data_list:
        data.append(int(element))

    # Use greedy method
    # Sum consecutive vals from data
    not_met = True
    i = 0
    while not_met:
        sum = 0
        nums = []
        for j in range(i,len(data)):
            sum += data[j]
            nums.append(data[j])
            if sum == special_num:
                return max(nums) + min(nums)
            elif sum > special_num:
                i += 1
                break
            else:
                continue

    return special_num
