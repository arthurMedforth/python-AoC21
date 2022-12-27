# Second day - Part 1 and Part 2
def AoC2(input_data_list):
    # Make dict
    better_format_input = []
    for element in input_data_list:
        better_format_input.append(element.replace(" ", "").split(':'))

    valid_count = 0
    for element in better_format_input:
        #no_hyphon = element[0][element[0].find()]
        letter_for_rule = element[0][-1]
        password_rule = re.split('[a-z|,]+', element[0])
        password_rule[1] = letter_for_rule
        del element[0]

        numerical_rule = password_rule[0].split("-")
        numerical_rule[0] = int(numerical_rule[0])
        numerical_rule[1] = int(numerical_rule[1])
        password_rule[0] = numerical_rule

        letter_instances = []
        [letter_instances.append(instance) for instance, ltr in enumerate(element[0]) if ltr == password_rule[1]]

        # P1
#        instances = len(letter_instances)
#        if instances >= password_rule[0][0] and instances <= password_rule[0][1]:
#            valid_count += 1
#        else:
#            valid_count = valid_count


        # P2
        for instance in letter_instances:
            temp_count = valid_count
            if instance == password_rule[0][0] - 1:
                # We have first character at right spot
                for instance_2_index in range(len(letter_instances)):
                    if letter_instances[instance_2_index] == password_rule[0][1] - 1:
                        valid_count = valid_count
                        break
                    elif letter_instances[instance_2_index] != password_rule[0][1] - 1 and instance_2_index == len(letter_instances) - 1:
                        valid_count += 1
                        break
                    else:
                        continue
            elif instance == password_rule[0][1] - 1:
                # We have first character at right spot
                for instance_2_index in range(len(letter_instances)):
                    if letter_instances[instance_2_index] == password_rule[0][0] - 1:
                        valid_count = valid_count
                        break
                    elif letter_instances[instance_2_index] != password_rule[0][0] - 1 and instance_2_index == len(letter_instances) - 1:
                        valid_count += 1
                        break
                    else:
                        continue
            else:
                valid_count = valid_count

    return valid_count
