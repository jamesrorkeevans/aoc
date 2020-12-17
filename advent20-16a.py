with open("advent20-16a-input.txt","r") as f:
    input = f.read().split('\n')
    del input[-1]


def create_rules(input):
    rules = {}

    for x in range(20):
        field = input[x].split(':')[0]
        ranges = input[x].split(': ')[1]
        range_1, range_2 = ranges.split(' or ')
        range_1a, range_1b = range_1.split('-')
        range_2a, range_2b = range_2.split('-')

        rules[field] = [int(range_1a), int(range_1b), int(range_2a), int(range_2b)]

    min_value = int(min([rules[field][0] for field in rules]))
    max_value = int(max([rules[field][3] for field in rules]))

    return rules, min_value, max_value

def part1(input, rules, min_value, max_value):


    errors = 0
    valid_tickets = []

    for ticket in range(25, len(input)):

        if min([int(x) for x in input[ticket].split(',')]) < min_value:
            errors += min([int(x) for x in input[ticket].split(',')])

        elif max([int(x) for x in input[ticket].split(',')]) > max_value:
            errors += max([int(x) for x in input[ticket].split(',')])
        else:
            valid_tickets.append(ticket)

    return errors, valid_tickets

rules, min_value, max_value = create_rules(input)

errors, valid_tickets = part1(input, rules, min_value, max_value)

def valid_fields(input, valid_tickets, rules, field):

    valid_fields = []

    for n in range(20):
        if valid_field(input, valid_tickets, rules, field, n):
            valid_fields.append(n)
        else:
            pass

    return valid_fields

def valid_field(input, valid_tickets, rules, field, n):
    values = [int(input[ticket].split(',')[n]) for ticket in valid_tickets]
    for value in values:
        if rules[field][0] <= value <= rules[field][1] or rules[field][2] <= value <= rules[field][3]:
            pass
        else:
            return False
    return True

constraints = {}

for field in rules:
    constraints[field] = valid_fields(input, valid_tickets, rules, field)

locked = []

while len(locked) < 20:
    for field in constraints:
        if field in locked:
            continue
        if len(constraints[field]) == 1:
            locked.append(field)
            for other_constraint in constraints:
                if len(constraints[other_constraint]) == 1:
                    continue
                else:
                    constraints[other_constraint].remove(constraints[field][0])

my_ticket = input[22]

solution = 1

for field in constraints:
    if field[0:3] == 'dep':
        solution *= int(my_ticket.split(',')[constraints[field][0]])

print solution
