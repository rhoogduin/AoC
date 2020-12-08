
"""read input"""
file = open("input.txt", "r")

lines = []

lines = file.read().splitlines()
    
file.close()

bags = {}

def processLine(line) :
    line = line.split()
    
    bag = line[0] + " " + line[1]
    
    i = 4
    contains = [0]
    
    while i < len (line) :
        
        if line[i] == "no" :
            break
        
        sub_bag = line[i+1] + " " + line[i+2]
        
        contains.append(sub_bag)
        
        i += 4
     
    bags[bag] = contains

for line in lines :
    processLine(line)

def canContain (bag, target) :
    
    if bags[bag][0] == 1 :
        return True
    if bags[bag][0] == -1 :
        return False
    
    if target in bags[bag][1:] :
        bags[bag][0] = 1
        return True
        
    for item in bags[bag][1:] :
        if canContain(item, target) :
            bags[bag][0] = 1
            return True

    bags[bag][0] = -1
    return False

counter = 0

for bag in bags :
    if canContain(bag, "shiny gold") :
        counter += 1
        
print (f"{counter} bags could contain a shiny gold bag.")