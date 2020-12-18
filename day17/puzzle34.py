
def zeros(dimensions, i = 0) :
    
    list = []
    
    if i == len(dimensions) - 1 :
        return [0] * dimensions[i]
    
    for _ in range(dimensions[i]) :
        list.append( zeros(dimensions, i+1) )
    
    return list

from time import perf_counter

SIZE = 20

# read input
file = open("input.txt", "r")

lines = []

lines = file.read().splitlines()
    
file.close()

# grid to hold the conway cubes
grid = zeros((SIZE, SIZE, SIZE, SIZE))

padding = int( (SIZE - len(lines[0])) / 2 )
z = w = int( (SIZE / 2) - 1 )

for i, line in enumerate(lines) :
    for j in range(len(line)) :
        if line[j] == '#' :
            grid[i+padding][j+padding][z][w] = 1
            
def show (z = 9, w = 9) :
    for x in range(SIZE) :
        temp = ""
        for y in range(SIZE) :
            if grid[x][y][z][w] :
                temp += '#'
            else :
                temp += '.'
        print(temp)

# count neighbours of a given location
def neighbours (x : int, y : int, z : int, w : int) -> int :
    
    if (grid[x][y][z][w]) :
        neighbours = -1
    else :
        neighbours = 0
    
    for i in range(x-1, x+2) :
        if not 0 <= i < SIZE :
            continue
        for j in range(y-1, y+2) :
            if not 0 <= j < SIZE :
                continue
            for k in range(z-1, z+2) :
                if not 0 <= k < SIZE :
                    continue
                for l in range(w-1, w+2) :
                    if not 0 <= l < SIZE :
                        continue
                    neighbours += grid[i][j][k][l]
    
    return neighbours

start = perf_counter()

# execute six cycles
for i in range(6) :
    
    new_grid = zeros((SIZE, SIZE, SIZE, SIZE))
    
    for x in range(SIZE) :
        for y in range(SIZE) :
            for z in range(SIZE) :
                for w in range(SIZE) :
                    n = neighbours(x, y, z, w)
                    
                    if n == 3 :
                        new_grid[x][y][z][w] = 1
                    elif n == 2 and grid[x][y][z][w] :
                        new_grid[x][y][z][w] = 1
    
    grid = new_grid

count = 0

for x in range(SIZE) :
    for y in range(SIZE) :
        for z in range(SIZE) : 
            for w in range(SIZE) :
                count += grid[x][y][z][w]
                
end = perf_counter()

print(f"Total cubes left: {count}.")
print(f"Done in {end-start} seconds.")