# Write a lambda function which accepts 3 numbers and returns largest no.

largest = lambda No1, No2, No3: No1 if (No1 > No2 and No1 > No3) else (No2 if (No2 > No3 and No2 > No1) else No3)

def main():
    val1 = int(input("Enter 1st nummber: "))
    val2 = int(input("Enter 2nd nummber: "))
    val3 = int(input("Enter 3nd nummber: "))
    
    Ret = largest(val1, val2, val3)
    print("Largest is:", Ret)

if __name__ == "__main__":
    main()