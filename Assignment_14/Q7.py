# Write a lambda function which accepts one number and return True if divisible by 5.

DivBy5 = lambda No: No % 5 == 0

def main():
    val = int(input("Enter nummber: "))
    Ret = DivBy5(val)

    if Ret == True:
        print("Divisible by 5")
    else:
        print("Not Divisible by 5")

if __name__ == "__main__":
    main()