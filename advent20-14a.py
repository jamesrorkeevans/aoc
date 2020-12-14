with open("advent20-14a-input.txt","r") as f:
    input = f.read().split('\n')
    del input[-1]

#Part 1 ---------------------------------------------

def update_memory_1(input, instruction, mask):

    location, value = instruction.split('] = ')
    location = int(location.replace('mem[', ''))
    value = format(int(value), '036b')
    output_value = ''

    for i in range(len(value)):
        if mask[i] == 'X':
            output_value += value[i]
        else:
            output_value += mask[i]

    output_value = int(output_value, base=2)

    return location, output_value



def part1(input):

    memory = {}
    mask = '000000000000000000000000000000000000'

    for instruction in input:

        if instruction.split(' = ')[0] == 'mask':
            mask = instruction[7:]
        else:
            k, v = update_memory_1(input, instruction, mask)
            memory[k] = v

    return sum(memory.values())



#Part 2 ---------------------------------------------

def expand_locations(location, mask):

    decoded_location = ''

    for i in range(len(mask)):
        if mask[i] == 'X':
            decoded_location += 'X'
        elif mask[i] == '1':
            decoded_location += '1'
        else:
            decoded_location += location[i]

    combinations = 2 ** decoded_location.count('X')
    locations_ = []

    for j in range(combinations):

        next_location = decoded_location
        number_of_Xs = decoded_location.count('X')
        bits = format(j, '0' + str(number_of_Xs) + 'b')

        for X in range(number_of_Xs):
            next_location = next_location.replace('X', bits[X], 1)
        locations_.append(next_location)

    return locations_



def update_memory_2(input, instruction, mask):

    location, value = instruction.split('] = ')
    location = int(location.replace('mem[', ''))
    location = format(int(location), '036b')

    locations_ = expand_locations(location, mask)

    value = int(value)
    output_values = {}

    for location in locations_:
        output_values[int(location, base=2)] = value

    return output_values



def part2(input):

    memory = {}
    mask = '000000000000000000000000000000000000'

    for instruction in input:


        if instruction.split(' = ')[0] == 'mask':
            mask = instruction[7:]
        else:
            new_mem = {}
            new_mem = update_memory_2(input, instruction, mask)
            for k in new_mem.keys():
                memory[k] = new_mem[k]

    return sum(memory.values())



print part1(input)
print part2(input)
