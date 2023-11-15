def Multiply(x,y):
    while x!=1:
        if x%2==0:
            x=x//2
            y=2*y
        else:
            x=(x-1)//2
            y=3*y
            
    return y
    
def expo(x,y):
    if y==1 or x==0:
        return x
    if y%2 ==0:
        return expo((x**2),y//2)
    else:
        return x*expo((x**2),(y-1)//2)
print("Multiply Testing")
print(Multiply(2,38))
print(Multiply(3,56))
print(Multiply(3,17))

print("Exponent Testing")
print(expo(2,5))
print(expo(3,4))
print(expo(7,3))



