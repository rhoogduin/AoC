
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
        number = numbers[i]
        break

def setCheck (i) :
    global numbers
    sum = 0
    j = i
    while sum < number and j < len(numbers) :
        sum += numbers[j]
        j += 1
        
    if sum == number and j > i+1 :
        numbers = numbers[i:j]
        numbers.sort()
        print (f"Smallest numer is {numbers[0]}, largest is {numbers[-1]}.")
        print (f"Sum is {numbers[0] + numbers[-1]}.")
        return True
    
    return False
    
for i in range( len(numbers) ) :
    if setCheck(i) :
        break