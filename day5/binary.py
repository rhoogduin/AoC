
"""read input"""
file = open("input.txt", "r")

codes = []

codes = file.read().splitlines()
    
file.close()

"""boardpass code to seatID"""
def toInt (input : str) -> int :
    bin = "" 
    for c in input :
        if c == 'B' or c == 'R' :
            bin += '1'
        else:
            bin += '0'
    return int (bin, 2)
    
seats = list( map(toInt, codes) )

seats.sort()

print (f"Highest seat ID: {seats[-1]}")

for i in range (1, len(seats)) :
    if seats[i-1] != seats[i]-1 :
        print (f"Your seat: {seats[i]-1}")
        break