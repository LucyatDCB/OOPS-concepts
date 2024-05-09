# Define a base class representing a Shape
class Shape:
    def __init__(self):
        self.name = "Shape"

    # Abstract method to calculate area (to be implemented by subclasses)
    def calculate_area(self):
        pass

# Concrete subclass representing a Rectangle
class Rectangle(Shape):
    def __init__(self, length, breadth):
        super().__init__()                                  # Call the constructor of the parent class
        self.name = "Rectangle"
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        return self.length * self.breadth
      
class Circle(Shape):
    def __init__(self, radius):
        super().__init__()                                   # Call the constructor of the parent class
        self.name = "Circle"
        self.radius = radius
      
    def calculate_area(self):
        return 3.14 * self.radius * self.radius

# Create objects of Rectangle and Circle
rectangle = Rectangle(5, 4)
circle = Circle(3)

# Calculate and print areas
print("Area of", rectangle.name, ":", rectangle.calculate_area())
print("Area of", circle.name, ":", circle.calculate_area())
