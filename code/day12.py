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

# just switch ns and ew values and change signals according to side
def rotate_direction(side,value,ns_offset,ew_offset):
    cycle = int(value/90)
    if side == "R":
        for i in range(cycle):
            offset_buf = ew_offset
            ew_offset = ns_offset
            ns_offset = -offset_buf
    else:
        for i in range(cycle):
            offset_buf = ns_offset
            ns_offset = ew_offset
            ew_offset = -offset_buf
    return ns_offset,ew_offset
    
# starting positions, first element in cardinal is where ship is facing
ns_A = 0
ew_A = 0
cardinal = ["E","S","W","N"]
ns_B = 0
ew_B = 0
ns_waypoint = 1
ew_waypoint = 10

# open input file and loop through instructions
with open("../input_files/navigation_instructions.txt","r") as nav_inst:
    inst_list = []
    for line in nav_inst.readlines():
        par = re.search("([A-Z])([0-9]*)",line.strip())
        if par:
            coordir = par.group(1)
            coorval = int(par.group(2))
        else: quit()

        # first part
        if coordir in cardinal: ns_A,ew_A = move_direction(coordir,coorval,ns_A,ew_A)
        elif coordir == "F": ns_A,ew_A = move_direction(cardinal[0],coorval,ns_A,ew_A)
        elif coordir in ["R","L"]: cardinal = turn_direction(coordir,coorval,cardinal)

        # second part
        if coordir in cardinal: ns_waypoint,ew_waypoint = move_direction(coordir,coorval,ns_waypoint,ew_waypoint)
        elif coordir == "F":
            ns_B,ew_B = move_direction("N",coorval*ns_waypoint,ns_B,ew_B)
            ns_B,ew_B = move_direction("E",coorval*ew_waypoint,ns_B,ew_B)
        elif coordir in ["R","L"]: ns_waypoint,ew_waypoint = rotate_direction(coordir,coorval,ns_waypoint,ew_waypoint)
manhattanA = abs(ns_A)+abs(ew_A)
manhattanB = abs(ns_B)+abs(ew_B)

print("*----- FIRST PART -----*\nThe Manhattan distance is %s\n" % manhattanA)
print("*----- SECOND PART -----*\nThe Manhattan distance is %s\n" % manhattanB)