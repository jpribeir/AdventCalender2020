#open inputs file and list inputs
with open("password_database.txt","r") as password_database:
    password_list = []
    for line in password_database.readlines():
        password_list.append(line)

#go through passwords and check validity of each
count_valid = 0
for line in password_list:
    range_occ = line.split()[0]
    min_occ = int(line.split()[0].split('-')[0])
    max_occ = int(line.split()[0].split('-')[-1])
    letter_occ = line.split()[1].split(':')[0]
    str_occ = line.split()[-1]
    count_occ = 0
    for char in str_occ:
        if char==letter_occ: count_occ +=1
    if (count_occ>=min_occ) and (count_occ<=max_occ): count_valid +=1

#output answers to file
strout = []
strout.append("There are %s valid passwords\n" % count_valid)

with open("outtest.txt","w") as outfile:
    for outline in strout: outfile.write(outline)