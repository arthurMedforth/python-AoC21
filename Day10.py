# Tenth day
# Part 1
def findValidRatingsPart1(data,current_rating):
    # Take the first rating that is differs
    # from my current rating by less than or equal to three
    for element in data:
        diff = element - current_rating
        if diff <= 3 and diff > 0:
            return element,diff
        else:
            continue
def AoC10a(input_data_list):
    data = []
    for element in input_data_list:
        data.append(int(element))
    data.sort()
    # Set current voltage to equal outlet
    current_rating = 0
    diff_vect = []
    cond = True
    while cond:
        current_rating,diff = findValidRatingsPart1(data,current_rating)
        diff_vect.append(diff)
        if current_rating == data[len(data)-1]:
            cond = False

    # Append one last three for in built adapter
    diff_vect.append(3)

    # Find product of instances of a difference of 1 and 3
    ans = diff_vect.count(1)*diff_vect.count(3)
    return ans
# Part 2
def findValidRatingsPart2(data,current_rating):
    # Take the first rating that is differs
    # from my current rating by less than or equal to three
    elements = []
    diffs = []
    for element in data:
        diff = element - current_rating
        if diff <= 3 and diff > 0:
            if len(elements) < 1:
                output_rating = element
                diff_to_save = diff
            elements.append(element)
            diffs.append(diff)
        else:
            continue

    return elements, diffs, output_rating, diff_to_save
def AoC10b(input_data_list):
    data = []
    for element in input_data_list:
        data.append(int(element))
    data.sort()
    # Set current voltage to equal outlet
    current_rating = 0
    rating_tracker = [0]
    diff_vect = []
    diff_gen = []
    elements = []
    cond = True
    while cond:
        elements_to_add, diffs, current_rating, diff_to_save = findValidRatingsPart2(data,current_rating)
        elements.append(elements_to_add)
        diff_vect.append(diffs)
        diff_gen.append(diff_to_save)
        rating_tracker.append(current_rating)
        if current_rating == data[len(data)-1]:
            cond = False

    # Append one last three for in built adapter
    diff_gen.append(3)
    rating_tracker.append(max(data)+3)

    # Now get combinations of lists in elements that are longer than length = 1
    solutions = []
    # Append first solution that we have already calculated
    solutions.append(rating_tracker)

    # Find choice indices
    choice_indices = []
    for i, list in enumerate(elements):
        if len(list) > 1:
            choice_indices.append(i)

    count_vect = []
    for index in choice_indices:
        count = 0
        for choice in elements[index]:
            count += 1
        count_vect.append(count)
