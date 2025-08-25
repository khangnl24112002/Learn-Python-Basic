# Write a Python program to create a class that represents a shape. 
# Include methods to calculate its area and perimeter. 
# Implement subclasses for different shapes like circle, triangle, and square.

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area")
    def perimeter(self):
        raise NotImplementedError("Subclasses must implement perimeter")