# Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
import math
import shape

class Circle(shape.Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius