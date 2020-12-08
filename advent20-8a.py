with open("advent20-8a-input.txt","r") as f:
    input = f.read().split('\n')
    del input[len(input) - 1]

def runProgram(instructions, accumulator, position):
    pos_cache = []
    while True:
        if position in pos_cache:
            return False, accumulator, position, pos_cache
        elif position == len(instructions):
            return True, accumulator, position, pos_cache
        else:
            pos_cache.append(position)

        if instructions[position][:3] == "nop":
            position += 1
            continue
        elif instructions[position][:3] == "acc":
            accumulator += int(instructions[position][4:])
            position += 1
            continue
        elif instructions[position][:3] == "jmp":
            position += int(instructions[position][4:])
            continue
        else:
            print 'error'
            return False

def modifyProgram(instructions):
    for i in range(len(instructions)):
        modified_instructions = []
        modified_instructions = [j for j in instructions]
        if instructions[i][:3] == 'nop':
            modified_instructions[i] = 'jmp' + instructions[i][3:]
        elif instructions[i][:3] == 'jmp':
            modified_instructions[i] = 'nop'
        else:
            continue
        if runProgram(modified_instructions, 0, 0)[0]:
            return runProgram(modified_instructions, 0, 0)
        else:
            continue

print modifyProgram(input)[1]
