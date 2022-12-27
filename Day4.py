# Fourth day
# Part 1 - add double return to input after last line
def AoC4a(input_data_list):
    passports_uniform_format = []
    # Use spaces in input_data_list to separate different passports
    onwards = True
    while onwards:
        for i in range(len(input_data_list)):
            j_save = [0]
            if input_data_list[i] == '':  # space = new line
                # Concatenate ALL previous lists elements as they are same passport
                temp_data = input_data_list[0]
                for j in range(i - 1):
                    temp_data = temp_data + ' ' + input_data_list[j + 1]
                    j_save.append(j + 1)

                passports_uniform_format.append(temp_data)
                j_save.append(j_save[-1] + 1)
                # Delete elements
                for k in sorted(j_save, reverse=True):
                    del input_data_list[k]
                break
            else:
                continue
        if len(input_data_list) == 0:
            onwards = False
        else:
            continue

    valid_count = 0
    for element in passports_uniform_format:
        byr_present = element.find('byr')
        iyr_present = element.find('iyr')
        hgt_present = element.find('hgt')
        eyr_present = element.find('eyr')
        hcl_present = element.find('hcl')
        ecl_present = element.find('ecl')
        pid_present = element.find('pid')

        if byr_present != -1 and iyr_present != -1 and hgt_present != -1 and eyr_present != -1 and hcl_present != -1 and ecl_present != -1 and pid_present != -1:
            valid_count += 1
        else:
            valid_count = valid_count

    return valid_count
# Part 2 - add double return to input after last line
def AoC4b(input_data_list):
    passports_uniform_format = []

    # Use spaces in input_data_list to separate different passports
    onwards = True
    while onwards:
        for i in range(len(input_data_list)):
            j_save = [0]
            if input_data_list[i] == '':  # space = new line
                # Concatenate ALL previous lists elements as they are same passport
                temp_data = input_data_list[0]
                for j in range(i - 1):
                    temp_data = temp_data + ' ' + input_data_list[j + 1]
                    j_save.append(j + 1)

                passports_uniform_format.append(temp_data)
                j_save.append(j_save[-1] + 1)
                # Delete elements
                for k in sorted(j_save, reverse=True):
                    del input_data_list[k]
                break
            else:
                continue
        if len(input_data_list) == 0:
            onwards = False
        else:
            continue
        delete_these = []
        for index, element in enumerate(passports_uniform_format):
            byr_present = element.find('byr')
            iyr_present = element.find('iyr')
            hgt_present = element.find('hgt')
            eyr_present = element.find('eyr')
            hcl_present = element.find('hcl')
            ecl_present = element.find('ecl')
            pid_present = element.find('pid')

            if byr_present != -1 and iyr_present != -1 and hgt_present != -1 and eyr_present != -1 and hcl_present != -1 and ecl_present != -1 and pid_present != -1:
                continue
            else:
                delete_these.append(index)

    for index in reversed(delete_these):
        del passports_uniform_format[index]

    new_format_passports = []
    for element in passports_uniform_format:
        new_format_passports.append(element.split())

    valid_count = 0
    for passport in new_format_passports:
        pass_count = 0
        for element in passport:
            key,value = element.split(':')
            # Rules
            if key == 'byr':
                if int(value) >= 1920 and int(value) <= 2002:
                    pass_count += 1
                    continue
                else:
                    continue
            elif key == 'iyr':
                if int(value) >= 2010 and int(value) <= 2020:
                    pass_count += 1
                    continue
                else:
                    continue
            elif key == 'eyr':
                if int(value) >= 2020 and int(value) <= 2030:
                    pass_count += 1
                    continue
                else:
                    continue
            elif key == 'hgt':
                if value[-2:] == 'cm':
                    if int(value[:-2]) >= 150 and int(value[:-2]) <= 193:
                        pass_count += 1
                        continue
                    else:
                        continue
                elif value[-2:] == 'in': # inches given
                    if int(value[:-2]) >= 59 and int(value[:-2])<= 76:
                        pass_count += 1
                        continue
                    else:
                        continue
                else:
                    continue
            elif key == 'hcl':
                if value[0] == '#' and len(value) == 7:
                    if value[1:].isalnum() == True:
                        pass_count += 1
                        continue
                    else:
                        continue
                else:
                    continue
            elif key == 'ecl':
                eye_colours = ['amb','blu','brn','gry','grn','hzl','oth']
                if (value in eye_colours):
                    pass_count += 1
                    continue
                else:
                    continue
            elif key == 'pid':
                if len(value) == 9:
                    pass_count += 1
                    continue
                else:
                    continue
        if pass_count == 7:
            valid_count += 1

    return valid_count
