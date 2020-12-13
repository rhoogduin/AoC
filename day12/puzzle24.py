
import math

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

# track distance to waypoint
WPNS = 1
WPWE = 10

def rotate (degrees) :
    global WPNS, WPWE
    
    radians = degrees * math.pi / 180
    
    # rotation matrix
    TEMPWE = WPWE * int( math.cos(radians) ) - WPNS * int( math.sin(radians) )
    TEMPNS = WPWE * int( math.sin(radians) ) + WPNS * int( math.cos(radians) )
    
    WPWE = TEMPWE
    WPNS = TEMPNS

for instruction in instructions :
    op = instruction[0]
    arg = instruction[1]
    
    if op == 'N' :
        WPNS += arg
    elif op == 'E' :
        WPWE += arg
    elif op == 'S' :
        WPNS -= arg
    elif op == 'W' :
        WPWE -= arg
    elif op == 'F' :
        DNS += WPNS * arg
        DWE += WPWE * arg
    elif op == 'L' :
        rotate(arg)
    elif op == 'R' :
        rotate(-arg)
    
print (f"Total distance north-south: {DNS}, total distance west-east: {DWE}.")
print (f"Manhattan distance: {abs(DNS) + abs(DWE)}.")