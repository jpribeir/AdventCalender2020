import re

# convert binary to decimal
def bin_to_dec(numbin):
    numdec = 0
    for i in range(0,36): numdec +=(numbin[i]*(2**(35-i)))
    return numdec

# convert decimal to binary
def dec_to_bin(numdec):
    numbin = [0]*36
    rest = numdec
    for i in range(0,36):
        if rest >= (2**(35-i)):
            numbin[i] = 1
            rest -= (2**(35-i))
        else: numbin[i] = 0
    return numbin

# mask binary number
def mask_num(numbin,mask):
    masked_num = [0]*36
    for i in range(0,36):
        if mask[i] == "X": masked_num[i] = numbin[i]
        else: masked_num[i] = int(mask[i])
    return masked_num

# open input file and loop through program
memory = {}
with open("../input_files/initialization_program.txt","r") as init_prog:
    for line in init_prog.readlines():
        if "mask" in line.split("=")[0]: mask = (line.split("=")[1]).strip()
        else:
            par = re.search("mem\[([0-9]*)\] = ([0-9]*)",line)
            if par:
                add = par.group(1)
                val = par.group(2)
            else: quit()
            memory[add] = bin_to_dec(mask_num(dec_to_bin(int(val)),mask))

# sum all values in memory
total_sum = 0
for each in memory: total_sum +=memory[each]

print("*----- FIRST PART -----*\nThe sum of all values in memory is %s\n" % total_sum)