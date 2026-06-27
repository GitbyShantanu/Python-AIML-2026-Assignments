# WAP which accepts one number and prints factorial of that number

def printFactorial(no):
    fact = 1
    for i in range(1, no+1):
        fact = fact * i
    
    return fact

def main():
    no = int(input("Enter no: "))

    ans = printFactorial(no)
    print(f"Factorial of {no} is: {ans}")

if __name__== "__main__":
    main()