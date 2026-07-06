# WAP which accept one number from user and return True if number is divisible by 5 otherwise return False.

def ChkDivisible(No):
    if No % 5 == 0:
        return True
    else:
        return False

def main():
    val = int(input("Enter number: "))
    
    Ret = ChkDivisible(val)
    if Ret == True:    
        print("divisible by 5")
    else:
        print("not divisible by 5")

if __name__ == "__main__":
    main()  