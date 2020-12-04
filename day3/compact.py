
file = open("input.txt", "r")

map = []

for line in file :
    strip = []
    for letter in line :
        if letter == '.' :
            strip.append(0)
        if letter == '#' :
            strip.append(1)
    map.append(strip)
    
file.close()

slopes = [(1,1),(1,3),(1,5),(1,7),(2,1)]

product = 1

for slope in slopes :
    x = y = counter = 0
    while x < len(map) :
        counter += map[x][y]
        x += slope[0]
        y = (y + slope[1]) % len(map[0])
    product *= counter
    
print (f"product:{product}")