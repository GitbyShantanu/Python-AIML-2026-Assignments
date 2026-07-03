# Write a lambda function which accepts one number and return True if even, otherwise False.

ChkEven = lambda No: No % 2 == 0

def main():
    val = int(input("Enter nummber: "))
    Ret = ChkEven(val)

    if Ret == True:
        print("Even number")
    else:
        print("Odd number")

if __name__ == "__main__":
    main()