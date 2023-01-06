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