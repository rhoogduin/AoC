
#read input
file = open("input.txt", "r")

lines = []

lines = file.read().splitlines()
    
file.close()

# timestamp dor departure
timestamp = int( lines[0] )

# list of all busses
busses = lines[1].split(',')


length = len(busses)
# clean bus list
for i in range( length ) :
    if busses[length - i - 1] == 'x' :
        busses.pop(length - i - 1)
    else :
        busses[length - i - 1] = int( busses[length - i - 1] )

best_bus = 0        
waittime = timestamp

for bus in busses :
    if bus - (timestamp % bus) < waittime :
        waittime = bus - (timestamp % bus)
        best_bus = bus

print(f"Best bus: {best_bus}, wait time: {waittime}.")
print(f"Puzzle answer: {best_bus * waittime}.")