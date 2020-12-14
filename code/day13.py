# open input file and loop through instructions
with open("../input_files/bus_info.txt","r") as bus_info:
    info_list = bus_info.readlines()
    arrival = int((info_list[0]).strip())
    earliest = arrival*2
    for each in (info_list[1]).split(","):
        #if each !="x": bus_schedule.append(each)
        if each == "x": continue
        t = int(each)
        while t < arrival: t +=int(each)
        if earliest > t:
            earliest = t
            chosen = int(each)

print("*----- FIRST PART -----*\nThe answer is %s\n" % ((earliest-arrival)*int(chosen)))