# WAP which contains one lambda function which accepts 2 params and return multiplication

Multiplication = lambda No1, No2: No1 * No2 

def main():
    val1 = int(input("Enter 1st number: "))
    val2 = int(input("Enter 2nd number: "))

    Ret = Multiplication(val1, val2)
    print(f"Multiplication is : {Ret}")

if __name__ == "__main__":
    main()