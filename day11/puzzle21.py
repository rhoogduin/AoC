
#enum
FLOOR  = -1
EMPTY  = 0
FILLED = 1

#read input
file = open("input.txt", "r")

lines = []

lines = file.read().splitlines()
    
file.close()

# lists that will represent the waiting area
WA_old = []
WA_new = []

# read input and populate waiting area
for line in lines :
    row = []
    for char in line :
        if char == '.' :
            row.append(FLOOR)
        elif char == 'L' :
            row.append(EMPTY)
        elif char == '#' :
            row.append(FILLED)        
    WA_new.append(row)
   
# dimensions of the waiting area   
DIM_X = len(WA_new[0])
DIM_Y = len(WA_new)

# initialise with zeroes
for i in range(DIM_Y) :
    row = []
    for j in range(DIM_X) :
        row.append(0)
    WA_old.append(row)

# check if seat
def valid (y, x) :
    if y < 0 or y >= DIM_Y :
        return False
    if x < 0 or x >= DIM_X :
        return False
    if WA_old[y][x] == FLOOR :
        return False
    return True

# calculate value of seat for next generation
def newValue (y, x) :
    if WA_old[y][x] == FLOOR :
        return FLOOR
        
    count = -WA_old[y][x]
    
    for i in range(y-1, y+2) :
        for j in range(x-1, x+2) :
            if valid(i, j) :
                count += WA_old[i][j]
    
    if WA_old[y][x] == EMPTY and count == 0 :
        return FILLED
    if WA_old[y][x] == FILLED and count >= 4 :
        return EMPTY
    
    return WA_old[y][x]

# calculate one generation
def generation () :
    # new board
    for i in range(DIM_Y) :
        for j in range(DIM_X) :
            WA_new[i][j] = newValue(i,j)

# check if boards are equal
def equal () :
    for i in range(DIM_Y) :
        for j in range(DIM_X) :
            if WA_new[i][j] != WA_old[i][j] :
                return False
    return True

# run simulation until stable situation is found
while not equal() :
    generation()
    ph = WA_new
    WA_new = WA_old
    WA_old = ph
    
count = 0

for i in range(DIM_Y) :
    for j in range(DIM_X) :
        if WA_new[i][j] == FILLED :
            count += 1
            
print (f"Amount of occupied seats: {count}")