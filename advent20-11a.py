with open("advent20-11a-input.txt","r") as f:
    input = f.read().split('\n')
    del input[-1]

def count_adjacent(input, x, y):
    occupied = 0
    for delta_x in [-1, 0, 1]:
        for delta_y in [-1, 0, 1]:
            if (delta_x, delta_y) == (0, 0):
                continue
            elif any([(x + delta_x) < 0, (y + delta_y) < 0, (x + delta_x) >= len(input[0]), (y + delta_y) >= len(input)]):
                continue
            else:
                occupied += (input[y + delta_y][x + delta_x] == '#')
    return occupied

def perform_round_1(input):
    output = [ '' for row in input]
    for y in range(len(input)):
        for x in range(len(input[0])):
            if input[y][x] == '.':
                output[y] += '.'
            elif input[y][x] == 'L' and count_adjacent(input, x, y) == 0:
                output[y] += '#'
            elif input[y][x] == '#' and count_adjacent(input, x, y) >= 4:
                output[y] += 'L'
            else:
                output[y] += input[y][x]
    return output

def count_occupied(input):
    return sum([row.count('#') for row in input])

def part1(input):
    old_grid = input
    while True:
        new_grid = perform_round_1(old_grid)
        if new_grid == old_grid:
            return new_grid
        else:
            old_grid = [x for x in new_grid]

def see(input, x, y, delta_x, delta_y):
    for distance in range(1,len(input)):
        if any( [ (x + distance * delta_x) < 0, (x + distance * delta_x > (len(input[0])-1)   ) ] ):
            return 0
        elif any( [ (y + distance * delta_y) < 0, (y + distance * delta_y > (len(input)-1)     ) ] ):
            return 0

        seat = input[y + distance * delta_y][x + distance * delta_x]

        if seat == '.':
            continue
        elif seat =='#':
            return 1
        else:
            return 0

def count_adjacent2(input, x, y):
    occupied = 0
    for delta_x in [-1, 0, 1]:
        for delta_y in [-1, 0, 1]:
            if (delta_x, delta_y) == (0, 0):
                continue
            occupied += see(input, x, y, delta_x, delta_y)
    return occupied

def perform_round_2(input):
    output = [ '' for row in input]
    for y in range(len(input)):
        for x in range(len(input[0])):

            if input[y][x] == '.':
                output[y] += '.'
            elif input[y][x] == 'L' and count_adjacent2(input, x, y) == 0:
                output[y] += '#'
            elif input[y][x] == '#' and count_adjacent2(input, x, y) >= 5:
                output[y] += 'L'
            else:
                output[y] += input[y][x]
    return output

def part2(input):
    old_grid = input

    while True:
        new_grid = perform_round_2(old_grid)

        if new_grid == old_grid:
            return new_grid
        else:
            old_grid = [x for x in new_grid]

print count_occupied(part1(input))
print count_occupied(part2(input))
