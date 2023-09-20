class Flights:
    def __init__(self):
        self._flightNo=0
        self._destination=""
        self._fuel=0.0
        self._distance=0.0
    def calfuel(self):
        if self._distance<=1000:
            self._fuel=500
        elif self._distance>1000 and self._distance<=2000:
            self._fuel=1100
        else:
            self._fuel=2200
    def feedinfo(self,flightNo,destination,distance):
        self._flightNo=flightNo
        self._destination=destination
        self._distance=distance
    
    def show_info(self):
        print("Flight Number:", self._flightNo)
        print("Destination:", self._destination)
        print("Distance:", self._distance, "miles")
        print("Fuel Required:", self._fuel, "gallons")


class Batsman:
    def __init__(self):
        self._bcode=0
        self._bname=""
        self._innings=0
        self._notout=0
        self._runs=0
        self._batavg=0.0
    def calcavg(self):
        try:
            self._batavg =self._runs/(self._innings-self._notout)
        except ZeroDivisionError:
            pass
    def readdata(self,bcode:int,bname:str,innings:int,notout:int,runs:int):
        self._bcode=bcode
        self._bname=bname
        self._innings=innings
        self._notout=notout
        self._runs=runs
        self.calcavg()
    def __repr__(self):
        return f'Code:{self._bcode} \n Name:{self._bname} \n Innings: {self._innings} \n Notouts: {self._notout} \n Runs: {self._runs} \n stored at {hex(id(self))}'

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


def main():
    obj=Flights()
    obj.feedinfo(20,"Karachi",2000)
    obj.calfuel()
    obj.show_info()
    print("----------------------")
    obj2=Batsman()
    obj2.readdata(2000,"John",10,5,500)
    print(obj2)
    print("-------------------")
    obj3=Person("Hasan")
    print(obj3.say("Hello Hasan!"))
    print(obj3.repeat())
    print(obj3.greet())
    print(obj3.repeat())
    print(obj3.ask("move aside"))
    print(obj3.repeat())
main()
