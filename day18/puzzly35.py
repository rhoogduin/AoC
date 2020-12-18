
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

def calc( expression ) -> int :
    
    # end of expression reached
    if type(expression) is int :
        return expression
    
    if len( expression ) == 1 :
        if type(expression[0]) is int :
            return expression[0]
        else :
            return calc(expression[0])
    
    left     = expression[:-2]
    operator = expression[-2]
    right    = expression[-1]
    
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