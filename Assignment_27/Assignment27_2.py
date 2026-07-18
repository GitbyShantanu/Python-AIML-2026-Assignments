# WAP to implement a class named BankAccount with following specs: 
# Class should contain 2 instance variables Name, Amount(balance)
# Class should contain 1 class variable ROI (initialise it to 10.5)
# Define a constructor (__init__) that accepts Name and initial amount

# Implement an instance method: 
#   Display() - should display acc holder name and current balance
#   Deposit() - accept amt from user and adds it to balance 
#   Withdraw() - accept amt from user and subtract from balance(Ensure allow only when sufficient balance)
#   CalculateInterest() - calculate and return interest using formula
#       Interest = (Amount * ROI) / 100

# Create multiple instances and demonstrate all methods

class BankAccount:
    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount    

    def Display(self):
        print(f"Name: {self.Name}, Current Balance: {self.Amount}")

    def Deposit(self, amt):
        self.Amount += amt

    def Withdraw(self, amt):
        if self.Amount >= amt:
            self.Amount -= amt
        else:
            print("Insufficient Balance")

    def CalculateInterest(self):
        return (self.Amount * BankAccount.ROI) / 100


obj1 = BankAccount("Shantanu", 2000)
obj1.Display()
obj1.Deposit(1000)
print("After Deposit 1000:")
obj1.Display()

obj2 = BankAccount("Nitin", 500)
obj2.Display()
obj2.Withdraw(500)
print("After Withdraw 500:")
obj2.Display()

    