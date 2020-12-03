with open("advent20-3a.txt","r") as f:
    input = f.read().split('\n')
    del input[len(input) - 1]

def count_trees(map, y_increment, x_increment):
    x = 0
    y = 0
    trees = 0
    for y in range(0, len(map), y_increment):
        if map[y][x] == '#':
            trees += 1
        x = (x + x_increment) % len(map[0])
        y = y + y_increment
    return trees

def add_paths(map, ys, xs):
    tree_product = 1
    for i in range(5):
        tree_product = tree_product * count_trees(map, ys[i], xs[i])
    return tree_product

print add_paths(input, [1,1,1,1,2], [1,3,5,7,1])
