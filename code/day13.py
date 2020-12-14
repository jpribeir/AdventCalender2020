# recursion
def find_time(bus_list,count,min_den,current_time):
    count +=1
    if count == len(bus_list): return current_time   #if end just return
    if bus_list[count] == "x": return find_time(bus_list,count,min_den,current_time)    #if "x" continue to next bus ID
    else:
        while True: #keep adding up the time until there is a common denominator time instant between the previous IDs and the current one
            if (current_time + count) % int(bus_list[count]) == 0: return find_time(bus_list,count,min_den*int(bus_list[count]),current_time)
            current_time +=min_den

# open input file and loop through instructions
with open("../input_files/bus_info.txt","r") as bus_info:
    info_list = bus_info.readlines()
    arrival = int((info_list[0]).strip())
    earliest = arrival*2
    bus_list = []
    for each in (info_list[1]).split(","):
        bus_list.append(each)
        if each == "x": continue
        t = int(each)
        while t < arrival: t +=int(each)
        if earliest > t:
            earliest = t
            chosen = int(each)

# find timestamp
timestamp = find_time(bus_list,0,int(bus_list[0]),int(bus_list[0]))

print("*----- FIRST PART -----*\nThe answer is %s\n" % ((earliest-arrival)*int(chosen)))
print("*----- SECOND PART -----*\nThe answer is %s\n" % timestamp)