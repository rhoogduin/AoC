
file = open("input.txt", "r")

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

"""variable declaration"""

X_STEP = 1
Y_STEP = 3
WIDTH = len(map[0])

"""x-position"""
x = 0 
"""y-position"""
y = 0 

"""do one step"""
def step() :
    global x, y
    x += X_STEP
    y += Y_STEP
    y = y % WIDTH

counter = 0

while x < len(map) :
    counter += map[x][y]
    step()

print (f"trees hit:{counter}")