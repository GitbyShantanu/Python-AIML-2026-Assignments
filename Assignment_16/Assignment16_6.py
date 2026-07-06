# WAP which accept one number from user and check whether that number is positive or negative or zero.

def ChkNum(No):
    if No > 0:
        return 1
    if No < 0:
        return -1   
    else:
        return 0
    
def main():
    val = int(input("Enter number: "))
    
    Ret = ChkNum(val)
    if Ret == 1:    
        print("Positive number")
    elif Ret == -1:
        print("Negative number")    
    else:
        print("Zero")

if __name__ == "__main__":
    main()  