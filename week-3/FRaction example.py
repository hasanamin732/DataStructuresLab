#################
## EXAMPLE: simple class to represent fractions
## Try adding more built-in operations like multiply, divide
### Try adding a reduce method to reduce the fraction (use gcd)
#################
from math import gcd
class Fraction:
    """
    A number represented as a fraction
    """
    def __init__(self, num, denom):
        """ num and denom are integers """
        self.num = num
        self.denom = denom
    def __str__(self):
        
        """ Returns a string representation of self """
        return self.reduce()
    def __add__(self, other):
        """ Returns a new fraction representing the addition """
        top = self.num*other.denom + self.denom*other.num
        bott = self.denom*other.denom
        return Fraction(top, bott)
    def __sub__(self, other):
        """ Returns a new fraction representing the subtraction """
        top = self.num*other.denom - self.denom*other.num
        bott = self.denom*other.denom
        return Fraction(top, bott)
    def __mul__(self,other):
        top=self.num*other.num
        bott=self.denom*other.denom
        return Fraction(top,bott)
    def __truediv__(self,other):
        if self.num==0:
            raise ValueError("Division by zero not allowed")
        new_num = self.num * other.denom
        new_denom = self.denom * other.num
        return Fraction(new_num, new_denom)

    def __float__(self):
        """ Returns a float value of the fraction """
        return self.num/self.denom
    def inverse(self):
        """ Returns a new fraction representing 1/self """
        if self.num==0:
            raise ValueError("Inverse of zero is not defined")
        return Fraction(self.denom, self.num)
    def reduce(self):
        GCD=gcd(self.num,self.denom)
        return str(int(self.num/GCD)) + "/" + str(int(self.denom/GCD))

a = Fraction(7,11)
b = Fraction(3,4)
c = a / b # c is a Fraction object
print(c)
print(float(c))
print(Fraction.__float__(c))
print(float(b.inverse()))
##c = Fraction(3.14, 2.7) # assertion error
##print a*b # error, did not define how to multiply two Fraction objects