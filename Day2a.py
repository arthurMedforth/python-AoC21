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