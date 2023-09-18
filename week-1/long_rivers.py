rivers = [
{"name": "Nile", "length": 4157},
{"name": "Yangtze", "length": 3434},
{"name": "Murray-Darling", "length": 2310},
{"name": "Volga", "length": 2290},
{"name": "Mississippi", "length": 2540},
{"name": "Amazon", "length": 3915}
]
# Task 1
for river in rivers:
    print(river["name"])

# Task 2
total_length=0
for river in rivers:
    total_length+=river["length"]
print(total_length)

# Task 3
for river in rivers:
    if river["name"].startswith("M"):
        print(river["name"])

# Task 4
for river in rivers:
    print(f'Name:{river["name"]}---Length:{round(river["length"]*1.6,3)} miles')

# Task 5
def overlap(lst1,lst2):
    newlst=[]
    for element1 in lst1:
        if element1 in lst2:
            newlst.append(element1)
    return newlst

def join(lst1,lst2):
    for element1 in lst1:
        if element1 not in lst2:
            lst2.append(element1)
    return lst2

print(f"Overlap:{overlap([1,2,3,4],[2,3,4,5,6,7])}")
print(f"Join:{join([1,2,3,4],[2,3,4,5,6,7])}")
                
