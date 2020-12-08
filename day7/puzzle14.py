
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
    
    contains = []
    
    while i < len (line) :
        
        if line[i] == "no" :
            break
        
        n = int (line[i])
        sub_bag = line[i+1] + " " + line[i+2]
        
        entry = (n, sub_bag)
        
        contains.append(entry)
        
        i += 4
     
    bags[bag] = contains

for line in lines :
    processLine(line)

def countContents (bag) :
    n = 0
    
    for item in bags[bag] :
        n += item[0] * ( 1 + countContents(item[1]) )
    
    return n
    
print (f"A shiny gold bag requires {countContents('shiny gold')} other bags inside it.")