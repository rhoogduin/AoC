
from time import perf_counter

# read input
file = open("input.txt", "r")

lines = []

lines = file.read().splitlines()
    
file.close()

# grid to hold the conway cubes
grid = {}

# initialise grid
for i, line in enumerate(lines) :
    for j in range(len(line)) :
        if line[j] == '#' :
            grid[(i,j,0,0)] = 1

# list to keep track of every position that is either an active cube
# or next to an active cube: the periphery
# only these positions need to be checked for updates
check = {}

# add 1 to the amount of neighbours every position in the periphery has
# if position not in the periphery add it and initialise with 1 neighbour
def addCheck (x, y, z, w) :
    for i in range( x - 1, x + 2 ) :
        for j in range( y - 1, y + 2 ) :
            for k in range ( z - 1, z + 2 ) :
                for l in range ( w - 1, w + 2 ) :
                    
                    try :
                        check[(i,j,k,l)] += 1
                    
                    except :
                        check[(i,j,k,l)] = 1

# initialise periphery
for x, y, z, w in grid :
    addCheck(x,y,z,w)

# remove 1 from the amount of neighbours every position in the periphery has
# if value drops to zero, remove position from the periphery
def subCheck (x, y, z, w) :
    for i in range( x - 1, x + 2 ) :
        for j in range( y - 1, y + 2 ) :
            for k in range ( z - 1, z + 2 ) :
                for l in range ( w - 1, w + 2 ) :
                    
                    try :
                        check[(i,j,k,l)] -= 1
                        
                        if check[(i,j,k,l)] == 0 :
                            del check[(i,j,k,l)]
                        
                    except :
                        continue

# update the grid and periphery
def update (toUpdate) :
    for operator, x, y, z, w in toUpdate :
        if operator == '-' :
            subCheck(x,y,z,w)
            del grid[(x,y,z,w)]
        elif operator == '+' :
            addCheck(x,y,z,w)
            grid[(x,y,z,w)] = 1
 
# count active neighbours on loc x, y, z, w 
def neighbours (x, y, z, w) :
    
    try :
        value = - grid[(x,y,z,w)]
    except :
        value = 0
    
    for i in range( x - 1, x + 2 ) :
        for j in range( y - 1, y + 2 ) :
            for k in range ( z - 1, z + 2 ) :
                for l in range ( w - 1, w + 2 ) :
                    try :
                        value += grid[(i,j,k,l)]
                    except :
                        continue
    
    return value

start = perf_counter()

# execute six cycles
for _ in range(6) :
    
    toUpdate = []
    
    for x, y, z, w in check :
        n = neighbours(x,y,z,w)
        
        try :
            if grid[(x, y, z, w)] :
                if 2 <= n <= 3 :
                    continue
                else :
                    toUpdate.append(('-',x, y, z, w))
                    
        except :
            if n == 3 :
                toUpdate.append(('+',x, y, z, w))
                
    update(toUpdate)
                
end = perf_counter()

print(f"Total cubes left: {len(grid)}.")
print(f"Done in {end-start} seconds.")