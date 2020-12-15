input = [20,9,11,0,1,2]

log = {}

for num in range(len(input)):
    log[input[num]] = [-1, num]

def part1(input, log, n_):

    turn = len(input)
    last_turn = input[len(input)-1]

    while True:

        if log[last_turn][0] == -1:

            this_turn = 0
            log[0][0] = log[0][1]
            log[0][1] = turn

        else:
            this_turn = log[last_turn][1] - log[last_turn][0]

            if this_turn in log:
                log[this_turn][0] = log[this_turn][1]
                log[this_turn][1] = turn
            else:
                log[this_turn] = [-1, turn]

        last_turn = this_turn

        turn += 1

        if turn == n_:
            return this_turn

print part1(input, log, 2020)
print part1(input, log, 30000000)
