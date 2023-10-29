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

class Person:
    def __init__(self, name):
        self.name = name
        self.last_call=None
        self.last_stuff=None

    def say(self, stuff):
        self.last_stuff=stuff
        self.last_call=self.say
        return stuff

    def ask(self, stuff):
        self.last_stuff=stuff
        self.last_call=self.ask
        return self.say("Would you please " + stuff)

    def greet(self):
        self.last_call=self.greet
        return self.say("Hello, my name is " + self.name)

    def repeat(self):
        if self.last_call is not None:
            if self.last_stuff is not None:
                return self.last_call(self.last_stuff)
            else:
                return self.last_call()
        else:
            return "No method called yet"

class DoubleTalker(Person):
    def say(self,stuff):
        result=super().say(stuff)
        return result +" "+ result


class Account: 
    interest = 0.02 
    def __init__(self, account_holder):
        self.balance = 0 
        self.holder = account_holder
        self.transactions=[]
    def deposit(self, amount):
        self.transactions.append(("deposit",amount))
        self.balance = self.balance + amount 
        print("Yes!") 
    def withdraw(self, amount):
        """Decrease the account balance by amount and return the new balance. """ 
        if amount > self.balance: 
            return 'Insufficient funds'
        self.balance = self.balance - amount 
        self.transactions.append(("withdraw",amount))
        return self.balance
class CheckingAccount(Account):
    def __init__(self,account_holder):
        Account.__init__(self,account_holder)
    def deposit(self, amount):
        print("Have a nice Day")
        return super().deposit(amount)

hasan=DoubleTalker("Hasan")
myacc=Account("Hasan")
myacc.deposit(2000)
myacc.withdraw(500)
print(myacc.transactions)
print(hasan.greet())
print(hasan.ask("Pass me the bowl"))
print(hasan.say("Hello World"))
print(hasan.repeat())
# a = Fraction(7,11)
# b = Fraction(3,4)
# c = a / b # c is a Fraction object
# print(c)
# print(float(c))
# print(Fraction.__float__(c))
# print(float(b.inverse()))



