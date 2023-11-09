from LQueue import LQueue
from Stack import Stack
def palindrome_check(string):
    myQueue=LQueue(len(string))
    myStack=Stack()
    for i in string:
        myQueue.insert(i.lower())
        myStack.push(i.lower())
    for i in range(len(string)):
        if len(myQueue)>1:
            front=myQueue.remove()
            rear=myStack.pop()
            if front==rear:
                continue
            else:return False
        else:
            break
    return True

   
    
        

print(palindrome_check("eMadammAdam"))