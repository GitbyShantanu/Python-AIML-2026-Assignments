# WAP to implement a class named Demo with following specifications:

# class should contain 2 instance variables: no1 and no2
# class should contain 1 class variable named Value
# define a contructor (__init__) that accepts 2 params and initialises the instance variables 

# Implement 2 instance methods: 
#   Fun() : displays values of instance variable no1 and no2.
#   Gun() : displays values of instance variable no1 and no2.

# Create 2 obj of Demo as follows 
# obj1 = Demo(11, 21)
# obj2 = Demo(51, 101)

# Call the instance methods in given sequnce: 
# obj1.Fun()
# obj2.Fun()
# obj1.Gun()
# obj2.Gun()

class Demo:
    Value = 10 #class variable

    def __init__(self, a, b):
        self.no1 = a # instance variables
        self.no2 = b 

    def Fun(self):
        print("Inside Fun")
        print("Value of no1: ", self.no1)
        print("Value of no2: ", self.no2)

    def Gun(self):
        print("Inside Gun")
        print("Value of no1: ", self.no1)
        print("Value of no2: ", self.no2)

obj1 = Demo(11, 21)
obj2 = Demo(51, 101)

obj1.Fun()
obj2.Fun()

obj1.Gun()
obj2.Gun()



