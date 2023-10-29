from Stack import Stack

def DenBin(value):
    stack=Stack()
    while value!=1:
        stack.push(value%2)
        value=value//2
    stack.push(1%2)
    string=""
    while not stack.is_empty():
        string+=str(stack.pop())
    return string

# just for completion
def BinDen(string:str):
    stack=Stack()
    for i in string:
        stack.push(int(i))
        total=0
    for i in range(len(string)):
        total+=((2**i)*(stack.pop()))
    return total

def DenHex(value):
    letters='ABCDEF'
    hex={i:str(i) for i in range(10)} | {i:letters[i-10] for i in range(10,16)}
    stack=Stack()
    while  value>16:
        stack.push(hex[value%16])
        value=value//16
    stack.push(hex[value])
    string=""
    while not stack.is_empty():
        string+=str(stack.pop())
    return string
    


k=23658
print(DenBin(k))
print(BinDen(DenBin(k)))
print(DenHex(k))
