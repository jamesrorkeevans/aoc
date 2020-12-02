with open("advent20-1a-input.txt","r") as f:
    expenses = f.read().split('\n')
    del expenses[len(expenses) - 1]

expenses = [int(string) for string in expenses]
top = len(expenses)

for i in range(top):
    for j in range(i,top):
        if expenses[i] + expenses[j] == 2020:
            part1 = expenses[i] * expenses[j]
        for k in range(j, top):
            if expenses[i] + expenses[j] + expenses[k] == 2020:
                part2 = expenses[i] * expenses[j] * expenses[k]

print part1
print part2
