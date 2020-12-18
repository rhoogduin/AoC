
# read input
file = open("input.txt", "r")

lines = []

lines = file.read().splitlines()
    
file.close()

expressions = []

for expression in lines :
    expression = expression.replace(")", " )")
    expression = expression.replace("(", "( ")
    expression = expression.split(' ')

    for i in range( len(expression) ) :
        try:
            expression[i] = int(expression[i])
        except :
            continue
    
    expressions.append(expression)

def makeParentheses (expression, i = 0) :
    
    parentheses = []
    
    while i < len(expression) :
        
        if expression[i] == ')' :
            return parentheses, i
            
        elif expression[i] == '(' :
            sebsection, i = makeParentheses(expression, i + 1)
            parentheses.append( sebsection )
            
        else :
            parentheses.append(expression[i])
     
        i += 1
    
    return parentheses

# finds right-most operator in expression return -1 if not found
def find (expression, operator) :
    
    search = expression[:-1]
    index = len(search) - 1
    
    for char in search[::-2] :
        if char == operator :
            return index
        index -= 2
    
    return -1

def calc( expression ) -> int :
    
    # end of expression reached
    if type(expression) is int :
        return expression
    
    if len( expression ) == 1 :
        if type(expression[0]) is int :
            return expression[0]
        else :
            return calc(expression[0])
    
    # handle multiplication first
    index = find(expression, '*')
    
    # no multiplication in the expression
    if index == -1 :
        left     = expression[:-2]
        operator = expression[-2]
        right    = expression[-1]
    else :
        left     = expression[:index]
        operator = expression[index]
        right    = expression[index+1:]
    
    left  = calc(left)
    right = calc(right)
    
    if operator == '+' :
        return left + right
    elif operator == '*' :
        return left * right
    else :
        raise Exception("Unknown operator.")

sum = 0

for expression in expressions :
    expression = makeParentheses(expression)
    sum += calc(expression)

print (f"Sum of homework questions is {sum}.")