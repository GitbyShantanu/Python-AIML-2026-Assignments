# Write a lambda function which accepts one number and return True if even, otherwise False.

ChkOdd = lambda No: No % 2 != 0

def main():
    val = int(input("Enter nummber: "))
    Ret = ChkOdd(val)

    if Ret == True:
        print("Odd number")
    else:
        print("Even number")

if __name__ == "__main__":
    main()