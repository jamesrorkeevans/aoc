from collections import defaultdict

with open("advent20-10a-input.txt","r") as f:
    input = f.read().split('\n')
    del input[-1]
    input = [int(n) for n in input]

input.append(0)
input.append(max(input)+3)
input.sort()


def part1(input):
    differences = defaultdict(int)

    for i in range(1,len(input)):
        differences[input[i] - input[i-1]] += 1

    return differences[3] * differences[1]

def count_routes(input, start, increment, end):
    try:
        if input[start + increment] - input[start] > 3:
            return False
        if input[start + increment] > input[end]:
            return False
        if input[start + increment] == input[end]:
            return True

    except IndexError:
        return 0

    return sum([ count_routes(input, start + increment, next_increment, end) for next_increment in (1,2,3)])

def part2(input):

    chunks = [0, max(input)]
    for i in range(1, len(input)-1):
        if input[i+1] - input[i] == 3:
            chunks.append(i)
    chunks.sort()

    routes = 1
    for j in range(1, len(chunks)-1):
        routes *= count_routes(input, chunks[j-1], 0, chunks[j])

    return routes

print part1(input)
print part2(input)
