
#read input
file = open("input.txt", "r")

lines = []

lines = file.read().splitlines()
    
file.close()

#list that will contain all numbers from input
numbers = []

#turn each line into a number and add to the list
for line in lines :
    numbers.append( int(line) )

def checkNumber (i) :
    for j in range(i-25, i-1) :
        for k in range(j, i) :
            if numbers[j] + numbers[k] == numbers[i] :
                return True
    return False

for i in range( 25, len(numbers) ) :
    if not checkNumber(i) :
        print (f"Number: {numbers[i]} at line: {i}.")