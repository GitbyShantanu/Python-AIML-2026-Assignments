# WAP to implement a class named Arithmetic with following specifications:

# class should contain 2 instance variables: Value1 and Value2
# define a contructor (__init__) that initialise all variable to 0.

# Implement 2 instance methods: 
#   Accept() : accepts values for value1 and value2
#   Addition() : return sum of instance variables
#   Suntraction() : return subtraction of instance variables
#   Multiplication() : return multiplication of instance variables
#   Division() : return division of instance variables (handle division by 0 properly)

# Create multiple obj of class and invoke all instance methods

class Arithmetic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter the value1: "))
        self.Value2 = int(input("Enter the value2: "))

    def Addition(self):
        return self.Value1 + self.Value2
    
    def Subtraction(self):
        return self.Value1 - self.Value2
    
    def Multiplication(self):
        return self.Value1 * self.Value2
    
    def Division(self):
        return self.Value1 / self.Value2

obj1 = Arithmetic()
obj1.Accept()
print("Addition: ", obj1.Addition())
print("Subtraction: ", obj1.Subtraction())
print("Multiplication: ", obj1.Multiplication())

try:
    print("Division: ", obj1.Division())
except Exception as e:
    print("Error: Value2 cannot be 0", e)

obj2 = Arithmetic()
obj2.Accept()
print("Addition: ", obj2.Addition())
print("Subtraction: ", obj2.Subtraction())
print("Multiplication: ", obj2.Multiplication())

try:
    print("Division: ", obj2.Division())
except Exception as e:
    print("Error: Value2 cannot be 0", e)