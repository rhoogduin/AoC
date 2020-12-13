
#read input
file = open("input.txt", "r")

lines = []

lines = file.read().splitlines()
    
file.close()

#list that will contain all numbers from input
adapters = [0]

#turn each line into a number and add to the list
for line in lines :
    adapters.append( int(line) )
    
adapters.sort()

def countSubArrangements (i, k) :
    counter = 0
    
    if i == k:
        return 1
    
    for j in range(1, 4) :
        if i+j > k :
            break
            
        if adapters[i+j] - adapters[i] <= 3 :
            counter += countSubArrangements(i+j, k)
        else :
            break
            
    return counter
    

def countArrangements() :
    counter = 1
    
    i = 0
    while i < len(adapters) - 1 :
        
        if adapters[i+1] - adapters[i] == 3 :
            i += 1
            continue
        
        j = i
        while j < len(adapters) - 1 and adapters[j+1] - adapters[j] != 3:
            j += 1
        
        counter *= countSubArrangements (i, j)
        
        i = j
        
    return counter


print (f"Amount of arrangements: {countArrangements()}.")