import re

# start from designated index (from jump) and go through instructions until next jump when recursion is called
def jump_to(start,code_list,accnum,called):
    for i in range(start,len(code_list)):
        instr = re.search("([a-z]*) ([+-][0-9]*)$",code_list[i])
        if instr:
            if i not in called:
                called.append(i)
                comm = instr.group(1)
                numb = int(instr.group(2))
            else: return accnum
        else:
            print("Error parsing command")
            quit()
        if comm == "acc": accnum += numb
        elif comm == "jmp":
            accnum = jump_to(i+numb,code_list,accnum,called)
            return accnum
    return accnum

# open input file and list instructions
with open("../input_files/console_code.txt","r") as console_code:
    code_list = []
    for line in console_code.readlines(): code_list.append(line)

# start by the first instruction
called = []
accnum = jump_to(0,code_list,0,called)

# output answers
print("*----- FIRST PART -----*\nAccumulator is at %s before second loop starts\n" % accnum)