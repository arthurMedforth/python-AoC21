# Third day - Part 1 and 2
def AoC3(input_data_list):
    # Find out how many times I will need to repeat the seq
    new_piste = []
    length_of_map = len(input_data_list)
    breadth_of_map = len(input_data_list[0])
    right_operation = length_of_map * 3
    maps_needed = math.ceil(right_operation/breadth_of_map)
    for element in input_data_list:
        new_piste.append(element*maps_needed)
    onwards = True
    tree_count2 = 0

    pos_x = 0
    pos_y = 0
    while onwards:
        pos_x += 3
        pos_y += 1
        if new_piste[pos_y][pos_x] == '#':
            tree_count2 += 1
        else:
            tree_count2 = tree_count2

        if pos_y == len(new_piste) - 1:
            onwards = False
    return tree_count2
