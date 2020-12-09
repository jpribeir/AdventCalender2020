# open input file and list numbers
with open("../input_files/XMAS_data.txt","r") as XMAS_data:
    data_list = []
    for line in XMAS_data.readlines(): data_list.append(line.strip())

# go through 3 nested loops until there is no match
preamble = 25
for num,line in enumerate(data_list[preamble:-1]):
    pairFound = False
    for ber,pairA in enumerate(data_list[num:num+preamble-1]):
        for pairB in data_list[ber+1:num+preamble]:
            if (pairA != pairB) and (int(pairA)+int(pairB) == int(line)):
                pairFound = True
                break
        if pairFound: break
    if not pairFound:
        first_weakness = line
        weakness_line = num+preamble
        break

# reverse list so it can start looking from the last line before weakness line
exploit_list = data_list[0:weakness_line-1]
exploit_list.reverse()
weakFound = False
# set starting point in outmost loop, set end point in next loop
for num,start in enumerate(exploit_list):
    for ber,end in enumerate(exploit_list[num+1:-1]):
        sumall = 0
        # innermost loop adds all numbers between the 2 points
        for each in range(num,num+ber+1): sumall += int(exploit_list[each])
        if sumall == int(first_weakness):
            minweak = int(first_weakness)
            maxweak = 0
            weakFound = True
            for each in range(num,num+ber+1):
                if int(exploit_list[each]) < minweak: minweak = int(exploit_list[each])
                if int(exploit_list[each]) > maxweak: maxweak = int(exploit_list[each])
                enc_weak = minweak + maxweak
            break
        # if sum is bigger than weakness, move start point up
        # else continue moving end point up
        elif sumall > int(first_weakness): break
    if weakFound: break

# output answers
print("*----- FIRST PART -----*\nThe first weakness in the code is %s in line %s\n" % (first_weakness,weakness_line+1))
print("*----- SECOND PART -----*\nThe encryption weakness in the code is %s\n" % enc_weak)