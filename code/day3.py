#class to instantiate slopes
class Toboggan:
    def __init__(self,horiz,verti):
        self.horiz = horiz
        self.verti = verti
        self.start_point = 0
        self.countOpen = 0
        self.countTree = 0
    
    #increment horizontal and check if tree
    def checkSpot(self,line):
        self.start_point +=self.horiz
        if self.start_point >= line_length: self.start_point -= line_length
        if line[self.start_point] == open_spot: self.countOpen +=1
        elif line[self.start_point] == tree_spot: self.countTree +=1

#open input file and list inputs
with open("tree_map.txt","r") as tree_map:
    tree_map_list = []
    for line in tree_map.readlines(): tree_map_list.append(line)

#set inits with vertical and horizontal steps
toboggan_list = []
toboggan_list.append(Toboggan(1,1))
toboggan_list.append(Toboggan(3,1))
toboggan_list.append(Toboggan(5,1))
toboggan_list.append(Toboggan(7,1))
toboggan_list.append(Toboggan(1,2))
open_spot = "."
tree_spot = "#"
line_length = len(tree_map_list[0].strip())

#go through map and check each slope
for num,line in enumerate(tree_map_list[1:]):
    for slope in toboggan_list:
        if (num+1)%slope.verti==0: slope.checkSpot(line)

#output answers
print("*----- FIRST PART -----*\nThere are %s trees in my path\n\n" % toboggan_list[1].countTree)
print("*----- SECOND PART -----*\n")
productTree = 1
for slope in toboggan_list:
    print("There are %s trees in my path\n" % slope.countTree)
    productTree *= slope.countTree
print("\nThe final product is %s" % productTree)