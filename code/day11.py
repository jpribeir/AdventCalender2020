# compare each corresponding value between 2 same dimension matrixes
def check_change(mxA,mxB):
    for row,line in enumerate(mxA):
        for col,each in enumerate(line):
            if mxA[row][col] != mxB[row][col]: return True
    else: return False

# count number of occupied seats around a seat
def count_neighbours(seat_matrix,x,y):
    num_neighbours = 0
    rowlen = len(seat_matrix)
    collen = len(seat_matrix[0])
    for row in range(max(x-1,0),min(x+2,rowlen)):
        for col in range(max(y-1,0),min(y+2,collen)):
             if row != x or col != y:
                if seat_matrix[row][col] == "#": num_neighbours +=1
    return num_neighbours

# count number of occupied seats in line of sight of a seat
def count_visible(seat_matrix,x,y):
    num_visible = 0
    rowlen = len(seat_matrix)
    collen = len(seat_matrix[0])
    for row in range(x+1,rowlen):   #down
        if seat_matrix[row][y] == "#":
            num_visible +=1
            break
        elif seat_matrix[row][y] == "L": break
    for col in range(y+1,collen):   #right
        if seat_matrix[x][col] == "#":
            num_visible +=1
            break
        elif seat_matrix[x][col] == "L": break
    for row in range(1,x+1):    #up
        if seat_matrix[x-row][y] == "#":
            num_visible +=1
            break
        elif seat_matrix[x-row][y] == "L": break
    for col in range(1,y+1):    #left
        if seat_matrix[x][y-col] == "#":
            num_visible +=1
            break
        elif seat_matrix[x][y-col] == "L": break
    for row in range(1,collen): #down and right
        if (x+row >= rowlen) or (y+row >= collen): break
        if seat_matrix[x+row][y+row] == "#":
            num_visible +=1
            break
        elif seat_matrix[x+row][y+row] == "L": break
    for row in range(1,collen): #down and left
        if (x+row >= rowlen) or (y-row < 0): break
        if seat_matrix[x+row][y-row] == "#": 
            num_visible +=1
            break
        elif seat_matrix[x+row][y-row] == "L": break
    for row in range(1,collen): #up and right
        if (x-row < 0) or (y+row >= collen): break
        if seat_matrix[x-row][y+row] == "#":
            num_visible +=1
            break
        elif seat_matrix[x-row][y+row] == "L": break
    for row in range(1,collen): #up and left
        if (x-row < 0) or (y-row < 0): break
        if seat_matrix[x-row][y-row] == "#": 
            num_visible +=1
            break
        elif seat_matrix[x-row][y-row] == "L": break
    return num_visible
    
# recursion to change seats until no change is seen
def change_seats(seat_matrix):
    new_matrix = []
    for row,line in enumerate(seat_matrix):
        new_matrix.append([])
        for col,each in enumerate(line):
            num_neighbours = count_neighbours(seat_matrix,row,col)
            if each == "L" and num_neighbours == 0: new_matrix[row].append("#")
            elif each == "#" and num_neighbours >= 4: new_matrix[row].append("L")
            else: new_matrix[row].append(seat_matrix[row][col])
    if check_change(seat_matrix,new_matrix): return change_seats(new_matrix)
    else: return new_matrix

# recursion to change seats until no change is seen
def change_seats_dot_one(seat_matrix):
    new_matrix = []
    for row,line in enumerate(seat_matrix):
        new_matrix.append([])
        for col,each in enumerate(line):
            num_visible = count_visible(seat_matrix,row,col)
            if each == "L" and num_visible == 0: new_matrix[row].append("#")
            elif each == "#" and num_visible >= 5: new_matrix[row].append("L")
            else: new_matrix[row].append(seat_matrix[row][col])
    if check_change(seat_matrix,new_matrix): return change_seats_dot_one(new_matrix)
    else: return new_matrix

# count number of free and occupied seats
def count_seats(seat_matrix):
    count_free = 0
    count_occupied = 0
    for row,line in enumerate(seat_matrix):
        for col,each in enumerate(line):
            if each == "L": count_free +=1
            elif each == "#": count_occupied +=1
    return count_free,count_occupied

# print seat grid to console
def print_grid(seat_matrix):
    print("\n")
    for row in seat_matrix:
        outstr = ""
        for col in row: outstr +=col
        print(outstr)

# open input file and list rows of seats
with open("../input_files/seat_grid.txt","r") as seat_grid:
    seat_matrix = []
    for line in seat_grid.readlines():
        row = []
        for each in line.strip(): row.append(each)
        seat_matrix.append(row)

# start seat change until no change is seen and then count seats
final_matrix = change_seats(seat_matrix)
num_free,num_occupied = count_seats(final_matrix)

# same for part 2 rules
final_matrix_dot_one = change_seats_dot_one(seat_matrix)
final_free,final_occupied = count_seats(final_matrix_dot_one)

# output answers
print("*----- FIRST PART -----*\nThere are %s free seats and %s occupied seats\n"%(num_free,num_occupied))
print("*----- SECOND PART -----*\nThere are %s free seats and %s occupied seats\n"%(final_free,final_occupied))