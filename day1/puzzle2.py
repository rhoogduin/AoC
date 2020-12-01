
import sys

file = open("input.txt", "r")

numbers = []

for line in file :
    numbers.append( int(line) )
    
file.close()

for i in range( len(numbers) - 2 ) :
    for j in range( i + 1, len(numbers) - 1 ) :
        for k in range( j + 1, len(numbers) ) :
            if numbers[i] + numbers[j] + numbers[k] == 2020 :
                print (f"numbers: {numbers[i]}, {numbers[j]}, {numbers[k]}")
                print (f"product: {numbers[i] * numbers[j] * numbers[k]}")
                sys.exit()