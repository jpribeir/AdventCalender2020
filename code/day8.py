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
            else: return False, accnum
        else: print("Error parsing command")
        if comm == "acc": accnum += numb
        elif comm == "jmp":
            finished, new_jmp = jump_to(i+numb,code_list,accnum,called)
            return finished, new_jmp
    return True, accnum

# go through the loop's instructions and correcting them until it no longer loops
def fix_loop(code_list,called):
    dellac = called
    dellac.reverse()
    for i in dellac:
        backup = code_list[i]
        instr = re.search("([a-z]*) ([+-][0-9]*)$",backup)
        if instr.group(1) == "nop": comm = "jmp"
        elif instr.group(1) == "jmp": comm = "nop"
        code_list[i] = comm+" "+instr.group(2)
        new_call = []
        finished, accnum = jump_to(0,code_list,0,new_call)
        if finished: return accnum
        else: code_list[i] = backup
    

# open input file and list instructions
with open("../input_files/console_code.txt","r") as console_code:
    code_list = []
    for line in console_code.readlines(): code_list.append(line)

# go through first loop
called = []
finsihed, accnum = jump_to(0,code_list,0,called)

# then find wrong instruction, fix it and run the code
accfinal = fix_loop(code_list,called)

# output answers
print("*----- FIRST PART -----*\nAccumulator is at %s before second loop starts\n" % accnum)
print("*----- SECOND PART -----*\nAccumulator is at %s after final instruction\n" % accfinal)