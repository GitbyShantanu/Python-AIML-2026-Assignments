# WAP which accepts one number and return number of digits in that number

def CntDigit(No):
    Cnt = 0
    while No > 0:
        Cnt = Cnt + 1
        No = No // 10

    return Cnt

def main():
    val = int(input("Enter number: "))

    Ret = CntDigit(val)
    print(f"Count of digits in {val} is: {Ret}")
    
if __name__ == "__main__":
    main()