pascal=lambda n,k: 1 if k==0 or n==k else pascal(n-1,k-1)+pascal(n-1,k)


print(pascal(4,2))
print(pascal(5,3))
print(pascal(10,7))