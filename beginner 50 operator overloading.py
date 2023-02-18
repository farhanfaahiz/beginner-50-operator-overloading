# Printing type of each objects
a = type(2)
print(a)

b = type(2.0)
print(b)

c = type('2')
print(c)

print(2 + 5)
print(2 * 5)
print('2' + '5')
print('2' * 5)



class a:
    pass

print(dir(a))

# Overloading operator in class

import math

class Circle:
    def __init__(self, radius) :
        self.__radius = radius
        
    def set_radius(self, value) :
        self.__radius = value 
        
    def get_radius(self) :
        return self.__radius
    
    def area(self) :
        return math.pi * self.__radius ** 2
    
    def __add__(self, circle_object) :
        return Circle(self.__radius + circle_object.__radius)
    def __lt__(self, circle_object) :
        return (self.__radius < circle_object.__radius)
    def __gt__(self, circle_object) :
        return (self.__radius > circle_object.__radius)
    def __str__(self) :
        return 'Circle area = ' + str(self.area())
    
c1 = Circle(2)
c2 = Circle(3)
c3 = c1 + c2  

print(c1.get_radius())  
print(c2.get_radius())  
print(c3.get_radius())  
print(c1.area())

print(c1 < c2)
print(c1 > c2)

print(str(c1))
print(str(c2))
print(str(c3))
