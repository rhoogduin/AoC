
"""read input"""
file = open("input.txt", "r")

lines = []

lines = file.read().splitlines()
    
file.close()

groups = []

group = []

def merge (toMerge) -> set :
    for i in range( 1, len(toMerge) ) :
        toMerge[0] = toMerge[0] & toMerge[i]
    return toMerge[0]

for line in lines :
    
    if line == "" :
        groups.append( merge(group) )
        group = []
    
    else :
        group.append( set(line) )
        
groups.append( merge(group) )
        
sum = 0

for group in groups :
    sum += len (group)
    
print (f"Total yes answers: {sum}")