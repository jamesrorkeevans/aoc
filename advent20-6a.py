with open("advent20-6a-input.txt","r") as f:
    input = f.read().split('\n')


def part1(input):
    responses = {}
    group = 0
    group_response = ''

    for person in range(len(input)):
        if input[person] == '':
            responses[group] = set(group_response)
            group_response = ''
            group += 1
            continue
        group_response += input[person]
    return responses

def part2(input):
    responses = {}
    group = 0
    group_response = input[0]

    for person in range(len(input)):
        if input[person] == '':
            responses[group] = set(group_response)
            try:
                group_response = input[person + 1]
            except IndexError:
                return responses
            group += 1
            person += 1
            continue
        group_response_new = group_response
        for char in group_response:
            if char in input[person]:
                continue
            else:
                group_response_new = group_response_new.replace(char,'')
        group_response = group_response_new
    return responses

part1 = sum([len(value) for value in part1(input).values()])
part2 = sum([len(value) for value in part2(input).values()])
print 'part1 = ', part1, 'part 2 = ', part2
