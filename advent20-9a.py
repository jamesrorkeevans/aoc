with open("advent20-9a-input.txt","r") as f:
    input = f.read().split('\n')
    del input[-1]
    input = [int(n) for n in input]

def check_digit(input, preamble_length, position):
    while True:
        for i in range(position - 25, position):
            for j in range(position - 25, position):
                if i == j:
                    continue
                elif input[i] + input[j] == input[position]:
                    return True
        return False

def part1(input, preamble_length):
    position = preamble_length
    while True:
        if check_digit(input, preamble_length, position):
            position += 1
        else:
            return input [position]

def part2(input, target):
    for i in range(input.index(target)):
        sum_ = input[i]
        chain_length = 1
        while sum_ < target:
            sum_ = sum(input[i : i + chain_length])
            if sum_ == target:
                return min(input[i : i + chain_length]) + max(input[i : i + chain_length])
            chain_length += 1

print part1(input, 25), part2(input, part1(input, 25))
