
# read input
file = open("input.txt", "r")

lines = []

lines = file.read().splitlines()
    
file.close()

rules = []

for i in range(20) :
    
    input = lines[i].split(':')
    
    field = input[0]
    
    input = input[1].split(' ')
    
    range_1 = input[1].split('-')
    
    range_2 = input[3].split('-')
    
    rules.append ( ( field, int(range_1[0]), int(range_1[1]), int(range_2[0]), int(range_2[1]) ) )
    
my_ticket = list( map( int, lines[22].split(',') ) )

tickets = []

for i in range(25, len(lines)) :

    ticket = list( map( int, lines[i].split(',') ) )

    tickets.append(ticket)
    
def checkValue (value) -> bool :
    
    for rule in rules :
        if rule[1] <= value <= rule[2] :
            return True
        if rule[3] <= value <= rule[4] :
            return True
    
    return False
    
def checkTicket (ticket) -> int :
    
    for value in ticket :
        if not checkValue(value) :
            return value
    
    return 0

error_rate = 0

for ticket in tickets :
    error_rate += checkTicket(ticket)

print (f"Error rate is {error_rate}.")