# Seventh day
# Part 1 - a took a few attempts
def findShinyGold(dict_of_bags,shiny_gold_bags,key,keys):
    if key in keys:
        return shiny_gold_bags
    loop_num = len(dict_of_bags[key])
    for i in range(loop_num):
        if dict_of_bags[key][i].find('shiny gold bag') > -1 or dict_of_bags[key][i].find('shiny gold bags') > -1:
            shiny_gold_bags += 1
            keys.append(key)
            return shiny_gold_bags
        elif dict_of_bags[key][i] == 'no other bags':
            return shiny_gold_bags
        else:
            key_form = dict_of_bags[key][i][2:]
            if key_form[-1] != 's':
                key_form += 's'
            shiny_gold_bags = findShinyGold(dict_of_bags,shiny_gold_bags,key_form,keys)
            keys.append(key_form)
            continue
    return shiny_gold_bags
def AoC7a1(input_data_list):
    dict_of_bags = {}
    for element in input_data_list:
        temp_1 = element.replace('.','')
        temp_2 = temp_1.split(' contain ')
        if temp_2[0] == 'shiny gold bags':
            continue
        else:
            dict_of_bags[temp_2[0]] = temp_2[1].split(', ')


    shiny_gold_bags = 0
    bags = []
    for x in range(len(dict_of_bags)):
        keys =[]
        print(list(dict_of_bags.keys())[x])
        shiny_gold_bags = findShinyGold(dict_of_bags,shiny_gold_bags,list(dict_of_bags.keys())[x],keys)
        print(shiny_gold_bags)
        bags.append(shiny_gold_bags)

    count = 0
    for bag in bags:
        if bag != 0:
            count += 1
    return count
def AoC7a2(input_data_list):
    dict_of_bags = {}
    for element in input_data_list:
        temp_1 = element.replace('.','')
        temp_2 = temp_1.split(' contain ')
        if temp_2[0] == 'shiny gold bags':
            continue
        else:
            dict_of_bags[temp_2[0]] = temp_2[1].split(', ')

    bags_with_shiny_gold = []
    bags_with_nothing = []
    for key in dict_of_bags:
        further_bags = len(dict_of_bags[key])
        for i in range(further_bags):
            if dict_of_bags[key][i].find('shiny gold bag') > -1 or dict_of_bags[key][i].find('shiny gold bags') > -1:
                bags_with_shiny_gold.append(key)
            elif dict_of_bags[key][i] == 'no other bags':
                bags_with_nothing.append(key)
                continue
            else:
                continue

    shiny_gold_count = 0
    for key in dict_of_bags:
        further_bags = len(dict_of_bags[key])
        for i in range(further_bags):
            if dict_of_bags[key][i].find('shiny gold bag') > -1 or dict_of_bags[key][i].find('shiny gold bags') > -1:
                shiny_gold_count += 1
                break
            elif dict_of_bags[key][i] == 'no other bags':
                break
            else:
                nothing_in_bag = False
                test = dict_of_bags[key][i][2:]
                for bag in bags_with_nothing:
                    if bag.find(dict_of_bags[key][i][2:]) > -1:
                        nothing_in_bag = True
                        break
                    else:
                        continue

                if nothing_in_bag != True:
                    for bag in bags_with_shiny_gold:
                        if bag.find(dict_of_bags[key][i][2:]) > -1:
                            shiny_gold_count += 1
                            break
                    break
                else:
                    continue

    return shiny_gold_count
def AoC7a3(input_data_list):
    dict_of_bags = {}
    for element in input_data_list:
        temp_1 = element.replace('.','')
        temp_2 = temp_1.split(' contain ')
        if temp_2[0] == 'shiny gold bags':
            continue
        else:
            dict_of_bags[temp_2[0]] = temp_2[1].split(', ')

    bags_with_shiny_gold = []
    bags_with_nothing = []
    for key in dict_of_bags:
        further_bags = len(dict_of_bags[key])
        for i in range(further_bags):
            if dict_of_bags[key][i].find('shiny gold bag') > -1 or dict_of_bags[key][i].find('shiny gold bags') > -1:
                bags_with_shiny_gold.append(key)
            elif dict_of_bags[key][i] == 'no other bags':
                bags_with_nothing.append(key)
                continue
            else:
                continue

    shiny_gold_count = 0
    for key in dict_of_bags:
        further_bags = len(dict_of_bags[key])
        for i in range(further_bags):
            if dict_of_bags[key][i][-1] != 's':
                val_with_s = dict_of_bags[key][i]+'s'
                if val_with_s[2:] == 'shiny gold bags' or val_with_s[2:] in bags_with_shiny_gold:
                    shiny_gold_count += 1
                    break
                else:
                    continue
            else:
                if dict_of_bags[key][i][2:] == 'shiny gold bags' or dict_of_bags[key][i][2:] == 'shiny gold bag' or dict_of_bags[key][i][2:] in bags_with_shiny_gold:
                    shiny_gold_count += 1
                    break
                else:
                    continue


    return shiny_gold_count
def AoC7a4(input_data_list):
    dict_of_bags = {}
    for element in input_data_list:
        temp_1 = element.replace('.','')
        temp_2 = temp_1.split(' contain ')
        if temp_2[0] == 'shiny gold bags':
            continue
        else:
            dict_of_bags[temp_2[0]] = temp_2[1].split(', ')

    bags_with_shiny_gold = []
    bags_with_nothing = []
    for key in dict_of_bags:
        further_bags = len(dict_of_bags[key])
        for i in range(further_bags):
            if dict_of_bags[key][i].find('shiny gold bag') > -1 or dict_of_bags[key][i].find('shiny gold bags') > -1:
                bags_with_shiny_gold.append(key)
            elif dict_of_bags[key][i] == 'no other bags':
                bags_with_nothing.append(key)
                continue
            else:
                continue

    shiny_gold_count = 0
    for key in dict_of_bags:
        if key in bags_with_shiny_gold:
            shiny_gold_count += 1
            continue
        further_bags = len(dict_of_bags[key])
        for i in range(further_bags):
            if dict_of_bags[key][i][-1] != 's':
                val_with_s = dict_of_bags[key][i]+'s'
                print(val_with_s[2:])
                if val_with_s[2:] in bags_with_shiny_gold:
                    shiny_gold_count += 1
                    break
                else:
                    continue
            else:
                if dict_of_bags[key][i][2:] in bags_with_shiny_gold:
                    shiny_gold_count += 1
                    break
                else:
                    continue
    return shiny_gold_count, bags_with_shiny_gold



# Winner
def findGold(dict_of_bags,bags_with_shiny_gold,bags_with_nothing,key,count):
    bags_inside = len(dict_of_bags[key])
    for i in range(bags_inside):
        if dict_of_bags[key][i][-1] != 's':
            val_with_s = dict_of_bags[key][i] + 's'
            if val_with_s[2:] in bags_with_nothing:
                if i == bags_inside - 1:
                    break
                else:
                    continue
            elif val_with_s[2:] in bags_with_shiny_gold:
                count += 1
                break
            else:
                temp_count = count
                count = findGold(dict_of_bags, bags_with_shiny_gold, bags_with_nothing, val_with_s[2:], count)
                if count > temp_count:
                    return count
                else:
                    continue
        else:
            if dict_of_bags[key][i][2:] in bags_with_nothing:
                if i == bags_inside - 1:
                    break
                else:
                    continue
            elif dict_of_bags[key][i][2:] in bags_with_shiny_gold:
                count += 1
                break
            else:
                temp_count = count
                count = findGold(dict_of_bags, bags_with_shiny_gold, bags_with_nothing, dict_of_bags[key][i][2:], count)
                if count > temp_count:
                    return count
                else:
                    continue
    return count
def AoC7a(input_data_list):
    dict_of_bags = {}
    for element in input_data_list:
        temp_1 = element.replace('.', '')
        temp_2 = temp_1.split(' contain ')
        if temp_2[0] == 'shiny gold bags':
            continue
        else:
            dict_of_bags[temp_2[0]] = temp_2[1].split(', ')

    bags_with_shiny_gold = []
    bags_with_nothing = []
    for key in dict_of_bags:
        further_bags = len(dict_of_bags[key])
        for i in range(further_bags):
            if dict_of_bags[key][i].find('shiny gold bag') > -1 or dict_of_bags[key][i].find('shiny gold bags') > -1:
                bags_with_shiny_gold.append(key)
            elif dict_of_bags[key][i] == 'no other bags':
                bags_with_nothing.append(key)
                continue
            else:
                continue
    count = 0
    for key in dict_of_bags:
        if key in bags_with_nothing:
            continue
        elif key in bags_with_shiny_gold:
            count += 1
        else:
            count = findGold(dict_of_bags, bags_with_shiny_gold, bags_with_nothing,key,count)

    return count

# Part 2 - Found extremely difficult
# But final solution was very simple in the end...
def findContents(key,dict_of_bags,count,thing,key_input_number):
    bags_types_inside = len(dict_of_bags[key])
    for i in range(bags_types_inside):
        if dict_of_bags[key][i] != 'no other bags':
            count += key_input_number * int(dict_of_bags[key][i][0])
            thing.append(int(dict_of_bags[key][i][0]))
            right_format_key = dict_of_bags[key][i][2:]
            if right_format_key[-1] != 's':
                right_format_key += 's'
            count,thing = findContents(right_format_key, dict_of_bags, count,thing,int(dict_of_bags[key][i][0]))
        else:
            return count, thing
    return count, thing
def AoC7b1(input_data_list):
    dict_of_bags = {}
    shiny_gold_bag_contents = []
    for element in input_data_list:
        temp_1 = element.replace('.', '')
        temp_2 = temp_1.split(' contain ')
        if temp_2[0] == 'shiny gold bags':
            shiny_gold_bag_contents = temp_2[1].split(', ')
            continue
        else:
            dict_of_bags[temp_2[0]] = temp_2[1].split(', ')

    count = 0
    thing = []
    for key in shiny_gold_bag_contents:
        thing.append(int(key[0]))
        right_format_key = key[2:]
        if right_format_key[-1] != 's':
            right_format_key += 's'
        count, thing = findContents(right_format_key,dict_of_bags,count,thing,int(key[0]))
        count += int(key[0])
    return count, thing
def countBags(bag_of_interest, dict_of_bags,count2):
    count1 = 0
    for element in bag_of_interest:
        if element != 'no other bags':
            # Save sum of bags at current level
            count1 += int(element[0])
            # Save outer bag num
            outer_bag_num = int(element[0])
            if element[-1] != 's':
                temp = element[2:] + 's'
                count_temp = countBags(dict_of_bags[temp], dict_of_bags,count2)
            else:
                count_temp = countBags(dict_of_bags[element[2:]], dict_of_bags,count2)
        else:
            return count2
        count2 += (count_temp * outer_bag_num)
    count2 += count1
    return count2
def countBags1(bag_of_interest,dict_of_bags,count2):
    for element in bag_of_interest:
        if element != 'no other bags':
            # Save outer bag num
            outer_bag_num = int(element[0])
            if element[-1] != 's':
                temp = element[2:] + 's'
                count2 += countBags1(dict_of_bags[temp], dict_of_bags, count2)
            else:
                count2 += countBags1(dict_of_bags[element[2:]], dict_of_bags, count2)
        else:
            return count2

    count2 += count2 * outer_bag_num
    count2 += outer_bag_num
    return count2
def AoC7b2(input_data_list):
    dict_of_bags = {}
    for element in input_data_list:
        temp_1 = element.replace('.', '')
        temp_2 = temp_1.split(' contain ')
        dict_of_bags[temp_2[0]] = temp_2[1].split(', ')

    bags_with_shiny_gold = []
    bags_with_nothing = []
    bags_in_bag = []
    for key in dict_of_bags:
        further_bags = len(dict_of_bags[key])
        bags_inside = 0
        for i in range(further_bags):
            if dict_of_bags[key][i].find('shiny gold bag') > -1 or dict_of_bags[key][i].find('shiny gold bags') > -1:
                bags_with_shiny_gold.append(key)
                bags_inside += int(dict_of_bags[key][i][0])
            elif dict_of_bags[key][i] == 'no other bags':
                bags_with_nothing.append(key)
                bags_inside += int(0)
            else:
                bags_inside += int(dict_of_bags[key][i][0])
                continue
        bags_in_bag.append([key,bags_inside])

    ans = foo(dict_of_bags, 'shiny gold bags')
    return ans
# Winner
def bagsInside(dict_of_bags,bag_x):
    ans = 0
    for element in dict_of_bags[bag_x]:
        if element != 'no other bags':
            if element[-1] != 's':
                temp = element + 's'
                ans += int(element[0]) + (int(element[0])*bagsInside(dict_of_bags,temp[2:]))
            else:
                ans += int(element[0]) + (int(element[0])*bagsInside(dict_of_bags,element[2:]))
        else:
            ans = 0
            return ans

    return ans
def AoC7b(input_data_list):
    dict_of_bags = {}
    for element in input_data_list:
        temp_1 = element.replace('.', '')
        temp_2 = temp_1.split(' contain ')
        dict_of_bags[temp_2[0]] = temp_2[1].split(', ')

    ans = bagsInside(dict_of_bags, 'shiny gold bags')
    return ans
