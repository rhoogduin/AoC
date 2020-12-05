file = open("input.txt", "r")

codes = []

"""parse input"""
for line in file :
    codes.append(line)
    
file.close()

seats = []

for code in codes :
    row = [i for i in range(128)]
    col = [i for i in range(8)]
    
    for i in range(7) :
        index_half = int (len(row) / 2)
        
        if code[i] == 'F' :
            row = row[:index_half]
        else :
            row = row[index_half:]
            
    for i in range(7, 10) :
        index_half = int (len(col) / 2)
        
        if code[i] == 'L' :
            col = col[:index_half]
        else :
            col = col[index_half:]
            
    seats.append(row[0] * 8 + col[0])

highest = -1

for i in seats:
    if i > highest :
        highest = i
        
print (highest)