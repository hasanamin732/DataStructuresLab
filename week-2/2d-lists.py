list1 = [[1, 2, 3], [2, 3, 3], [1, 3, 3]]

def find_max(mylist):
    max_sum=0
    for i in mylist:
        if sum(i)>max_sum:
            max_sum=sum(i)
            index=list1.index(i)
    return index

print(f"The row with the highest sum is at index:{find_max(list1)}")
