class Rectangle: 
    def __init__(self, width, height): 

        self.width = width 

        self.height = height 
 
    def area(self): 

        return self.width * self.height 

class Circle: 
    def __init__(self, radius): 

        self.radius = radius 

    def area(self):
        return 3.141592653 * self.radius * self.radius