with open("advent20-2a-input.txt","r") as f:
    input = f.read().split('\n')
    del input[len(input) - 1]

def check_policy1(string):
    #string = '15-16 d: dndddddddjdddddbdld'
    fewest = int(string[0:string.index("-")])
    most = int(string[string.index("-")+1 : string.index(" ")])
    letter = string[string.index(":")-1]
    count_letter = string[string.index(":"):].count(letter)
    return count_letter <= most and count_letter >= fewest

passwords = {}

for i in range(len(input)):
    passwords[input[i]] = check_policy1(input[i])

print sum(passwords.values())

def check_policy2(string):
    first_position = int(string[0:string.index("-")]) + int(string.index(":")) + 1
    second_position = int(string[string.index("-")+1 : string.index(" ")]) + int(string.index(":")) + 1
    letter = string[string.index(":")-1]
    return (string[first_position] == letter) != (string[second_position] == letter)

passwords = {}

for i in range(len(input)):
    passwords[input[i]] = check_policy2(input[i])

print sum(passwords.values())
