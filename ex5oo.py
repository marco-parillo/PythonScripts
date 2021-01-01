# Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.

class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (((x2-x1)**2)+((y2-y1)**2))**.5
    
    def slope(self):
        x1 = self.coor1[0]
        y1 = self.coor1[1]
        x2 = self.coor2[0]
        y2 = self.coor2[1]
        return ((y2-y1)/(x2-x1))

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
print (li.distance())
# 9.433981132056603
print (li.slope())
# 1.6


class Cylinder:
    
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        self.pi = 3.14
    
    def volume(self):
        return self.height * self.pi * (self.radius**2)
    
    def surface_area(self):
        return (self.height*2*self.pi*self.radius)+(2*self.pi*(self.radius)**2)

# EXAMPLE OUTPUT
c = Cylinder(2,3)
print (c.volume())
# 56.52
print (c.surface_area())
# 94.2
