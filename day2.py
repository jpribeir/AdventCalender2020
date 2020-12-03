#open input file and list inputs
with open("password_database.txt","r") as password_database:
    password_list = []
    for line in password_database.readlines():
        password_list.append(line)

#go through password list
countA = 0
countB = 0
for line in password_list:
    #parse info
    min_occ = int(line.split()[0].split('-')[0])
    max_occ = int(line.split()[0].split('-')[-1])
    letter_occ = line.split()[1].split(':')[0]
    str_occ = line.split()[-1]

    #check if specific character is between designated range
    count_occ = 0
    for char in str_occ:
        if char==letter_occ: count_occ +=1
    if (count_occ>=min_occ) and (count_occ<=max_occ): countA +=1

    #check if specific character is in only one of the two designated array indexes
    checkFirst = (str_occ[min_occ-1]==letter_occ)
    checkLast = (str_occ[max_occ-1]==letter_occ)
    if (checkFirst or checkLast) and (checkFirst != checkLast): countB +=1

#output answers to file
strout = []
strout.append("*----- FIRST PART -----*\nThere are %s valid passwords\n\n" % countA)
strout.append("*----- SECOND PART -----*\nThere are %s valid passwords\n\n" % countB)
with open("outtest.txt","w") as outfile:
    for outline in strout: outfile.write(outline)