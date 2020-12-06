
"""read input"""
file = open("input.txt", "r")

lines = []

lines = file.read().splitlines()
    
file.close()

groups = []

group = ""

for line in lines :
    
    if line == "" :
        groups.append( set(group) )
        group = ""
    
    else :
        group += line
        
groups.append( set(group) )
        
sum = 0

for group in groups :
    sum += len (group)
    
print (f"Total yes answers: {sum}")