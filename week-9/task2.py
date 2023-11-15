def element_of(x,mylist):
    for i in mylist:
        if isinstance(i,(list,tuple)):
            returned=element_of(x,i)
            if returned==True:
                return True
        else:
            if i==x:
                return True
    return False

def filter_by_depth(depth, nested_list):
    if depth < 0:
        raise ValueError("Depth should be a non-negative integer")
    elif depth==0:
        return []
    
    mylist=[
        filter_by_depth(depth - 1, el) if isinstance(el, list) else el
        for el in nested_list
    ]
    return [x for x in mylist if x != []]

print("Element of() Testing")
print(element_of(5, [1,2,3,4,5,6,7]))
print(element_of(7, [1,2,[3,4,[5,6]],[7]]) )
print(element_of(77, [1,2,[3,4,[5,6]],[7]]))

print("Filter by Depth() Testing")
print(filter_by_depth(0, [1,2,3])) 
print(filter_by_depth(1, [1,2,3]) ) 
print(filter_by_depth(5, [1,2,3]) ) 
print(filter_by_depth(2, [1,2,[3,4,[5,6]],[7]])) 
