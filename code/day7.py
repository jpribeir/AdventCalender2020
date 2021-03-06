import re

global my_col
my_col = "shiny gold"

# recursion to go through color chain until one color has shiny gold inside
def look_for_gold(rules, bag, shiny_containers):
    if bag == my_col or bag in shiny_containers: return True
    else:
        foundOne = False
        for each in rules[bag]:
            if look_for_gold(rules, each, shiny_containers):
                foundOne = True
                if bag not in shiny_containers: shiny_containers.append(bag)
        else: return foundOne

# recursion to count and add bags in each level
def count_bags(rules,bag,numbags):
    subnum = 0
    for each in rules[bag]: subnum += (rules[bag][each])*(1+count_bags(rules,each,subnum))
    return subnum

# open input file and list what each color bag has inside
with open("../input_files/luggage_rules.txt","r") as luggage_rules:
    rules = {}
    rule_del = " bags contain "
    for line in luggage_rules.readlines():
        bag_col = line.split(rule_del)[0]
        rules[bag_col] = {}
        for item in (line.split(rule_del)[1]).split(", "):
            col = re.search("([0-9]) ([a-z]* [a-z]*) bag", item)
            if col: rules[bag_col][col.group(2)] = int(col.group(1))

# go through each color, if one of its recipients was positive, it also becomes positive
shiny_containers = []
for bag in rules:
    if look_for_gold(rules, bag, shiny_containers):
        if bag != my_col and bag not in shiny_containers: shiny_containers.append(bag)

# count bags inside my one bag
total_bags = count_bags(rules,my_col,0)


# output answers
print("*----- FIRST PART -----*\n%s colors can contain at least one %s bag\n" % (len(shiny_containers), my_col))
print("*----- SECOND PART -----*\nMy %s bag has %s bags inside of it\n" % (my_col, total_bags))