
from time import perf_counter

ITERATIONS = 30000000

# read input
file = open("input.txt", "r")

lines = []

lines = file.read().splitlines()
    
file.close()

# dict to hold numbers, turn they were said, and difference to previous occurence
numbers = [-1] * ITERATIONS
numbers_amount = 0

for line in lines :
    input = line.split(',')
    for i in range( len(input) ) :
        numbers[int(input[i])] = i + 1

numbers_amount = len(input)

start = perf_counter()

lastSaid = 0

for turn in range( numbers_amount + 2 , ITERATIONS + 1) :    
    
    lastOccurence = numbers[lastSaid]
    
    if lastOccurence >= 0 :
        difference = turn - 1 - lastOccurence
    else :
        difference = 0
    
    numbers[lastSaid] = turn - 1

    lastSaid = difference
    
end = perf_counter()
    
print (f"The {ITERATIONS}th number spoken is: {lastSaid}!")
print (f"Took: {end-start} seconds.")