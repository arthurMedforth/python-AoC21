# Sixth day
# Part 1 - add double return to input after last line
def AoC6a(input_data_list):
    data = []
    temp = []
    for element in input_data_list:
        if element != '':
            temp.append(element)
        else:
            data.append(temp)
            temp = []

    yes_count_groups = 0
    for element in data:
        yes_count = 0
        letter_vec = []
        for person in element:
            for question in person:
                if question in letter_vec:
                    yes_count = yes_count

                else:
                    yes_count += 1
                    letter_vec.append(question)
        yes_count_groups += yes_count

    return yes_count_groups
# Part 2 - add double return to input after last line
def AoC6b(input_data_list):
    data = []
    temp = []
    for element in input_data_list:
        if element != '':
            temp.append(element)
        else:
            data.append(temp)
            temp = []
    yes_count_groups = 0
    for element in data:
        letter_vec = []
        people = len(element)
        if people == 1:
            yes_count_groups += len(element[0])
            continue
        for i, person in enumerate(element):
            if i == 0:
                letter_vec = [char for char in person]
            else:
                for q in letter_vec:
                    yes_count = 0
                    for stud in element[1:]:
                        if stud.find(q) > -1:
                            yes_count += 1
                        if yes_count == len(element)-1:
                            yes_count_groups += 1
                        else:
                            continue
                break
    return yes_count_groups
