# WAP which contains one function named as ChkNum() which accept one parameter as number. If number is even then it should display "Even number" otherwise display "Odd number".

def ChkNum(No):
    if No % 2 == 0:
        return True
    else:
        return False

def main():
    value = int(input("Enter number: "))
    
    ret = ChkNum(value)
    if ret == True:
        print("Even number")
    else:
        print("Odd number")

if __name__ == "__main__":
    main()