import math

with open("advent20-12a-input.txt","r") as f:
    input = f.read().split('\n')
    del input[-1]

def makeMove1(move, x, y, theta):
    inst = move[0]
    mag = int(move[1:])
    if inst == 'N':
        y += mag
    elif inst == 'S':
        y -= mag
    elif inst == 'E':
        x += mag
    elif inst == 'W':
        x -= mag
    elif inst == 'L':
        theta += mag*math.pi/180
    elif inst == 'R':
        theta -= mag*math.pi/180
    elif inst == 'F':
        x += math.cos(theta)*mag
        y += math.sin(theta)*mag

    return x, y, theta

def part1(input):
    x, y, theta = 0, 0, 0

    for instruction in input:
        x, y, theta = makeMove1(instruction, x, y, theta)

    return abs(x) + abs(y)

def makeMove2(move, ship_x, ship_y, waypoint_angle, waypoint_dist):
    inst = move[0]
    mag = int(move[1:])

    if inst == 'F':
        ship_x += math.cos(waypoint_angle) * mag * waypoint_dist
        ship_y += math.sin(waypoint_angle) * mag * waypoint_dist
        return ship_x, ship_y, waypoint_angle, waypoint_dist

    waypoint_x = waypoint_dist * math.cos(waypoint_angle)
    waypoint_y = waypoint_dist * math.sin(waypoint_angle)

    if inst == 'N':
        waypoint_y += mag
    elif inst == 'S':
        waypoint_y -= mag
    elif inst == 'E':
        waypoint_x += mag
    elif inst == 'W':
        waypoint_x -= mag
    elif inst == 'L':
        waypoint_angle += mag*math.pi/180
        waypoint_x = waypoint_dist * math.cos(waypoint_angle)
        waypoint_y = waypoint_dist * math.sin(waypoint_angle)
    elif inst == 'R':
        waypoint_angle -= mag*math.pi/180
        waypoint_x = waypoint_dist * math.cos(waypoint_angle)
        waypoint_y = waypoint_dist * math.sin(waypoint_angle)

    return ship_x, ship_y, math.atan2(waypoint_y, waypoint_x), (waypoint_x ** 2 + waypoint_y ** 2) ** 0.5


def part2(input):
    ship_x = 0
    ship_y = 0

    waypoint_angle = math.atan2(1, 10)
    waypoint_dist = (10**2 + 1)**0.5

    for instruction in input:
        ship_x, ship_y, waypoint_angle, waypoint_dist = makeMove2(instruction, ship_x, ship_y, waypoint_angle, waypoint_dist)

    return abs(ship_x) + abs(ship_y)

print part1(input)
print part2(input)
