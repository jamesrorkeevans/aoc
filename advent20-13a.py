with open("advent20-13a-input.txt","r") as f:
    input = f.read().split('\n')
    del input[-1]

depart = int(input[0])
input = input[1].split(',')

def find_bus_gaps(input):

    bus_gaps = {}

    for i in range(len(input)):
        if input[i] == 'x':
            pass
        else:
            bus_gaps[int(input[i])] = int(i)

    return bus_gaps

def check_bus(t, bus, gap):
    if (t + gap) % bus == 0:
        return True
    else:
        return False

def lcm(x, y):
    from fractions import gcd
    return x * y // gcd(x, y)

def part2(input):

    bus_gaps = find_bus_gaps(input)
    buses = [x for x in bus_gaps]

    buses.sort(reverse=True)

    step = int(input[0])
    t = 0

    for bus in buses:
        t1 = 0
        t2 = 0
        while True:
            if check_bus(t, bus, bus_gaps[bus]):
                t1 = t
                break
            t += step
        t += step
        while True:
            if check_bus(t, bus, bus_gaps[bus]):
                t2 = t
                break
            t += step

        step = lcm(step, (t2 - t1))
        t = t1

    return t

print part2(input)
