
"""read input"""
file = open("input.txt", "r")

codes = []

codes = file.read().splitlines()
    
file.close()

"""boardpass code to seatID"""
def toInt (input : str) -> int :
    n = 0
    length = len(input)
    for i in range(length):
        if input[i] == 'B' or input[i] == 'R' :
            n += 2 ** (length - i - 1)
    return n
    
seats = list( map(toInt, codes) )

seats.sort()

print (f"Highest seat ID: {seats[-1]}")

for i in range (1, len(seats)) :
    if seats[i-1] != seats[i]-1 :
        print (f"Your seat: {seats[i]-1}")
        break