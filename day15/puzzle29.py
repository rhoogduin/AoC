
ITERATIONS = 2020

# read input
file = open("input.txt", "r")

lines = []

lines = file.read().splitlines()
    
file.close()

# dict to hold numbers, turn they were said, and difference to previous occurence
numbers = {}

for line in lines :
    input = line.split(',')
    for i in range( len(input) ) :
        numbers[int(input[i])] = i + 1

lastSaid = 0

for turn in range( len(numbers) + 2 , ITERATIONS + 1) :    
    
    try:
        difference = turn - 1 - numbers[lastSaid]
    except :
        difference = 0
    
    numbers[lastSaid] = turn - 1

    lastSaid = difference
    
print (f"The {ITERATIONS}th number spoken is: {lastSaid}!")