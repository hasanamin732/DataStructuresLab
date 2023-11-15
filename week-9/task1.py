gcd = lambda a,b : a if (b==0) else gcd(abs(b),abs(a)%abs(b))

print(gcd(2,3))
print(gcd(16,100))
print(gcd(0,100))