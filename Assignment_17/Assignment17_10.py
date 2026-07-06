# WAP which accepts one number and return addition of digits

def SumDigit(No):
    sum = 0
    digit = 0
    
    while No > 0:
        digit = No % 10
        sum = sum + digit
        No = No // 10
    
    return sum

def main():
    val = int(input("Enter number: "))

    Ret = SumDigit(val)
    print(f"Sum of digits in {val} is: {Ret}")
    
if __name__ == "__main__":
    main()