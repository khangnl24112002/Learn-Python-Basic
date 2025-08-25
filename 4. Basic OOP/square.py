import shape

class Square(shape.Shape):
    def __init__(self, edge):
        self.edge = edge
    def area(self):
        return self.edge ** 2
    def perimeter(self):
        return self.edge * 4