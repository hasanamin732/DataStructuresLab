from LQueue import LQueue
from rpnEvaluator import rpnEvaluator
import os
import time

Expqueue=LQueue(5)
Ansqueue=LQueue(5)


while True:
    expression=input("Enter a Mathematical Expression,Enter 'e' to exit")
    if expression=='e':
        print("Goodbye")
        break
    result=rpnEvaluator(expression)
    if not Expqueue.isFull():
        Expqueue.insert(result[0])
        Ansqueue.insert(result[1])
    else:
        Expqueue.remove()
        Ansqueue.remove()
        Expqueue.insert(result[0])
        Ansqueue.insert(result[1])
    os.system('cls')
    print(Expqueue)
    print(Ansqueue)
    time.sleep(0.25)
