# open input file
with open("form_answers.txt","r") as form_answers:
    group = {}
    num_ppl = 0
    count_yes = 0
    count_all_yes = 0
    for line in form_answers.readlines():
        if line=="\n":  # if group ended 
            count_yes += len(group) # adding number of people who said yes
            for ans in group:
                if group[ans] == num_ppl: count_all_yes +=1 # counting unanimous yeses in group
            group = {}
            num_ppl = 0
        else:
            for ans in line.strip():
                if ans in group: group[ans] +=1
                else: group[ans] = 1
            num_ppl +=1

    # in case the last groups isn't picked up due to lack of "\n"
    if group:
        count_yes += len(group)
        for ans in group:
            if group[ans] == num_ppl: count_all_yes +=1


# output answers
print("*----- FIRST PART -----*\nThere are a total of %s different answers\n" % count_yes)
print("*----- SECOND PART -----*\nThere are a total of %s unanimous answers\n" % count_all_yes)