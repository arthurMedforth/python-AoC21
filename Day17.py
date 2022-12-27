# Seventeenth day
# Part 1
# Appalling first try
# Went to learn about arrays and operations
def findNeighbours(pocket,dim,row,col):
    neighbours_states = []
    pos_vector = [-1,0,1]
    if dim==0 or row == 0 or col == 0:
        return neighbours_states
    for i in pos_vector:
        for j in pos_vector:
            for k in pos_vector:
                if i == 0 and j == 0 and k == 0:
                    continue
                else:
                    neighbours_states.append(pocket[dim+i][row+j][col+k])
    return neighbours_states
def AoC17a(input_data_list):
    # Split up chars
    brute_force = 20
    mid_dim = math.ceil(brute_force/2)
    data_for_later = []
    data = []
    for element in input_data_list:
        data.append(list(element))
        data_for_later.append(list(element))
    for i, element in enumerate(input_data_list):
        for j in range(len(element)):
            data[i][j] = '.'
    for i, element in enumerate(data):
        for j in range(brute_force):
            data[i].append('.')
    for j in range(brute_force):
        data.append(element)

    # Create giant array
    pocket = np.array([data]*brute_force)

    # Add in active starting sheet at the mid dimension

    for i in range(len(data_for_later)):
        for j in range(len(data_for_later[0])):
            pocket[mid_dim][math.floor(brute_force/2)+i][math.floor(brute_force/2)+j] = data_for_later[i][j]
    col = 0
    row = 0
    dim = 0
    for cycle in range(6):
        for dim in range(len(pocket)):
            if col == len(pocket[dim])-10 or dim == len(pocket)-10 or row == len(pocket[dim])-10:
                break
            for row in range(len(pocket[dim])):
                for col in range(len(pocket[dim][row])):
                    neighbours_states = findNeighbours(pocket,dim,row,col)
                    num_active = neighbours_states.count('#')
                    if pocket[dim][row][col] == '#':
                        remain_active = num_active == 2 or num_active == 3
                        if remain_active is False:
                            pocket[dim][row][col] = '.'
                        else:
                            continue
                    else:
                        convert_to_active = num_active == 3
                        if convert_to_active is True:
                            pocket[dim][row][col] = '#'
                        else:
                            continue

    return pocket
