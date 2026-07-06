# WAP which accpets 1 no return its factorial

def Factorial(no):
    fact = 1
    for i in range(1, no+1):
        fact = fact * i

    return fact

def main():
    val = int(input("Enter number: "))

    Ret = Factorial(val)
    print(f"Factorial of {val} is: {Ret}")

if __name__ == "__main__":
    main()