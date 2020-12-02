
import sys

if len(sys.argv) != 4 :
    print("usage: python expensereport.py inputfile #entries target")
    print("inputfile - file with input numbers")
    print("#entries  - number of entries to sum and compare to target")
    print("target    - target to hit with sum of entries")
    sys.exit()

filename = sys.argv[1]

entries = int(sys.argv[2])

target = int(sys.argv[3])

numbers = []

file = open(filename, "r")

for line in file :
    numbers.append( int(line) )
    
file.close()

def test ( entries = [], a = 0, n = entries ) :
    
    if n == 0 :
        
        sum = 0
        
        for i in range ( len(entries) ) :
            sum += entries[i]
        
        if sum == target :
            print (f"numbers: {entries}")
            
            product = 1
            for i in range ( len(entries) ) :
                product *= entries[i]
            
            print (f"product: {product}")
            
            sys.exit()
        
        return

    for i in range( a, len(numbers) - (n - 1) ) :
        entries.append(numbers[i])
        test( entries, a + 1, n - 1 )
        entries.pop()

test()
