def is_balanced(expression):
    stack = []
    open_brackets = "([{"
    close_brackets = ")]}"
    bracket_pairs = {')': '(', ']': '[', '}': '{'}
    
    for i, char in enumerate(expression):
        if char in open_brackets:
            stack.append((char, i))
        elif char in close_brackets:
            if not stack:
                raise ArithmeticError(f"This expression is NOT correct e.g. error at character # {i}. '{char}' - not opened.")
                
            last_open, index = stack.pop()
            if last_open != bracket_pairs[char]:
                raise ArithmeticError(f"This expression is NOT correct e.g. error at character # {i}. '{char}' - not closed.")
                
    
    if not stack:
        print("This expression is correct.")
        return True
    else:
        last_open, index = stack.pop()
        raise ArithmeticError(f"This expression is NOT correct e.g. error at character # {index}. '{last_open}' - not closed.")
        

# Input expression from the user
if __name__ == "__main__":
    expression = input("Enter an expression: ")
    is_balanced(expression)

