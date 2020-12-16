
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
def memWrite(memList, value) :
    for memAddress in memList :
        mem[memAddress] = value

# hold the and 1's and X's of the mask
mask1 = 0
maskX = ""

# translate the mask string to two masks representing 1's and X's
def setMask(mask) :
    global mask1, maskX
    
    mask1 = 0
    maskX = mask
    
    for i in range( len(mask) ) :
        mask1 *= 2
        
        if mask[i] == '1' :
            mask1 += 1

# generate both options for floating bits
def maskFloatingBits(index, memAddress, memList) :
    
    if index >= len(maskX) :
        memList.append(memAddress)
        return value
    
    if maskX[index] == 'X' :
        maskFloatingBits(index+1, memAddress, memList)
        memAddress = memAddress ^ (1 * (2 ** (len(maskX)-index-1) ) )
    maskFloatingBits(index+1, memAddress, memList)

# apply mask to memAddress
def maskMemAddress(memAddress) :
    memList = []
    
    # overwrite memAddress with 1
    memAddress = memAddress | mask1
    
    maskFloatingBits(0, memAddress, memList)
            
    if memList == [] :
        memList.append(memAddress)
    
    return memList

for operation in program:
    # update mask
    if operation[0] == 0 :
        setMask(operation[1])
    # write value to maskewd memory addresses
    else :
        memAddress = operation[1]
        value = operation[2]
        
        memList = maskMemAddress(memAddress)
        
        memWrite(memList, value)
        
# add up all values in memory
sum = 0
       
for address in mem:
    sum += mem[address]
    
print(f"Sum of values in memory is: {sum}.")


    