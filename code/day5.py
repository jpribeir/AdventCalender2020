# convert binary str to a decimal through binary search
def bin_to_dec(numbin,max):
    low = 0
    hi = max
    count = 1
    while (low != hi):
        if numbin[0] == "F" or  numbin[0] == "L": hi -= (max+1)/(2**count)
        elif numbin[0] == "B" or  numbin[0] == "R": low += (max+1)/(2**count)
        count +=1
        numbin = numbin[1:]
    return int(hi)

# initialize
numchar_row = 7
numchar_col = 3
max_row = 2**numchar_row-1
max_col = 2**numchar_col-1
MAX_ID = 0
seat_matrix = []
for row in range(max_row+1):
    seat_matrix.append([])
    for col in range(max_col+1): seat_matrix[row].append(False)

# open input file and go thorugh each seat ID
with open("../input_files/plane_seats.txt","r") as plane_seats:
    for line in plane_seats.readlines():
        seat_row = bin_to_dec(line[0:numchar_row],max_row)
        seat_col = bin_to_dec(line[numchar_row:-1],max_col)
        seat_ID = seat_row*8 + seat_col
        seat_matrix[seat_row][seat_col] = seat_ID
        if seat_ID > MAX_ID: MAX_ID = seat_ID

# go through matrix and find missing spot
found = False
for row in range(1,max_row-1):
    for col in range(max_col):
        #print(seat_matrix[row][col])
        if not seat_matrix[row][col]:
            my_row = row
            my_col = col
            my_ID = row*8 + col
            if ((my_ID-1) in seat_matrix[row] or (my_ID-1) in seat_matrix[row-1]) and ((my_ID+1) in seat_matrix[row] or (my_ID+1) in seat_matrix[row+1]): found = True
        if found: break
    if found: break

# output answers
print("*----- FIRST PART -----*\nThe highest number ID is %s\n" % MAX_ID)
print("*----- SECOND PART -----*\nMy seat is in row %s col %s and its ID is %s" % (my_row,my_col,my_ID))