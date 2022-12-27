# Fifth day
def Ao5findIt(lower,upper,instruction,row_or_col1,row_or_col2):
    mid_point = int(((upper + 1)-lower) / 2) + lower
    if instruction == row_or_col1:
        lower = lower
        upper = mid_point - 1
    elif instruction == row_or_col2:
        lower = mid_point
        upper = upper
    else:
        error('Something weird going on here')

    return lower, upper
def AoC5(input_data_list):
    row_and_col = []
    seat_IDs = []
    for line in input_data_list:
        lower_row = 0
        upper_row = 127
        lower_column = 0
        upper_column = 7

        # Find row
        for char in line[0:7]:
            lower_row,upper_row = Ao5findIt(lower_row,upper_row,char,'F','B')

        # Find column
        for char in line[7:]:
            lower_column,upper_column = Ao5findIt(lower_column,upper_column,char,'L','R')

        row_and_col.append([lower_row,lower_column])
        seat_IDs.append((lower_row*8)+lower_column)

    # Find missing seats
    missing_seats = []
    max_ID = (127 * 8)+8
    check_range = range(1,max_ID)

    for element in check_range:
        if element in seat_IDs:
            continue
        else:
            missing_seats.append(element)

    return missing_seats
