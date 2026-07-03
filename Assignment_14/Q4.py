# Write a lambda function which accepts 2 numbers and returns minimum.

minimum = lambda No1, No2: No1 < No2

def main():
    val1 = int(input("Enter 1st nummber: "))
    val2 = int(input("Enter 2nd nummber: "))
    Ret = minimum(val1, val2)
    
    if Ret == True:
        print("Minimum is :", val1)
    else:
        print("Minimum is :", val2)

if __name__ == "__main__":
    main()