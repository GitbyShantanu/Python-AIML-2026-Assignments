# Create a module named as Arithmetic which contains four functions as Add(), Subtract(), Multiply() and Divide(). All functions accept 2 paramters as number and perform the operation. Write a python program which calls all the functions from Arithmetic module by accepting the user input.

# Client code to call the functions from Arithmetic module
from Arithmetic import Add, Sub, Mult, Div

def main():
    Val1 = int(input("Enter first number: "))
    Val2 = int(input("Enter second number: "))
    
    Ret = Add(Val1, Val2)
    print("Addition is:", Ret)

    Ret = Sub(Val1, Val2)  
    print("Subtraction is:", Ret)

    Ret = Mult(Val1, Val2)
    print("Multiplication is:", Ret)

    Ret = Div(Val1, Val2)
    print("Division is:", Ret)

if __name__ == "__main__":
    main()

