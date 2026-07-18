# WAP to implement a class named Circle with following specifications:

# class should contain 3 instance variables: Radius, Area, Circumference
# class should contain 1 class variable named PI, initialised to 3.14 
# define a contructor (__init__) that accepts 2 params and initialises all variables to 0.0

# Implement following instance methods: 
#   Accept() : accepts the radius of circle from user
#   CalculateArea() : calculates the area of circle and stores in Area variable
#   CalculateCircumference() : calculates the circumference of circle and stores in Circumference variable
#   Display() : displays the values of Radius, Area and Circumference

# Create multiple objects of circle class and invoke all instance methods for each obj  


class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0   
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        self.Radius = float(input("Enter the radius: "))    

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print("Radius: ", self.Radius)
        print("Area: ", self.Area)
        print("Circumference: ", self.Circumference)

obj1 = Circle()
obj1.Accept()
obj1.CalculateArea()
obj1.CalculateCircumference()
obj1.Display()

obj2 = Circle()
obj2.Accept()
obj2.CalculateArea()
obj2.CalculateCircumference()
obj2.Display()



