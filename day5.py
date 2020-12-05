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
    return hi

# initialize
numchar_row = 7
numchar_col = 3
max_row = 2**numchar_row-1
max_col = 2**numchar_col-1
MAX_ID = 0

# open input file and go thorugh each seat ID
with open("plane_seats.txt","r") as plane_seats:
    for line in plane_seats.readlines():
        seat_row = bin_to_dec(line[0:numchar_row],max_row)
        seat_col = bin_to_dec(line[numchar_row:-1],max_col)
        seat_ID = seat_row*8 + seat_col
        if seat_ID > MAX_ID: MAX_ID = seat_ID

# output answers
print("*----- FIRST PART -----*\nThe highest number ID is %s\n" % MAX_ID)
print("*----- SECOND PART -----*\n")