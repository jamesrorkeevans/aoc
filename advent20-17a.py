with open("advent20-17a-input.txt","r") as f:
    input = f.read().split('\n')
    del input[-1]

active_cubes = []
active_hypercubes = []

for y in range(8):
    for x in range(8):
        z = 0
        w = 0
        if input[y][x] == '#':
            active_cubes.append([x, y, z])
            active_hypercubes.append([x, y, z, w])

def count_neighbours(cube, active_cubes):

    neighbours = 0

    for active_cube in active_cubes:

        if active_cube == cube:
            continue

        if active_cube[0] < cube[0] - 1 or active_cube[0] > cube[0] + 1:
            continue
        if active_cube[1] < cube[1] - 1 or active_cube[1] > cube[1] + 1:
            continue
        if active_cube[2] < cube[2] - 1 or active_cube[2] > cube[2] + 1:
            continue
        if len(cube) == 4:
            if active_cube[3] < cube[3] - 1 or active_cube[3] > cube[3] + 1:
                continue

        neighbours += 1

    return neighbours

def cube_cycle_1(active_cubes):

    new_active_cubes = []

    for z in range(-6, 6):
        for y in range(-6, 14):
            for x in range(-6, 14):

                neighbours = count_neighbours([x, y, z], active_cubes)

                if neighbours == 2 or neighbours == 3:
                    if [x, y, z] in active_cubes:
                        new_active_cubes.append([x, y, z])
                if neighbours == 3 and [x, y, z] not in active_cubes:
                    new_active_cubes.append([x, y, z])

    return new_active_cubes

def part1(active_cubes, cycles):

    for cycle in range(cycles):
        active_cubes = cube_cycle_1(active_cubes)

    return len(active_cubes)

def cube_cycle_2(active_hypercubes, cycle):

    new_active_hypercubes = []
    for w in range(1 - cycle, 0 + cycle):
        for z in range(1 - cycle, 0 + cycle):
            for y in range(1 - cycle, 8 + cycle):
                for x in range(1 - cycle, 8 + cycle):

                    neighbours = count_neighbours([x, y, z, w], active_hypercubes)

                    if neighbours == 2 or neighbours == 3:
                        if [x, y, z, w] in active_hypercubes:
                            new_active_hypercubes.append([x, y, z, w])
                    if neighbours == 3 and [x, y, z, w] not in active_hypercubes:
                        new_active_hypercubes.append([x, y, z, w])

    return new_active_hypercubes

def part2(active_hypercubes, cycles):

    for cycle in range(cycles):
        active_hypercubes = cube_cycle_2(active_hypercubes, cycle + 2)

    return len(active_hypercubes)

print part1(active_cubes, 6)
print part2(active_hypercubes, 6)
