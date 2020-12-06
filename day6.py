# open input file, go thorugh forms and count diverse yeses
with open("form_answers.txt","r") as form_answers:
    group = {}
    count_yes = 0
    for line in form_answers.readlines():
        if line=="\n":
            count_yes += len(group)
            group = {}
        else:
            for ans in line:
                if ans in group: group[ans] +=1
                elif ans != "\n": group[ans] = 1
    
    # in case the last batch of answers isn't picked up
    if group: count_yes += len(group)


# output answers
print("*----- FIRST PART -----*\nThere are a total of %s different answers\n" % count_yes)
print("*----- SECOND PART -----*\nThere are a total of %s different answers\n" % count_yes)