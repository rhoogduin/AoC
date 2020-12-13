
#read input
file = open("input.txt", "r")

lines = []

lines = file.read().splitlines()
    
file.close()

instructions = []

# read input and populate waiting area
for line in lines :
    instruction = (line[0], int(line[1:]))
    instructions.append(instruction)

# track total distance travelled 
DNS = 0
DWE = 0

# track direction the ship is facing
DIRECTION = 90
NORTH = 0
EAST  = 90
SOUTH = 180
WEST  = 270

def moveForward (distance) :
    global DNS, DWE
    if DIRECTION == NORTH :
        DNS += distance
    elif DIRECTION == EAST :
        DWE += arg
    elif DIRECTION == SOUTH :
        DNS -= arg
    elif DIRECTION == WEST :
        DWE -= arg

for instruction in instructions :
    op = instruction[0]
    arg = instruction[1]
    
    if op == 'N' :
        DNS += arg
    elif op == 'E' :
        DWE += arg
    elif op == 'S' :
        DNS -= arg
    elif op == 'W' :
        DWE -= arg
    elif op == 'F' :
        moveForward(arg)
    elif op == 'L' :
        DIRECTION -= arg
        while DIRECTION < 0 :
            DIRECTION += 360
    elif op == 'R' :
        DIRECTION += arg
        while DIRECTION >= 360 :
            DIRECTION -= 360
    
print (f"Total distance north-south: {DNS}, total distance west-east: {DWE}.")
print (f"Manhattan distance: {abs(DNS) + abs(DWE)}.")