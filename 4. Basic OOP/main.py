from circle import Circle
from square import Square

shapes = [
    Circle(3),
    Square(4),
    Circle(2),
    Square(5)
]

for shape in shapes:
    print(f"Shape {shape.__class__.__name__}: Area: {shape.area():2f}, Perimeter: {shape.perimeter():2f}")