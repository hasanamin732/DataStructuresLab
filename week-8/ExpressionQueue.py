from LQueue import LQueue
from rpnEvaluator import rpnEvaluator
Expqueue=LQueue(5)
Ansqueue=LQueue(5)

expressions = [
    "(3+5)*(7/2)-4",
    "2^3 + (4 * 5) - (6 / 2)",
    "(10 - 2) * (15 / 3) + 7",
    "8 / 2 + (5 * 3) - 1",
    "4^2 / (6 - 2) + 9",
    "(2 + 6) * 3 - (5 / 2)",
    "7 * (9 / 3) + 2^2",
    # "(3 + 4) * (6 - 1) / 2",
    # "5 * (8 / 4) + 3^2",
    # "4^2 - (6 / 2) + 5"
]

for exp in expressions:
    print(exp)
    result=rpnEvaluator(exp)
    if not Expqueue.isFull():
        Expqueue.insert(result[0])
        Ansqueue.insert(result[1])
    else:
        Expqueue.remove()
        Ansqueue.remove()
        Expqueue.insert(result[0])
        Ansqueue.insert(result[1])
print(Expqueue)
print(Ansqueue)