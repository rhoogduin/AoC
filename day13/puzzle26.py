
def EEA (a, b) :
    
    q = [0]
    r = [a,b]
    s = [1,0]
    t = [0,1]
    
    i = 1
    while True :
        q.append( int(r[i-1] / r[i]) )
        r.append( r[i-1] - q[i] * r[i] )
        s.append( s[i-1] - q[i] * s[i] )
        t.append( t[i-1] - q[i] * t[i] )
        
        if r[i+1] == 0 :
            break
        
        i += 1
    
    return s[i]
    
#read input
file = open("input.txt", "r")

lines = []

lines = file.read().splitlines()
    
file.close()

# list of all busses
busses = lines[1].split(',')

busspairs = []

# clean bus list
for i in range( len(busses) ) :
    if busses[i] != 'x' :
        busspairs.append( ( i , int( busses[i]) ) )

# product of all bus IDs
N = 1

for bus in busspairs :
    N *= bus[1]

def subSum (pair) :
    Ni = int( N / bus[1] )
    
    Mi = EEA(Ni, bus[1])
    
    if bus[0] == 0 :
        ai = 0
    elif bus[1] > bus[0] :
        ai = bus[1] - bus[0]
    else :
        ai = bus[1] - ( bus[0] - bus[1] )
    
    return ai * Mi * Ni

sum = 0
    
for bus in busspairs :
    sum += subSum(bus)
    
print (f"Lowest number is: {sum % N}.")