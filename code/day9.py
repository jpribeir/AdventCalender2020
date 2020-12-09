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
        break

# output answers
print("*----- FIRST PART -----*\nThe first weakness in the code is %s in line %s\n" % (first_weakness,num+preamble+1 ))