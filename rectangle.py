class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width


    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
    def print_dimensions(self):
        print(f"Length: {self.length}, Width: {self.width}")
    
    
rect= Rectangle(5, 3)
rect.print_dimensions()
print(rect.area())
print(rect.perimeter())

