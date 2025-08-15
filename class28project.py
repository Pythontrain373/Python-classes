radius = int(input("What is the radius: "))
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        ans=3.14*self.radius**2
        print("The area is",ans)
    def perimeter(self):
        ans=2*3.14*self.radius
        print("The perimeter is",ans)
circle=Circle(radius)
circle.area()
circle.perimeter()
