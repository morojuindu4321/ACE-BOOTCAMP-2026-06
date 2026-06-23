from abc import ABC, abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2
    def perimeter(self):
        return 4 * self.side
class Triangle(Shape):
    def __init__(self, a, b, c, height):
        self.a = a
        self.b = b
        self.c = c
        self.height = height
    def area(self):
        return 0.5 * self.a * self.height
    def perimeter(self):
        return self.a + self.b + self.c
c = Circle(5)
s = Square(4)
t = Triangle(6, 8, 10, 4)
print("Circle Area:", c.area())
print("Circle Perimeter:", c.perimeter())
print("Square Area:", s.area())
print("Square Perimeter:", s.perimeter())
print("Triangle Area:", t.area())
print("Triangle Perimeter:", t.perimeter())