from ReversePolish import RPN
from Stack import Stack

# this function uses floor division inplace of true division
def rpnEvaluator(expression:str):
    rpn_string=RPN(expression=expression)
    print(rpn_string)
    operands=Stack()
    digits="0123456789"
    operators="*^+-/"
    i=0
    while i<=len(rpn_string)-1:
        # print(operands)
        # print(rpn_string[i])
        char=rpn_string[i]
        if char==" ":
            i+=1
            continue
        while rpn_string[i] in digits and rpn_string[i+1] in digits: # accumulating digits of numerals with number of digits>1 
            char+=rpn_string[i+1]
            i+=1
        if char in operators:
            i+=1
            print(operands)
            SecondOperand=operands.pop()
            FirstOperand=operands.pop()
            if char =="+":
                result=int(FirstOperand)+int(SecondOperand)
            elif char =="-":
                result=int(FirstOperand)-int(SecondOperand)
            elif char =="*":
                result=int(FirstOperand)*int(SecondOperand)
            elif char =="^":
                result=int(FirstOperand)**int(SecondOperand)
            else:
                if SecondOperand!="0":
                    result=int(FirstOperand)//int(SecondOperand)
                else:raise ZeroDivisionError("Cannot divide by zero")
            operands.push(result)
        else: # only numerals left
            i+=1
            operands.push(int(char))
    final_result=operands.pop()
    
    return(expression,final_result)

# exp="2+44/(7+2)^3-(6*2*234/8)"
# print(rpnEvaluator(exp))
# # 2 44 7 2 +3 ^/+6 2 *234 *8 /-