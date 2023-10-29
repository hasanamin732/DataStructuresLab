class Point:
    def __init__(self,x,y):
        self._x=x
        self._y=y
    @property
    def xCoord(self):
        return self._x
    @xCoord.setter
    def xCoord(self,x):
        self._x=x
    @property
    def yCoord(self):
        return self._y
    @yCoord.setter
    def yCoord(self,y):
        self._y=y
    def move(self,x,y):
        self.xCoord=x
        self.yCoord=y
    def __repr__(self):
        return f"X-Coordinate={self.xCoord}, Y-Coordinate={self.yCoord}"
    
class Circle(Point):
    def __init__(self, radius, point):
        super().__init__(point.xCoord, point.yCoord) 
        self._radius = radius
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        self._radius = r
    def move(self,x,y):
        super().move(x,y)
    def __repr__(self):
        return f"X-Coordinate={self.xCoord}, Y-Coordinate={self.yCoord}, Radius={self.radius}"



p=Point(2,3)
print(p)
p.xCoord=5
p.yCoord=7

print(p)
c=Circle(20,p)
print(c)
c.radius=10
c.move(4,9)
print(c)