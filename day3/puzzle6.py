
file = open("input.txt", "r")

"""map to track location of trees"""
map = []

"""parse input"""
for line in file :
    strip = []
    for letter in line :
        if letter == '.' :
            strip.append(0)
        if letter == '#' :
            strip.append(1)
    map.append(strip)
    
file.close()

"""slopes to check"""
slopes = [(1,1),(1,3),(1,5),(1,7),(2,1)]

"""position coordinates"""
x = 0 
y = 0 

"""size of each step"""
X_STEP = 0
Y_STEP = 0

"""width of the map"""
WIDTH = len(map[0])

"""do one step"""
def step() :
    global x, y
    x += X_STEP
    y += Y_STEP
    y %= WIDTH

"""set step size to follow slope"""
def setSlope(slope : tuple) :
    global X_STEP, Y_STEP
    X_STEP = slope[0]
    Y_STEP = slope[1]

"""variable to calculate product"""
product = 1

for slope in slopes :

    """reset position to top left"""
    x = 0
    y = 0
    
    """set slope to check"""
    setSlope(slope)

    """reset counter"""
    counter = 0

    """check slope for trees"""
    while x < len(map) :
        counter += map[x][y]
        step()

    """calculate product of trees hit on each slope"""
    product *= counter
    
print (f"product:{product}")