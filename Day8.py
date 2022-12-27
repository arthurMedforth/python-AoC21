# Eighth day
# Part 1
def AoC8a(input_data_list):
    data = []
    for m, element in enumerate(input_data_list):
        data.append(element.split(' '))

    # Convert input into a list with incremental key
    dict_instructions = {}
    for i, element in enumerate(data):
        dict_instructions[i] = element

    # Execute game instructions
    # Stopping when any instruction is repeated
    acc = 0 # Initialise accumulator
    pointer = 0
    keep_going = True
    instruction_history = []
    while keep_going:
        if pointer in instruction_history:
            ans = acc
            keep_going = False

        # Save instruction history
        instruction_history.append(pointer)
        instr = dict_instructions[pointer][0]
        sign = dict_instructions[pointer][1][0]
        if sign == '-':
            val = -1 * int(dict_instructions[pointer][1][1:])
        else:
            val = int(dict_instructions[pointer][1][1:])

        if instr == 'jmp':
            pointer += val
        elif instr == 'acc':
            pointer += 1
            acc += val
        elif instr == 'nop':
            pointer += 1
        else:
            raise ValueError('Invalid instruction', instr)

    return ans
# Part 2
def AoC8b(input_data_list):
    data = []
    for m, element in enumerate(input_data_list):
        data.append(element.split(' '))

    # Convert input into a list with incremental key
    dict_instructions = {}
    for i, element in enumerate(data):
        dict_instructions[i] = element

    # Get keys of instr that are nop or jmp
    nop_or_jmp_keys = []
    for key in dict_instructions:
        if dict_instructions[key][0] == 'jmp' or dict_instructions[key][0] == 'nop':
            nop_or_jmp_keys.append(key)

    # Try flipping each occurence of nop and jmp
    for key in nop_or_jmp_keys:
        # Execute game instructions
        # Stopping when any instruction is repeated
        acc = 0  # Initialise accumulator
        pointer = 0
        keep_going = True
        instruction_history = []
        while keep_going:
            if pointer == len(input_data_list):
                return acc

            if pointer in instruction_history:
                keep_going = False

            # Save instruction history
            instruction_history.append(pointer)
            instr = dict_instructions[pointer][0]
            if pointer == key and instr == 'nop':
                instr = 'jmp'
            elif pointer == key and instr == 'jmp':
                instr = 'nop'
            else:
                instr = instr

            sign = dict_instructions[pointer][1][0]
            if sign == '-':
                val = -1 * int(dict_instructions[pointer][1][1:])
            else:
                val = int(dict_instructions[pointer][1][1:])

            if instr == 'jmp':
                pointer += val
            elif instr == 'acc':
                pointer += 1
                acc += val
            elif instr == 'nop':
                pointer += 1
            else:
                raise ValueError('Invalid instruction', instr)
