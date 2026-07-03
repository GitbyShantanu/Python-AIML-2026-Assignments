# Write a lambda function which accepts 2 numbers and returns multiplication.

Multi = lambda No1, No2: No1 * No2

def main():
    val1 = int(input("Enter 1st nummber: "))
    val2 = int(input("Enter 2nd nummber: "))
    
    Ret = Multi(val1, val2)
    print("Multiplication is:", Ret)

if __name__ == "__main__":
    main()