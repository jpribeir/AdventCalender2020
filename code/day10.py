# open input file and list adapters
with open("../input_files/jolt_adapters.txt","r") as jolt_adapters:
    adapter_list = []
    for line in jolt_adapters.readlines(): adapter_list.append(int(line.strip()))

# sort adapters and add device built-in adapter at the end
adapter_list.sort()
adapter_list.append(adapter_list[-1]+3)
rating_diffs = {1:0, 2:0, 3:0}

# add 0 as outlet adapter, go through list and count number of 1 and 3 rating diffs between adapters
prev_adp = 0
for adp in adapter_list:
    if (adp - prev_adp) in rating_diffs.keys(): rating_diffs[adp - prev_adp] +=1
    else: print("%s is not compatible with previous adapter"%adp)
    prev_adp = adp

# output answers
print("*----- FIRST PART -----*\nThere are %s 1-jolt differences and %s 3-jolt differences,\nwhich multiplied is %s\n"%(rating_diffs[1], rating_diffs[3], rating_diffs[1]*rating_diffs[3]))