with open("advent20-7a-input.txt","r") as f:
    input = f.read().split('\n')
    del input[len(input) - 1]

def rules_dict(input):
    outers = {}
    for rule in input:
        inners = {}
        outer_bag, inner_bags = rule.split(" bags contain ")
        inner_bags  = inner_bags.split(",")
        for bag in inner_bags:
            bag = bag.replace(" bags.","").replace(" bags","").replace(" bag.","").replace(" bag","").strip()
            inners[bag[2:]] = bag[:1]
        outers[outer_bag] = inners
    return outers

def can_contain(rules_dict, outer_bag, target_bag):
    if ' other' in rules_dict[outer_bag].keys():
        return False
    elif target_bag in rules_dict[outer_bag].keys():
        return True
    else:
        for bag in rules_dict[outer_bag].keys():
            return any(can_contain(rules_dict, bag, target_bag) for bag in rules_dict[outer_bag].keys())

def part1(rules_dict):
    return sum(can_contain(rules_dict, rule, 'shiny gold') for rule in rules_dict)

def count_bags(rules_dict, outer_bag):
    if ' other' in rules_dict[outer_bag]:
        return 0
    else:
        return sum((count_bags(rules_dict, bag)+1)*int(rules_dict[outer_bag][bag]) for bag in rules_dict[outer_bag].keys())

print part1(rules_dict(input))
print count_bags(rules_dict(input), 'shiny gold')
