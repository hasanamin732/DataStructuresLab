from Stack import Stack
from BalancedExpression import is_balanced

    
    
def RPN(expression):
    if not is_balanced(expression=expression):
        print("Invalid Expression")
        return False
    stack=Stack()
    precedence = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1}
    bracket_pairs = {')': '(', ']': '[', '}': '{'}
    RPNstring=''
    for index,i in enumerate(expression):
        if i in '[{(':
            stack.push(i)
        elif i in '^*/+-':
            while (
                stack.peek() in precedence
                and precedence.get(stack.peek(), 0) >= precedence.get(i, 0)
            ):
                RPNstring += stack.pop()

            stack.push(i)
        elif i in ']})':
            while stack.peek() !=  bracket_pairs[i]:
                RPNstring+=stack.pop()
            stack.pop()
        else:
            if not expression[index]==expression[-1]: # only if the character is not the last character of the expression to avoid index out of range error when checking for index+1
                if expression[index+1] in '0123456789.':
                    RPNstring+=i
                else:
                    RPNstring=RPNstring  + i+" "
            else:
                RPNstring=RPNstring  + i+" "
            
    while not stack.is_empty():
        RPNstring+=stack.pop()

    return RPNstring

# print(RPN("(3+5)*(7/2)-4"))