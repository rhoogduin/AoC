
# read input
file = open("input.txt", "r")

lines = []

lines = file.read().splitlines()
    
file.close()

# list to hold the program
program = []

for line in lines :
    
    if line[0:4] == "mask" :
        mask = line[7:]
        program.append( (0, mask) )
        
    else :
        index = line.index(']')
        memAddress = int( line[4:index] )
        
        index = line.index('=') + 2
        value = int( line[index:] )
        
        program.append( (1, memAddress, value) )

# memory
mem = {}

# write to memory
def memWrite(memAddress, value) :
    mem[memAddress] = value

# hold the 0's and 1's of the mask
mask0 = 0
mask1 = 0

# translate the mask string to two ints representing the 0's and 1's
def setMask(mask) :
    global mask0, mask1
    
    mask0 = 0
    mask1 = 0
    
    for i in range( len(mask) ) :
        mask0 *= 2
        mask1 *= 2
        
        if mask[i] != '0' :
            mask0 += 1
        if mask[i] == '1' :
            mask1 += 1

# apply mask to value
def maskValue(value) :            
    # overwrite values with 0
    value = value & mask0
    # overwrite values with 1
    value = value | mask1
    
    return value

for operation in program:
    # update mask
    if operation[0] == 0 :
        setMask(operation[1])
    # mask value and write to memory
    else :
        memAddress = operation[1]
        value = operation[2]
        
        value = maskValue(value)
        
        memWrite(memAddress, value)

# add up all values in memory
sum = 0
       
for address in mem:
    sum += mem[address]
    
print(f"Sum of values in memory is: {sum}.")
    