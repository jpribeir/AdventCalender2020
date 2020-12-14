import re

# add or subtract coordinates according to direction and value
def move_direction(direction,value,ns_pos,ew_pos):
    if direction == "E": ew_pos +=value
    elif direction == "W": ew_pos -=value
    elif direction == "N": ns_pos +=value
    elif direction == "S": ns_pos -=value
    return ns_pos,ew_pos

# turn ship to new direction according to side and value
def turn_direction(side,value,cardinal):
    if side == "R": cycle = int(value/90)
    else: cycle = int(-value/90)
    return cardinal[cycle:] + cardinal[:cycle]

# open input file and list rows of seats
with open("../input_files/navigation_instructions.txt","r") as nav_inst:
    inst_list = []
    for line in nav_inst.readlines(): inst_list.append(line.strip())
    
# starting position, first element in cardinal is where ship is facing
ns_pos = 0
ew_pos = 0
cardinal = ["E","S","W","N"]

# each instruction moves or turns the ship
for line in inst_list:
    par = re.search("([A-Z])([0-9]*)",line)
    if par:
        coordir = par.group(1)
        coorval = int(par.group(2))
    else: quit()
    if coordir in cardinal: ns_pos,ew_pos = move_direction(coordir,coorval,ns_pos,ew_pos)
    elif coordir == "F": ns_pos,ew_pos = move_direction(cardinal[0],coorval,ns_pos,ew_pos)
    elif coordir in ["R","L"]: cardinal = turn_direction(coordir,coorval,cardinal)
manhattan_val = abs(ns_pos)+abs(ew_pos)

print("*----- FIRST PART -----*\nThe Manhattan distance is %s\n" % manhattan_val)