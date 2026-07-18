# WAP to implement a class named Numbers with following specs:
 
# Class should contain one instance variable Value
# Define a constructor (__init__) accepts number from user & initialise Value

# Implement the following instance methods: 
#   ChkPrime()
#   ChkPerfect()
#   Factors()
#   SumFactors()

# Create multiple instances and demonstrate all methods

class Numbers:
    def __init__(self):
        self.Value = int(input("Enter a number: "))

    def ChkPrime(self):
        for i in range(2, self.Value//2+1):
            if self.Value % i == 0:
                return False
        return True
    
    
    def ChkPerfect(self):
        sum = 0
        for i in range(1, self.Value//2+1):
            if self.Value % i == 0:
                sum += i
        return sum == self.Value
    

    def Factors(self):
        print("Factors:", end=" ")
        for i in range(1, self.Value//2+1):
            if self.Value % i == 0:
                print(i, end=" ")    
        print()


    def SumFactors(self):
        sum = 0
        for i in range(1, self.Value//2+1):
            if self.Value % i == 0:
                sum += i
        return sum


obj1 = Numbers()    
print("Prime:",obj1.ChkPrime())
print("Perfect:",obj1.ChkPerfect())
obj1.Factors()
print("sum of factors:",obj1.SumFactors())

obj2 = Numbers()    
print("Prime:",obj2.ChkPrime())
print("Perfect:",obj2.ChkPerfect())
obj2.Factors()
print("sum of factors:",obj2.SumFactors())