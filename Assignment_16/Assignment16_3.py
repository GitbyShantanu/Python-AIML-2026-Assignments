# WAP which contains one function named as Add() which accept two parameters as number. It should return addition of that two numbers.

def Add(No1, No2):
    Ans = No1 + No2
    return Ans

def main():
    value1 = int(input("Enter 1st number: "))
    value2 = int(input("Enter 2nd number: "))
    
    Ret = Add(value1, value2)
    print("Addition is:", Ret)

if __name__ == "__main__":
    main()