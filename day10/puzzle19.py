
#read input
file = open("input.txt", "r")

lines = []

lines = file.read().splitlines()
    
file.close()

#list that will contain all numbers from input
adapters = []

#turn each line into a number and add to the list
for line in lines :
    adapters.append( int(line) )
    
adapters.sort()

delta_1 = 0
delta_3 = 1

if adapters[0] == 1 :
    delta_1 += 1
elif adapters[0] == 3 :
    delta_3 += 1

for i in range( 1, len(adapters) ) :
    delta = adapters[i] - adapters[i-1]
    if delta == 1 :
        delta_1 += 1
    elif delta == 3 :
        delta_3 += 1
        
print (f"Puzzle solution is: {delta_1 * delta_3}")
